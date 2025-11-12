# Design Document

## Overview
This document provides detailed design specifications for the TaskMaster Pro task management system components.

## Design Principles
- **Single Responsibility**: Each component has a single, well-defined responsibility
- **Loose Coupling**: Components interact through well-defined interfaces
- **High Cohesion**: Related functionality is grouped together
- **Scalability**: Design supports future growth and expansion
- **Security**: All components implement proper authentication and authorization

## Component Specifications

### Component: UserAuthenticationService
**Purpose**: Handles user registration, login, and session management

**Location**: `src/services/auth/UserAuthenticationService.py`

**Interface**:
```python
class UserAuthenticationService:
    """
    User authentication and authorization service
    Implements: Req 1.1, 1.2, 1.3, 1.4, 7.1, 7.2
    """

    def __init__(self, user_repository: UserRepository, email_service: EmailService):
        """Initialize authentication service with dependencies"""
        self.user_repository = user_repository
        self.email_service = email_service
        self.jwt_secret = os.getenv('JWT_SECRET')
        self.token_expiry = int(os.getenv('TOKEN_EXPIRY_HOURS', '24'))

    def register_user(self, user_data: UserRegistrationData) -> AuthResult:
        """
        Register a new user account with email verification
        Implements: Req 1.1
        """
        pass

    def authenticate_user(self, credentials: LoginCredentials) -> AuthResult:
        """
        Authenticate user and return JWT token
        Implements: Req 1.2
        """
        pass

    def reset_password(self, email: str) -> PasswordResetResult:
        """
        Initiate password reset process
        Implements: Req 1.3
        """
        pass

    def validate_token(self, token: str) -> TokenValidationResult:
        """
        Validate JWT token and extract user information
        Implements: Req 1.4
        """
        pass

    def hash_password(self, password: str) -> str:
        """
        Hash password using bcrypt
        Implements: Req 7.2
        """
        pass
```

**Dependencies**:
- UserRepository: Database access for user operations
- EmailService: Email sending functionality
- JWT library: Token generation and validation
- bcrypt: Password hashing

**Data Model**:
```python
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime
from enum import Enum

class UserRole(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    MEMBER = "member"

@dataclass
class User:
    """User entity model"""
    id: str
    email: str
    username: str
    password_hash: str
    role: UserRole
    is_active: bool
    email_verified: bool
    created_at: datetime
    last_login: Optional[datetime] = None

@dataclass
class UserRegistrationData:
    """User registration request data"""
    email: str
    username: str
    password: str
    confirm_password: str

@dataclass
class LoginCredentials:
    """User login credentials"""
    email: str
    password: str

@dataclass
class AuthResult:
    """Authentication operation result"""
    success: bool
    token: Optional[str] = None
    user: Optional[User] = None
    message: str = ""
```

### Component: TaskManagementEngine
**Purpose**: Core task CRUD operations and business logic

**Location**: `src/services/tasks/TaskManagementEngine.py`

**Interface**:
```python
class TaskManagementEngine:
    """
    Task management and business logic engine
    Implements: Req 2.1, 2.2, 2.3, 2.4, 6.1, 7.3
    """

    def __init__(self, task_repository: TaskRepository,
                 notification_service: NotificationService,
                 auth_service: UserAuthenticationService):
        """Initialize task engine with dependencies"""
        self.task_repository = task_repository
        self.notification_service = notification_service
        self.auth_service = auth_service

    def create_task(self, task_data: TaskCreationData, user_id: str) -> TaskCreationResult:
        """
        Create a new task with validation and assignment
        Implements: Req 2.1
        """
        pass

    def update_task(self, task_id: str, updates: TaskUpdateData, user_id: str) -> TaskUpdateResult:
        """
        Update existing task with change tracking
        Implements: Req 2.2
        """
        pass

    def assign_task(self, task_id: str, assignee_id: str, assigner_id: str) -> TaskAssignmentResult:
        """
        Assign task to user and send notification
        Implements: Req 2.3
        """
        pass

    def change_task_status(self, task_id: str, new_status: TaskStatus, user_id: str) -> StatusChangeResult:
        """
        Change task status and notify relevant users
        Implements: Req 2.4
        """
        pass

    def get_user_tasks(self, user_id: str, filters: TaskFilters) -> List[Task]:
        """
        Retrieve tasks for a specific user with filters
        Implements: Req 6.1
        """
        pass
```

**Dependencies**:
- TaskRepository: Database access for task operations
- NotificationService: Real-time notifications
- UserAuthenticationService: User validation and permissions

**Data Model**:
```python
from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class TaskPriority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

@dataclass
class Task:
    """Task entity model"""
    id: str
    title: str
    description: str
    status: TaskStatus
    priority: TaskPriority
    assignee_id: Optional[str]
    creator_id: str
    project_id: str
    due_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None
    tags: List[str] = None
    custom_fields: Dict[str, Any] = None

@dataclass
class TaskCreationData:
    """Task creation request data"""
    title: str
    description: str
    priority: TaskPriority
    assignee_id: Optional[str]
    project_id: str
    due_date: Optional[datetime]
    tags: List[str] = None

@dataclass
class TaskUpdateData:
    """Task update request data"""
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[TaskPriority] = None
    assignee_id: Optional[str] = None
    due_date: Optional[datetime] = None
    tags: Optional[List[str]] = None
```

### Component: NotificationService
**Purpose**: Handles real-time notifications and email alerts

**Location**: `src/services/notifications/NotificationService.py`

**Interface**:
```python
class NotificationService:
    """
    Real-time notification and alert service
    Implements: Req 4.1, 4.2, 4.3, 4.4, 6.4
    """

    def __init__(self, websocket_manager: WebSocketManager,
                 email_service: EmailService,
                 notification_repository: NotificationRepository):
        """Initialize notification service with dependencies"""
        self.websocket_manager = websocket_manager
        self.email_service = email_service
        self.notification_repository = notification_repository

    def send_task_assignment_notification(self, task_id: str, assignee_id: str) -> NotificationResult:
        """
        Send real-time notification for task assignment
        Implements: Req 4.1
        """
        pass

    def send_deadline_reminder(self, task_id: str, assignee_id: str) -> NotificationResult:
        """
        Send reminder notification for approaching deadline
        Implements: Req 4.2
        """
        pass

    def broadcast_task_update(self, task_id: str, update_data: Dict[str, Any]) -> BroadcastResult:
        """
        Broadcast real-time task updates to prevent conflicts
        Implements: Req 4.3
        """
        pass

    def send_maintenance_notification(self, message: str, scheduled_time: datetime) -> NotificationResult:
        """
        Send system maintenance notifications
        Implements: Req 4.4
        """
        pass
```

**Dependencies**:
- WebSocketManager: Real-time WebSocket connection management
- EmailService: Email notification delivery
- NotificationRepository: Database storage for notifications

## Integration Design

### API Contracts
```python
# REST API between User Interface and TaskManagementEngine
POST /api/tasks
Authorization: Bearer {jwt_token}
Content-Type: application/json

Request:
{
    "title": "Complete user authentication",
    "description": "Implement JWT-based authentication system",
    "priority": "high",
    "assignee_id": "user123",
    "project_id": "proj456",
    "due_date": "2024-01-15T17:00:00Z",
    "tags": ["backend", "security"]
}

Response:
{
    "id": "task789",
    "status": "todo",
    "created_at": "2024-01-01T12:00:00Z",
    "assigned_at": "2024-01-01T12:00:00Z"
}
```

### Database Schema
```sql
-- Users table for UserAuthenticationService
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'member',
    is_active BOOLEAN DEFAULT true,
    email_verified BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);

-- Tasks table for TaskManagementEngine
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(20) NOT NULL DEFAULT 'todo',
    priority VARCHAR(10) NOT NULL DEFAULT 'medium',
    assignee_id UUID REFERENCES users(id),
    creator_id UUID NOT NULL REFERENCES users(id),
    project_id UUID NOT NULL REFERENCES projects(id),
    due_date TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE
);

-- Projects table for ProjectOrganizer
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    owner_id UUID NOT NULL REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Security Implementation
```python
# JWT Token validation middleware
def require_auth(func):
    """Decorator to require JWT authentication"""
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return jsonify({'error': 'Authentication required'}), 401

        token = token.split(' ')[1]
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            request.user_id = payload['user_id']
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
    return wrapper
```
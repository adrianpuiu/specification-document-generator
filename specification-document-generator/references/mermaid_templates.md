# Mermaid Diagram Templates

Ready-to-use templates for common specification diagrams.

## Component Diagram Templates

### Basic System Architecture
```mermaid
graph TB
    subgraph "Presentation Layer"
        UI[User Interface]
        API[REST API]
    end

    subgraph "Business Logic Layer"
        Service[Business Service]
        Validator[Data Validator]
    end

    subgraph "Data Layer"
        DB[(Database)]
        Cache[(Cache)]
    end

    subgraph "External Systems"
        External[External API]
        Queue[Message Queue]
    end

    UI --> API
    API --> Service
    Service --> Validator
    Service --> DB
    Service --> Cache
    Service --> External
    Service --> Queue
```

### Microservices Architecture
```mermaid
graph TB
    subgraph "Client Layer"
        Web[Web App]
        Mobile[Mobile App]
    end

    subgraph "API Gateway"
        Gateway[API Gateway]
        Auth[Authentication Service]
    end

    subgraph "Microservices"
        UserService[User Service]
        OrderService[Order Service]
        PaymentService[Payment Service]
        NotificationService[Notification Service]
    end

    subgraph "Data Layer"
        UserDB[(User DB)]
        OrderDB[(Order DB)]
        PaymentDB[(Payment DB)]
    end

    subgraph "Infrastructure"
        MessageQueue[Message Queue]
        Cache[Redis Cache]
    end

    Web --> Gateway
    Mobile --> Gateway
    Gateway --> Auth
    Gateway --> UserService
    Gateway --> OrderService
    Gateway --> PaymentService

    UserService --> UserDB
    OrderService --> OrderDB
    PaymentService --> PaymentDB

    OrderService --> MessageQueue
    PaymentService --> MessageQueue
    MessageQueue --> NotificationService

    UserService --> Cache
    OrderService --> Cache
```

### Real-time System Architecture
```mermaid
graph TB
    subgraph "Data Sources"
        DataSource1[Data Source 1]
        DataSource2[Data Source 2]
        DataSource3[Data Source 3]
    end

    subgraph "Processing Layer"
        Collector[Data Collector]
        Processor[Data Processor]
        Analyzer[Data Analyzer]
    end

    subgraph "Storage Layer"
        Stream[Data Stream]
        Cache[(Cache)]
        Archive[(Archive)]
    end

    subgraph "Output Layer"
        Dashboard[Real-time Dashboard]
        Alert[Alert System]
        API[Streaming API]
    end

    DataSource1 --> Collector
    DataSource2 --> Collector
    DataSource3 --> Collector

    Collector --> Stream
    Stream --> Processor
    Processor --> Analyzer

    Analyzer --> Dashboard
    Analyzer --> Alert
    Analyzer --> API

    Processor --> Cache
    Analyzer --> Archive
```

## Sequence Diagram Templates

### User Authentication Flow
```mermaid
sequenceDiagram
    participant User
    participant UI
    participant AuthService
    participant Database
    participant TokenService

    User->>UI: Enter credentials
    UI->>AuthService: Login request
    AuthService->>Database: Validate user
    Database-->>AuthService: User data
    AuthService->>TokenService: Generate JWT
    TokenService-->>AuthService: JWT token
    AuthService-->>UI: Authentication response
    UI-->>User: Login success/failure
```

### Order Processing Flow
```mermaid
sequenceDiagram
    participant Customer
    participant OrderService
    participant PaymentService
    participant InventoryService
    participant NotificationService
    participant Database

    Customer->>OrderService: Create order
    OrderService->>InventoryService: Check availability
    InventoryService-->>OrderService: Available items

    OrderService->>PaymentService: Process payment
    PaymentService->>PaymentService: Validate payment
    PaymentService-->>OrderService: Payment confirmation

    OrderService->>Database: Save order
    Database-->>OrderService: Order saved

    OrderService->>InventoryService: Update inventory
    InventoryService-->>OrderService: Inventory updated

    OrderService->>NotificationService: Send confirmation
    NotificationService-->>OrderService: Notification sent

    OrderService-->>Customer: Order confirmation
```

### API Request Flow
```mermaid
sequenceDiagram
    participant Client
    participant LoadBalancer
    participant APIGateway
    participant Microservice
    participant Database
    participant Cache

    Client->>LoadBalancer: HTTP Request
    LoadBalancer->>APIGateway: Forward request
    APIGateway->>APIGateway: Authenticate request
    APIGateway->>Cache: Check cache
    alt Cache hit
        Cache-->>APIGateway: Cached data
    else Cache miss
        APIGateway->>Microservice: Forward to service
        Microservice->>Database: Query data
        Database-->>Microservice: Query result
        Microservice-->>APIGateway: Processed data
        APIGateway->>Cache: Update cache
    end
    APIGateway-->>LoadBalancer: API Response
    LoadBalancer-->>Client: HTTP Response
```

### Error Handling Flow
```mermaid
sequenceDiagram
    participant Client
    participant Service
    participant RetryHandler
    participant CircuitBreaker
    participant FallbackService

    Client->>Service: Request
    Service->>Service: Process request

    alt Service failure
        Service->>RetryHandler: Report failure
        RetryHandler->>RetryHandler: Check retry count

        alt Retries available
            RetryHandler->>Service: Retry request
            Service-->>Client: Success response
        else No more retries
            RetryHandler->>CircuitBreaker: Report consecutive failures
            CircuitBreaker->>CircuitBreaker: Check failure threshold

            alt Circuit open
                CircuitBreaker->>FallbackService: Use fallback
                FallbackService-->>Client: Fallback response
            else Circuit half-open
                CircuitBreaker->>Service: Test request
                alt Service succeeds
                    Service-->>Client: Success response
                    CircuitBreaker->>CircuitBreaker: Close circuit
                else Service fails
                    CircuitBreaker->>FallbackService: Use fallback
                    FallbackService-->>Client: Fallback response
                end
            end
        end
    else Service success
        Service-->>Client: Success response
    end
```

## State Diagram Templates

### Order Lifecycle
```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> Processing: Start processing
    Processing --> Payment: Payment required
    Processing --> Shipped: Payment confirmed
    Payment --> Processing: Payment successful
    Payment --> Cancelled: Payment failed
    Shipped --> Delivered: Package delivered
    Delivered --> [*]
    Cancelled --> [*]

    Processing --> Cancelled: Cancel requested
    Shipped --> Cancelled: Return requested
```

### User Session State
```mermaid
stateDiagram-v2
    [*] --> Anonymous
    Anonymous --> Authenticating: Login attempt
    Authenticating --> Authenticated: Credentials valid
    Authenticating --> Anonymous: Credentials invalid
    Authenticated --> Active: Session active
    Active --> Idle: No activity
    Idle --> Active: Activity detected
    Idle --> Expired: Timeout reached
    Active --> Expired: Manual logout
    Expired --> Anonymous: Session cleared
```

### Circuit Breaker States
```mermaid
stateDiagram-v2
    [*] --> Closed
    Closed --> Open: Failure threshold reached
    Open --> HalfOpen: Timeout elapsed
    HalfOpen --> Closed: Request succeeds
    HalfOpen --> Open: Request fails
```

## Flowchart Templates

### Data Processing Pipeline
```mermaid
flowchart TD
    Start([Start]) --> Input[Input Data]
    Input --> Validate{Validate Data}
    Validate -->|Valid| Process[Process Data]
    Validate -->|Invalid| Error[Log Error]
    Error --> End([End])
    Process --> Transform{Transform Required}
    Transform -->|Yes| Transform[Apply Transformation]
    Transform --> NoTransform[No Transformation]
    Transform --> Output[Output Result]
    NoTransform --> Output
    Output --> End
```

### Decision Making Process
```mermaid
flowchart TD
    Start([Start]) --> Receive[Receive Request]
    Receive --> CheckAuth{Authenticated?}
    CheckAuth -->|No| Unauthorized[Return 401]
    CheckAuth -->|Yes| CheckPerms{Has Permission?}
    CheckPerms -->|No| Forbidden[Return 403]
    CheckPerms -->|Yes| Process[Process Request]
    Process --> Success{Success?}
    Success -->|Yes| SuccessResp[Return 200]
    Success -->|No| ErrorResp[Return 500]
    Unauthorized --> End([End])
    Forbidden --> End
    SuccessResp --> End
    ErrorResp --> End
```

## ER Diagram Templates

### User Order System
```mermaid
erDiagram
    User {
        string user_id PK
        string username
        string email
        datetime created_at
        datetime updated_at
    }

    Order {
        string order_id PK
        string user_id FK
        decimal total_amount
        string status
        datetime created_at
        datetime updated_at
    }

    OrderItem {
        string item_id PK
        string order_id FK
        string product_id FK
        int quantity
        decimal unit_price
        decimal total_price
    }

    Product {
        string product_id PK
        string name
        string description
        decimal price
        int stock_quantity
    }

    User ||--o{ Order : places
    Order ||--|{ OrderItem : contains
    Product ||--o{ OrderItem : includes
```

### Blog System
```mermaid
erDiagram
    User {
        int user_id PK
        string username
        string email
        datetime created_at
    }

    Post {
        int post_id PK
        int author_id FK
        string title
        text content
        string status
        datetime created_at
        datetime updated_at
    }

    Comment {
        int comment_id PK
        int post_id FK
        int user_id FK
        text content
        datetime created_at
    }

    Category {
        int category_id PK
        string name
        string description
    }

    PostCategory {
        int post_id FK
        int category_id FK
    }

    User ||--o{ Post : writes
    Post ||--o{ Comment : has
    User ||--o{ Comment : writes
    Post ||--o{ PostCategory : belongs_to
    Category ||--o{ PostCategory : contains
```

## Usage Guidelines

### Component Diagrams
- Use for high-level architecture overview
- Group related components into layers or modules
- Show data flow and dependencies
- Include external systems and integrations

### Sequence Diagrams
- Use for showing interaction between components over time
- Focus on specific use cases or scenarios
- Include error handling paths
- Show both happy path and exceptional flows

### State Diagrams
- Use for objects with complex lifecycle states
- Show all possible states and transitions
- Include events that trigger state changes
- Consider concurrent states if applicable

### Flowcharts
- Use for business processes and decision logic
- Keep diagrams simple and readable
- Use consistent shapes for different elements
- Include error handling and alternative paths

### ER Diagrams
- Use for database schema design
- Show entities, attributes, and relationships
- Include cardinality and constraints
- Normalize relationships appropriately

## Customization Tips

### Styling
- Add colors to distinguish different layers or types
- Use consistent color schemes across diagrams
- Consider accessibility (colorblind-friendly palettes)

### Layout
- Arrange components logically (left to right, top to bottom)
- Minimize crossing lines
- Group related components together

### Labels
- Use clear, descriptive names
- Include relevant details (protocols, data formats)
- Add annotations for complex interactions

### Best Practices
- Keep diagrams focused on a single concern
- Don't overcrowd with too much detail
- Use multiple diagrams for complex systems
- Maintain consistency across related diagrams
# Design Patterns Library

Common architectural patterns and their applications in specification documents.

## Architectural Patterns

### Model-View-Controller (MVC)
**When to use**: Web applications, desktop applications with user interfaces

**Components**:
- Model: Data structures and business logic
- View: User interface representation
- Controller: Handles user input and coordinates Model/View

**Benefits**:
- Separation of concerns
- Multiple views for same model
- Independent development

**Example Components**:
- `UserModel`: User data and validation
- `UserView`: User profile display
- `UserController`: Registration/login logic

### Microservices Architecture
**When to use**: Large-scale applications, distributed systems

**Components**:
- API Gateway: Request routing and composition
- Service Registry: Service discovery
- Configuration Service: Centralized configuration
- Circuit Breaker: Fault tolerance

**Benefits**:
- Scalability
- Independent deployment
- Technology diversity

**Example Components**:
- `UserService`: User management
- `OrderService`: Order processing
- `PaymentService`: Payment handling

### Event-Driven Architecture
**When to use**: Real-time systems, asynchronous processing

**Components**:
- Event Bus: Message routing
- Event Store: Event persistence
- Event Handler: Business logic
- Event Sourcing: State reconstruction

**Benefits**:
- Loose coupling
- Scalability
- Audit trail

**Example Components**:
- `EventPublisher`: Broadcasts events
- `EventSubscriber`: Listens for events
- `EventStore`: Persists events

### Repository Pattern
**When to use**: Data access, database operations

**Components**:
- Repository Interface: Data contract
- Repository Implementation: Data access logic
- Unit of Work: Transaction management

**Benefits**:
- Testability
- Centralized data logic
- Consistency

**Example Components**:
- `UserRepository`: User data operations
- `OrderRepository`: Order data operations
- `UnitOfWork`: Transaction management

## Data Patterns

### Data Transfer Object (DTO)
**When to use**: API responses, data exchange between layers

**Structure**:
```python
@dataclass
class UserDTO:
    user_id: str
    username: str
    email: str
    created_at: datetime

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
```

### Value Object
**When to use**: Immutable concepts with no identity

**Structure**:
```python
@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")
```

### Aggregate Root
**When to use**: Domain-driven design, consistency boundaries

**Structure**:
```python
class OrderAggregate:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.items: List[OrderItem] = []
        self.status: OrderStatus = OrderStatus.PENDING

    def add_item(self, product_id: str, quantity: int, price: Money):
        """Business logic for adding items"""
        if self.status != OrderStatus.PENDING:
            raise OrderNotModifiableError()
        self.items.append(OrderItem(product_id, quantity, price))
```

## Integration Patterns

### API Gateway Pattern
**When to use**: Microservices, external API management

**Components**:
- `APIGateway`: Request routing and composition
- `AuthenticationMiddleware`: Security handling
- `RateLimitingMiddleware`: Request throttling

### Circuit Breaker Pattern
**When to use**: External service integration, fault tolerance

**Components**:
- `CircuitBreaker`: Fault detection and isolation
- `RetryMechanism`: Automatic retry logic
- `FallbackService`: Alternative behavior

### Message Queue Pattern
**When to use**: Asynchronous processing, system integration

**Components**:
- `MessageProducer`: Sends messages
- `MessageConsumer`: Processes messages
- `MessageQueue`: Message storage and delivery

## Security Patterns

### Authentication and Authorization
**When to use**: User access control, security

**Components**:
- `AuthenticationService`: Identity verification
- `AuthorizationService`: Permission checking
- `TokenManager`: JWT token handling

### Data Encryption
**When to use**: Sensitive data protection

**Components**:
- `EncryptionService`: Data encryption/decryption
- `KeyManager`: Cryptographic key management
- `SecureStorage`: Encrypted data storage

## Performance Patterns

### Caching Pattern
**When to use**: Performance optimization, data access

**Components**:
- `CacheManager`: Cache operations
- `CacheInvalidation`: Cache updates
- `DistributedCache`: Multi-node caching

### Connection Pooling
**When to use**: Database connections, external services

**Components**:
- `ConnectionPool`: Connection management
- `PoolConfiguration`: Pool settings
- `HealthChecker`: Connection validation

## Monitoring Patterns

### Logging Pattern
**When to use**: System observability, debugging

**Components**:
- `Logger`: Log writing
- `LogFormatter`: Log formatting
- `LogAggregator`: Log collection

### Metrics Pattern
**When to use**: Performance monitoring, system health

**Components**:
- `MetricsCollector`: Metrics gathering
- `MetricsRegistry`: Metrics storage
- `AlertingService`: Alert generation

## UI Patterns

### Component-Based UI
**When to use**: Web applications, mobile apps

**Components**:
- `ComponentManager`: Component lifecycle
- `StateManager`: State handling
- `EventBus`: Component communication

### Form Validation Pattern
**When to use**: User input validation

**Components**:
- `ValidationRule`: Validation logic
- `FormValidator`: Form validation
- `ErrorHandler`: Error display

## Database Patterns

### Unit of Work Pattern
**When to use**: Transaction management, data consistency

**Components**:
- `UnitOfWork`: Transaction coordination
- `Repository`: Data access
- `DbContext`: Database context

### Query Object Pattern
**When to use**: Complex queries, dynamic search

**Components**:
- `QueryBuilder`: Query construction
- `CriteriaBuilder`: Query conditions
- `ResultMapper`: Result mapping

## Testing Patterns

### Test Data Builder Pattern
**When to use**: Test data creation

**Structure**:
```python
class UserBuilder:
    def __init__(self):
        self.user = User(
            user_id="default-id",
            username="default-user",
            email="default@example.com"
        )

    def with_username(self, username: str):
        self.user.username = username
        return self

    def build(self) -> User:
        return self.user
```

### Mock/Stub Pattern
**When to use**: Unit testing, external dependencies

**Components**:
- `MockService`: Test double implementation
- `TestDataFactory`: Test data creation
- `TestFixture`: Test environment setup

## Pattern Selection Guidelines

### Consider Project Size
- **Small projects**: Simple patterns (MVC, Repository)
- **Medium projects**: Additional patterns (Caching, Validation)
- **Large projects**: Complex patterns (Microservices, Event-Driven)

### Consider Team Expertise
- **Junior teams**: Well-documented patterns (MVC, Repository)
- **Senior teams**: Advanced patterns (Event Sourcing, CQRS)

### Consider Performance Requirements
- **High performance**: Caching, Connection Pooling, Async patterns
- **Standard performance**: Basic architectural patterns

### Consider Maintenance Needs
- **Long-term maintenance**: SOLID principles, clean architecture
- **Short-term projects**: Quick implementation patterns

## Anti-Patterns to Avoid

### God Object
**Problem**: Single class doing too much
**Solution**: Single Responsibility Principle, separate concerns

### Tight Coupling
**Problem**: Components depend heavily on each other
**Solution**: Dependency Injection, Interface Segregation

### Hard-coded Dependencies
**Problem**: Configuration and logic mixed
**Solution**: Configuration files, dependency injection

### Missing Error Handling
**Problem**: No consideration for failure scenarios
**Solution**: Circuit breakers, retry patterns, fallback mechanisms
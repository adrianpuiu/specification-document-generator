# EARS Notation Guide

EARS (Easy Approach to Requirements Syntax) provides a structured way to write unambiguous, testable requirements.

## EARS Pattern Structure

### Core Components

**WHEN** - Temporal triggers and events
- Defines when the system should perform an action
- Used for user actions, system events, time-based triggers
- Example: "WHEN the user clicks the submit button"

**WHERE** - Contextual conditions and states
- Defines the context or environmental conditions
- Used for system states, locations, modes, or preconditions
- Example: "WHERE the user is authenticated"

**IF/THEN** - Conditional logic branches
- Defines conditional behavior with explicit conditions and responses
- Used for business rules, validation, decision points
- Example: "IF the payment amount exceeds the limit, THEN display an error"

**WHILE** - Continuous or ongoing behaviors
- Defines continuous requirements or constraints during operations
- Used for performance requirements, ongoing behaviors, constraints
- Example: "WHILE processing the batch, maintain memory usage below 80%"

**THE [component] SHALL** - Mandatory, testable behavior
- Specifies what the system must do, always referencing a specific component
- The behavior must be measurable and testable
- Example: "THE authentication service SHALL validate credentials"

## EARS Template Patterns

### Event-Response Pattern
```
WHEN [trigger event], THE [system component] SHALL [specific behavior]
```

Examples:
- WHEN the user submits the login form, THE authentication service SHALL validate credentials
- WHEN the market data feed is interrupted, THE trading engine SHALL pause all orders
- WHEN the inventory level drops below threshold, THE notification system SHALL alert managers

### Conditional Pattern
```
IF [condition], THEN THE [system component] SHALL [response action]
```

Examples:
- IF the payment amount exceeds daily limit, THEN THE payment processor SHALL reject the transaction
- IF the user session expires, THEN THE session manager SHALL redirect to login page
- IF the backup fails, THEN THE monitoring system SHALL send critical alert

### State-Based Pattern
```
WHERE [context/state], THE [system component] SHALL [expected behavior]
```

Examples:
- WHERE the system is in maintenance mode, THE user interface SHALL display maintenance message
- WHERE the user has admin privileges, THE admin panel SHALL show advanced options
- WHERE the connection is offline, THE application SHALL enable offline mode

### Continuous Behavior Pattern
```
WHILE [ongoing state], THE [system component] SHALL [continuous requirement]
```

Examples:
- WHILE processing large files, THE memory manager SHALL keep usage below 2GB
- WHILE the user is active, THE session timer SHALL reset every 5 minutes
- WHILE the system is under load, THE load balancer SHALL distribute requests evenly

### Complex Pattern (Multiple Conditions)
```
WHEN [trigger], WHERE [context], THE [component] SHALL [behavior]
IF [additional condition], THEN THE [component] SHALL [alternative behavior]
```

Examples:
- WHEN a new order is received, WHERE the market is open, THE order processor SHALL validate the order. IF the order size exceeds limits, THEN THE order processor SHALL flag for manual review.

## Component Specification Rules

### Always Specify the Component
Every requirement must explicitly state which system component is responsible:

✅ Good:
- THE user authentication service SHALL verify credentials
- THE database connection pool SHALL maintain 10 minimum connections
- THE email notification system SHALL send password reset emails

❌ Bad:
- The system shall verify credentials
- Credentials shall be verified
- Password reset emails shall be sent

### Use Consistent Component Naming
Maintain consistent component names across all requirements:

- UserAuthenticationService (not Auth Service, User Auth, etc.)
- OrderProcessingEngine (not Order Engine, Processing Service)
- PaymentGateway (not Payment Service, Gateway)

## Measurable Requirements

### Include Specific Metrics
Every requirement must include measurable criteria:

✅ Good:
- THE API SHALL respond within 200 milliseconds
- THE system SHALL support 1000 concurrent users
- THE backup SHALL complete within 30 minutes
- THE cache SHALL achieve 90% hit rate

❌ Bad:
- THE API SHALL respond quickly
- THE system SHALL support many users
- THE backup SHALL complete in reasonable time
- THE cache SHALL have good performance

### Performance Requirement Pattern
```
THE [component] SHALL [achieve performance metric] of [specific value] under [conditions]
```

Examples:
- THE web server SHALL maintain response time under 500ms for 95% of requests
- THE database SHALL support 10,000 transactions per second during peak hours
- THE file upload SHALL support files up to 100MB in size

## Error Handling Requirements

### Error Scenario Pattern
```
WHEN [error condition], THE [component] SHALL [error handling behavior]
```

Examples:
- WHEN the database connection fails, THE connection pool SHALL attempt reconnection 3 times with exponential backoff
- WHEN the API rate limit is exceeded, THE rate limiter SHALL return HTTP 429 with retry-after header
- WHEN invalid data is received, THE validator SHALL log the error and return specific error code

### Fallback Behavior Pattern
```
IF [failure scenario], THEN THE [component] SHALL [fallback behavior]
```

Examples:
- IF the primary service is unavailable, THEN THE load balancer SHALL route traffic to backup service
- IF the external API times out, THEN THE client SHALL use cached data
- IF the payment gateway fails, THEN THE checkout system SHALL offer alternative payment methods

## EARS Quality Checklist

For each requirement, verify:

- [ ] Has a clear temporal trigger (WHEN)
- [ ] Specifies the responsible component (THE [component])
- [ ] Uses SHALL for mandatory behavior
- [ ] Includes measurable criteria with specific numbers
- [ ] Defines error conditions and handling
- [ ] Is testable and verifiable
- [ ] Uses consistent terminology
- [ ] Avoids ambiguous terms (e.g., "appropriate", "suitable", "adequate")
- [ ] Specifies conditions and context (WHERE/IF)
- [ ] Addresses edge cases and failure scenarios

## Common Anti-Patterns

### Vague Requirements
❌ "The system should provide good performance"
✅ "THE API SHALL respond within 200ms for 95% of requests"

### Unspecified Components
❌ "Users shall be authenticated"
✅ "THE authentication service SHALL verify user credentials"

### Missing Error Handling
❌ "The system shall process payments"
✅ "WHEN the payment fails, THE payment processor SHALL log the error and notify the user"

### Ambiguous Conditions
❌ "The system should handle large files efficiently"
✅ "WHEN processing files up to 100MB, THE file processor SHALL complete within 30 seconds"

## Project-Specific Adaptations

### Software Development
- Focus on APIs, databases, services, and user interfaces
- Include performance, security, and scalability requirements
- Specify integration points and data formats

### Construction Projects
- Focus on materials, equipment, and site conditions
- Include safety, regulatory, and environmental requirements
- Specify quality standards and inspection criteria

### Manufacturing
- Focus on production processes and equipment
- Include quality control, efficiency, and safety requirements
- Specify material specifications and tolerances

### Business Processes
- Focus on workflows, roles, and business rules
- Include compliance, audit, and reporting requirements
- Specify service level agreements and metrics
# Project Type Templates

Domain-specific templates and terminology for different project types.

## Software Development Projects

### Common Components
- **API Gateway**: Request routing and management
- **Authentication Service**: User identity verification
- **Database Layer**: Data persistence and retrieval
- **Cache Layer**: Performance optimization
- **Message Queue**: Asynchronous communication
- **Logging Service**: System observability
- **Configuration Service**: Centralized settings
- **Monitoring Service**: Health and performance tracking

### Typical Requirements Patterns
- Performance requirements (response time, throughput)
- Security requirements (authentication, authorization, encryption)
- Scalability requirements (concurrent users, data volume)
- Reliability requirements (uptime, error handling)
- Integration requirements (APIs, third-party services)

### EARS Notation Examples
- WHEN a user submits the registration form, THE authentication service SHALL validate email format
- IF the password strength is insufficient, THEN THE user interface SHALL display specific requirements
- WHERE the user session is expired, THE application SHALL redirect to login page
- THE API SHALL respond within 200ms for 95% of requests under normal load
- WHEN the database connection fails, THE connection pool SHALL attempt reconnection with exponential backoff

### Common Design Patterns
- MVC (Model-View-Controller)
- Repository Pattern
- Unit of Work Pattern
- Circuit Breaker Pattern
- CQRS (Command Query Responsibility Segregation)
- Event Sourcing

## Construction Projects

### Common Components
- **Site Preparation**: Land clearing, grading, excavation
- **Foundation System**: Structural base, footings, pilings
- **Structural Frame**: Load-bearing elements, beams, columns
- **Building Envelope**: Exterior walls, roofing, insulation
- **MEP Systems**: Mechanical, Electrical, Plumbing systems
- **Interior Finishes**: Flooring, walls, ceilings
- **Safety Systems**: Fire protection, emergency exits
- **Quality Control**: Inspections, testing, documentation

### Typical Requirements Patterns
- Structural requirements (load capacity, material specifications)
- Safety requirements (building codes, OSHA compliance)
- Environmental requirements (sustainability, waste management)
- Schedule requirements (milestones, completion dates)
- Budget requirements (cost constraints, material costs)

### EARS Notation Examples
- WHEN pouring concrete foundations, THE construction team SHALL maintain proper curing temperature
- IF soil bearing capacity is insufficient, THEN THE engineers SHALL specify deep foundations
- WHERE work areas are above 6 feet, THE safety coordinator SHALL ensure fall protection is installed
- THE structural steel SHALL meet ASTM A36 specifications for all columns and beams
- WHEN installing electrical systems, THE electrician SHALL follow NEC 2023 code requirements
- DURING concrete curing, THE quality inspector SHALL verify moisture content every 12 hours

### Common Design Patterns
- Phased Construction
- Critical Path Management
- Just-in-Time Material Delivery
- Lean Construction
- Building Information Modeling (BIM)

## Manufacturing Projects

### Common Components
- **Raw Materials**: Input materials and components
- **Production Equipment**: Machines, tools, fixtures
- **Assembly Lines**: Production flow and workstations
- **Quality Control**: Inspection, testing, verification
- **Inventory Management**: Storage, tracking, replenishment
- **Packaging Systems**: Product preparation for shipment
- **Maintenance Systems**: Equipment upkeep and repair
- **Safety Systems**: Worker protection and emergency systems

### Typical Requirements Patterns
- Production requirements (output volume, cycle time)
- Quality requirements (defect rates, specifications)
- Efficiency requirements (material utilization, energy consumption)
- Safety requirements (OSHA compliance, equipment guarding)
- Maintenance requirements (uptime, preventive maintenance schedules)

### EARS Notation Examples
- WHEN the assembly line starts, THE quality system SHALL perform initial calibration checks
- IF the defect rate exceeds 2%, THEN THE production supervisor SHALL stop the line for investigation
- WHERE hazardous materials are used, THE safety officer SHALL ensure proper ventilation and PPE
- THE production equipment SHALL maintain 98% uptime during scheduled production hours
- WHEN performing quality inspections, THE inspector SHALL follow ISO 9001 procedures
- DURING machine operation, THE operators SHALL monitor temperature and vibration levels

### Common Design Patterns
- Cellular Manufacturing
- Just-in-Time Production
- Total Quality Management (TQM)
- Six Sigma
- Lean Manufacturing
- Predictive Maintenance

## Business Process Projects

### Common Components
- **Stakeholder Management**: User identification and communication
- **Process Workflow**: Step-by-step business procedures
- **Decision Points**: Business rules and approval gates
- **Data Management**: Information capture and storage
- **Reporting Systems**: Analytics and business intelligence
- **Compliance Management**: Regulatory adherence
- **Change Management**: Process updates and training
- **Performance Metrics**: KPIs and measurement systems

### Typical Requirements Patterns
- Process requirements (workflow steps, approval chains)
- Compliance requirements (regulations, standards)
- Performance requirements (cycle time, accuracy)
- User requirements (usability, accessibility)
- Reporting requirements (metrics, dashboards)

### EARS Notation Examples
- WHEN an expense report is submitted, THE approval system SHALL route to the appropriate manager
- IF the expense amount exceeds $1000, THEN THE system SHALL require additional approval
- WHERE personal data is processed, THE compliance officer SHALL ensure GDPR compliance
- THE approval process SHALL complete within 48 hours for standard expense reports
- WHEN generating monthly reports, THE finance system SHALL include all transactions from the previous month
- DURING the annual audit, THE compliance team SHALL provide access to all required documentation

### Common Design Patterns
- Business Process Modeling (BPMN)
- Workflow Automation
- Document Management
- Case Management
- Service-Oriented Architecture (SOA)

## Healthcare Projects

### Common Components
- **Patient Management**: Registration, records, scheduling
- **Clinical Systems**: Electronic health records, orders, results
- **Medical Devices**: Diagnostic equipment, monitoring systems
- **Pharmacy Systems**: Medication management, dispensing
- **Laboratory Systems**: Testing, results reporting
- **Billing Systems**: Insurance, claims, payments
- **Compliance Systems**: HIPAA, FDA, accreditation
- **Emergency Systems**: Critical care, alerts, response

### Typical Requirements Patterns
- Clinical requirements (patient care, treatment protocols)
- Safety requirements (medication safety, infection control)
- Privacy requirements (HIPAA compliance, data security)
- Regulatory requirements (FDA, Joint Commission)
- Interoperability requirements (HL7, FHIR standards)

### EARS Notation Examples
- WHEN a patient is registered, THE system SHALL verify insurance eligibility in real-time
- IF a medication allergy is detected, THEN THE prescribing system SHALL display an alert
- WHERE protected health information is stored, THE security system SHALL enforce role-based access
- THE electronic health record SHALL maintain audit trails for all access and modifications
- WHEN processing laboratory orders, THE system SHALL use HL7 v2.5.1 messaging format
- DURING patient care, THE clinical decision support SHALL provide evidence-based recommendations

### Common Design Patterns
- Clinical Workflow Engines
- Health Information Exchange (HIE)
- Clinical Decision Support Systems
- Telemedicine Platforms
- Population Health Management

## Financial Services Projects

### Common Components
- **Account Management**: Customer accounts, balances, transactions
- **Trading Systems**: Order execution, market data, risk management
- **Compliance Systems**: Regulatory reporting, AML, KYC
- **Payment Processing**: Transactions, settlements, clearing
- **Risk Management**: Credit risk, market risk, operational risk
- **Customer Service**: Support, inquiries, dispute resolution
- **Security Systems**: Fraud detection, authentication, encryption
- **Reporting Systems**: Regulatory reports, analytics, dashboards

### Typical Requirements Patterns
- Security requirements (encryption, authentication, audit trails)
- Compliance requirements (SOX, PCI-DSS, GDPR)
- Performance requirements (transaction processing, real-time updates)
- Reliability requirements (uptime, disaster recovery)
- Risk requirements (fraud detection, limit checking)

### EARS Notation Examples
- WHEN a trade is executed, THE risk system SHALL verify position limits in real-time
- IF suspicious activity is detected, THEN THE AML system SHALL generate an alert within 5 minutes
- WHERE customer data is processed, THE security system SHALL implement end-to-end encryption
- THE trading system SHALL process 10,000 transactions per second with 99.99% uptime
- WHEN generating regulatory reports, THE compliance system SHALL follow SEC Rule 17a-4 requirements
- DURING market hours, THE market data feed SHALL maintain latency below 10 milliseconds

### Common Design Patterns
- Event-Driven Architecture
- Microservices for Trading
- Real-time Processing
- High-Frequency Trading Systems
- Blockchain for Settlement

## Customization Guidelines

### Selecting Appropriate Templates

1. **Identify Primary Domain**: Choose the template that best matches your project's main focus
2. **Blend Templates**: Combine elements from multiple templates for hybrid projects
3. **Adapt Terminology**: Modify component names and terminology to match your organization
4. **Consider Stakeholders**: Use language familiar to all project stakeholders
5. **Scale Appropriately**: Adjust complexity based on project size and scope

### Domain-Specific Considerations

**Regulatory Compliance**:
- Healthcare: HIPAA, FDA, HITECH
- Finance: SOX, PCI-DSS, GDPR, AML regulations
- Construction: OSHA, building codes, environmental regulations
- Manufacturing: ISO standards, safety regulations

**Quality Standards**:
- Software: ISO/IEC 27001, CMMI
- Healthcare: Joint Commission, ISO 9001
- Manufacturing: ISO 9001, Six Sigma
- Finance: Basel III, SOC reports

**Performance Metrics**:
- Software: Response time, throughput, availability
- Healthcare: Patient outcomes, wait times, readmission rates
- Manufacturing: Production rate, defect rate, OEE
- Finance: Transaction speed, risk metrics, customer satisfaction

### Template Customization Process

1. **Review Standard Template**: Start with the closest matching template
2. **Identify Gaps**: Determine what's missing for your specific context
3. **Add Domain-Specific Components**: Include industry-specific elements
4. **Adjust Terminology**: Use your organization's preferred terms
5. **Validate with Stakeholders**: Ensure the template meets all stakeholder needs
6. **Iterate**: Refine based on feedback and usage patterns
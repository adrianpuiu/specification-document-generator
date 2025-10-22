# Implementation Plan

- [ ] 1. [Task description with primary objective]
  - [Implement specific component in specific file]
  - [Add initialization with dependencies]
  - [Create core methods with functionality]
  - [Implement error handling and logging]
  - [Add configuration support]
  - _Requirements: X.Y, X.Z, A.B, A.C_

- [ ] 2. [Data model or configuration task]
  - [Create model/dataclass structure]
  - [Add all required fields with proper types]
  - [Implement serialization methods]
  - [Add validation and documentation]
  - _Requirements: A.B, A.C, D.E_

- [ ] 3. [Service or business logic task]
  - [Implement service class with business logic]
  - [Add methods for core operations]
  - [Handle integration with other services]
  - [Implement error scenarios and recovery]
  - [Add logging and monitoring]
  - _Requirements: X.Y, X.Z, Y.Z, Z.A_

- [ ] 4. [API or interface task]
  - [Create API endpoints or interfaces]
  - [Implement request/response handling]
  - [Add validation and error responses]
  - [Document API contracts]
  - [Add authentication/authorization if needed]
  - _Requirements: Y.Z, Y.A, Z.B, Z.C_

- [ ] 5. [Integration or external system task]
  - [Implement integration with external systems]
  - [Add client or adapter classes]
  - [Handle communication protocols]
  - [Implement retry logic and error handling]
  - [Add configuration for external connections]
  - _Requirements: Z.A, Z.B, Z.C, W.X_

[Continue with additional tasks...]

Task Generation Rules:
- **Precise File Paths**: Always specify exact file location
  - Good: `backend/services/position_price_monitor.py`
  - Bad: "monitoring service file"
- **Detailed Sub-steps**: Break complex tasks into specific actions
  - List every method to implement
  - Specify each field to add
  - Name specific functions and parameters
- **Requirements Traceability**:
  - EVERY task must have `_Requirements: X.Y, X.Z_` format
  - Reference acceptance criteria numbers, not whole requirements
  - List ALL applicable criteria numbers
- **Task Sizing**:
  - Each top-level task: 1-4 hours of work
  - If larger, break into sub-tasks (X.1, X.2)
  - No task should exceed 15 sub-steps
- **Continuous Numbering**:
  - Don't restart numbering between phases
  - If 5 tasks in Phase 1, Phase 2 starts with task 6
- **Implementation Order**:
  - Core models and configs first (tasks 1-3)
  - Service implementations next (tasks 4-7)
  - API integrations (tasks 8-10)
  - Testing last (tasks 11-13)

Approval Gate:
"Implementation plan created with [N] tasks covering all [M] acceptance criteria. Requirements traceability matrix complete. Type 'execute' to begin implementation or 'review' to see coverage analysis."
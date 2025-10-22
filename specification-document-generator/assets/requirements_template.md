# Requirements Document

## Introduction

[2-3 paragraphs describing the feature's purpose, business context, and high-level goals. Include what problem this solves and who benefits.]

## Glossary

- **[Technical Term]**: [Clear definition in business context]
- **[System Component]**: [What it is and its responsibility]
- **[Business Concept]**: [Definition relevant to this feature]
[Include 5-10 key terms that appear throughout the document]

## Requirements

### Requirement 1

**User Story:** As a [role], I want [capability], so that [business value]

#### Acceptance Criteria

1. WHEN [trigger event], THE [system component] SHALL [specific behavior]
2. IF [condition], THEN THE [system component] SHALL [response action]
3. WHERE [context/state], THE [system component] SHALL [expected behavior]
4. THE [system component] SHALL [continuous requirement or constraint]
5. WHEN [error condition], THE [system component] SHALL [error handling behavior]

### Requirement 2

**User Story:** As a [role], I want [capability], so that [business value]

#### Acceptance Criteria

1. WHEN [trigger], THE [component] SHALL [action]
2. WHERE [condition], THE [component] SHALL [behavior]
3. THE [component] SHALL [performance requirement with specific metric]
4. IF [failure scenario], THEN THE [component] SHALL [fallback behavior]
5. WHILE [ongoing state], THE [component] SHALL [continuous behavior]

[Continue pattern for all requirements...]

EARS Notation Rules:
- WHEN: Temporal triggers (user actions, system events)
- WHERE: Contextual conditions (states, locations, modes)
- IF/THEN: Conditional logic branches
- WHILE: Continuous/ongoing behaviors
- THE [component] SHALL: Mandatory, testable behavior
- Always specify WHICH component is responsible
- Include specific metrics (5 seconds, 500ms, 90%, etc.)

Approval Gate:
"Requirements documented with [N] functional requirements and [M] total acceptance criteria. Each criterion is numbered for precise task traceability. Review and type 'approved' to proceed to design phase."
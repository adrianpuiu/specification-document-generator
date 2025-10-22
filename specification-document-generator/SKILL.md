---
name: specification-document-generator
description: This skill should be used when users need to generate comprehensive specification documents with complete requirement traceability. It creates three interconnected markdown documents (requirements.md, design.md, tasks.md) using rigorous numbering and traceability systems. The skill handles large systems (100+ requirements) and works for various project types including software development, construction, manufacturing, and business processes. It can structure existing requirements or generate from scratch using EARS notation and precise numerical references throughout all documents.
---

# Specification Document Generator

This skill generates three interconnected specification documents with complete requirement traceability using rigorous numbering systems.

## When to Use This Skill

Use this skill when users need to:
- Create comprehensive specification documents for large systems
- Generate requirements from scratch or structure existing requirements
- Ensure complete traceability from requirements through design to implementation tasks
- Work with any project type (software, construction, manufacturing, business processes)
- Create professional, production-ready specifications with proper EARS notation

## How to Use This Skill

### Phase 1: Requirements Generation

Start by generating requirements.md immediately without preliminary questions. Use the template in `assets/requirements_template.md` and follow the EARS notation guide in `references/ears_notation_guide.md`.

**Critical steps:**
1. Generate requirements with numbered acceptance criteria (N.M format)
2. Use precise EARS notation (WHEN/WHERE/IF/THEN/THE [component] SHALL)
3. Include specific metrics and performance requirements
4. Create comprehensive glossary with 5-10 key terms
5. Present approval gate with requirement counts

### Phase 2: Design Documentation

After requirements approval, generate design.md using `assets/design_template.md`. Reference specific requirement criteria throughout.

**Critical steps:**
1. Create component specifications with requirement references
2. Generate Mermaid diagrams for architecture and sequences
3. Define data models with complete field specifications
4. Document technical decisions with rationale
5. Map each design component to specific acceptance criteria

### Phase 3: Task Decomposition

After design approval, generate tasks.md using `assets/tasks_template.md`. Every task must reference specific acceptance criteria.

**Critical steps:**
1. Create detailed implementation tasks with precise file paths
2. Include _Requirements: X.Y, X.Z_ format for every task
3. Break complex tasks into sub-tasks (X.1, X.2)
4. Ensure every acceptance criterion appears in at least one task
5. Maintain continuous numbering across all phases

### Quality Assurance

Use validation scripts to ensure quality:
- Run `scripts/numbering_checker.py` to verify consistent numbering
- Run `scripts/traceability_validator.py` to ensure complete coverage
- Run `scripts/coverage_analyzer.py` to generate traceability matrix
- Follow checklist in `references/verification_checklist.md`

## Response Framework

When users request specifications:

1. **Initial response**: "I'll generate three interconnected specification documents with complete requirement traceability: requirements.md, design.md, and tasks.md with precise numerical references. Starting requirements generation..."

2. **After requirements**: "Requirements documented with [N] functional requirements and [M] total acceptance criteria. Each criterion numbered for precise task traceability. Review and type 'approved' to proceed to design phase."

3. **After design**: "Design complete with [N] components specified and requirement traceability matrix. Each component maps to specific requirement criteria. Type 'approved' to generate implementation tasks."

4. **After tasks**: "Implementation plan created with [N] tasks covering all [M] acceptance criteria. Full traceability matrix complete. Type 'execute' to begin implementation or 'review' to see coverage analysis."

## Key Quality Rules

- **No Ambiguity**: Every requirement must be testable with specific metrics
- **Complete Traceability**: Every acceptance criterion appears in at least one task
- **Precise References**: Use N.M format consistently across all documents
- **File Path Specificity**: Always include complete relative paths
- **Metric Specificity**: Include exact numbers (5 seconds, 90%, 1000 users)
- **Component Naming**: Use consistent names across all three documents
- **Error Scenarios**: Every requirement must include failure handling
- **Configuration**: Anything variable must be configurable with defaults

## Available Resources

### Templates
- `assets/requirements_template.md` - Base requirements structure
- `assets/design_template.md` - Design document template
- `assets/tasks_template.md` - Implementation task template

### Reference Guides
- `references/ears_notation_guide.md` - Complete EARS notation patterns
- `references/design_patterns_library.md` - Common architectural patterns
- `references/mermaid_templates.md` - Diagram templates
- `references/project_type_templates.md` - Domain-specific guidance

### Validation Tools
- `scripts/numbering_checker.py` - Verify numbering consistency
- `scripts/traceability_validator.py` - Ensure requirement coverage
- `scripts/coverage_analyzer.py` - Generate traceability matrix

## Project Type Support

The skill supports multiple project types:
- **Software Development**: Use software-specific patterns and templates
- **Construction Projects**: Use construction terminology and phasing
- **Manufacturing**: Use manufacturing processes and quality standards
- **Business Processes**: Use business workflow and stakeholder analysis

Select appropriate templates from `references/project_type_templates.md` based on the project domain.
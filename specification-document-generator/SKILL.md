---
name: specification-document-generator
description: This skill should be used when users need to generate comprehensive specification documents with complete requirement traceability. It creates five interconnected markdown documents (requirements.md, design.md, tasks.md, data_flow_specifications.md, traceability_matrix.md) using rigorous numbering and traceability systems. The skill handles large systems (100+ requirements) and works for various project types including software development, construction, manufacturing, and business processes. It includes comprehensive data flow mapping with visual diagrams and detailed processing pipelines. It can structure existing requirements or generate from scratch using EARS notation and precise numerical references throughout all documents.
---

# Specification Document Generator

This skill generates five interconnected specification documents with complete requirement traceability using rigorous numbering systems, including comprehensive data flow mapping with visual diagrams and detailed processing pipelines.

## When to Use This Skill

Use this skill when users need to:
- Create comprehensive specification documents for large systems
- Generate requirements from scratch or structure existing requirements
- Ensure complete traceability from requirements through design to implementation tasks
- Map comprehensive data flows with visual diagrams and processing pipelines
- Work with any project type (software, construction, manufacturing, business processes)
- Create professional, production-ready specifications with proper EARS notation
- Document end-to-end data movement and transformation processes

## How to Use This Skill

### Phase 1: Research and Requirements Generation

**STEP 0: Pre-Generation Setup (MANDATORY)**
Before beginning any research or document generation, execute the following mandatory setup:

```bash
# Get current date and time
CURRENT_DATE=$(date +"%Y-%m-%d")
CURRENT_YEAR=$(date +"%Y")
CURRENT_MONTH=$(date +"%m")
CURRENT_DAY=$(date +"%d")

echo "Specification Generation Started: $CURRENT_DATE"
echo "Reference Year: $CURRENT_YEAR"
echo "Document timestamps will use: $CURRENT_DATE"
```

**CRITICAL: All generated documents MUST use the current date from the system date command, not the AI's training data.**

**STEP 1: Real-Time Research (MANDATORY)**
Before generating requirements, perform comprehensive web research to gather current industry knowledge using the current year ($CURRENT_YEAR) from the system date:

1. **Current Technology Trends Research**:
   - Search for latest architectural patterns in the specific domain
   - Research current security frameworks and threat models
   - Investigate modern development tools and ecosystems
   - Find recent compliance requirements and regulations
   - Identify current best practices and anti-patterns

2. **Industry-Specific Research**:
   - Search for recent successful projects in the domain
   - Research current technology stack preferences
   - Investigate emerging technologies and adoption rates
   - Find current performance benchmarks and standards
   - Research current integration patterns and tools

3. **Regulatory and Compliance Research**:
   - Search for latest regulations affecting the domain
   - Research current compliance frameworks and standards
   - Investigate recent legal requirements and data privacy laws
   - Find current audit requirements and reporting standards
   - Research industry-specific regulatory guidance

**Research Sources to Consult:**
- Technical blogs (Martin Fowler, InfoQ, High Scalability)
- Developer communities (Stack Overflow, GitHub, Reddit programming)
- Conference talks (KubeCon, AWS re:Invent, GOTO, Devoxx)
- Official documentation (frameworks, cloud providers, security organizations)
- Industry publications and whitepapers
- Regulatory bodies and compliance organizations
- Recent project case studies and post-mortems

**STEP 2: Requirements Generation**
Use the template in `assets/requirements_template.md` and follow the EARS notation guide in `references/ears_notation_guide.md`.

**Critical steps:**
1. Generate requirements with numbered acceptance criteria (N.M format)
2. Use precise EARS notation (WHEN/WHERE/IF/THEN/THE [component] SHALL)
3. Incorporate current industry best practices from research
4. Include specific metrics and performance requirements
5. Address current security threats and compliance requirements
6. Reference current technology trends and tools
7. Create comprehensive glossary with 5-10 key terms
8. Present approval gate with requirement counts

### Phase 2: Research and Design Documentation

**STEP 1: Current Design Pattern Research (MANDATORY)**
Before generating design documentation, research current design patterns and architectures:

1. **Modern Architecture Research**:
   - Search for current architectural patterns (microservices, serverless, event-driven)
   - Research current technology stack combinations for the domain
   - Investigate modern integration patterns and API designs
   - Find current database and data storage patterns
   - Research current DevOps and infrastructure patterns

2. **Performance and Scalability Research**:
   - Search for current performance optimization techniques
   - Research current caching strategies and patterns
   - Investigate modern database optimization approaches
   - Find current scalability patterns and solutions
   - Research current monitoring and observability practices

3. **Security Architecture Research**:
   - Search for current security architecture patterns
   - Research current authentication and authorization frameworks
   - Investigate modern threat modeling approaches
   - Find current security best practices and patterns
   - Research current compliance and audit requirements

**STEP 2: Design Documentation Generation**
Generate design.md using `assets/design_template.md`. Reference specific requirement criteria throughout and incorporate current research findings.

**Critical steps:**
1. Create component specifications with requirement references
2. Generate Mermaid diagrams for architecture and sequences
3. Define data models with complete field specifications
4. Document technical decisions with rationale
5. Map each design component to specific acceptance criteria
6. Incorporate current architectural patterns and best practices from research
7. Include modern technology stack recommendations
8. Address current security architecture requirements

### Phase 3: Research and Design Documentation

**STEP 1: Current Design Pattern Research (MANDATORY)**
Before generating design documentation, research current design patterns and architectures:

1. **Modern Development Practices Research**:
   - Search for current development methodologies and practices
   - Research current tooling and frameworks in the domain
   - Investigate modern testing strategies and automation
   - Find current deployment and CI/CD practices
   - Research current code quality and review practices

2. **Current Technology Ecosystem Research**:
   - Search for current popular frameworks and libraries
   - Research current development tools and IDEs
   - Investigate modern testing frameworks and practices
   - Find current database and storage solutions
   - Research current monitoring and observability tools

3. **Security Implementation Research**:
   - Search for current secure coding practices
   - Research current security testing approaches
   - Investigate modern vulnerability scanning tools
   - Find current authentication and authorization libraries
   - Research current compliance and audit tools

**STEP 2: Task Generation**
Generate tasks.md using `assets/tasks_template.md`. Every task must reference specific acceptance criteria and incorporate current research findings.

**Critical steps:**
1. Create detailed implementation tasks with precise file paths
2. Include _Requirements: X.Y, X.Z_ format for every task
3. Break complex tasks into sub-tasks (X.1, X.2)
4. Ensure every acceptance criterion appears in at least one task
5. Maintain continuous numbering across all phases
6. Incorporate current development best practices and tools from research
7. Include modern testing and security implementation approaches
8. Reference current deployment and DevOps practices

### Phase 4: Data Flow Mapping

After design approval, generate data_flow_specifications.md with comprehensive data flow documentation.

**Critical steps:**
1. Create visual data flow architecture diagrams using Mermaid
2. Document detailed processing pipelines with step-by-step workflows
3. Map data transformation flows from external sources through storage to delivery
4. Define caching strategies, invalidation flows, and performance optimization
5. Document error handling, recovery flows, and monitoring strategies
6. Map real-time data distribution and quality assurance processes

### Phase 5: Task Generation and Implementation Planning

**After data flow approval**, generate comprehensive implementation tasks that reference all previous documents.

**STEP 1: Implementation Research (MANDATORY)**
Before generating implementation tasks, research current development practices and tools:

1. **Modern Development Practices Research**:
   - Search for current development methodologies and practices
   - Research current tooling and frameworks in the domain
   - Investigate modern testing strategies and automation
   - Find current deployment and CI/CD practices
   - Research current code quality and review practices

2. **Current Technology Ecosystem Research**:
   - Search for current popular frameworks and libraries
   - Research current development tools and IDEs
   - Investigate modern testing frameworks and practices
   - Find current database and storage solutions
   - Research current monitoring and observability tools

3. **Security Implementation Research**:
   - Search for current secure coding practices
   - Research current security testing approaches
   - Investigate modern vulnerability scanning tools
   - Find current authentication and authorization libraries
   - Research current compliance and audit tools

**STEP 2: Task Generation**
Generate tasks.md using `assets/tasks_template.md`. Reference requirements, design components, AND data flows:

**Critical steps:**
1. Create detailed implementation tasks with precise file paths
2. Include _Requirements: X.Y, X.Z_ format for every task
3. Break complex tasks into sub-tasks (X.1, X.2)
4. Ensure every acceptance criterion appears in at least one task
5. Maintain continuous numbering across all phases
6. Incorporate current development best practices and tools from research
7. Include modern testing and security implementation approaches
8. Reference data flow specifications for implementation guidance
9. Include design component references for architectural alignment

### Phase 6: Traceability Matrix Generation

After task approval, generate traceability_matrix.md with complete coverage analysis.

**Critical steps:**
1. Create comprehensive requirement-to-component mapping
2. Map design components to implementation tasks with traceability
3. Validate 100% requirement coverage across all documents
4. Include complexity assessment and risk analysis
5. Document quality gates and validation procedures

### Quality Assurance

Use validation scripts to ensure quality:
- Run `scripts/numbering_checker.py` to verify consistent numbering
- Run `scripts/traceability_validator.py` to ensure complete coverage
- Run `scripts/coverage_analyzer.py` to generate traceability matrix
- Follow checklist in `references/verification_checklist.md`

## Response Framework

When users request specifications:

**MANDATORY PRE-GENERATION CHECKLIST:**

1. **Execute Date Command**:
   ```bash
   CURRENT_DATE=$(date +"%Y-%m-%d")
   CURRENT_YEAR=$(date +"%Y")
   echo "Specification Generation Started: $CURRENT_DATE"
   ```

2. **Verify Current Year**: Confirm that $CURRENT_YEAR matches the actual current year from the system date command, not the AI's training data.

3. **Real-Time Research Validation**: Verify that web search queries use the current year ($CURRENT_YEAR) from system date.

**Response Process:**

1. **Initial response**: "I'll generate five interconnected specification documents with complete requirement traceability: requirements.md, design.md, tasks.md, data_flow_specifications.md, and traceability_matrix.md with precise numerical references and comprehensive data flow mapping. First, let me get the current date and perform real-time research for [CURRENT_YEAR]..."

2. **After requirements**: "Requirements documented with [N] functional requirements and [M] total acceptance criteria. Each criterion numbered for precise task traceability. Review and type 'approved' to proceed to design phase."

3. **After design**: "Design complete with [N] components specified and requirement traceability matrix. Each component maps to specific requirement criteria. Type 'approved' to proceed to data flow mapping."

4. **After data flows**: "Data flow specifications complete with visual architecture diagrams, processing pipelines, caching strategies, and error handling flows. Type 'approved' to proceed to implementation task generation."

5. **After tasks**: "Implementation plan created with [N] tasks covering all [M] acceptance criteria with references to requirements, design components, and data flows. Full task traceability complete. Type 'approved' to generate final traceability matrix."

6. **After traceability**: "Complete specification set generated with 100% requirement coverage, comprehensive data flow mapping, detailed implementation tasks, and full traceability matrix. Type 'execute' to begin implementation or 'review' to see coverage analysis."

## Key Quality Rules

- **Current Date Usage**: MUST use system date command (`date +"%Y-%m-%d"`) for all timestamps, NEVER use AI training data dates
- **Real-Time Research**: MUST perform web research using current year from system date, not stale knowledge
- **No Ambiguity**: Every requirement must be testable with specific metrics
- **Complete Traceability**: Every acceptance criterion appears in at least one task and data flow
- **Precise References**: Use N.M format consistently across all documents
- **File Path Specificity**: Always include complete relative paths
- **Metric Specificity**: Include exact numbers (5 seconds, 90%, 1000 users)
- **Component Naming**: Use consistent names across all five documents
- **Data Flow Mapping**: Every data transformation must be visually mapped with detailed processing
- **Error Scenarios**: Every requirement must include failure handling and recovery flows
- **Configuration**: Anything variable must be configurable with defaults
- **Performance Flows**: Include timing, caching, and optimization strategies in data flows

## CRITICAL ERROR PREVENTION

**MANDATORY DATE VERIFICATION:**
```bash
# Always execute this before any document generation
CURRENT_DATE=$(date +"%Y-%m-%d")
CURRENT_YEAR=$(date +"%Y")
echo "Using current date: $CURRENT_DATE"
echo "Using current year: $CURRENT_YEAR"
```

**RESEARCH VALIDATION:**
- All web searches MUST include current year from system date
- All regulatory references MUST be current year standards
- All technology trends MUST be researched for current year
- NEVER rely on AI training data cutoff dates

## Available Resources

### Templates
- `assets/requirements_template.md` - Base requirements structure
- `assets/design_template.md` - Design document template
- `assets/tasks_template.md` - Implementation task template
- `assets/data_flow_template.md` - Data flow mapping template
- `assets/traceability_matrix_template.md` - Traceability matrix template

### Reference Guides
- `references/ears_notation_guide.md` - Complete EARS notation patterns
- `references/design_patterns_library.md` - Common architectural patterns
- `references/mermaid_templates.md` - Diagram templates
- `references/data_flow_patterns.md` - Data flow mapping patterns and best practices
- `references/cache_strategies.md` - Caching and performance optimization patterns
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
# Specification Architect AI Skill

## 📦 Installation

### Option 1: Install from this Repository

```bash
/plugin marketplace add adrianpuiu/specification-document-generator
/plugin install specification-architect@specification-document-generator
```

### Option 2: Install from Claude Skills Marketplace

```bash
/plugin marketplace add adrianpuiu/claude-skills-marketplace
/plugin install specification-architect@claude-skills-marketplace
```

### Option 3: Direct Repository Clone

```bash
git clone https://github.com/adrianpuiu/specification-document-generator.git
cd specification-document-generator
# Use the skill directly or install locally
```

## Overview

A rigorous, evidence-based system that generates six interconnected architectural documents while **eliminating "research slop"** and preventing AI-generated misinformation. Every technological decision is backed by verifiable sources with complete traceability from research through implementation.

## 🚨 CRITICAL: Preventing "Research Slop"

**The Problem**: AI generates content that is polished, articulate, and inspires "faith-like confidence," yet is often unverified and factually incorrect. This has led to:
- **Legal sanctions** for law firms submitting fabricated citations
- **Financial penalties** for consulting firms providing incorrect statistics
- **Professional ruin** from relying on plausible-sounding falsehoods

**Our Solution**: **Mandatory verification protocol** that transforms AI from "confident author" to "diligent research assistant" with auditable evidence trails.

## 🎯 Evidence-Based Architecture

**The quality of your architectural specification is directly proportional to the verifiability of your research evidence.**

### What This Skill Does

1. **Phase 0**: 🔍 **Verifiable Research** (Mandatory Web Search + Browsing + Citations)
2. **Phase 1**: Architectural Blueprint (Evidence-Based Component Mapping)
3. **Phase 2**: Requirements Generation (Research-Backed Acceptance Criteria)
4. **Phase 3**: Detailed Design (Source-Validated Specifications)
5. **Phase 4**: Task Decomposition (Traceable Implementation Plan)
6. **Phase 5**: Validation & Traceability (100% Coverage + Evidence Verification)

## 🚀 Example: Clear Input = Clear Output

### User Prompt (High Quality):
```
"I need to architect an inventory management system for a growing e-commerce business.
The system must handle 50,000 SKUs, integrate with our existing Shopify store,
and provide real-time stock updates. We need barcode scanning, low-stock alerts,
and supplier management. Please do NOT include POS functionality or customer-facing
features. Our team uses Node.js/React and we need cloud deployment with automatic backups."
```

### What This Prompt Provides:
✅ **Clear Business Context**: E-commerce inventory management
✅ **Specific Constraints**: 50,000 SKUs, Shopify integration, real-time updates
✅ **Technology Stack**: Node.js/React, cloud deployment
✅ **Clear Scope Boundaries**: No POS, no customer-facing features
✅ **Success Metrics**: Barcode scanning, stock alerts, supplier management

### Resulting Architecture Quality:
🎯 **Clear Component Boundaries**: Each service has single responsibility
🎯 **Explicit Data Flow**: Complete journey from barcode scan to inventory update
🎯 **Defined Integration Points**: Shopify API, backup systems, cloud infrastructure
🎯 **Traceable Requirements**: Every feature traced to implementation tasks
🎯 **No Scope Creep**: Clear boundaries prevent "feature additions"

## 📋 Generated Documents

1. **research.md** - Web search findings, technology comparison, stack selection (NEW!)
2. **blueprint.md** - Component mapping, data flow diagrams, integration points
3. **requirements.md** - Testable acceptance criteria with component assignments
4. **design.md** - Detailed component specifications and interfaces
5. **tasks.md** - Implementation plan with requirement traceability
6. **validation.md** - Automated validation confirming 100% coverage

## ✨ Key Features

- **🚫 Research Slop Prevention**: Mandatory verification eliminates AI-generated misinformation
- **🔍 Evidence-Based Research**: Every claim supported by browsed sources with citations
- **📋 Citation Protocol**: Strict `[cite:INDEX]` format creates auditable evidence trails
- **🛡️ Professional Standards**: Prevents legal sanctions, financial penalties, and professional ruin
- **Automated Validation**: Python script ensures 100% requirements coverage + evidence verification
- **Source Verification**: Mandatory browsing of sources, not just search snippets
- **Template Enforcement**: Guarantees consistency and completeness
- **Component Consistency**: Exact name matching across all documents
- **Traceability Matrix**: Complete mapping from requirements to tasks
- **Quality Gates**: Sequential approval process with evidence verification

## 🔍 Phase 0: VERIFIABLE Research - ANTI-SLOP PROTOCOL

**CRITICAL**: This phase prevents the exact types of AI errors that cause legal sanctions and professional ruin.

### Mandatory Verification Process:
1. **Search THEN Browse**: Use WebSearch to find sources, then WebFetch to read actual content
2. **NO Search Snippets**: You MUST read full source content, not just search results
3. **Cite Every Claim**: Every factual statement MUST end with `[cite:INDEX]` citation
4. **Evidence-Based Decisions**: Technology choices only from verified sources
5. **Auditable Trail**: Complete citation trail from claim to source

### Examples of What We Prevent:
❌ **Research Slop**: "Node.js is great for real-time apps"
✅ **Evidence-Based**: "Node.js excels at real-time applications due to its event-driven, non-blocking I/O model [cite:1]"

❌ **Research Slop**: "TypeScript reduces errors"
✅ **Evidence-Based**: "TypeScript adds static typing that reduces runtime errors by approximately 15% in large codebases [cite:2]"

### Professional Impact:
This protocol prevents the types of errors that have led to:
- **Legal sanctions** for law firms (fabricated citations)
- **Financial penalties** for consulting firms (incorrect statistics)
- **Professional ruin** from AI-generated misinformation

## 🎖️ Critical Success Factors

### 1. Research-Driven Decisions
Never skip Phase 0! Web research ensures:
- Current best practices and patterns
- Proven technology stacks
- Industry-specific considerations
- Avoidance of outdated approaches

### 2. Component Clarity
Each component must have a single, well-defined responsibility. If you find yourself saying "and also," split into multiple components.

### 2. Data Flow Visualization
Map how data moves through the system from input to output. The Mermaid diagram should show the complete journey.

### 3. Integration Points
Clearly define all APIs, protocols, and external system connections. Specify data formats, authentication, and error handling.

### 4. Boundaries Setting
Explicitly define what's in scope vs. out of scope to prevent scope creep and enable accurate estimation.

## 🔧 Usage

1. **Provide Clear Requirements**: Include business objectives, constraints, and scope boundaries
2. **Follow Sequential Phases**: Each phase builds upon the previous one
3. **Review Quality Gates**: Ensure each phase meets quality criteria before proceeding
4. **Validate Traceability**: Use the automated validator to confirm complete coverage

## 📊 Validation Example

```
Validation Report:
- Total Acceptance Criteria: 28
- Criteria Covered by Tasks: 28
- Coverage Percentage: 100%
- Invalid References: 0
✅ Plan validated and ready for execution
```

## 🎯 Bottom Line

**Clear upfront goals + structured methodology = high-quality architectural specifications**

This skill transforms vague project ideas into concrete, implementable plans with guaranteed traceability from business requirements to implementation tasks.

---

*"The best architectural plans come from the clearest upfront thinking."*
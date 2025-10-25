# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Specification Architect** - an AI skill that generates rigorous, evidence-based architectural documentation with complete traceability. It implements a 6-phase process that eliminates "research slop" by mandating verification of all claims through web browsing and citations.

## Core Commands

### Validation (Most Common)
```bash
# Primary validation - ensures 100% requirements coverage
python validate_specifications.py

# With options
python validate_specifications.py --path ./specs --verbose --generate-validation

# Advanced traceability validation
python scripts/traceability_validator.py
```

### Cross-Platform Helpers
```bash
# Linux/macOS
./validate.sh --verbose --generate

# Windows
validate.bat --verbose --generate
```

## Critical Methodology Rules

### 1. Evidence-Based Research (Phase 0)
- **MANDATORY**: Use WebSearch THEN WebFetch - never rely on search snippets
- **CITATION FORMAT**: Every factual claim must end with `[cite:INDEX]`
- **VERIFICATION**: Read full source content before making claims
- **EVIDENCE TRAIL**: Create auditable trail from claim to source

### 2. Document Generation Sequence
1. **research.md** - Verified research with citations (NEW anti-slop phase)
2. **blueprint.md** - Component architecture and data flow
3. **requirements.md** - Acceptance criteria with component assignments
4. **design.md** - Detailed component specifications
5. **tasks.md** - Implementation tasks with requirement traceability
6. **validation.md** - Automated validation results

### 3. Quality Gates
- Each phase requires explicit approval before proceeding
- Component names must match EXACTLY across all documents
- 100% requirements coverage is mandatory for validation success
- Template format must be followed precisely

## Architecture Understanding

### Core Components
- **Validation Engine**: Python-based multi-layer validation system
- **Template System**: Enforces consistent document structure
- **Traceability Matrix**: Maps requirements to implementation tasks
- **Evidence Protocol**: Prevents AI-generated misinformation

### Key Files
- `validate_specifications.py` - Main validation script (165 lines)
- `scripts/traceability_validator.py` - Advanced validation (340 lines)
- `SKILL.md` - Complete skill documentation (328 lines)
- `references/document_templates.md` - Template examples (448 lines)

### Validation Exit Codes
- **0**: Success (100% coverage achieved)
- **1**: Failure (missing files, incomplete coverage, format errors)

## Professional Standards

This system prevents:
- **Legal sanctions** from fabricated citations
- **Financial penalties** from incorrect statistics
- **Professional ruin** from AI-generated misinformation

### Anti-"Research Slop" Protocol
1. Search for sources
2. Browse and read full content
3. Cite every factual claim
4. Create auditable evidence trail
5. Never generate "facts" without verification

## Development Workflow

When working with this repository:

1. **Always run validation** after document changes: `python validate_specifications.py`
2. **Check sample outputs** in `assets/sample_outputs/` for format examples
3. **Follow templates** strictly from `references/document_templates.md`
4. **Verify research claims** with proper citation format
5. **Maintain traceability** - every requirement must map to tasks

## Quality Assurance

The validation system ensures:
- All required documents exist
- Component names are consistent across documents
- Requirements have 100% task coverage
- Citations follow proper format
- Templates are correctly implemented

**Remember**: This system prioritizes verifiable accuracy over polished but unverified content. When in doubt, find sources and cite them properly.
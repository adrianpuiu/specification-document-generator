# Specification Architect Skill

An AI skill that generates rigorous, evidence-based architectural documentation with complete traceability.

## Quick Start

### Generate Specification Documents

The skill follows a 6-phase sequential process:

1. **Phase 0: Verifiable Research** (research.md) - Evidence-based technology research with citations
2. **Phase 1: Blueprint** (blueprint.md) - Component architecture and data flow
3. **Phase 2: Requirements** (requirements.md) - Acceptance criteria with component assignments
4. **Phase 3: Design** (design.md) - Detailed component specifications
5. **Phase 4: Tasks** (tasks.md) - Implementation tasks with requirement traceability
6. **Phase 5: Validation** (validation.md) - Automated validation results

### Validation Commands

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

## Key Files

- **validate_specifications.py** - Main validation script
- **scripts/traceability_validator.py** - Advanced traceability validation
- **SKILL.md** - Complete skill documentation
- **references/document_templates.md** - Template examples and format specifications
- **assets/sample_outputs/** - Example generated documents

## Validation Exit Codes

- **0**: Success (100% coverage achieved)
- **1**: Failure (missing files, incomplete coverage, format errors)

## Evidence-Based Research Protocol

This skill implements a strict anti-"research slop" protocol:

1. **Search THEN Browse**: Use WebSearch to find sources, then WebFetch to read actual content
2. **Cite Every Claim**: Every factual statement must end with `[cite:INDEX]` citation
3. **Verify Sources**: Read full source content, not just search snippets
4. **Auditable Trail**: Complete citation trail from claim to source

## Quality Assurance

The validation system ensures:
- All required documents exist
- Component names are consistent across documents
- Requirements have 100% task coverage
- Citations follow proper format
- Templates are correctly implemented

## License

MIT

## Author

George A Puiu (puiu.adrian@gmail.com)

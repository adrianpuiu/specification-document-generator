# Validation Scripts Documentation

This directory includes automated validation scripts that verify complete traceability across all five specification documents.

## Quick Start

### Linux/macOS
```bash
# Make script executable
chmod +x validate.sh

# Basic validation
./validate.sh

# Validate specific directory
./validate.sh --path ./specs

# Generate validation.md
./validate.sh --generate

# Verbose output
./validate.sh --verbose
```

### Windows
```cmd
# Basic validation
validate.bat

# Validate specific directory
validate.bat --path .\specs

# Generate validation.md
validate.bat --generate

# Verbose output
validate.bat --verbose
```

### Python (Cross-Platform)
```bash
# Basic validation
python validate_specifications.py

# Validate specific directory
python validate_specifications.py --path ./specs

# Generate validation.md
python validate_specifications.py --generate-validation

# JSON output
python validate_specifications.py --json

# Verbose mode
python validate_specifications.py --verbose
```

## What Gets Validated

The scripts perform comprehensive validation checks:

1. **File Presence**
   - blueprint.md exists
   - requirements.md exists
   - design.md exists
   - tasks.md exists

2. **Component Consistency**
   - All components from blueprint.md are used in requirements.md
   - No undefined components are referenced
   - Component names match exactly (case-sensitive)

3. **Requirements Format**
   - Requirement numbers: "### Requirement N: [Name]"
   - Acceptance criteria: "N. WHEN ... THE **ComponentName** SHALL ..."
   - Criteria use decimal notation (1.1, 1.2, 2.1, etc.)

4. **Task Requirements Tags**
   - All tasks include `_Requirements: X.Y, X.Z, ..._` tags
   - All referenced criteria IDs are valid
   - Format is correct with underscores and spaces

5. **Traceability Coverage**
   - Every acceptance criterion is referenced in at least one task
   - No orphaned requirements exist
   - No invalid requirement references

6. **Coverage Calculation**
   - Total acceptance criteria count
   - Number covered by tasks
   - Coverage percentage (must be 100%)

## Output Examples

### Success (100% Coverage)
```
================================================================================
SPECIFICATION VALIDATION REPORT
================================================================================

SUMMARY
--------------------------------------------------------------------------------
Total Acceptance Criteria:     12
Criteria Covered by Tasks:     12
Coverage Percentage:           100.0%

COVERAGE STATUS
--------------------------------------------------------------------------------
✓ Covered Criteria:            12
✗ Missing Criteria:            0
! Invalid References:          0

VALIDATION STATUS
--------------------------------------------------------------------------------
✅ VALIDATION PASSED
All acceptance criteria are fully traced to implementation tasks.
```

### Failure (Incomplete Coverage)
```
MISSING CRITERIA (Not covered by any task)
--------------------------------------------------------------------------------
  - 3.1
  - 4.2

VALIDATION STATUS
--------------------------------------------------------------------------------
❌ VALIDATION FAILED
  - 2 acceptance criteria are not covered by tasks
```

## Command Options

### --path DIR
Path to directory containing specification documents.

**Default**: `.` (current directory)

```bash
python validate_specifications.py --path /path/to/specs
```

### --verbose
Enable detailed output showing extraction progress.

```bash
./validate.sh --verbose
```

Shows:
- Components found
- Requirements extracted
- Tasks parsed
- Validation steps

### --generate-validation
Generate or update `validation.md` file with report.

```bash
python validate_specifications.py --generate-validation
```

Creates `validation.md` with:
- Traceability matrix
- Coverage analysis
- Validation status

### --json
Output results as JSON instead of human-readable text.

```bash
python validate_specifications.py --json
```

Output:
```json
{
  "total_criteria": 12,
  "covered_criteria": 12,
  "missing_criteria": [],
  "coverage_percentage": 100.0,
  "is_valid": true,
  "errors": [],
  "warnings": []
}
```

## Exit Codes

- **0** = Success (validation passed, 100% coverage)
- **1** = Failure (incomplete coverage or errors)

Use in scripts:
```bash
python validate_specifications.py --path ./specs
if [ $? -eq 0 ]; then
    echo "Deployment approved"
    ./deploy.sh
else
    echo "Validation failed - fix requirements first"
    exit 1
fi
```

## Document Format Requirements

For validation to work correctly:

### Blueprint.md Format
```markdown
## 3. Core System Components

| Component Name | Responsibility |
|---|---|
| **AuthenticationComponent** | Handles user authentication |
| **DatabaseAdapter** | Manages database connections |
```

### Requirements.md Format
```markdown
### Requirement 1: User Authentication

#### Acceptance Criteria

1. WHEN user submits credentials, THE **AuthenticationComponent** SHALL validate them.

2. WHEN validation succeeds, THE **AuthenticationComponent** SHALL return a session token.
```

### Tasks.md Format
```markdown
## Task 1: Implement AuthenticationComponent

- [ ] 1.1 Create AuthenticationComponent class
- [ ] 1.2 Implement validation method
- [ ] 1.3 Add unit tests
- _Requirements: 1.1, 1.2_
```

## Troubleshooting

### Components not extracted
**Issue**: "No components found in blueprint.md"

**Solution**: Verify format matches exactly:
- `| **ComponentName** | description |`
- Component name must be between `**` markers
- Must be in a markdown table

### Requirements not found
**Issue**: "No requirements found"

**Solution**: Use exact format:
- `### Requirement N: [Name]`
- Criteria: `N. WHEN ... THE **Component** SHALL ...`
- Must have numbers and exact spacing

### Missing criteria list has items
**Issue**: Validation fails with missing criteria

**Solution**: Add `_Requirements:` tags to all tasks:
- Format: `_Requirements: 1.1, 1.2, 3.1_`
- Underscore prefix and suffix
- Space after colon
- IDs separated by commas

### Invalid component names
**Issue**: "Unknown component: ComponentName"

**Solution**: Check spelling and capitalization:
- Use exact names from blueprint
- Names are case-sensitive
- Verify in requirements criteria

## Integration Examples

### GitHub Actions
```yaml
name: Validate Specifications

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - name: Validate specifications
        run: |
          python validate_specifications.py \
            --path ./specs \
            --generate-validation
```

### GitLab CI
```yaml
validate_specs:
  image: python:3.9
  script:
    - python validate_specifications.py --path ./specs --generate-validation
  only:
    changes:
      - specs/**
```

### Local Pre-commit Hook
```bash
#!/bin/bash
python validate_specifications.py --path ./specs
if [ $? -ne 0 ]; then
    echo "Specifications validation failed!"
    exit 1
fi
```

## Performance

- Validates 100+ requirements in <1 second
- Handles 1000+ tasks efficiently
- Minimal memory usage
- No external dependencies

## Requirements

- **Python**: 3.7 or higher
- **Dependencies**: None (standard library only)

## File Structure

```
specification-architect-skill/
├── validate_specifications.py      # Main validation script
├── validate.bat                    # Windows helper
├── validate.sh                     # Linux/macOS helper  
├── VALIDATION_SCRIPTS_README.md   # This file
├── SKILL.md                        # Full skill documentation
├── TEMPLATE_REFERENCE.md          # Document templates
├── USAGE_GUIDE.md                 # Phase-by-phase guide
└── README.md                       # Quick start
```

## Complete Validation Workflow

1. **Write Specifications**
   - Create blueprint.md
   - Create requirements.md
   - Create design.md
   - Create tasks.md

2. **Run Validation**
   ```bash
   python validate_specifications.py --path ./specs --verbose
   ```

3. **Review Results**
   - Check coverage percentage
   - Review missing criteria (if any)
   - Review invalid references (if any)

4. **Fix Issues**
   - Add missing requirement tags to tasks
   - Fix invalid requirement references
   - Update requirements if needed

5. **Validate Again**
   ```bash
   python validate_specifications.py --path ./specs
   ```

6. **Generate Report**
   ```bash
   python validate_specifications.py --path ./specs --generate-validation
   ```

7. **Ready to Execute**
   - validation.md confirms 100% coverage
   - Commit all spec files
   - Begin implementation

## API Usage (Python)

Use the validator as a Python module:

```python
from validate_specifications import SpecificationValidator

# Create validator
validator = SpecificationValidator("./specs", verbose=True)

# Run validation
result = validator.validate_all()

# Check results
if result.is_valid:
    print("✅ Validation passed!")
    print(f"Coverage: {result.coverage_percentage}%")
else:
    print(f"❌ {len(result.missing_criteria)} missing criteria")
    
# Generate and save validation.md
validator.save_validation_markdown()
```

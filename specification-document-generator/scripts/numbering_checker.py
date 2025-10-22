#!/usr/bin/env python3
"""
Numbering Checker for Specification Documents
Verifies consistent numbering across requirements.md, design.md, and tasks.md
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

def extract_requirement_numbers(content: str) -> List[Tuple[str, int]]:
    """Extract requirement numbers and their acceptance criteria counts"""
    pattern = r'### Requirement (\d+)'
    requirements = []

    for match in re.finditer(pattern, content):
        req_num = int(match.group(1))

        # Find acceptance criteria for this requirement
        start_pos = match.start()
        next_req_pos = content.find('### Requirement', start_pos + 1)
        section_content = content[start_pos:next_req_pos] if next_req_pos != -1 else content[start_pos:]

        # Count acceptance criteria
        ac_pattern = r'#### Acceptance Criteria.*?\n((?:\d+\..*\n?)*)'
        ac_match = re.search(ac_pattern, section_content, re.DOTALL)
        if ac_match:
            ac_content = ac_match.group(1)
            ac_count = len(re.findall(r'^\d+\.', ac_content, re.MULTILINE))
            requirements.append((f"Requirement {req_num}", ac_count))

    return requirements

def extract_task_requirements(content: str) -> List[str]:
    """Extract requirement references from tasks"""
    pattern = r'_Requirements: ([\d.,\s]+)_'
    references = []

    for match in re.finditer(pattern, content):
        req_refs = match.group(1).strip()
        # Split by comma and clean up
        for ref in req_refs.split(','):
            ref = ref.strip()
            if ref:
                references.append(ref)

    return references

def extract_design_references(content: str) -> List[str]:
    """Extract requirement references from design document"""
    pattern = r'\((\d+\.\d+)\)'
    references = []

    for match in re.finditer(pattern, content):
        references.append(match.group(1))

    return references

def validate_numbering_consistency(requirements_file: Path, design_file: Path, tasks_file: Path) -> Dict[str, List[str]]:
    """Validate numbering consistency across all documents"""
    issues = []

    # Read files
    req_content = requirements_file.read_text() if requirements_file.exists() else ""
    design_content = design_file.read_text() if design_file.exists() else ""
    tasks_content = tasks_file.read_text() if tasks_file.exists() else ""

    # Extract requirements from requirements.md
    requirements = extract_requirement_numbers(req_content)

    # Build expected acceptance criteria list
    expected_criteria = set()
    for req_name, ac_count in requirements:
        req_num = req_name.split()[-1]
        for i in range(1, ac_count + 1):
            expected_criteria.add(f"{req_num}.{i}")

    # Check design references
    design_refs = extract_design_references(design_content)
    for ref in design_refs:
        if ref not in expected_criteria:
            issues.append(f"Design references non-existent criterion: {ref}")

    # Check task references
    task_refs = extract_task_requirements(tasks_content)
    for ref in task_refs:
        if ref not in expected_criteria:
            issues.append(f"Task references non-existent criterion: {ref}")

    # Check for missing references
    for criterion in expected_criteria:
        if criterion not in design_refs:
            issues.append(f"Criterion {criterion} not referenced in design")
        if criterion not in task_refs:
            issues.append(f"Criterion {criterion} not referenced in tasks")

    return {
        "issues": issues,
        "total_criteria": len(expected_criteria),
        "design_coverage": len(set(design_refs) & expected_criteria),
        "task_coverage": len(set(task_refs) & expected_criteria)
    }

def main():
    """Main validation function"""
    if len(sys.argv) < 2:
        print("Usage: python numbering_checker.py <project_directory>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    requirements_file = project_dir / "requirements.md"
    design_file = project_dir / "design.md"
    tasks_file = project_dir / "tasks.md"

    result = validate_numbering_consistency(requirements_file, design_file, tasks_file)

    if result["issues"]:
        print("❌ Numbering Issues Found:")
        for issue in result["issues"]:
            print(f"  - {issue}")
    else:
        print("✅ Numbering is consistent across all documents")

    print(f"\n📊 Coverage Summary:")
    print(f"  Total Acceptance Criteria: {result['total_criteria']}")
    print(f"  Design Document Coverage: {result['design_coverage']}/{result['total_criteria']}")
    print(f"  Tasks Document Coverage: {result['task_coverage']}/{result['total_criteria']}")

    return len(result["issues"])

if __name__ == "__main__":
    sys.exit(main())
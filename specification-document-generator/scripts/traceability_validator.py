#!/usr/bin/env python3
"""
Traceability Validator for Specification Documents
Ensures every acceptance criterion is traced through design to implementation
"""

import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass

@dataclass
class TraceabilityItem:
    """Represents a traceability item"""
    criterion: str
    in_design: bool = False
    in_tasks: bool = False
    design_components: List[str] = None
    task_items: List[str] = None

    def __post_init__(self):
        if self.design_components is None:
            self.design_components = []
        if self.task_items is None:
            self.task_items = []

class TraceabilityValidator:
    """Validates traceability across specification documents"""

    def __init__(self, project_dir: Path):
        self.project_dir = project_dir
        self.requirements_file = project_dir / "requirements.md"
        self.design_file = project_dir / "design.md"
        self.tasks_file = project_dir / "tasks.md"

    def extract_acceptance_criteria(self) -> Set[str]:
        """Extract all acceptance criteria from requirements.md"""
        if not self.requirements_file.exists():
            return set()

        content = self.requirements_file.read_text()
        criteria = set()

        # Find requirement sections
        req_pattern = r'### Requirement (\d+)'
        req_matches = list(re.finditer(req_pattern, content))

        for i, match in enumerate(req_matches):
            req_num = match.group(1)
            start_pos = match.end()

            # Find next requirement or end of file
            end_pos = (req_matches[i + 1].start()
                      if i + 1 < len(req_matches)
                      else len(content))

            section = content[start_pos:end_pos]

            # Extract acceptance criteria
            ac_pattern = r'#### Acceptance Criteria.*?\n((?:\d+\..*\n?)*)'
            ac_match = re.search(ac_pattern, section, re.DOTALL)

            if ac_match:
                ac_content = ac_match.group(1)
                ac_matches = re.finditer(r'^(\d+)\.\s*(.*)', ac_content, re.MULTILINE)

                for ac_match in ac_matches:
                    ac_num = ac_match.group(1)
                    criteria.add(f"{req_num}.{ac_num}")

        return criteria

    def extract_design_references(self) -> Dict[str, List[str]]:
        """Extract requirement references from design.md"""
        if not self.design_file.exists():
            return {}

        content = self.design_file.read_text()
        references = {}

        # Find component sections
        component_pattern = r'#### Component: ([^\n]+)'
        components = list(re.finditer(component_pattern, content))

        for i, match in enumerate(components):
            component_name = match.group(1)
            start_pos = match.start()

            # Find next component or end of section
            next_component = (components[i + 1].start()
                            if i + 1 < len(components)
                            else content.find('## ', start_pos + 1))

            if next_component == -1:
                next_component = len(content)

            section = content[start_pos:next_component]

            # Extract requirement references
            req_pattern = r'\((\d+\.\d+)\)'
            req_matches = re.findall(req_pattern, section)

            for req_ref in req_matches:
                if req_ref not in references:
                    references[req_ref] = []
                references[req_ref].append(component_name)

        return references

    def extract_task_references(self) -> Dict[str, List[str]]:
        """Extract requirement references from tasks.md"""
        if not self.tasks_file.exists():
            return {}

        content = self.tasks_file.read_text()
        references = {}

        # Find task items
        task_pattern = r'^- \[ \] (\d+(?:\.\d+)*)\.(.*)$'
        tasks = re.finditer(task_pattern, content, re.MULTILINE)

        for match in tasks:
            task_num = match.group(1)
            task_desc = match.group(2).strip()

            # Extract requirement references from task
            req_pattern = r'_Requirements: ([\d.,\s]+)_'
            req_match = re.search(req_pattern, task_desc)

            if req_match:
                req_refs = req_match.group(1).strip()
                for ref in req_refs.split(','):
                    ref = ref.strip()
                    if ref:
                        if ref not in references:
                            references[ref] = []
                        references[ref].append(f"Task {task_num}")

        return references

    def validate_traceability(self) -> Tuple[List[TraceabilityItem], Dict[str, int]]:
        """Perform complete traceability validation"""
        acceptance_criteria = self.extract_acceptance_criteria()
        design_refs = self.extract_design_references()
        task_refs = self.extract_task_references()

        traceability_items = []
        orphaned_design = []
        orphaned_tasks = []

        for criterion in acceptance_criteria:
            item = TraceabilityItem(
                criterion=criterion,
                in_design=criterion in design_refs,
                in_tasks=criterion in task_refs,
                design_components=design_refs.get(criterion, []),
                task_items=task_refs.get(criterion, [])
            )
            traceability_items.append(item)

        # Check for orphaned references
        for ref in design_refs:
            if ref not in acceptance_criteria:
                orphaned_design.extend(design_refs[ref])

        for ref in task_refs:
            if ref not in acceptance_criteria:
                orphaned_tasks.extend(task_refs[ref])

        stats = {
            "total_criteria": len(acceptance_criteria),
            "covered_in_design": len([item for item in traceability_items if item.in_design]),
            "covered_in_tasks": len([item for item in traceability_items if item.in_tasks]),
            "fully_covered": len([item for item in traceability_items if item.in_design and item.in_tasks]),
            "orphaned_design_refs": len(orphaned_design),
            "orphaned_task_refs": len(orphaned_tasks)
        }

        return traceability_items, stats

    def generate_traceability_matrix(self) -> str:
        """Generate a markdown traceability matrix"""
        items, stats = self.validate_traceability()

        matrix = "# Traceability Matrix\n\n"
        matrix += "| Requirement | Acceptance Criteria | In Design | In Tasks | Design Components | Task Items |\n"
        matrix += "|------------|--------------------|-----------|----------|-------------------|------------|\n"

        for item in items:
            req_num = item.criterion.split('.')[0]
            design_check = "✅" if item.in_design else "❌"
            task_check = "✅" if item.in_tasks else "❌"
            design_comps = ", ".join(item.design_components) if item.design_components else "None"
            task_items = ", ".join(item.task_items) if item.task_items else "None"

            matrix += f"| Req {req_num} | {item.criterion} | {design_check} | {task_check} | {design_comps} | {task_items} |\n"

        matrix += f"\n## Summary\n\n"
        matrix += f"- **Total Acceptance Criteria**: {stats['total_criteria']}\n"
        matrix += f"- **Covered in Design**: {stats['covered_in_design']}/{stats['total_criteria']}\n"
        matrix += f"- **Covered in Tasks**: {stats['covered_in_tasks']}/{stats['total_criteria']}\n"
        matrix += f"- **Fully Covered**: {stats['fully_covered']}/{stats['total_criteria']}\n"

        if stats['orphaned_design_refs'] > 0:
            matrix += f"- ⚠️ **Orphaned Design References**: {stats['orphaned_design_refs']}\n"

        if stats['orphaned_task_refs'] > 0:
            matrix += f"- ⚠️ **Orphaned Task References**: {stats['orphaned_task_refs']}\n"

        return matrix

def main():
    """Main validation function"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python traceability_validator.py <project_directory>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    validator = TraceabilityValidator(project_dir)

    items, stats = validator.validate_traceability()

    # Print validation results
    print("🔍 Traceability Validation Results")
    print("=" * 40)

    issues = []
    for item in items:
        if not item.in_design:
            issues.append(f"❌ {item.criterion} not referenced in design")
        if not item.in_tasks:
            issues.append(f"❌ {item.criterion} not referenced in tasks")

    if issues:
        print("\n❌ Traceability Issues:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("\n✅ Complete traceability achieved!")

    print(f"\n📊 Coverage Statistics:")
    print(f"  Total Acceptance Criteria: {stats['total_criteria']}")
    print(f"  Design Coverage: {stats['covered_in_design']}/{stats['total_criteria']} ({stats['covered_in_design']/stats['total_criteria']*100:.1f}%)")
    print(f"  Task Coverage: {stats['covered_in_tasks']}/{stats['total_criteria']} ({stats['covered_in_tasks']/stats['total_criteria']*100:.1f}%)")
    print(f"  Full Coverage: {stats['fully_covered']}/{stats['total_criteria']} ({stats['fully_covered']/stats['total_criteria']*100:.1f}%)")

    if stats['orphaned_design_refs'] > 0 or stats['orphaned_task_refs'] > 0:
        print(f"\n⚠️ Orphaned References:")
        print(f"  Design: {stats['orphaned_design_refs']}")
        print(f"  Tasks: {stats['orphaned_task_refs']}")

    # Generate traceability matrix file
    matrix_content = validator.generate_traceability_matrix()
    matrix_file = project_dir / "traceability_matrix.md"
    matrix_file.write_text(matrix_content)
    print(f"\n📄 Traceability matrix generated: {matrix_file}")

    return len(issues)

if __name__ == "__main__":
    import sys
    sys.exit(main())
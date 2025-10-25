#!/usr/bin/env python3
"""
Traceability validator for specification architect skill.
Validates that all requirements are covered by implementation tasks.
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set

class TraceabilityValidator:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.requirements = {}
        self.tasks = []
        self.research_citations = {}

    def parse_requirements(self, requirements_file: str) -> Dict:
        """Parse requirements.md to extract requirements and acceptance criteria."""
        req_file = self.base_path / requirements_file
        if not req_file.exists():
            raise FileNotFoundError(f"Requirements file not found: {requirements_file}")

        content = req_file.read_text(encoding='utf-8')

        # Split content by requirement headers and capture requirement numbers
        pattern = r'\n### Requirement (\d+): ([^\n]+)'
        matches = list(re.finditer(pattern, content))

        requirements = {}

        for match in matches:
            req_num = match.group(1).strip()
            req_title = match.group(2).strip()

            # Find the start and end of this requirement section
            start_pos = match.start()
            end_pos = content.find('\n### Requirement', start_pos + 1)
            if end_pos == -1:
                end_pos = len(content)

            # Extract this requirement's content
            section_content = content[start_pos:end_pos]

            # Find acceptance criteria within this section
            ac_match = re.search(r'#### Acceptance Criteria\n(.*?)(?=\n###|\n##|\Z)', section_content, re.DOTALL)
            if not ac_match:
                continue

            ac_text = ac_match.group(1).strip()

            
            # Parse acceptance criteria
            requirements[req_num] = {
                "title": req_title,
                "acceptance_criteria": {}
            }

            ac_pattern = r"(\d+)\.\s+(.+)"
            ac_matches = re.findall(ac_pattern, ac_text)
            for ac_num, ac_text in ac_matches:
                requirements[req_num]["acceptance_criteria"][f"{req_num}.{ac_num}"] = ac_text.strip()

        self.requirements = requirements
        return requirements

    def parse_tasks(self, tasks_file: str) -> List[Dict]:
        """Parse tasks.md to extract tasks and their requirement references."""
        task_file = self.base_path / tasks_file
        if not task_file.exists():
            raise FileNotFoundError(f"Tasks file not found: {tasks_file}")

        content = task_file.read_text(encoding='utf-8')

        # Parse tasks and requirement references
        task_pattern = r"- \[ \] (\d+).+?_Requirements: (.+?)_"
        matches = re.findall(task_pattern, content, re.MULTILINE | re.DOTALL)

        tasks = []
        for task_num, req_refs in matches:
            # Parse requirement references
            req_refs = [ref.strip() for ref in req_refs.split(",")]
            tasks.append({
                "task_id": task_num,
                "requirement_references": req_refs
            })

        self.tasks = tasks
        return tasks

    def validate_traceability(self) -> Tuple[Dict, List[str], List[str]]:
        """Validate that all requirements are covered by tasks."""
        all_criteria = set()
        for req_num, req_data in self.requirements.items():
            for ac_ref in req_data["acceptance_criteria"]:
                all_criteria.add(ac_ref)

        covered_criteria = set()
        invalid_references = set()

        for task in self.tasks:
            for req_ref in task["requirement_references"]:
                if req_ref in all_criteria:
                    covered_criteria.add(req_ref)
                else:
                    invalid_references.add(req_ref)

        missing_criteria = all_criteria - covered_criteria

        return {
            "total_criteria": len(all_criteria),
            "covered_criteria": len(covered_criteria),
            "coverage_percentage": (len(covered_criteria) / len(all_criteria) * 100) if all_criteria else 100
        }, list(missing_criteria), list(invalid_references)

    def validate_research_evidence(self, research_file: str = "example_research.md") -> Dict:
        """Validate research document for proper citations and evidence."""
        research_path = self.base_path / research_file
        if not research_path.exists():
            return {"valid": False, "error": f"Research file not found: {research_file}"}

        content = research_path.read_text(encoding='utf-8')

        validation_results = {
            "valid": True,
            "citation_errors": [],
            "missing_sources": [],
            "uncited_claims": [],
            "total_sources": 0,
            "total_citations": 0
        }

        # Extract source list (## 3. Browsed Sources section)
        source_pattern = r'## 3\. Browsed Sources\n(.*?)(?=\n##|\Z)'
        source_match = re.search(source_pattern, content, re.DOTALL)

        if not source_match:
            validation_results["valid"] = False
            validation_results["citation_errors"].append("Missing 'Browsed Sources' section")
            return validation_results

        sources_text = source_match.group(1)
        source_lines = [line.strip() for line in sources_text.split('\n') if line.strip()]

        # Extract source URLs and indices
        sources = {}
        for line in source_lines:
            source_match = re.match(r'- \[(\d+)\] (https?://\S+)', line)
            if source_match:
                index = source_match.group(1)
                url = source_match.group(2)
                sources[index] = url

        validation_results["total_sources"] = len(sources)

        # Check for citations in rationale section
        rationale_pattern = r'\| \*\*(.+?)\*\* \| (.+?) \|'
        rationale_matches = re.findall(rationale_pattern, content, re.DOTALL)

        total_citations = 0
        for technology, rationale in rationale_matches:
            # Find all citations in rationale
            citations = re.findall(r'\[cite:(\d+)\]', rationale)
            total_citations += len(citations)

            # Check each citation has corresponding source
            for citation in citations:
                if citation not in sources:
                    validation_results["citation_errors"].append(f"Citation [cite:{citation}] references non-existent source")
                    validation_results["valid"] = False

        validation_results["total_citations"] = total_citations

        # Check for factual claims without citations (simplified detection)
        # Look for sentences with specific numbers, percentages, or strong claims
        factual_claims = re.findall(r'[^.!?]*\d+(?:\.\d+)?%?[^.!?]*\.|[^.!?]*?(excellent|proven|ideal|best|optimal)[^.!?]*\.', content)

        for claim in factual_claims:
            if not re.search(r'\[cite:\d+\]', claim):
                validation_results["uncited_claims"].append(claim.strip())

        # Validate that we have both sources and citations
        if len(sources) == 0:
            validation_results["valid"] = False
            validation_results["citation_errors"].append("No sources found in research document")

        if total_citations == 0:
            validation_results["valid"] = False
            validation_results["citation_errors"].append("No citations found in technology rationales")

        # Check citation to source ratio (should have reasonable coverage)
        if total_citations < len(sources):
            validation_results["citation_errors"].append(f"Too few citations ({total_citations}) for number of sources ({len(sources)})")

        return validation_results

    def generate_validation_report(self, requirements_file: str = "requirements.md",
                                 tasks_file: str = "tasks.md",
                                 research_file: str = "example_research.md") -> str:
        """Generate a complete validation report."""

        self.parse_requirements(requirements_file)
        self.parse_tasks(tasks_file)

        validation_result, missing, invalid = self.validate_traceability()
        research_validation = self.validate_research_evidence(research_file)

        report = f"""# Validation Report

## 1. Requirements to Tasks Traceability Matrix

| Requirement | Acceptance Criterion | Implementing Task(s) | Status |
|---|---|---|---|"""

        # Generate traceability matrix
        for req_num, req_data in self.requirements.items():
            for ac_ref, ac_text in req_data["acceptance_criteria"].items():
                # Find tasks implementing this criterion
                implementing_tasks = []
                for task in self.tasks:
                    if ac_ref in task["requirement_references"]:
                        implementing_tasks.append(f"Task {task['task_id']}")

                status = "Covered" if implementing_tasks else "Missing"
                tasks_str = ", ".join(implementing_tasks) if implementing_tasks else "None"

                report += f"\n| {req_num} | {ac_ref} | {tasks_str} | {status} |"

        report += f"""

## 2. Coverage Analysis

### Summary
- **Total Acceptance Criteria**: {validation_result['total_criteria']}
- **Criteria Covered by Tasks**: {validation_result['covered_criteria']}
- **Coverage Percentage**: {validation_result['coverage_percentage']:.1f}%

### Detailed Status
- **Covered Criteria**: {[ref for ref in self._get_all_criteria() if ref in self._get_covered_criteria()]}
- **Missing Criteria**: {missing if missing else 'None'}
- **Invalid References**: {invalid if invalid else 'None'}

## 3. Research Evidence Validation

### Summary
- **Total Sources**: {research_validation['total_sources']}
- **Total Citations**: {research_validation['total_citations']}
- **Research Validation**: {'PASSED' if research_validation['valid'] else 'FAILED'}

### Evidence Quality
- **Citation Errors**: {len(research_validation['citation_errors'])}
- **Uncited Claims**: {len(research_validation['uncited_claims'])}
"""

        if research_validation['citation_errors']:
            report += "\n#### Citation Issues:\n"
            for error in research_validation['citation_errors']:
                report += f"- {error}\n"

        if research_validation['uncited_claims']:
            report += "\n#### Uncited Factual Claims:\n"
            for claim in research_validation['uncited_claims'][:5]:  # Limit to first 5
                report += f"- {claim}\n"
            if len(research_validation['uncited_claims']) > 5:
                report += f"- ... and {len(research_validation['uncited_claims']) - 5} more\n"

        report += """

## 4. Final Validation
"""

        requirements_valid = validation_result['coverage_percentage'] == 100 and not invalid
        research_valid = research_validation['valid']

        if requirements_valid and research_valid:
            report += f"[PASS] **VALIDATION PASSED**\n\nAll {validation_result['total_criteria']} acceptance criteria are fully traced to implementation tasks AND all research claims are properly cited with verifiable sources. The plan is validated and ready for execution."
        elif not requirements_valid and research_valid:
            report += f"[FAIL] **VALIDATION FAILED** - Requirements Issues\n\n{len(missing)} criteria not covered, {len(invalid)} invalid references. Research evidence is properly cited, but requirements traceability needs attention."
        elif requirements_valid and not research_valid:
            report += f"[FAIL] **VALIDATION FAILED** - Research Evidence Issues\n\nRequirements traceability is complete, but research evidence has {len(research_validation['citation_errors'])} citation errors and {len(research_validation['uncited_claims'])} uncited claims. This violates the evidence-based protocol and prevents professional use."
        else:
            report += f"[FAIL] **VALIDATION FAILED** - Multiple Issues\n\nRequirements: {len(missing)} criteria not covered, {len(invalid)} invalid references. Research: {len(research_validation['citation_errors'])} citation errors, {len(research_validation['uncited_claims'])} uncited claims."

        return report

    def _get_all_criteria(self) -> Set[str]:
        """Get all acceptance criteria references."""
        all_criteria = set()
        for req_num, req_data in self.requirements.items():
            for ac_ref in req_data["acceptance_criteria"]:
                all_criteria.add(ac_ref)
        return all_criteria

    def _get_covered_criteria(self) -> Set[str]:
        """Get all covered acceptance criteria references."""
        covered_criteria = set()
        all_criteria = self._get_all_criteria()

        for task in self.tasks:
            for req_ref in task["requirement_references"]:
                if req_ref in all_criteria:
                    covered_criteria.add(req_ref)

        return covered_criteria

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Validate specification architect traceability")
    parser.add_argument("--path", default=".", help="Base path containing specification files")
    parser.add_argument("--requirements", default="requirements.md", help="Requirements file name")
    parser.add_argument("--tasks", default="tasks.md", help="Tasks file name")
    parser.add_argument("--research", default="example_research.md", help="Research file name")

    args = parser.parse_args()

    try:
        validator = TraceabilityValidator(args.path)
        report = validator.generate_validation_report(args.requirements, args.tasks, args.research)
        print(report)

        # Exit with error code if validation fails
        validation_result, missing, invalid = validator.validate_traceability()
        research_validation = validator.validate_research_evidence(args.research)

        requirements_valid = validation_result['coverage_percentage'] == 100 and not invalid
        research_valid = research_validation['valid']

        if not requirements_valid or not research_valid:
            sys.exit(1)
        else:
            sys.exit(0)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
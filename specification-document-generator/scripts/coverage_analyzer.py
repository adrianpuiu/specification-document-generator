#!/usr/bin/env python3
"""
Coverage Analyzer for Specification Documents
Generates detailed coverage analysis and reports
"""

import json
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict

class CoverageAnalyzer:
    """Analyzes coverage across specification documents"""

    def __init__(self, project_dir: Path):
        self.project_dir = project_dir
        self.requirements_file = project_dir / "requirements.md"
        self.design_file = project_dir / "design.md"
        self.tasks_file = project_dir / "tasks.md"

    def analyze_document_complexity(self) -> Dict[str, Any]:
        """Analyze complexity metrics for each document"""
        analysis = {}

        # Requirements analysis
        if self.requirements_file.exists():
            req_content = self.requirements_file.read_text()
            analysis['requirements'] = {
                'file_size': len(req_content),
                'line_count': len(req_content.splitlines()),
                'requirement_count': req_content.count('### Requirement'),
                'acceptance_criteria_count': len(list(
                    line.strip() for line in req_content.splitlines()
                    if line.strip().match(r'^\d+\.')
                )),
                'glossary_terms': len(list(
                    line.strip() for line in req_content.splitlines()
                    if line.strip().startswith('- **')
                ))
            }

        # Design analysis
        if self.design_file.exists():
            design_content = self.design_file.read_text()
            analysis['design'] = {
                'file_size': len(design_content),
                'line_count': len(design_content.splitlines()),
                'component_count': design_content.count('#### Component:'),
                'diagram_count': design_content.count('```mermaid'),
                'decision_count': design_content.count('### Decision'),
                'data_model_count': design_content.count('#### Data Model')
            }

        # Tasks analysis
        if self.tasks_file.exists():
            tasks_content = self.tasks_file.read_text()
            analysis['tasks'] = {
                'file_size': len(tasks_content),
                'line_count': len(tasks_content.splitlines()),
                'task_count': len(list(
                    line.strip() for line in tasks_content.splitlines()
                    if line.strip().match(r'^- \[ \] \d+\.')
                )),
                'subtask_count': len(list(
                    line.strip() for line in tasks_content.splitlines()
                    if line.strip().match(r'^- \[ \] \d+\.\d+\.')
                )),
                'requirement_references': tasks_content.count('_Requirements:')
            }

        return analysis

    def generate_coverage_report(self) -> str:
        """Generate comprehensive coverage report"""
        complexity = self.analyze_document_complexity()

        report = "# Specification Document Coverage Report\n\n"
        report += f"Generated on: {self._get_timestamp()}\n\n"

        # Document Statistics
        report += "## Document Statistics\n\n"
        report += "| Document | File Size | Lines | Key Metrics |\n"
        report += "|----------|-----------|-------|-------------|\n"

        if 'requirements' in complexity:
            req = complexity['requirements']
            report += f"| requirements.md | {req['file_size']:,} chars | {req['line_count']} | {req['requirement_count']} reqs, {req['acceptance_criteria_count']} criteria |\n"

        if 'design' in complexity:
            des = complexity['design']
            report += f"| design.md | {des['file_size']:,} chars | {des['line_count']} | {des['component_count']} components, {des['diagram_count']} diagrams |\n"

        if 'tasks' in complexity:
            task = complexity['tasks']
            report += f"| tasks.md | {task['file_size']:,} chars | {task['line_count']} | {task['task_count']} tasks, {task['subtask_count']} subtasks |\n"

        # Quality Metrics
        report += "\n## Quality Metrics\n\n"
        if 'requirements' in complexity and 'tasks' in complexity:
            req_count = complexity['requirements']['acceptance_criteria_count']
            task_refs = complexity['tasks']['requirement_references']
            coverage_percentage = (task_refs / req_count * 100) if req_count > 0 else 0
            report += f"- **Acceptance Criteria Coverage**: {task_refs}/{req_count} ({coverage_percentage:.1f}%)\n"

        if 'requirements' in complexity and 'design' in complexity:
            req_count = complexity['requirements']['acceptance_criteria_count']
            # This would need actual reference counting from design.md
            report += f"- **Design Document Coverage**: To be calculated\n"

        # Recommendations
        report += "\n## Recommendations\n\n"
        report += self._generate_recommendations(complexity)

        return report

    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _generate_recommendations(self, complexity: Dict[str, Any]) -> str:
        """Generate improvement recommendations"""
        recommendations = []

        if 'requirements' in complexity:
            req = complexity['requirements']
            if req['requirement_count'] == 0:
                recommendations.append("- ❌ No requirements found - requirements.md needs requirements")
            if req['acceptance_criteria_count'] < req['requirement_count'] * 3:
                recommendations.append("- ⚠️ Low acceptance criteria count - consider adding more criteria for better testability")

        if 'design' in complexity:
            des = complexity['design']
            if des['component_count'] == 0:
                recommendations.append("- ❌ No components specified - design.md needs component architecture")
            if des['diagram_count'] == 0:
                recommendations.append("- ⚠️ No diagrams found - consider adding architectural diagrams")

        if 'tasks' in complexity:
            task = complexity['tasks']
            if task['task_count'] == 0:
                recommendations.append("- ❌ No tasks found - tasks.md needs implementation tasks")
            if task['requirement_references'] == 0:
                recommendations.append("- ❌ No requirement references found - tasks need requirement traceability")

        if not recommendations:
            recommendations.append("- ✅ All documents appear to have necessary content")

        return "\n".join(recommendations)

    def export_analysis_json(self, output_file: Path = None) -> Path:
        """Export analysis as JSON"""
        if output_file is None:
            output_file = self.project_dir / "coverage_analysis.json"

        analysis = {
            'timestamp': self._get_timestamp(),
            'complexity': self.analyze_document_complexity(),
            'project_directory': str(self.project_dir)
        }

        output_file.write_text(json.dumps(analysis, indent=2))
        return output_file

def main():
    """Main analysis function"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python coverage_analyzer.py <project_directory>")
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    analyzer = CoverageAnalyzer(project_dir)

    # Generate report
    report = analyzer.generate_coverage_report()
    report_file = project_dir / "coverage_report.md"
    report_file.write_text(report)

    # Export JSON
    json_file = analyzer.export_analysis_json()

    print("📊 Coverage Analysis Complete")
    print(f"📄 Report generated: {report_file}")
    print(f"📋 JSON export: {json_file}")

    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
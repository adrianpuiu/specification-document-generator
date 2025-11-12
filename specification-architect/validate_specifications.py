#!/usr/bin/env python3
"""Specification Architect Validation Script"""
import re, sys, json, argparse
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, Set, List

@dataclass
class Result:
    total: int = 0
    covered: Set[str] = field(default_factory=set)
    missing: Set[str] = field(default_factory=set)
    coverage: float = 0.0
    valid: bool = False
    errors: List[str] = field(default_factory=list)

class Validator:
    def __init__(self, spec_dir: str, verbose=False):
        self.dir = Path(spec_dir)
        self.verbose = verbose
        self.result = Result()
        self.components = set()
        self.requirements = {}
        self.task_reqs = set()
    
    def log(self, msg, level="INFO"):
        if self.verbose or level=="ERROR":
            print(f"[{level}] {msg}")
    
    def validate(self) -> Result:
        self.log("Starting validation...")
        
        if not self._files_exist():
            return self.result
        if not self._extract_components():
            return self.result
        if not self._extract_requirements():
            return self.result
        if not self._extract_tasks():
            return self.result
        
        self._calculate()
        self._report()
        return self.result
    
    def _files_exist(self) -> bool:
        for name in ["blueprint.md", "requirements.md", "tasks.md"]:
            if not (self.dir / name).exists():
                self.result.errors.append(f"Missing: {name}")
        return len(self.result.errors) == 0
    
    def _extract_components(self) -> bool:
        try:
            content = (self.dir / "blueprint.md").read_text()
            self.components = set(re.findall(r'\|\s*\*\*([A-Za-z0-9_]+)\*\*\s*\|', content))
            if not self.components:
                self.log("No components found", "WARNING")
                return False
            self.log(f"Found {len(self.components)} components")
            return True
        except Exception as e:
            self.log(f"Error: {e}", "ERROR")
            return False
    
    def _extract_requirements(self) -> bool:
        try:
            content = (self.dir / "requirements.md").read_text()
            for match in re.finditer(r'### Requirement (\d+):', content):
                req_num = match.group(1)
                start = match.end()
                end = len(content)
                text = content[start:end]
                
                criteria = [f"{req_num}.{c}" for c, _ in re.findall(
                    r'(\d+)\.\s+WHEN.*?THE\s+\*\*([A-Za-z0-9_]+)\*\*\s+SHALL',
                    text, re.DOTALL)]
                if criteria:
                    self.requirements[req_num] = criteria
            
            self.result.total = sum(len(v) for v in self.requirements.values())
            self.log(f"Found {self.result.total} criteria")
            return self.result.total > 0
        except Exception as e:
            self.log(f"Error: {e}", "ERROR")
            return False
    
    def _extract_tasks(self) -> bool:
        try:
            content = (self.dir / "tasks.md").read_text()
            for match in re.findall(r'_Requirements:\s*([\d., ]+)_', content):
                for c in match.split(','):
                    self.task_reqs.add(c.strip())
            if not self.task_reqs:
                self.log("No requirement tags found", "WARNING")
                return False
            self.log(f"Found {len(self.task_reqs)} covered criteria")
            return True
        except Exception as e:
            self.log(f"Error: {e}", "ERROR")
            return False
    
    def _calculate(self):
        all_crit = set()
        for crit_list in self.requirements.values():
            all_crit.update(crit_list)
        
        self.result.covered = self.task_reqs & all_crit
        self.result.missing = all_crit - self.task_reqs
        
        if all_crit:
            self.result.coverage = (len(self.result.covered) / len(all_crit)) * 100
        
        self.result.valid = self.result.coverage == 100.0
    
    def _report(self):
        print("\n" + "="*80)
        print("SPECIFICATION VALIDATION REPORT")
        print("="*80 + "\n")
        
        print("SUMMARY")
        print("-"*80)
        print(f"Total Criteria:        {self.result.total}")
        print(f"Covered by Tasks:      {len(self.result.covered)}")
        print(f"Coverage:              {self.result.coverage:.1f}%\n")
        
        if self.result.missing:
            print("MISSING CRITERIA")
            print("-"*80)
            for c in sorted(self.result.missing, key=lambda x: tuple(map(int, x.split('.')))):
                print(f"  - {c}")
            print()
        
        print("VALIDATION STATUS")
        print("-"*80)
        if self.result.valid:
            print("✅ PASSED - All criteria covered\n")
        else:
            print(f"❌ FAILED - {len(self.result.missing)} uncovered\n")
        
        print("="*80 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Validate specifications")
    parser.add_argument("--path", default=".", help="Spec directory")
    parser.add_argument("--verbose", action="store_true", help="Verbose")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()
    
    v = Validator(args.path, args.verbose)
    result = v.validate()
    
    if args.json:
        print(json.dumps({
            "total": result.total,
            "covered": len(result.covered),
            "missing": list(result.missing),
            "coverage": result.coverage,
            "valid": result.valid,
        }, indent=2))
    
    sys.exit(0 if result.valid else 1)

if __name__ == "__main__":
    main()

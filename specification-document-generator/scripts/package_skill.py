#!/usr/bin/env python3
"""
Package Skill Script
Creates a distributable zip file of the specification document generator skill
"""

import json
import zipfile
from pathlib import Path
from typing import Dict, List, Any
import sys
import os

class SkillPackager:
    """Packages the skill into a distributable zip file"""

    def __init__(self, skill_dir: Path):
        self.skill_dir = skill_dir
        self.skill_name = skill_dir.name
        self.validation_errors = []

    def validate_skill_structure(self) -> bool:
        """Validate the skill structure and content"""
        print("🔍 Validating skill structure...")

        # Check required files
        required_files = [
            "SKILL.md",
        ]

        for file_path in required_files:
            full_path = self.skill_dir / file_path
            if not full_path.exists():
                self.validation_errors.append(f"Missing required file: {file_path}")
            else:
                print(f"  ✅ Found {file_path}")

        # Check SKILL.md frontmatter
        skill_md = self.skill_dir / "SKILL.md"
        if skill_md.exists():
            content = skill_md.read_text()
            if not content.startswith('---'):
                self.validation_errors.append("SKILL.md missing YAML frontmatter")
            else:
                # Extract frontmatter
                try:
                    frontmatter_end = content.find('---', 3)
                    frontmatter = content[3:frontmatter_end]
                    frontmatter_data = json.loads(frontmatter.replace('---', '').strip())

                    # Check required fields
                    if 'name' not in frontmatter_data:
                        self.validation_errors.append("SKILL.md missing 'name' in frontmatter")
                    if 'description' not in frontmatter_data:
                        self.validation_errors.append("SKILL.md missing 'description' in frontmatter")

                    if 'name' in frontmatter_data and 'description' in frontmatter_data:
                        print(f"  ✅ Frontmatter complete: {frontmatter_data['name']}")

                except Exception as e:
                    self.validation_errors.append(f"Invalid YAML frontmatter: {e}")

        # Check directory structure
        expected_dirs = ["scripts", "references", "assets"]
        for dir_name in expected_dirs:
            dir_path = self.skill_dir / dir_name
            if dir_path.exists():
                print(f"  ✅ Found {dir_name}/ directory")
                # Check if directory has content
                if not list(dir_path.iterdir()):
                    print(f"  ⚠️  {dir_name}/ directory is empty")
            else:
                print(f"  ⚠️  Optional {dir_name}/ directory not found")

        # Check script files
        scripts_dir = self.skill_dir / "scripts"
        if scripts_dir.exists():
            py_files = list(scripts_dir.glob("*.py"))
            print(f"  ✅ Found {len(py_files)} Python scripts")
            for script in py_files:
                if not os.access(script, os.X_OK):
                    print(f"  ⚠️  {script.name} is not executable")

        return len(self.validation_errors) == 0

    def calculate_skill_stats(self) -> Dict[str, Any]:
        """Calculate statistics about the skill"""
        stats = {
            "skill_name": self.skill_name,
            "total_files": 0,
            "total_size": 0,
            "file_breakdown": {},
            "resource_counts": {}
        }

        for file_path in self.skill_dir.rglob("*"):
            if file_path.is_file():
                stats["total_files"] += 1
                size = file_path.stat().st_size
                stats["total_size"] += size

                # Categorize files
                suffix = file_path.suffix.lower()
                if suffix not in stats["file_breakdown"]:
                    stats["file_breakdown"][suffix] = {"count": 0, "size": 0}
                stats["file_breakdown"][suffix]["count"] += 1
                stats["file_breakdown"][suffix]["size"] += size

                # Count resources by directory
                parent_dir = file_path.parent.name
                if parent_dir not in stats["resource_counts"]:
                    stats["resource_counts"][parent_dir] = 0
                stats["resource_counts"][parent_dir] += 1

        return stats

    def create_package(self, output_dir: Path = None) -> Path:
        """Create the distributable package"""
        if output_dir is None:
            output_dir = self.skill_dir.parent

        package_name = f"{self.skill_name}.zip"
        package_path = output_dir / package_name

        print(f"📦 Creating package: {package_path}")

        with zipfile.ZipFile(package_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in self.skill_dir.rglob("*"):
                if file_path.is_file():
                    # Calculate relative path for zip archive
                    arcname = file_path.relative_to(self.skill_dir)
                    zipf.write(file_path, arcname)

        return package_path

    def generate_package_info(self, package_path: Path) -> Dict[str, Any]:
        """Generate package information"""
        stats = self.calculate_skill_stats()

        package_info = {
            "skill_name": self.skill_name,
            "package_path": str(package_path),
            "package_size": package_path.stat().st_size,
            "validation_errors": self.validation_errors,
            "statistics": stats,
            "quality_checks": {
                "has_required_files": "SKILL.md" in [f.name for f in self.skill_dir.iterdir()],
                "has_scripts": (self.skill_dir / "scripts").exists(),
                "has_references": (self.skill_dir / "references").exists(),
                "has_assets": (self.skill_dir / "assets").exists(),
                "validation_passed": len(self.validation_errors) == 0
            }
        }

        return package_info

def main():
    """Main packaging function"""
    if len(sys.argv) < 2:
        print("Usage: python package_skill.py <skill_directory> [output_directory]")
        sys.exit(1)

    skill_dir = Path(sys.argv[1]).resolve()
    output_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else skill_dir.parent

    if not skill_dir.exists():
        print(f"❌ Skill directory not found: {skill_dir}")
        sys.exit(1)

    packager = SkillPackager(skill_dir)

    # Validate skill
    if not packager.validate_skill_structure():
        print("\n❌ Validation failed:")
        for error in packager.validation_errors:
            print(f"  - {error}")
        print("\nPlease fix validation errors before packaging.")
        sys.exit(1)

    print("✅ Skill validation passed")

    # Create package
    try:
        package_path = packager.create_package(output_dir)
        print(f"✅ Package created: {package_path}")

        # Generate package info
        package_info = packager.generate_package_info(package_path)
        info_path = output_dir / f"{skill_dir.name}_package_info.json"
        info_path.write_text(json.dumps(package_info, indent=2))

        print(f"📋 Package info saved: {info_path}")
        print(f"📊 Package size: {package_info['package_size']:,} bytes")
        print(f"📄 Total files: {package_info['statistics']['total_files']}")

        print("\n🎉 Skill packaging complete!")
        return 0

    except Exception as e:
        print(f"❌ Packaging failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    sys.exit(main())
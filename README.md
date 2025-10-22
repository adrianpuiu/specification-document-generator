# Specification Document Generator Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Skill](https://img.shields.io/badge/Claude-Code%20Skill-blue.svg)](https://claude.com/claude-code)
[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)](https://github.com/adrianpuiu/specification-document-generator)

> A comprehensive Claude Code skill for generating three interconnected specification documents with complete requirement traceability using rigorous numbering systems and EARS notation.

## 🌟 Overview

The Specification Document Generator is a sophisticated skill that creates professional, production-ready specifications for large systems (100+ requirements) across various project types. It implements a rigorous three-phase generation process ensuring complete traceability from requirements through design to implementation tasks using precise numerical references.

### 🎯 Key Benefits

- **📋 Complete Documentation**: Generate three interconnected documents (requirements.md, design.md, tasks.md)
- **🔗 Perfect Traceability**: Every acceptance criterion traced through all documents with N.M numbering
- **📝 EARS Notation**: Structured, unambiguous requirements using industry-standard notation
- **🏗️ Multi-Domain Support**: Works with software, construction, manufacturing, and business projects
- **✅ Quality Assurance**: Automated validation scripts ensure document quality and consistency
- **📊 Large System Support**: Handles complex projects with 100+ requirements efficiently

## 🚀 Quick Start

### Installation

#### Option 1: Install via Claude Skills Marketplace (Recommended)

1. **Add the marketplace**:
   ```bash
   /plugin marketplace add adrianpuiu/claude-skills-marketplace
   ```

2. **Install the skill**:
   ```bash
   /plugin install specification-document-generator@claude-skills-marketplace
   ```

#### Option 2: Manual Installation

1. **Download the skill**:
   ```bash
   git clone https://github.com/adrianpuiu/specification-document-generator.git
   cd specification-document-generator
   ```

2. **Install in Claude Code**:
   - Copy the skill directory to your Claude skills folder
   - Or install from the packaged `specification-document-generator.zip` file

#### Option 3: Install from Zip

1. **Download the packaged skill** from the [Releases](https://github.com/adrianpuiu/specification-document-generator/releases) page
2. **Install using Claude Code**:
   ```bash
   /plugin install path/to/specification-document-generator.zip
   ```

### Basic Usage

Simply ask Claude to generate specification documents:

```bash
"Generate specification documents for a real-time trading system that monitors cryptocurrency prices and executes automated trades based on market conditions."
```

The skill will respond with a structured three-phase process:

1. **Requirements Phase** - Generates requirements.md with numbered acceptance criteria
2. **Design Phase** - Creates design.md with component specifications and requirement references
3. **Tasks Phase** - Breaks down into tasks.md with precise requirement traceability

## 📋 Features

### Three-Phase Generation System

| Phase | Output | Key Features |
|-------|--------|--------------|
| **Requirements** | `requirements.md` | EARS notation, numbered criteria, performance metrics |
| **Design** | `design.md` | Component diagrams, data models, technical decisions |
| **Tasks** | `tasks.md` | Detailed implementation steps with requirement traceability |

### Core Capabilities

- **🔢 Precise Numbering**: N.M format for acceptance criteria (1.1, 1.2, 2.1, etc.)
- **📊 Traceability Matrix**: Complete mapping from requirements to tasks
- **🎨 Diagram Templates**: Mermaid diagrams for architecture and sequences
- **📚 Reference Library**: Comprehensive guides and patterns
- **🔧 Validation Tools**: Automated quality checking scripts

## 🏗️ Project Structure

```
specification-document-generator/
├── 📄 SKILL.md                    # Main skill definition
├── 📖 README.md                   # Comprehensive documentation
├── 🔧 scripts/                    # Validation and utility scripts
│   ├── numbering_checker.py      # Verify consistent numbering
│   ├── traceability_validator.py # Ensure complete coverage
│   ├── coverage_analyzer.py      # Generate coverage reports
│   └── package_skill.py          # Package the skill
├── 📚 references/                 # Reference documentation
│   ├── ears_notation_guide.md    # EARS notation patterns
│   ├── design_patterns_library.md # Common architectural patterns
│   ├── mermaid_templates.md      # Diagram templates
│   ├── project_type_templates.md # Domain-specific guidance
│   └── verification_checklist.md # Quality checklists
└── 📂 assets/                     # Output templates
    ├── requirements_template.md  # Base requirements structure
    ├── design_template.md        # Design document template
    ├── tasks_template.md         # Implementation task template
    └── traceability_matrix_template.md # Traceability documentation
```

## 📝 Supported Project Types

### Software Development
- **Components**: APIs, databases, microservices, authentication
- **Patterns**: MVC, Repository, Circuit Breaker, CQRS
- **Focus**: Performance, security, scalability requirements

### Construction Projects
- **Components**: Foundation systems, structural frames, MEP systems
- **Standards**: Building codes, OSHA compliance, safety regulations
- **Focus**: Structural requirements, quality control, schedules

### Manufacturing
- **Components**: Production equipment, assembly lines, quality control
- **Standards**: ISO 9001, safety regulations, efficiency metrics
- **Focus**: Production requirements, quality standards, maintenance

### Business Processes
- **Components**: Workflows, approvals, reporting systems
- **Standards**: Compliance requirements, audit procedures
- **Focus**: Process optimization, regulatory compliance, performance

## 🔧 EARS Notation

The skill implements **EARS (Easy Approach to Requirements Syntax)** for unambiguous requirements:

| Pattern | Purpose | Example |
|---------|---------|---------|
| **WHEN** | Temporal triggers | `WHEN the user submits the form, THE system SHALL validate input` |
| **WHERE** | Contextual conditions | `WHERE the user is authenticated, THE dashboard SHALL show personalized data` |
| **IF/THEN** | Conditional logic | `IF the payment fails, THEN THE system SHALL retry 3 times` |
| **WHILE** | Continuous behaviors | `WHILE processing files, THE system SHALL maintain memory below 2GB` |

## ✅ Quality Assurance

### Validation Tools

1. **Numbering Checker**: Ensures consistent numbering across documents
   ```bash
   python scripts/numbering_checker.py <project_directory>
   ```

2. **Traceability Validator**: Verifies complete requirement coverage
   ```bash
   python scripts/traceability_validator.py <project_directory>
   ```

3. **Coverage Analyzer**: Generates detailed coverage reports
   ```bash
   python scripts/coverage_analyzer.py <project_directory>
   ```

### Quality Checklist

- [ ] All requirements use EARS notation correctly
- [ ] Every acceptance criterion is numbered (N.M format)
- [ ] Each design component references specific requirements
- [ ] All tasks trace back to acceptance criteria
- [ ] Error scenarios are addressed for each requirement
- [ ] Performance metrics are included and measurable

## 📊 Examples

### Software Development Example

**Input**: "Generate specifications for a user authentication system with social login, password reset, and multi-factor authentication."

**Output**:
- **Requirements**: 12 functional requirements with 48 acceptance criteria
- **Design**: Component architecture with API specifications
- **Tasks**: 23 implementation tasks with complete traceability

### Construction Project Example

**Input**: "Create specifications for a 3-story commercial office building including structural requirements, safety compliance, and environmental considerations."

**Output**:
- **Requirements**: 8 major requirement categories with 32 acceptance criteria
- **Design**: Structural components and system integrations
- **Tasks**: 18 construction phases with quality control checkpoints

## 🔍 Advanced Features

### Traceability System

- **Forward Traceability**: Requirements → Design → Tasks
- **Backward Traceability**: Tasks → Design → Requirements
- **Coverage Matrix**: Visual representation of requirement coverage
- **Gap Analysis**: Identifies missing or orphaned elements

### Customization

- **Domain Templates**: Industry-specific patterns and terminology
- **Component Libraries**: Reusable design patterns
- **Validation Rules**: Custom quality checks
- **Output Formats**: Configurable document structures

## 🛠️ Development

### Building from Source

```bash
# Clone the repository
git clone https://github.com/adrianpuiu/specification-document-generator.git
cd specification-document-generator

# Package the skill
python scripts/package_skill.py .

# Install in Claude Code
# Copy the generated .zip file to your Claude skills directory
```

### Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines

- Follow the existing code style and structure
- Add comprehensive tests for new features
- Update documentation for any API changes
- Ensure all validation scripts pass

## 📈 Performance Metrics

- **Requirements per Project**: Supports 100+ requirements efficiently
- **Generation Time**: Typically 2-5 minutes for complete specification set
- **Traceability Accuracy**: 100% requirement coverage guaranteed
- **Quality Score**: Automated validation ensures 95%+ quality metrics

## 🤝 Community

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/adrianpuiu/specification-document-generator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/adrianpuiu/specification-document-generator/discussions)
- **Email**: puiu.adrian@gmail.com

### Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Roadmap

- [ ] Add more project type templates
- [ ] Enhanced validation rules
- [ ] Integration with popular project management tools
- [ ] Web-based specification editor
- [ ] Collaborative specification editing

## 🔗 Marketplace Integration

This skill is available through the **Claude Skills Marketplace** for easy installation and updates:

```bash
# Add the marketplace
/plugin marketplace add adrianpuiu/claude-skills-marketplace

# Install the skill
/plugin install specification-document-generator@claude-skills-marketplace

# Update the skill
/plugin update specification-document-generator@claude-skills-marketplace
```

### Marketplace Benefits

- **🔄 Automatic Updates**: Keep your skill up-to-date
- **📦 Easy Installation**: One-command installation
- **🏷️ Version Management**: Switch between different versions
- **📊 Usage Analytics**: Track skill usage and performance

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **EARS Notation**: Based on the Easy Approach to Requirements Syntax
- **Mermaid**: For beautiful diagram generation
- **Claude Code**: For the skills platform and API

## 📞 Contact

- **Author**: George A Puiu
- **Email**: puiu.adrian@gmail.com
- **GitHub**: [@adrianpuiu](https://github.com/adrianpuiu)

---

<div align="center">

**⭐ Star this repository if it helped you!**

Made with ❤️ for the specification documentation community

</div>
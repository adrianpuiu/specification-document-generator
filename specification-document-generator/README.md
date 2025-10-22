# Specification Document Generator Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Skill](https://img.shields.io/badge/Claude-Code%20Skill-blue.svg)](https://claude.com/claude-code)
[![Version](https://img.shields.io/badge/Version-2.0.0-green.svg)](https://github.com/adrianpuiu/specification-document-generator)
[![Real-Time Research](https://img.shields.io/badge/Research-Real--Time-brightgreen.svg)](https://github.com/adrianpuiu/specification-document-generator)

> A comprehensive Claude Code skill for generating five interconnected specification documents with complete requirement traceability, real-time research integration, and current industry best practices using rigorous numbering systems and EARS notation.

## 🌟 Overview

The Specification Document Generator is a sophisticated skill that creates professional, production-ready specifications for large systems (100+ requirements) across various project types. It implements a rigorous five-phase generation process ensuring complete traceability from requirements through design to implementation tasks using precise numerical references, with **mandatory real-time research** to ensure all specifications use current industry knowledge and avoid stale AI training data.

### 🎯 Key Benefits

- **📋 Complete Documentation**: Generate **five interconnected documents** (requirements.md, design.md, tasks.md, data_flow_specifications.md, traceability_matrix.md)
- **🔗 Perfect Traceability**: Every acceptance criterion traced through all documents with N.M numbering
- **📝 EARS Notation**: Structured, unambiguous requirements using industry-standard notation
- **🌐 Real-Time Research**: Mandatory current industry research prevents stale AI knowledge and outdated specifications
- **📊 Data Flow Mapping**: Comprehensive visual data flow architecture with detailed processing pipelines
- **🏗️ Multi-Domain Support**: Works with software, construction, manufacturing, healthcare, and business projects
- **✅ Quality Assurance**: Automated validation scripts ensure document quality and consistency
- **📊 Large System Support**: Handles complex projects with 100+ requirements efficiently
- **🔒 Current Date Accuracy**: Uses system date command to ensure correct temporal references

## 🚀 Quick Start

### Installation

1. **Download the skill**:
   ```bash
   git clone https://github.com/adrianpuiu/specification-document-generator.git
   cd specification-document-generator
   ```

2. **Install in Claude Code**:
   - Copy the skill directory to your Claude skills folder
   - Or install from the packaged `specification-document-generator.zip` file

### Basic Usage

Simply ask Claude to generate specification documents:

```bash
"Generate specification documents for a real-time trading system that monitors cryptocurrency prices and executes automated trades based on market conditions."
```

The skill will respond with a structured six-phase process:

1. **Real-Time Research Phase** - Performs mandatory current industry research using system date
2. **Requirements Phase** - Generates requirements.md with numbered acceptance criteria
3. **Design Phase** - Creates design.md with component specifications and requirement references
4. **Data Flow Phase** - Maps comprehensive data flows with visual architecture diagrams
5. **Tasks Phase** - Creates tasks.md with references to ALL previous documents (requirements, design, data flows)
6. **Traceability Phase** - Generates traceability_matrix.md with complete coverage analysis

## 📋 Features

### Six-Phase Generation System

| Phase | Output | Key Features |
|-------|--------|--------------|
| **Real-Time Research** | Current Industry Analysis | Mandatory web research, current year validation, latest trends |
| **Requirements** | `requirements.md` | EARS notation, numbered criteria, performance metrics |
| **Design** | `design.md` | Component diagrams, data models, technical decisions |
| **Data Flows** | `data_flow_specifications.md` | Visual architecture, processing pipelines, caching strategies |
| **Tasks** | `tasks.md` | Implementation steps with references to ALL previous documents |
| **Traceability** | `traceability_matrix.md` | Complete coverage analysis, cross-document mapping |

### Core Capabilities

- **🔢 Precise Numbering**: N.M format for acceptance criteria (1.1, 1.2, 2.1, etc.)
- **🌐 Real-Time Research**: Mandatory current industry research with latest trends and regulations
- **📊 Traceability Matrix**: Complete mapping from requirements to tasks with 100% coverage validation
- **📈 Data Flow Mapping**: Comprehensive visual architecture with detailed processing pipelines
- **🎨 Diagram Templates**: Mermaid diagrams for architecture, sequences, and data flows
- **📚 Reference Library**: Comprehensive guides, patterns, and research frameworks
- **🔧 Validation Tools**: Automated quality checking scripts and coverage analysis
- **📅 Current Date Integration**: System date command integration prevents temporal errors

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
│   ├── data_flow_patterns.md     # Data flow mapping patterns and best practices
│   ├── cache_strategies.md       # Caching and performance optimization techniques
│   ├── project_type_templates.md # Domain-specific guidance
│   ├── real_time_research_guide.md # Comprehensive research methodology
│   └── verification_checklist.md # Quality checklists
└── 📂 assets/                     # Output templates
    ├── requirements_template.md  # Base requirements structure
    ├── design_template.md        # Design document template
    ├── tasks_template.md         # Implementation task template
    ├── data_flow_template.md     # Data flow mapping template
    └── traceability_matrix_template.md # Traceability documentation
```

## 📝 Supported Project Types

### Software Development
- **Components**: APIs, databases, microservices, authentication, edge computing
- **Patterns**: MVC, Repository, Circuit Breaker, CQRS, Event-Driven Architecture
- **Focus**: Performance, security, scalability requirements, current technology stacks

### Healthcare Systems
- **Components**: EHR integration, HIPAA compliance, clinical decision support, telehealth
- **Standards**: HIPAA 2025, HITECH, FDA AI guidelines, FHIR R4, HL7 v2.x
- **Focus**: Patient privacy, clinical workflows, regulatory compliance, AI medical validation

### IoT Analytics
- **Components**: Edge gateways, time-series databases, real-time processing, device management
- **Standards**: NISTIR 8259 IoT guidelines, zero-trust security, TPM 2.0
- **Focus**: Real-time analytics, edge computing, device lifecycle management, scalable infrastructure

### Construction Projects
- **Components**: Foundation systems, structural frames, MEP systems, smart building integration
- **Standards**: Building codes, OSHA compliance, safety regulations, BIM integration
- **Focus**: Structural requirements, quality control, schedules, IoT sensor integration

### Manufacturing
- **Components**: Production equipment, assembly lines, quality control, predictive maintenance
- **Standards**: ISO 9001, safety regulations, efficiency metrics, Industry 4.0
- **Focus**: Production requirements, quality standards, maintenance, IoT integration

### Business Processes
- **Components**: Workflows, approvals, reporting systems, compliance automation
- **Standards**: Compliance requirements, audit procedures, GDPR, SOX
- **Focus**: Process optimization, regulatory compliance, performance, automation

## 🔧 EARS Notation

The skill implements **EARS (Easy Approach to Requirements Syntax)** for unambiguous requirements:

| Pattern | Purpose | Example |
|---------|---------|---------|
| **WHEN** | Temporal triggers | `WHEN the user submits the form, THE system SHALL validate input` |
| **WHERE** | Contextual conditions | `WHERE the user is authenticated, THE dashboard SHALL show personalized data` |
| **IF/THEN** | Conditional logic | `IF the payment fails, THEN THE system SHALL retry 3 times` |
| **WHILE** | Continuous behaviors | `WHILE processing files, THE system SHALL maintain memory below 2GB` |

## 🔍 Real-Time Research Integration

### Mandatory Research Process

The skill performs **mandatory real-time research** before generating any specifications to ensure current industry knowledge:

1. **System Date Verification**:
   ```bash
   CURRENT_DATE=$(date +"%Y-%m-%d")
   CURRENT_YEAR=$(date +"%Y")
   echo "Using current date: $CURRENT_DATE"
   ```

2. **Current Technology Trends Research**:
   - Latest architectural patterns and frameworks
   - Current security threats and mitigation strategies
   - Modern development tools and ecosystems
   - Recent compliance requirements and regulations

3. **Industry-Specific Research**:
   - Recent successful projects and case studies
   - Current technology stack preferences
   - Emerging technologies and adoption rates
   - Latest performance benchmarks and standards

4. **Regulatory Compliance Research**:
   - Latest regulations affecting the domain
   - Current compliance frameworks and standards
   - Recent legal requirements and data privacy laws
   - Current audit requirements and reporting standards

### Research Sources

- **Technical Communities**: GitHub, Stack Overflow, Reddit programming
- **Conference Talks**: Recent KubeCon, AWS re:Invent, GOTO, Devoxx
- **Industry Blogs**: Martin Fowler, InfoQ, Netflix TechBlog, Uber Engineering
- **Security Sources**: OWASP, NIST, vendor security advisories
- **Regulatory Bodies**: Industry associations, compliance organizations

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

- [ ] **Current Date Verification**: System date command used for all timestamps
- [ ] **Real-Time Research**: Current year research completed before generation
- [ ] All requirements use EARS notation correctly
- [ ] Every acceptance criterion is numbered (N.M format)
- [ ] Each design component references specific requirements
- [ ] All tasks trace back to acceptance criteria
- [ ] Data flows are visually mapped with detailed processing
- [ ] Error scenarios are addressed for each requirement
- [ ] Performance metrics are included and measurable
- [ ] All regulatory references are current year compliant

## 📊 Examples

### Software Development Example

**Input**: "Generate specifications for a microservices-based e-commerce platform with real-time inventory management and AI-powered recommendations."

**Output**:
- **Requirements**: 10 functional requirements with 56 acceptance criteria
- **Design**: Microservices architecture with event-driven patterns
- **Data Flows**: Comprehensive order processing and inventory management flows
- **Tasks**: 28 implementation tasks with complete traceability
- **Traceability**: 100% requirement coverage with validation matrix

### Healthcare AI System Example

**Input**: "Create specifications for an AI-powered clinical decision support system with HIPAA compliance and FHIR interoperability."

**Output**:
- **Requirements**: 8 functional requirements with 64 acceptance criteria
- **Design**: HIPAA-compliant architecture with zero-trust security
- **Data Flows**: PHI-protected clinical data processing pipelines
- **Tasks**: 15 implementation phases with regulatory compliance validation
- **Traceability**: Complete coverage analysis with healthcare compliance mapping

### IoT Analytics Platform Example

**Input**: "Generate specifications for a real-time IoT analytics platform with edge computing and device management."

**Output**:
- **Requirements**: 8 functional requirements with 64 acceptance criteria
- **Design**: Edge computing architecture with scalable analytics
- **Data Flows**: End-to-end data movement from devices to insights
- **Tasks**: 13 implementation phases with complete requirement traceability
- **Traceability**: 100% coverage validation with performance metrics

### Construction Project Example

**Input**: "Create specifications for a smart commercial building with IoT integration and energy management."

**Output**:
- **Requirements**: 9 major requirement categories with 36 acceptance criteria
- **Design**: Smart building systems with IoT sensor integration
- **Data Flows**: Building automation and energy optimization workflows
- **Tasks**: 20 construction phases with technology integration checkpoints
- **Traceability**: Complete requirement coverage with compliance validation

## 🔍 Advanced Features

### Traceability System

- **Forward Traceability**: Requirements → Design → Data Flows → Tasks
- **Backward Traceability**: Tasks → Data Flows → Design → Requirements
- **Coverage Matrix**: Visual representation of requirement coverage (100% guaranteed)
- **Gap Analysis**: Identifies missing or orphaned elements
- **Cross-Document Validation**: Ensures consistency across all 5 documents
- **Requirement Impact Analysis**: Tracks changes across all document types

### Real-Time Research Features

- **Current Year Validation**: Uses system date to ensure correct temporal references
- **Multi-Source Research**: Validates findings across multiple industry sources
- **Expert Opinion Integration**: Incorporates current expert viewpoints and practices
- **Practical Application Focus**: Research targets what's actually used in production
- **Domain-Specific Intelligence**: Tailored research for each industry vertical

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
- **Generation Time**: Typically 5-10 minutes for complete 5-document specification set
- **Traceability Accuracy**: 100% requirement coverage guaranteed across all documents
- **Quality Score**: Automated validation ensures 95%+ quality metrics
- **Research Integration**: Real-time research ensures current industry compliance
- **Date Accuracy**: System date integration prevents temporal errors
- **Document Count**: Generates 5 interconnected documents vs. previous 3 documents

## 🆕 Version 2.0 Updates

### Major Enhancements

- **✅ Real-Time Research Integration**: Mandatory current industry research before generation
- **📅 System Date Integration**: Prevents stale AI knowledge and temporal errors
- **📊 Data Flow Specifications**: New comprehensive data flow mapping document
- **🔍 Enhanced Traceability**: 5-document traceability with complete coverage analysis
- **🏥 Healthcare Support**: Specialized healthcare system specifications with HIPAA compliance
- **🌐 IoT Analytics**: Edge computing and real-time analytics platform support
- **📚 Expanded Templates**: Additional reference guides and patterns
- **🛡️ Security Focus**: Zero-trust architecture and modern security frameworks

### Research Quality Improvements

- **Multi-Source Validation**: Research findings validated across multiple sources
- **Current Year Enforcement**: All research uses current year from system date
- **Expert Opinion Integration**: Incorporates current industry expert viewpoints
- **Practical Application Focus**: Research targets production-used technologies
- **Regulatory Compliance**: Latest regulatory requirements and compliance frameworks

## 🤝 Community

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/adrianpuiu/specification-document-generator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/adrianpuiu/specification-document-generator/discussions)
- **Email**: puiu.adrian@gmail.com

### Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Roadmap

- [ ] **Web-based specification editor** with real-time collaboration
- [ ] **Integration with popular project management tools** (Jira, Azure DevOps, GitHub Projects)
- [ ] **Enhanced AI model training** with specification document datasets
- [ ] **Automated requirement extraction** from existing documentation
- [ ] **Multi-language support** for international teams
- [ ] **Specification template marketplace** with community contributions
- [ ] **Advanced analytics dashboard** for specification quality metrics
- [ ] **API-first specification generation** for integration pipelines

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
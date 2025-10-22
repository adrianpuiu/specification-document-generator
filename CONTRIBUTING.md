# Contributing to Specification Document Generator

Thank you for your interest in contributing to the Specification Document Generator skill! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

1. **Search existing issues** before creating a new one
2. **Use the issue templates** if available
3. **Provide detailed information**:
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details
   - Screenshots if applicable

### Submitting Pull Requests

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** following the guidelines below
4. **Test your changes** thoroughly
5. **Commit your changes** with clear messages
6. **Push to your fork**: `git push origin feature/your-feature-name`
7. **Create a pull request** with a detailed description

## 📝 Development Guidelines

### Code Style

- Follow the existing code style and structure
- Use clear, descriptive variable and function names
- Add comments where the code is complex
- Keep functions small and focused

### Documentation

- Update documentation for any API changes
- Add examples for new features
- Keep the README.md up to date
- Document any breaking changes

### Testing

- Test all changes thoroughly
- Ensure all validation scripts pass
- Add tests for new functionality
- Test with different project types and scenarios

## 🏗️ Project Structure

```
specification-document-generator/
├── SKILL.md                    # Main skill definition
├── scripts/                    # Validation and utility scripts
├── references/                 # Reference documentation
└── assets/                     # Document templates
```

### Adding New Features

1. **Templates**: Add new templates to `assets/` directory
2. **References**: Add documentation to `references/` directory
3. **Scripts**: Add validation tools to `scripts/` directory
4. **Tests**: Update validation scripts to cover new features

### Validation Scripts

- `numbering_checker.py`: Validates numbering consistency
- `traceability_validator.py`: Ensures requirement coverage
- `coverage_analyzer.py`: Generates coverage reports
- `package_skill.py`: Packages the skill for distribution

## 🎯 Contribution Areas

We welcome contributions in the following areas:

### 📚 Documentation

- Improve existing documentation
- Add more examples and use cases
- Translate documentation to other languages
- Create tutorials and guides

### 🏗️ Templates and Patterns

- Add new project type templates
- Improve existing templates
- Add new design patterns
- Create specialized templates for industries

### 🔧 Validation and Quality

- Improve validation scripts
- Add new quality checks
- Enhance error messages
- Add automated testing

### 🌐 Multi-Domain Support

- Add support for new project types
- Improve existing domain templates
- Add industry-specific patterns
- Create specialized validation rules

## 📋 Pull Request Process

### Before Submitting

1. **Test your changes** thoroughly
2. **Run all validation scripts**
3. **Update documentation**
4. **Check for existing issues** that might be related
5. **Ensure your branch is up to date**

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Other

## Testing
- [ ] All validation scripts pass
- [ ] Tested with different project types
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Environment**: OS, Python version, Claude Code version
2. **Steps to reproduce**: Detailed steps to reproduce the issue
3. **Expected behavior**: What you expected to happen
4. **Actual behavior**: What actually happened
5. **Error messages**: Any error messages or logs
6. **Additional context**: Any other relevant information

## 💡 Feature Requests

When requesting features, please include:

1. **Use case**: Why you need this feature
2. **Proposed solution**: How you envision the feature working
3. **Alternatives considered**: Other approaches you've thought about
4. **Additional context**: Any other relevant information

## 📧 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Email**: puiu.adrian@gmail.com

## 📄 Code of Conduct

Please be respectful and constructive in all interactions. We are committed to providing a welcoming and inclusive environment for all contributors.

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Commit history (with proper attribution)

Thank you for contributing to the Specification Document Generator! 🎉
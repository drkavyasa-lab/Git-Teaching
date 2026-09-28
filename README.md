# Student Grade Calculator — Git, GitHub & GitHub Actions Teaching Repository

A small Python project designed for university practical sessions covering Git, GitHub collaboration, project management, and GitHub Actions CI.

## Learning path

1. Git repository and working tree
2. Staging and commits
3. Git history and diff
4. Branching and feature branches
5. Merging and conflict resolution
6. GitHub push/pull and Pull Requests
7. Issues and GitHub Projects
8. GitHub Actions
9. Automated testing and failed CI
10. End-to-end DevOps workflow

## Prerequisites

- Git
- GitHub account
- Python 3.10+ (3.12 recommended)
- Git GUI, GitHub Desktop, SourceTree, or command line
- Basic Python knowledge

## Run locally

```bash
python -m pip install -r requirements.txt
pytest
```

## Project structure

```text
student-grade-calculator/
├── src/
│   └── grade_calculator.py
├── tests/
│   └── test_grade_calculator.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── LAB_SHEET.md
│   └── INSTRUCTOR_GUIDE.md
├── .gitignore
├── requirements.txt
└── README.md
```

## Suggested classroom workflow

Issue → branch → edit → stage → commit → push → Pull Request → GitHub Actions → review → merge → close issue.

The repository intentionally starts simple so that students can focus on version control and CI/CD concepts.

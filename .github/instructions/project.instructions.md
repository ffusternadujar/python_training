---
applyTo: '**'
---

# project.instructions.md

This file provides guidance to AI Assistant when working with code in this repository.

## Project Overview

This is a private Python training project focused on learning Python language fundamentals. The repository is in its initial stages and will contain Python scripts, exercises, and learning materials as the training progresses.

## Build/Test Commands

- Run Python scripts: `python script_name.py` or `python3 script_name.py`
- Run tests (when available): `pytest` for all tests, `pytest path/to/test_file.py` for a single test file, `pytest path/to/test_file.py::test_function_name` for a specific test
- Linting: `ruff check .` or `flake8 .` (if configured)
- Format code: `ruff format .` or `black .` (if configured)
- Type checking: `mypy .` (if configured)

## Code Style Guidelines

- **Python Version**: Use modern Python 3.x features
- **Imports**: Group imports in order: standard library, third-party, local. Use absolute imports
- **Formatting**: Follow PEP 8 style guide (4 spaces for indentation, 79-88 character line length)
- **Type Hints**: Use type hints for function signatures where beneficial for learning
- **Naming**: snake_case for functions/variables, PascalCase for classes, UPPER_CASE for constants
- **Error Handling**: Use specific exception types, avoid bare except clauses
- **Documentation**: Add docstrings to functions and classes explaining purpose and parameters
- **Comments**: Write clear, concise comments for learning purposes to explain concepts

## Project Structure

As this is a training project, organize code logically by topic or chapter (e.g., `basics/`, `data_structures/`, `oop/`, etc.). Keep example scripts self-contained and well-documented for reference.

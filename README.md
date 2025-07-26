# python-calculator

A simple command-line calculator app written in Python.

## Features

- Addition, subtraction, multiplication, and division
- Handles division by zero with a clear error message
- Interactive CLI for user input
- Unit tests for all operations
- GitHub Actions workflow for automated testing
- Dockerfile for containerized execution

## Usage

### Run Locally

```sh
python calculator.py
```

Follow the prompts to enter numbers and select an operation (`+`, `-`, `*`, `/`).

### Run Tests

```sh
python -m unittest test_calculator.py
```

### Continuous Integration

All pushes and pull requests to `main` run tests automatically via [GitHub Actions](.github/workflows/py-cal.yml).

### Docker

Build and run the calculator in a container:

```sh
docker build -t python-calculator .
docker run -it python-calculator
```

## Project Structure

- `calculator.py` — Main calculator logic and CLI
- `test_calculator.py` — Unit tests
- `.github/workflows/py-cal.yml` — CI workflow
- `dockerfile` — Docker container setup
- `.gitignore` — Python cache exclusion

## Requirements

- Python 3.11+
- No external dependencies
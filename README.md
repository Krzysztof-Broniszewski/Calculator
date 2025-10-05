# Colab/Notebook cell — generate README.md for the refactored CLI calculator
readme = """# Refactored CLI Calculator (Python)

A small, robust command-line calculator that supports chained operations. Designed for clarity and safe input handling.

## Features
- **Operations:** `+`, `-`, `*`, `/`, `**`
- **Chained mode:** the result becomes the next first number
- **Float-friendly input:** accepts commas (`,` -> `.`)
- **Commands:** `reset`, `exit`
- **Validation:** guards against invalid numbers, division by zero, and extreme exponent values

## Requirements
- Python **3.10+**
- **No external dependencies**

## How to run
```bash
# from the project root
python src/calculator.py

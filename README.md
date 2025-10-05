# >>> Replace <USER>/<REPO> (and notebook path if different) before running this cell <<<

readme = """# Refactored CLI Calculator (Python)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](
https://colab.research.google.com/github/<USER>/<REPO>/blob/main/notebooks/01_calculator.ipynb)

A small, robust command-line calculator that supports chained operations and safe input handling.
This repository includes a Colab notebook for one-click execution and a plain Python script for local use.

---

## Features
- **Operations:** `+`, `-`, `*`, `/`, `**`
- **Chained mode:** the result becomes the next first number
- **User commands:** `reset`, `exit`
- **Validation:** invalid numbers, division by zero, extreme exponents guarded
- **No external dependencies** (pure Python 3.10+)

---

## Run in Colab (recommended for quick review)
1. Click the **Open in Colab** badge above.  
2. In Colab, choose **Runtime → Run all**.  
3. The notebook will:
   - show the calculator code,
   - (optionally) write `src/calculator.py`,
   - and run the interactive CLI inside Colab (you'll be prompted for input).

> Tip: Colab handles `input()` in the cell output; answer prompts directly in the notebook UI.

---

## Run locally
```bash
# 1) (Optional) create a clean environment
#    conda/mamba example:
mamba create -n calc -c conda-forge python=3.11
mamba activate calc

# 2) Run the calculator
python src/calculator.py

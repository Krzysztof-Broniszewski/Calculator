# One-cell generator: README.md for the refactored CLI calculator (EN)
README = """# Refactored CLI Calculator (Python)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1KakZBEuOUkq8fIIrNX5Ixwp-PjPdiUpV?usp=sharing)
<br>
**Direct link:** https://colab.research.google.com/drive/1KakZBEuOUkq8fIIrNX5Ixwp-PjPdiUpV?usp=sharing

A small, robust command-line calculator that supports chained operations and safe input handling.
This repository includes a Colab notebook for one-click execution and a plain Python script for local use.

---

## Features
- **Operations:** `+`, `-`, `*`, `/`, `**`
- **Chained mode:** the result becomes the next first number
- **User commands:** `reset`, `exit`
- **Validation:** guards for invalid numbers, division by zero, and extreme exponents
- **No external dependencies** (pure Python 3.10+)

---

## Run in Colab (quick review)
1. Click the **Open in Colab** badge (or the direct link) above.  
2. In Colab choose **Runtime → Run all**.  
3. The notebook will:
   - display the calculator code,
   - (optionally) write `src/calculator.py`,
   - run the interactive CLI (you can respond to `input()` prompts in the cell output area).

> Tip: If the notebook writes `src/calculator.py`, you can download it or push it to your repo.

---

## Run locally
```bash
# 1) (Optional) create a clean environment (conda/mamba example)
mamba create -n calc -c conda-forge python=3.11
mamba activate calc

# 2) Run the calculator
python src/calculator.py

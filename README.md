# Personal Expense Tracker

A console-based **Personal Expense Tracker** built with Python.  
It helps a student record daily expenses, set a monthly budget, delete incorrect entries, and generate category-wise monthly spending reports.

**Student:** ARPIT PANDEY (`26BCE10075`)  
**Faculty:** DHERESH SONI  
**Subject:** Introduction to Problem Solving and Programming  
**Institution:** VIT Bhopal  
**Repository:** https://github.com/arpit26bce10075-lgtm/expense-tracker  

> This project uses **no database** and **no third-party packages**.  
> Data is stored locally in `data/expenses.csv` and `data/budget.json`.

---

## Overview

Students make many small daily payments for food, travel, education, and other needs. Without a simple record, it is hard to know where money goes and whether spending stays within a planned budget.

This application solves that problem with a simple offline command-line tool that:

1. Captures expenses with validation
2. Saves them permanently in local files
3. Compares monthly spending against a budget
4. Shows category-wise totals for review

---

## Features

| Feature | Description |
|---------|-------------|
| Add expense | Save date, category, amount, and description |
| View expenses | List all saved expense records |
| Delete expense | Remove an incorrect entry by ID |
| Set monthly budget | Store a spending limit for a `YYYY-MM` month |
| Monthly report | Show total spent, budget, remaining amount, and category totals |
| Input validation | Reject invalid dates, amounts, categories, and empty descriptions |
| Local persistence | Keep data between runs using CSV and JSON |

---

## Approach

The solution follows a **modular layered design**:

```text
User
  |
  v
Console Interface (main.py)
  |
  +----------------+----------------+----------------+
  | ExpenseManager | BudgetManager  | ReportService  |
  +----------------+----------------+----------------+
  |
  v
Storage Layer (storage.py)
 /                       \
expenses.csv              budget.json
```

**Design choices:**

- **CSV for expenses** – tabular records that are easy to inspect and edit
- **JSON for budgets** – simple month-to-amount mapping
- **Standard library only** – easy to run on any lab/personal computer
- **Validation before save** – bad input never reaches storage
- **Separate modules** – each file has one clear responsibility

Detailed design, algorithms, testing, and findings are documented in  
[`project report.pdf`](./project%20report.pdf).

---

## Technologies

- Python 3.10+ (recommended)
- Standard library modules: `csv`, `json`, `pathlib`, `dataclasses`, `datetime`, `unittest`
- Storage: CSV + JSON
- Interface: Command Line (CLI)

---

## Project Structure

```text
expense-tracker/
|-- main.py                 # Menu-driven console interface
|-- models.py               # Expense and Budget data classes
|-- config.py               # Paths and allowed categories
|-- validators.py           # Input validation rules
|-- storage.py              # CSV/JSON read and write
|-- expense_manager.py      # Add, delete, list expenses
|-- budget_manager.py       # Set and get monthly budget
|-- reports.py              # Monthly and category reports
|-- utils.py                # Small helper functions
|-- requirements.txt        # Notes that no packages are required
|-- README.md               # This documentation
|-- statement.md            # Problem statement and scope
|-- project report.pdf      # Full academic project report
|-- data/
|   |-- expenses.csv        # Saved expense records
|   `-- budget.json         # Saved monthly budgets
|-- tests/
|   `-- test_project.py     # Unit tests for validation
`-- docs/
    `-- diagrams.md         # Architecture and workflow diagrams
```

---

## Requirements

- Python 3.10 or newer
- No MySQL / database server
- No `pip install` step required

---

## How to Run (Windows)

### 1. Install Python
Install Python from the official website and enable **Add Python to PATH**.

### 2. Open the project folder
Clone or download this repository, then open the folder in Command Prompt / PowerShell:

```bash
cd path\to\expense-tracker
```

### 3. Check Python

```bash
python --version
```

If needed:

```bash
py --version
```

### 4. Start the application

```bash
python main.py
```

or:

```bash
py main.py
```

### 5. Use the menu

```text
=== PERSONAL EXPENSE TRACKER ===
1. Add expense
2. View expenses
3. Delete expense
4. Set monthly budget
5. Monthly report
6. Exit
```

---

## Example Usage

**Add an expense (option 1):**

```text
Date: 2026-09-26
Category: Food
Amount: 150
Description: Lunch
```

**Generate a monthly report (option 5):**

```text
Month: 2026-09
```

Sample report output:

```text
REPORT - 2026-09
Total spent: Rs 700.00
Budget: Rs 5,000.00
Remaining: Rs 4,300.00

Category-wise spending:
Education   Rs 350.00
Food        Rs 270.00
Travel      Rs  80.00
```

---

## Testing

From the project root:

```bash
python -m unittest discover -s tests -v
```

Tests cover:

- Positive and negative amounts
- Correct and incorrect date formats
- Accepted and rejected categories

---

## Resetting Data

To clear expenses, keep only the header in `data/expenses.csv`:

```csv
expense_id,date,category,amount,description
```

To clear budgets, replace `data/budget.json` with:

```json
{}
```

---

## Documentation

| File | Purpose |
|------|---------|
| [README.md](./README.md) | Setup, features, and usage |
| [statement.md](./statement.md) | Problem statement and scope |
| [project report.pdf](./project%20report.pdf) | Full report: approach, design, testing, findings |
| [docs/diagrams.md](./docs/diagrams.md) | Architecture and workflow diagrams |

---

## Findings (Summary)

Building and testing this project showed that:

1. A file-based design is enough for a single-user personal expense tool.
2. Early validation prevents corrupted CSV/JSON data.
3. Separating UI, business logic, and storage makes the code easier to explain and extend.
4. Category-wise monthly reports make spending patterns easy to understand quickly.
5. Automated tests give confidence that validation rules behave as expected.

For the complete discussion of approach and findings, see [`project report.pdf`](./project%20report.pdf).

---

## Author

**ARPIT PANDEY**  
Registration No.: **26BCE10075**  
VIT Bhopal  
Faculty: **DHERESH SONI**  
Subject: **Introduction to Problem Solving and Programming**

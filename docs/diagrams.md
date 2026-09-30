# Design Diagrams

## System Architecture
```text
+----------------------+
|       User           |
+----------+-----------+
           |
           v
+----------------------+
|      main.py         |
|   Console Interface  |
+----------+-----------+
           |
   +-------+--------+----------------+
   |                |                |
   v                v                v
ExpenseManager  BudgetManager   ReportService
   |                |                |
   +--------+-------+--------+-------+
            v
        Storage Layer
       /             \
      v               v
expenses.csv      budget.json
```

## Workflow
```text
Start → Main Menu → Select Operation
                    |
       +------------+------------+
       |            |            |
     Expense      Budget       Report
       |            |            |
 Validate → Save  Validate → Save  Read → Calculate → Display
       |            |            |
       +------------+------------+
                    |
                   Exit
```

## Use Case Diagram (text form)
```text
User
 |-- Add Expense
 |-- View Expenses
 |-- Delete Expense
 |-- Set Monthly Budget
 `-- Generate Monthly Report
```

## Sequence: Add Expense
```text
User → main.py: enter expense details
main.py → validators.py: validate details
validators.py → main.py: valid / errors
main.py → ExpenseManager: add expense
ExpenseManager → storage.py: save CSV
storage.py → ExpenseManager: saved
ExpenseManager → main.py: expense ID
main.py → User: success message
```

## Component/Class Design
```text
Expense
 ├── expense_id
 ├── date
 ├── category
 ├── amount
 └── description

Budget
 ├── month
 └── amount

ExpenseManager
 ├── add()
 ├── delete()
 └── list_all()

ReportService
 ├── monthly_summary()
 └── dashboard()
```

## File Storage Design
`expenses.csv`
- expense_id
- date
- category
- amount
- description

`budget.json`
- month as key
- budget amount as value

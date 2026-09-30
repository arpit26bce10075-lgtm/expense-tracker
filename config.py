# Project paths and the fixed category list used by the app
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
data_folder = PROJECT_ROOT / 'data'
SPEND_FILE = data_folder / 'expenses.csv'
budget_path = data_folder / 'budget.json'
categoryOptions = ['Food', 'Travel', 'Education', 'Shopping', 'Entertainment', 'Bills', 'Health', 'Other']
DATE_MASK = '%Y-%m-%d'  # standerd date format used when parsing input

# Checks user input before an expense is saved
from datetime import datetime
from config import DATE_MASK, categoryOptions

def amt_ok(raw):
    # amount should be grater than zero
    try:
        return float(raw) > 0
    except (ValueError, TypeError):
        return False

def dateLooksFine(raw):
    # try parsing the date string against the expected mask
    try:
        datetime.strptime(raw, DATE_MASK)
        return True
    except ValueError:
        return False

def category_is_known(raw):
    # category must exist in the fixed options list
    return raw.title() in categoryOptions

def gather_input_problems(when, kind, cost, details=''):
    # collect every validation message to show the user
    problems = []
    if not dateLooksFine(when): problems.append('Date must be in YYYY-MM-DD format.')
    if not category_is_known(kind): problems.append('Choose a category from the available list.')
    if not amt_ok(cost): problems.append('Amount must be a positive number.')
    if not details.strip(): problems.append('Description cannot be empty.')
    return problems

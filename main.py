# Main menu for the personal expense tracker
from datetime import date
from expense_manager import ExpenseManager
from budget_manager import put_cap
from reports import ReportService
from utils import rupees, listCats, hold_screen
from storage import ensure_files_ready

mgr = ExpenseManager(); reporter = ReportService()

def do_add():
    # ask the user for details and try to save
    when = input(f'Date [{date.today()}]: ').strip() or str(date.today())
    listCats(); kind = input('Category: ').strip()
    cost = input('Amount (₹): ').strip(); details = input('Description: ').strip()
    ok, result = mgr.insert_spend(when, kind, cost, details)
    print('Expense added successfully. ID:', result if ok else '') if ok else print('Errors:', *result, sep='\n- ')

def showAll():
    # show every saved expense in a simple table
    rows = mgr.pullAll()
    if not rows: print('No expenses recorded.'); return
    print(f'\n{"ID":<5}{"Date":<12}{"Category":<16}{"Amount":>12}  Description')
    print('-'*70)
    for row in rows: print(f'{row.id_num:<5}{row.when:<12}{row.kind:<16}{rupees(row.cost):>12}  {row.details}')

def do_delete():
    # remove one record by its numeric id
    try: wanted = int(input('Expense ID to delete: ')); print('Deleted.' if mgr.dropById(wanted) else 'ID not found.')
    except ValueError: print('Enter a valid numeric ID.')

def setCapMenu():
    # let the user set how much they can spend that month
    month_key = input('Month (YYYY-MM): ').strip(); raw_cap = input('Monthly budget (₹): ').strip()
    try: put_cap(month_key, raw_cap); print('Budget saved.')
    except ValueError as err: print('Error:', err)

def printMonthReport():
    # print the total and category breakdown for a month
    month_key = input('Month (YYYY-MM): ').strip(); bundle = reporter.report_bundle(month_key)
    print(f'\nREPORT — {month_key}\nTotal spent: {rupees(bundle["total"])}')
    if bundle['budget'] is not None: print(f'Budget: {rupees(bundle["budget"])}\nRemaining: {rupees(bundle["remaining"])}')
    print('\nCategory-wise spending:')
    for kind, spent in bundle['categories'].items(): print(f'  {kind:<16} {rupees(spent)}')

def start():
    # loop the menu untill the user exits
    ensure_files_ready()
    while True:
        print('\n=== PERSONAL EXPENSE TRACKER ===\n1. Add expense\n2. View expenses\n3. Delete expense\n4. Set monthly budget\n5. Monthly report\n6. Exit')
        choice = input('Choose an option: ').strip()
        if choice == '1': do_add()
        elif choice == '2': showAll()
        elif choice == '3': do_delete()
        elif choice == '4': setCapMenu()
        elif choice == '5': printMonthReport()
        elif choice == '6': print('Thank you for using Expense Tracker.'); break
        else: print('Invalid choice. Please select 1-6.')

if __name__ == '__main__': start()

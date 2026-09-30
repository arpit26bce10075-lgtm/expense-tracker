# Read and write files so data survives after the program closes
import csv, json
from config import data_folder, SPEND_FILE, budget_path
from models import Expense, Budget

csv_headers = ['expense_id', 'date', 'category', 'amount', 'description']

def ensure_files_ready():
    # make sure the data folder and empty starter files exist
    data_folder.mkdir(exist_ok=True)
    if not SPEND_FILE.exists():
        with SPEND_FILE.open('w', newline='', encoding='utf-8') as fh:
            csv.DictWriter(fh, fieldnames=csv_headers).writeheader()
    if not budget_path.exists():
        budget_path.write_text('{}', encoding='utf-8')

def pull_spends():
    # load every expense row from the csv file
    ensure_files_ready()
    with SPEND_FILE.open(newline='', encoding='utf-8') as fh:
        return [Expense(int(row['expense_id']), row['date'], row['category'], float(row['amount']), row['description']) for row in csv.DictReader(fh)]

def dumpSpends(rows):
    # overrite the csv with the current list of rows
    ensure_files_ready()
    with SPEND_FILE.open('w', newline='', encoding='utf-8') as fh:
        out = csv.DictWriter(fh, fieldnames=csv_headers)
        out.writeheader()
        for row in rows:
            out.writerow({'expense_id': row.id_num, 'date': row.when, 'category': row.kind, 'amount': f'{row.cost:.2f}', 'description': row.details})

def loadCaps():
    # load monthly budget values from the json file
    ensure_files_ready()
    raw = json.loads(budget_path.read_text(encoding='utf-8'))
    return {mk: Budget(mk, float(val)) for mk, val in raw.items()}

def persist_caps(caps):
    # write the budget map back to disk
    ensure_files_ready()
    budget_path.write_text(json.dumps({mk: obj.cap for mk, obj in caps.items()}, indent=2), encoding='utf-8')

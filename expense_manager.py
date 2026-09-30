# Handles adding, listing, and removing expenses
from models import Expense
from storage import pull_spends, dumpSpends
from validators import gather_input_problems

class ExpenseManager:
    def insert_spend(self, when, kind, cost, details):
        # validate first, then append a new row
        problems = gather_input_problems(when, kind, cost, details)
        if problems: return False, problems
        rows = pull_spends()
        new_id = max((row.id_num for row in rows), default=0) + 1  # next free id
        rows.append(Expense(new_id, when, kind.title(), float(cost), details.strip()))
        dumpSpends(rows)
        return True, new_id

    def dropById(self, wanted):
        # delete the expense if that id is present
        rows = pull_spends()
        kept = [row for row in rows if row.id_num != wanted]
        if len(kept) == len(rows): return False
        dumpSpends(kept); return True

    def pullAll(self):
        # newest dates appear at the top of the list
        return sorted(pull_spends(), key=lambda row: (row.when, row.id_num), reverse=True)

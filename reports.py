# Builds the monthly summary shown on the report screen
from collections import defaultdict
from expense_manager import ExpenseManager
from budget_manager import getCap

class ReportService:
    def monthTotals(self, month_key):
        # filter spends for the choosen month
        matched = [row for row in ExpenseManager().pullAll() if row.when.startswith(month_key)]
        by_kind = defaultdict(float)
        for row in matched: by_kind[row.kind] += row.cost
        total = sum(by_kind.values())
        budget_row = getCap(month_key)
        # sort categories by highest spend first
        return total, dict(sorted(by_kind.items(), key=lambda item: item[1], reverse=True)), budget_row.cap if budget_row else None

    def report_bundle(self, month_key):
        # pack all report values into one dictionary
        total, by_kind, cap = self.monthTotals(month_key)
        left = cap - total if cap is not None else None
        return {'month': month_key, 'total': total, 'categories': by_kind, 'budget': cap, 'remaining': left}

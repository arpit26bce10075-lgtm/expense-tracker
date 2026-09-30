# Save and look up a monthly spending limit
from models import Budget
from storage import loadCaps, persist_caps

def put_cap(month_key, raw_cap):
    # month string must look like YYYY-MM
    if len(month_key) != 7 or month_key[4] != '-' or not month_key[:4].isdigit() or not month_key[5:].isdigit():
        raise ValueError('Month must be YYYY-MM.')
    raw_cap = float(raw_cap)
    if raw_cap <= 0: raise ValueError('Budget must be positive.')
    caps = loadCaps(); caps[month_key] = Budget(month_key, raw_cap); persist_caps(caps)  # store the new limit

def getCap(month_key):
    # return None when no budget exists for that month
    return loadCaps().get(month_key)

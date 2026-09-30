# Data shapes for a single expense and a monthly budget
from dataclasses import dataclass

@dataclass
class Expense:
    id_num: int
    when: str
    kind: str
    cost: float
    details: str  # short note about where the money went

@dataclass
class Budget:
    month_key: str  # month written as YYYY-MM
    cap: float

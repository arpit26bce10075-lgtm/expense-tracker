# Basic unit tests for the input checkers
import unittest, tempfile
from validators import amt_ok, dateLooksFine, category_is_known

class TestValidators(unittest.TestCase):
    def test_amount(self): self.assertTrue(amt_ok('250.50')); self.assertFalse(amt_ok('-1'))
    def test_date(self): self.assertTrue(dateLooksFine('2026-09-26')); self.assertFalse(dateLooksFine('26-09-2026'))
    def test_category(self): self.assertTrue(category_is_known('Food')); self.assertFalse(category_is_known('Unknown'))

if __name__ == '__main__': unittest.main()

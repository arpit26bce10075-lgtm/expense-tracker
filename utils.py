# Small helpers shared by the console screens
from config import categoryOptions

def listCats():
    # print the allowed categories so the user can pick one
    print('Categories:', ', '.join(categoryOptions))

def rupees(n):
    # format a number as Indian rupees for display
    return f'₹{n:,.2f}'

def hold_screen():
    # wait until the user presses Enter
    input('\nPress Enter to continue...')

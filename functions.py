'''
import csv
from datetime import datetime
'''
# ADD EXPENSES BY TYPE
# EDIT EXPENSE TYPES
# VIEW TOTAL EXPENSES AND EXPENSES BY CATAGORY
# SAVE IN SPREADSHEET


# Defining Types of income and expense
def expense_type():
    types = ['Bills', 'Groceries', 'Fun', 'Savings', 'Other']
    print(f"Expense Types: {', '.join(types)}")
    category = input("What category is this expense? ")
    
    if category in types:
        print(f"You selected: {category}")
        return category
    else:
        print("Invalid category. Please try again.")
        return expense_type()

def income_type():
    types = ['Work', 'Side Job', 'Other']
    print(f"Income Types: {', '.join(types)}")
    category = input("What category is this form of income? ")
    
    if category in types:
        print(f"You selected: {category}")
        return category
    else:
        print("Invalid category. Please try again.")
        return income_type()
    
def expense():
    name = input('please enter the name of this expense')
    amonut = input('Please Enter the amount of this expense: ')
    category = expense_type()
    print(f'Expense to Add: {name}, £{amonut}, {category}')
    
    expense()
    

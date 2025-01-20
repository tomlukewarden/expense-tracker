
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
    while True:
        category = input("What category is this expense? ")
        if category in types:
            print(f"You selected: {category}")
            return category
        else:
            print("Invalid category. Please try again.")

def income_type():
    types = ['Work', 'Side Job', 'Other']
    print(f"Income Types: {', '.join(types)}")
    while True:
        category = input("What category is this form of income? ")
        if category in types:
            print(f"You selected: {category}")
            return category
        else:
            print("Invalid category. Please try again.")

def expense():
    while True:
        name = input('Please enter the name of this expense: ')
        amount = input('Please enter the amount of this expense: ')
        category = expense_type()
        print(f'Expense to Add: {name}, £{amount}, {category}')
        
        another = input("Do you want to add another expense? (yes/no): ").lower()
        if another != 'yes':
            break

def income():
    while True:
        name = input('Please enter the name of this income: ')
        amount = input('Please enter the amount of this income: ')
        category = income_type()
        print(f'Income to Add: {name}, £{amount}, {category}')
        
        another = input("Do you want to add another income? (yes/no): ").lower()
        if another != 'yes':
            break
def view_expenses():
    print("Expenses: ")
    # Read expenses from a file or database and print them here
    
def view_income():
    print("Income: ")
    # Read income from a file or database and print them here

def menu():
    while True:
        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Expenses")
        print("4. View Income")
        print("5. Exit")

        choice = input("Please select an option: ")
        if choice == '1':
            expense()
        elif choice == '2':
            income()
        elif choice == '3':
            view_expenses()
        elif choice == '4':
            view_income()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
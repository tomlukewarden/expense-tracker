
'''
import csv

from datetime import datetime
'''

import tkinter as tk
# ADD EXPENSES BY TYPE
# EDIT EXPENSE TYPES
# VIEW TOTAL EXPENSES AND EXPENSES BY CATAGORY
# SAVE IN SPREADSHEET


# Defining Types of income and expense

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
        root = tk.Tk()
        root.geometry('400x300')
        root.title("Expense Manager")
        
        label = tk.Label(root, text="Enter the details of your expense:")
        label.pack(pady=10)

        # Label for Title
        title_label = tk.Label(root, text="Title:")
        title_label.pack(padx=10, pady=5)

        # Entry for Title
        name = tk.Entry(root)
        name.pack(padx=10, pady=5)

        # Label for Amount
        amount_label = tk.Label(root, text="Amount (£):")
        amount_label.pack(padx=10, pady=5)

        # Entry for Amount
        amount = tk.Entry(root)
        amount.pack(padx=10, pady=5)

        # Label for Category
        category_label = tk.Label(root, text="Category Options:")
        category_label.pack(padx=10, pady=10)
        
        # Checkbox for Category
        category1 = tk.Checkbutton(root, text="Bills")
        category1.pack(padx=10, pady=10)
        category2 = tk.Checkbutton(root, text='Groceries')
        category2.pack(padx=10, pady=10)
        category3 = tk.Checkbutton(root, text='Savings')
        category3.pack(padx=10, pady=10)
        category4 = tk.Checkbutton(root, text='Transport')
        category4.pack(padx=10, pady=10)
        category5 = tk.Checkbutton(root, text='Other')
        category5.pack(padx=10, pady=10)
        
        # Add Another
        another_button = tk.Button(root, text='Add Another Expense')
        another_button.pack(padx=10, pady=10)
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

def gui_menu():
    root = tk.Tk()
    root.title("Expense and Income Manager")
    root.geometry("400x300") 

    # Add a label
    title_label = tk.Label(root, text="Expense Manager", font=("Helvetica", 14))
    title_label.pack(pady=20)

    # Add buttons 
    btn_add_expense = tk.Button(root, text="Add Expense", width=20, command=expense)
    btn_add_expense.pack(pady=10)

    btn_add_income = tk.Button(root, text="Add Income", width=20, command=income)
    btn_add_income.pack(pady=10)

    btn_view_expenses = tk.Button(root, text="View Expenses", width=20, command=view_expenses)
    btn_view_expenses.pack(pady=10)

    btn_view_income = tk.Button(root, text="View Income", width=20, command=view_income)
    btn_view_income.pack(pady=10)

    btn_exit = tk.Button(root, text="Exit", width=20, command=root.destroy)
    btn_exit.pack(pady=10)

    root.mainloop()

gui_menu()
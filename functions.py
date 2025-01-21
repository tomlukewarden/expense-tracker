
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
    root = tk.Tk()
    root.geometry('400x400')
    root.title("Expense Manager")

    # Title Label
    label = tk.Label(root, text="Enter the details of your expense:", font=("Helvetica", 14))
    label.grid(row=0, column=0, columnspan=2, pady=10)

    # Title Input
    title_label = tk.Label(root, text="Title:")
    title_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)

    name = tk.Entry(root, width=30)
    name.grid(row=1, column=1, padx=10, pady=5)

    # Amount Input
    amount_label = tk.Label(root, text="Amount (£):")
    amount_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)

    amount = tk.Entry(root, width=30)
    amount.grid(row=2, column=1, padx=10, pady=5)

    # Category Options Label
    category_label = tk.Label(root, text="Category:")
    category_label.grid(row=3, column=0, sticky="ne", padx=10, pady=5)

    # Category Checkboxes
    categories_frame = tk.Frame(root)  # Frame to group the checkboxes
    categories_frame.grid(row=3, column=1, sticky="w", padx=10, pady=5)

    category1 = tk.Checkbutton(categories_frame, text="Bills")
    category1.pack(anchor="w")
    category2 = tk.Checkbutton(categories_frame, text="Groceries")
    category2.pack(anchor="w")
    category3 = tk.Checkbutton(categories_frame, text="Savings")
    category3.pack(anchor="w")
    category4 = tk.Checkbutton(categories_frame, text="Transport")
    category4.pack(anchor="w")
    category5 = tk.Checkbutton(categories_frame, text="Other")
    category5.pack(anchor="w")

    # Add Another Expense Button
    another_button = tk.Button(root, text="Add Another Expense", width=25)
    another_button.grid(row=4, column=0, columnspan=2, pady=20)
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
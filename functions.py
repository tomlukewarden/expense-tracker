import tkinter as tk
import csv
from datetime import datetime


def save_expense_to_csv(title, amount, category):
    filename = "expenses.csv"
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # Add headers if the file is empty
                writer.writerow(["Title", "Amount (£)", "Category", "Date"])
            writer.writerow([title, amount, category, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    except Exception as e:
        print(f"Error writing to file: {e}")

def save_income_to_csv(title, amount, category):
    filename = "income.csv"
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:  # Add headers if the file is empty
                writer.writerow(["Title", "Amount (£)", "Category", "Date"])
            writer.writerow([title, amount, category, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    except Exception as e:
        print(f"Error writing to file: {e}")
        
def expense_form():
    expense_window = tk.Toplevel(root)
    expense_window.title("Expense Manager")
    expense_window.geometry("400x400")

    def submit_expense():
        title = name_entry.get()
        amount = amount_entry.get()
        category = category_var.get()

        if not title or not amount or not category:
            error_label.config(text="All fields are required!", fg="red")
            return

        try:
            float(amount)
        except ValueError:
            error_label.config(text="Amount must be a number!", fg="red")
            return

        save_expense_to_csv(title, amount, category)
        error_label.config(text="Expense added successfully!", fg="green")
        name_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        category_var.set("")

    tk.Label(expense_window, text="Enter the details of your expense:", font=("Helvetica", 14)).grid(
        row=0, column=0, columnspan=2, pady=10
    )
    tk.Label(expense_window, text="Title:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    name_entry = tk.Entry(expense_window, width=30)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(expense_window, text="Amount (£):").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    amount_entry = tk.Entry(expense_window, width=30)
    amount_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(expense_window, text="Category:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    category_var = tk.StringVar(value="")
    category_dropdown = tk.OptionMenu(expense_window, category_var, "Bills", "Groceries", "Savings", "Transport", "Other")
    category_dropdown.grid(row=3, column=1, sticky="w", padx=10, pady=5)

    submit_button = tk.Button(expense_window, text="Submit Expense", width=25, command=submit_expense)
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    error_label = tk.Label(expense_window, text="", font=("Helvetica", 10))
    error_label.grid(row=5, column=0, columnspan=2)

def income_form():
    income_window = tk.Toplevel(root)
    income_window.title("Income Tracker")
    income_window.geometry("400x400")

    def submit_income():
        title = source_entry.get()
        amount = amount_entry.get()
        income_type = income_var.get()

        if not title or not amount or not income_type:
            error_label.config(text="All fields are required!", fg="red")
            return

        try:
            float(amount)
        except ValueError:
            error_label.config(text="Amount must be a number!", fg="red")
            return

        save_income_to_csv(title, amount, income_type)
        error_label.config(text="Income added successfully!", fg="green")
        source_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        income_var.set("Work")

    tk.Label(income_window, text="Enter the details of your income:", font=("Helvetica", 14)).grid(
        row=0, column=0, columnspan=2, pady=10
    )
    tk.Label(income_window, text="Source:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    source_entry = tk.Entry(income_window, width=30)
    source_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(income_window, text="Amount (£):").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    amount_entry = tk.Entry(income_window, width=30)
    amount_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(income_window, text="Income Type:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    income_var = tk.StringVar(value="Work")
    tk.Radiobutton(income_window, text="Work", variable=income_var, value="Work").grid(row=3, column=1, sticky="w", padx=10)
    tk.Radiobutton(income_window, text="Side Job", variable=income_var, value="Side Job").grid(row=4, column=1, sticky="w", padx=10)
    tk.Radiobutton(income_window, text="Other", variable=income_var, value="Other").grid(row=5, column=1, sticky="w", padx=10)

    submit_button = tk.Button(income_window, text="Submit Income", width=25, command=submit_income)
    submit_button.grid(row=6, column=0, columnspan=2, pady=10)

    error_label = tk.Label(income_window, text="", fg="red")
    error_label.grid(row=7, column=0, columnspan=2)

def total_left():
    print('total')
    
root = tk.Tk()
root.title("Expense and Income Manager")
root.config(bg="grey")
root.geometry("600x400")
tk.Label(root, text="Choose an option:", font=("Helvetica", 14)).pack(pady=20)
tk.Button(root, text="Add New Expenses", width=25, command=expense_form).pack(pady=10)
tk.Button(root, text="Add New Income", width=25, command=income_form).pack(pady=10)
tk.Button(root, text="View Remaining Money", width=25, command=total_left).pack(pady=10)

root.mainloop()
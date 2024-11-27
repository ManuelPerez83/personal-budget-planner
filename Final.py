# Personal Budget Planner

## Description

The **Personal Budget Planner** is a Python application designed to help users manage their finances. The app allows users to input their monthly income and expenses, calculates the total expenses, and displays the balance (surplus/deficit). It also provides suggestions to help optimize the budget.

### Features:
- **Income & Expense Tracking**: Easily input income and expenses in various categories like rent, food, utilities, etc.
- **Budget Calculation**: Get an immediate summary of total expenses and balance.
- **Dark Mode**: Toggle between light and dark modes for better usability.
- **Advanced Validation**: Get helpful tips if your expenses are too high in certain categories.

---

## Code:

```python
import tkinter as tk
from tkinter import messagebox
import csv

# Function to calculate the budget
def calculate_budget():
    try:
        income = float(income_entry.get())
        rent = float(rent_entry.get())
        food = float(food_entry.get())
        utilities = float(utilities_entry.get())
        transportation = float(transportation_entry.get())
        entertainment = float(entertainment_entry.get())
        health = float(health_entry.get())
        education = float(education_entry.get())
        miscellaneous = float(miscellaneous_entry.get())

        # Calculate total expenses and balance
        total_expenses = rent + food + utilities + transportation + entertainment + health + education + miscellaneous
        balance = income - total_expenses

        # Show the result
        result = f"Total Expenses: ${total_expenses:.2f}\nBalance: ${balance:.2f}"

        # Advanced validation suggestions
        suggestions = ""
        if rent / income > 0.30:
            suggestions += "Consider reducing rent expenses (should be less than 30% of income).\n"
        if food / income > 0.15:
            suggestions += "Consider reducing food expenses (should be less than 15% of income).\n"
        if balance < 0:
            suggestions += "You are in deficit! Try to cut down on non-essential expenses.\n"

        # Show message with validation suggestions
        if balance >= 0:
            messagebox.showinfo("Budget Summary", f"Surplus! 🎉\n\n{result}")
        else:
            messagebox.showwarning("Budget Summary", f"Deficit! 😞\n\n{result}\n\n{suggestions}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# Function to save the budget to a file
def save_budget():
    data = {
        "Income": income_entry.get(),
        "Rent": rent_entry.get(),
        "Food": food_entry.get(),
        "Utilities": utilities_entry.get(),
        "Transportation": transportation_entry.get(),
        "Entertainment": entertainment_entry.get(),
        "Health": health_entry.get(),
        "Education": education_entry.get(),
        "Miscellaneous": miscellaneous_entry.get()
    }
    try:
        with open("budget.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)
        messagebox.showinfo("Save Successful", "Budget saved to budget.csv")
    except Exception as e:
        messagebox.showerror("Save Error", f"An error occurred: {e}")

# Function to toggle dark mode
def toggle_dark_mode():
    global dark_mode  # Use the global variable to track mode
    if dark_mode:  # If the current mode is dark, switch to light mode
        window.config(bg="#f1f1f1")
        title_label.config(bg="#f1f1f1", fg="#333333")
        for widget in window.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(bg="#f1f1f1", fg="#333333")
            elif isinstance(widget, tk.Entry):
                widget.config(bg="#ffffff", fg="#333333")
            elif isinstance(widget, tk.Button):
                widget.config(bg="#3498db", fg="white")
        dark_mode = False  # Set the mode to light
    else:  # If the current mode is light, switch to dark mode
        window.config(bg="#2c3e50")
        title_label.config(bg="#2c3e50", fg="#ecf0f1")
        for widget in window.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(bg="#2c3e50", fg="#ecf0f1")
            elif isinstance(widget, tk.Entry):
                widget.config(bg="#34495e", fg="#ecf0f1")
            elif isinstance(widget, tk.Button):
                widget.config(bg="#3498db", fg="white")
        dark_mode = True  # Set the mode to dark

# Create the main window
window = tk.Tk()
window.title("Personal Budget Planner")
window.geometry("600x650")
window.config(bg="#f1f1f1")  # Default light mode

# Set initial dark mode state
dark_mode = False

# Create and place the title label
title_label = tk.Label(window, text="Personal Budget Planner", font=("Helvetica", 20, "bold"), bg="#f1f1f1", fg="#333333")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Create input labels and entry fields for income and expenses
labels = ["Income", "Rent", "Food", "Utilities", "Transportation", "Entertainment", "Health", "Education", "Miscellaneous"]
entries = {}

# Left side section (inputs)
input_frame = tk.Frame(window, bg="#f1f1f1")
input_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

for idx, label in enumerate(labels):
    tk.Label(input_frame, text=label, bg="#f1f1f1", fg="#333333", font=("Arial", 12)).grid(row=idx, column=0, pady=5, sticky="w")
    entry = tk.Entry(input_frame, bg="#ffffff", fg="#333333", font=("Arial", 12))
    entry.grid(row=idx, column=1, pady=5, padx=10, sticky="ew")
    entries[label] = entry

income_entry = entries["Income"]
rent_entry = entries["Rent"]
food_entry = entries["Food"]
utilities_entry = entries["Utilities"]
transportation_entry = entries["Transportation"]
entertainment_entry = entries["Entertainment"]
health_entry = entries["Health"]
education_entry = entries["Education"]
miscellaneous_entry = entries["Miscellaneous"]

# Right side section (buttons & toggle)
button_frame = tk.Frame(window, bg="#f1f1f1")
button_frame.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")

# Create buttons for calculate, save, and toggle
calculate_button = tk.Button(button_frame, text="Calculate Budget", bg="#3498db", fg="white", font=("Arial", 12), command=calculate_budget, relief="flat")
calculate_button.grid(row=0, column=0, pady=10, padx=40, sticky="ew")

save_button = tk.Button(button_frame, text="Save Budget", bg="#3498db", fg="white", font=("Arial", 12), command=save_budget, relief="flat")
save_button.grid(row=1, column=0, pady=10, padx=40, sticky="ew")

toggle_button = tk.Button(button_frame, text="Toggle Dark Mode", bg="#3498db", fg="white", font=("Arial", 12), command=toggle_dark_mode, relief="flat")
toggle_button.grid(row=2, column=0, pady=20, padx=40, sticky="ew")

# Run the application
window.mainloop()

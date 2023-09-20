import json
import tkinter as tk
from tkinter import messagebox

# Function to load user data from a JSON file
def load_user_data():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save user data to a JSON file
def save_user_data(users):
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)

# Function to handle the login button click event
def login_button_click():
    username = username_entry.get()
    password = password_entry.get()
    users = load_user_data()
    if username in users and users[username]["password"] == password:
        messagebox.showinfo("Login", "Logged in successfully.")
        main_menu(username)
    else:
        messagebox.showerror("Login Error", "Invalid username or password. Please try again.")

# Function to handle the create account button click event
def create_account_button_click():
    username = create_username_entry.get()
    password = create_password_entry.get()
    users = load_user_data()
    if username in users:
        messagebox.showerror("Create Account Error", "Username already exists. Please choose another username.")
    else:
        users[username] = {"password": password, "expenses": []}
        save_user_data(users)
        messagebox.showinfo("Create Account", "Account created successfully!")

# Function to open the expense tracker section
def open_expense_tracker(username):
    global expense_tracker_window  # Define expense_tracker_window as a global variable
    expense_tracker_window = tk.Toplevel()
    expense_tracker_window.title("Expense Tracker")

    # Create and place widgets for the expense tracker
    # You can add labels, entry fields, buttons, and other UI elements here
    # For example:
    expense_label = tk.Label(expense_tracker_window, text="Expense:")
    expense_label.pack()

    expense_entry = tk.Entry(expense_tracker_window)
    expense_entry.pack()

    add_expense_button = tk.Button(expense_tracker_window, text="Add Expense", command=lambda: add_expense(username, expense_entry.get()))
    add_expense_button.pack()
def open_expense_tracker(username):
    global expense_tracker_window  # Define expense_tracker_window as a global variable
    expense_tracker_window = tk.Toplevel()
    expense_tracker_window.title("Expense Tracker")

    # Create and place widgets for the expense tracker
    expense_label = tk.Label(expense_tracker_window, text="Expense:")
    expense_label.pack()

    expense_entry = tk.Entry(expense_tracker_window)
    expense_entry.pack()

    add_expense_button = tk.Button(expense_tracker_window, text="Add Expense", command=lambda: add_expense(username, expense_entry.get()))
    add_expense_button.pack()

    display_expense_button = tk.Button(expense_tracker_window, text="Display Expenses", command=lambda: display_expenses(username))
    display_expense_button.pack()

    # You can continue adding more widgets as needed

# Rest of your code remains the same
# Function to add an expense to the user's expenses list
def add_expense(username, expense):
    users = load_user_data()
    if username in users:
        users[username]["expenses"].append(expense)
        save_user_data(users)
        messagebox.showinfo("Add Expense", "Expense added successfully!")
    else:
        messagebox.showerror("Add Expense Error", "User not found.")

# Function to display the user's expenses
def display_expenses(username):
    users = load_user_data()
    if username in users:
        expenses = users[username]["expenses"]
        if expenses:
            expense_list = "\n".join(expenses)
            messagebox.showinfo("Expenses", f"Your expenses:\n{expense_list}")
        else:
            messagebox.showinfo("Expenses", "No expenses recorded.")
    else:
        messagebox.showerror("Display Expenses Error", "User not found.")


    # You can continue adding more widgets as needed

# Rest of the code remains the same
# Define currency_converter_window as a global variable
currency_converter_window = None

# ...

def open_currency_converter():
    global currency_converter_window
    currency_converter_window = tk.Toplevel()
    currency_converter_window.title("Currency Converter")

def convert_currency():
    global currency_converter_window  # Make sure to access the global variable
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()
    amount = amount_entry.get()

    try:
        amount = float(amount)
    except ValueError:
        result_label.config(text="Invalid amount")
        return

    if from_currency in exchange_rates and to_currency in exchange_rates:
        # Perform the conversion
        conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * conversion_rate

        # Display the result
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        result_label.config(text="Invalid currency code(s)")

# Rest of the code remains the same
# Function to perform currency conversion
def open_currency_converter():
    global currency_converter_window
    currency_converter_window = tk.Toplevel()
    currency_converter_window.title("Currency Converter")

    # Create and place widgets for currency conversion
    from_currency_label = tk.Label(currency_converter_window, text="From Currency:")
    from_currency_label.pack()
    from_currency_entry = tk.Entry(currency_converter_window)
    from_currency_entry.pack()

    to_currency_label = tk.Label(currency_converter_window, text="To Currency:")
    to_currency_label.pack()
    to_currency_entry = tk.Entry(currency_converter_window)
    to_currency_entry.pack()

    amount_label = tk.Label(currency_converter_window, text="Amount:")
    amount_label.pack()
    amount_entry = tk.Entry(currency_converter_window)
    amount_entry.pack()

    # Create a label for displaying the result
    result_label = tk.Label(currency_converter_window, text="")
    result_label.pack()

    # Create a Convert button and link it to the convert_currency function
    convert_button = tk.Button(currency_converter_window, text="Convert", command=lambda: convert_currency(from_currency_entry, to_currency_entry, amount_entry, result_label))
    convert_button.pack()

def convert_currency(from_currency_entry, to_currency_entry, amount_entry, result_label):
    # Define a dictionary with exchange rates (as an example)
    exchange_rates = {
        "USD": 1.0,  # Base currency
        "EUR": 0.85,
        "GBP": 0.73,
        "JPY": 110.0,
        "INR": 74.22,  # Indian Rupee
        "AUD": 1.34,   # Australian Dollar
        "CAD": 1.25,   # Canadian Dollar
        "CNY": 6.45,   # Chinese Yuan
        "SGD": 1.35,   # Singapore Dollar
        "CHF": 0.92,   # Swiss Franc
        "HKD": 7.77,   # Hong Kong Dollar
        "KRW": 1160.0, # South Korean Won
        "MXN": 20.25,  # Mexican Peso
        # Add more currencies and their rates here
    }

    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()
    amount = amount_entry.get()

    try:
        amount = float(amount)
    except ValueError:
        result_label.config(text="Invalid amount")
        return

    if from_currency in exchange_rates and to_currency in exchange_rates:
        # Perform the conversion
        conversion_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * conversion_rate

        # Display the result
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        result_label.config(text="Invalid currency code(s)")


# Create a label for displaying the result
result_label = tk.Label(currency_converter_window, text="")
result_label.pack()

# Create a Convert button and link it to the convert_currency function
convert_button = tk.Button(currency_converter_window, text="Convert", command=convert_currency)
convert_button.pack()

pass

# Function to display the main menu after login
def main_menu(username):
    login_window.destroy()  # Close the login window
    main_menu_window = tk.Tk()
    main_menu_window.title("Main Menu")
    
    # Create and place buttons for different sections
    expense_tracker_button = tk.Button(main_menu_window, text="Expense Tracker", command=lambda: open_expense_tracker(username))
    expense_tracker_button.pack()
    
    currency_converter_button = tk.Button(main_menu_window, text="Currency Converter", command=open_currency_converter)
    currency_converter_button.pack()
    
    # You can add more buttons for other features here

    main_menu_window.mainloop()

# Create the login window
login_window = tk.Tk()
login_window.title("Login")

# Create and place widgets for login
username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

login_button = tk.Button(login_window, text="Login", command=login_button_click)
login_button.pack()

# Create and place widgets for account creation
create_username_label = tk.Label(login_window, text="Create Username:")
create_username_label.pack()
create_username_entry = tk.Entry(login_window)
create_username_entry.pack()

create_password_label = tk.Label(login_window, text="Create Password:")
create_password_label.pack()
create_password_entry = tk.Entry(login_window, show="*")
create_password_entry.pack()

create_account_button = tk.Button(login_window, text="Create Account", command=create_account_button_click)
create_account_button.pack()

login_window.mainloop()

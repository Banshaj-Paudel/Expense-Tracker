import datetime
import argparse

class Expense:
    def __init__(self, amount, category):
        self.amount = amount        
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.category = category

    def __str__(self):
        return f"Your expense is Rs.{self.amount} on {self.date}. Category: {self.category}"
    

class ExpenseTracker:
    expenses = []

    def add_expenses(self, expense):
        self.expenses.append(expense)

    def categorize_expenses(self):
        categories = {
            "food": [],
            "bills": [],
            "fun": [],
            "loan": [],
            "other": []
        }

        for expense in self.expenses:
            if expense.category in categories:
                categories[expense.category].append({
                    "amount": expense.amount,
                    "date": expense.date
                })
            else:
                categories["other"].append({
                    "category": expense.category,
                    "amount": expense.amount,
                    "date": expense.date
                })
        print(categories)
    
    def generate_report(self, start_date, end_date):
        filtered_expenses = [expense for expense in self.expenses if start_date <= expense.date <= end_date]
        for expense in filtered_expenses:
            print(expense)

    def display_expenses(self):
        for i in self.expenses:
            print(i)

def main():
    tracker = ExpenseTracker()
    print("Welcome to the Expense Tracker!")
    print("Available commands: add <amount> <category>, categorize, display, report <start_date> <end_date>, exit")

    while True:
        command = input("\nEnter command: ").strip().split()
        if not command:
            continue

        if command[0] == "exit":
            print("Exiting the Expense Tracker. Goodbye!")
            break

        elif command[0] == "add":
            if len(command) != 3:
                print("Invalid command. Usage: add <amount> <category>")
                continue
            try:
                amount = float(command[1])
                category = command[2]
                expense = Expense(amount, category)
                tracker.add_expenses(expense)
                print(f"Added expense: {expense}")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

        elif command[0] == "categorize":
            tracker.categorize_expenses()

        elif command[0] == "display":
            tracker.display_expenses()

        elif command[0] == "report":
            if len(command) != 3:
                print("Invalid command. Usage: report <start_date> <end_date>")
                continue
            start_date = command[1]
            end_date = command[2]
            tracker.generate_report(start_date, end_date)

        else:
            print("Invalid command. Available commands: add, categorize, display, report, exit")

if __name__ == "__main__":
    main()

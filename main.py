import datetime

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
    
    def generate_report(start_date,end_date):
        pass

    def display_expenses(self):
        for i in self.expenses:
            print(i)


ex1 = Expense(100,"food")
ex2 = Expense(300,"food")
ex3 = Expense(200,"bills")
ex4 = Expense(1200,"fun")
ex5 = Expense(1020,"loan")
ext1 = ExpenseTracker()
ext1.add_expenses(ex1)
ext1.add_expenses(ex2)
ext1.add_expenses(ex3)
ext1.add_expenses(ex4)
ext1.add_expenses(ex5)
ext1.display_expenses()
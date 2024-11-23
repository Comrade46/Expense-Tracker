import datetime
import json

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """Load expenses from a file."""
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_expenses(self):
        """Save expenses to a file."""
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, date, category, description, amount):
        """Add a new expense."""
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount,
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        """View all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nAll Expenses:")
        print("-" * 50)
        for expense in self.expenses:
            print(
                f"Date: {expense['date']}, Category: {expense['category']}, "
                f"Description: {expense['description']}, Amount: ${expense['amount']:.2f}"
            )
        print("-" * 50)

    def view_by_category(self, category):
        """View expenses by category."""
        filtered_expenses = [exp for exp in self.expenses if exp["category"].lower() == category.lower()]
        if not filtered_expenses:
            print(f"No expenses found in category: {category}")
            return
        print(f"\nExpenses in Category: {category}")
        print("-" * 50)
        for expense in filtered_expenses:
            print(
                f"Date: {expense['date']}, Description: {expense['description']}, Amount: ${expense['amount']:.2f}"
            )
        print("-" * 50)

    def calculate_total(self):
        """Calculate the total expenses."""
        total = sum(exp["amount"] for exp in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Calculate Total Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
            category = input("Enter category (e.g., Food, Rent, Utilities): ")
            description = input("Enter description: ")
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue
            tracker.add_expense(date, category, description, amount)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            category = input("Enter category to view: ")
            tracker.view_by_category(category)

        elif choice == "4":
            tracker.calculate_total()

        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

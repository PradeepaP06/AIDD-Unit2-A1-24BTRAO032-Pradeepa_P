"""Student Expense Splitter CLI."""

expenses = []


def add_expense(name, amount, category):
    """Add a new expense."""
    if not name:
        raise ValueError("Expense name cannot be empty")

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    expense = {
        "name": name,
        "amount": float(amount),
        "category": category
    }

    expenses.append(expense)
    return expense


def get_expenses():
    """Return all expenses."""
    return expenses


def calculate_total():
    """Calculate total expenses."""
    return sum(expense["amount"] for expense in expenses)


def calculate_category_total(category):
    """Calculate expenses for a category."""
    return sum(
        expense["amount"]
        for expense in expenses
        if expense["category"].lower() == category.lower()
    )


def delete_expense(index):
    """Delete an expense by index."""
    if index < 0 or index >= len(expenses):
        raise IndexError("Invalid expense index")

    return expenses.pop(index)


def display_expenses():
    """Display all expenses."""
    if not expenses:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['name']} - "
            f"₹{expense['amount']:.2f} - "
            f"{expense['category']}"
        )


def main():
    """Run the expense tracker CLI."""
    while True:
        print("\n--- Student Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. View Category Total")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                name = input("Expense name: ")
                amount = float(input("Amount: "))
                category = input("Category: ")

                add_expense(name, amount, category)
                print("Expense added successfully!")

            elif choice == "2":
                display_expenses()

            elif choice == "3":
                print(f"Total: ₹{calculate_total():.2f}")

            elif choice == "4":
                category = input("Enter category: ")
                print(
                    f"Total for {category}: "
                    f"₹{calculate_category_total(category):.2f}"
                )

            elif choice == "5":
                display_expenses()
                index = int(input("Enter expense number to delete: ")) - 1
                delete_expense(index)
                print("Expense deleted successfully!")

            elif choice == "6":
                print("Thank you for using Expense Tracker!")
                break

            else:
                print("Invalid choice.")

        except (ValueError, IndexError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
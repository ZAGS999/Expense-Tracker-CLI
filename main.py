from tracker import init_file, add_expense, view_expenses, total_spending, delete_expenses

def main():
    init_file()

    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Total expenses")
        print("4. Delete expense")
        print("5. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            date_str = input("Date (YYYY-MM-DD): ")
            category = input("Category: ")
            amount = input("Amount: ")
            description = input("Description: ")
            add_expense(date_str, category, amount, description)
            print("Expense added.")

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            total_spending()

        elif choice == '4':
            view_expenses()
            try:
                index = int(input("Enter the row number to delete: "))
                delete_expenses(index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '5':
            print("See you next time!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

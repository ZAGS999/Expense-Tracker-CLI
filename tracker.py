import csv
from datetime import datetime

FILENAME = "expenses.csv"
FIELDS = ["date", "category", "amount", "description"]

def init_file():
    try:
        with open(FILENAME, 'x', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()  
    except FileExistsError:
        pass

def add_expense(date_str, category, amount, description):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD")
        return

    with open(FILENAME, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow({
            "date": date_str,
            "category": category,
            "amount": f"{float(amount):.2f}",
            "description": description
        })

def view_expenses():
    with open(FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            print(f"{i}: {row}")

def total_spending():
    total = 0
    with open(FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                total += float(row["amount"])
            except ValueError:
                print(f"Skipping invalid row: {row}")
    print(f"Total spending: ${total:.2f}")

def delete_expenses(index_to_delete):
    expenses = []
    with open(FILENAME, 'r') as f:
        reader = csv.DictReader(f)
        expenses = list(reader)

    if 0 <= index_to_delete < len(expenses):
        deleted = expenses.pop(index_to_delete)
        print(f"Deleted: {deleted}")
    else:
        print("Invalid index.")
        return

    with open(FILENAME, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)

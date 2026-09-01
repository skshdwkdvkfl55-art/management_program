import csv

def save_expenses(file_path, expenses):
    # CSV의 열(Column) 이름표 정의
    fieldnames = ["date", "category", "description", "amount"]
    
    with open(file_path, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


def load_expenses(file_path):
    expenses = []
    
    try:
        with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row["amount"] = int(row["amount"])
                    expenses.append(row)
                except ValueError:
                    print("⚠️ 금액이 올바르지 않은 행은 건너뜁니다:", row)
                    continue
                    
    except FileNotFoundError:
        return []
        
    return expenses

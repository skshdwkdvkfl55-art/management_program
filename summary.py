def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total

def calculate_by_category(expenses):
    category_totals = {}
    
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
            
    return category_totals


purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(purchases):
    return sum(p["price"] * p["quantity"] for p in purchases)

def items_by_category(purchases):
    result = {}
    for p in purchases:
        cat = p["category"]
        item = p["item"]
        if cat not in result:
            result[cat] = set()
        result[cat].add(item)
    return {k: list(v) for k, v in result.items()}

def expensive_purchases(purchases, min_price):
    return [p for p in purchases if p["price"] >= min_price]

def average_price_by_category(purchases):
    sums = {}
    counts = {}

    for p in purchases:
        cat = p["category"]
        sums[cat] = sums.get(cat, 0) + p["price"]
        counts[cat] = counts.get(cat, 0) + 1

    return {cat: sums[cat] / counts[cat] for cat in sums}

def most_frequent_category(purchases):
    totals = {}
    for p in purchases:
        cat = p["category"]
        totals[cat] = totals.get(cat, 0) + p["quantity"]
    return max(totals, key=totals.get)


report = []

report.append(f"Общая выручка: {total_revenue(purchases)}")
report.append(f"Товары по категориям: {items_by_category(purchases)}")
report.append(f"Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}")
report.append(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
report.append(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")

# вывод в консоль
for line in report:
    print(line)

# запись в файл
with open("report.txt", "w", encoding="utf-8") as f:
    for line in report:
        f.write(str(line) + "\n")

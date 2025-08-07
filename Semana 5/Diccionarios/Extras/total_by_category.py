products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]


def get_total_by_category(sales):
    grouped_sales = {}

    for sale in sales:
        category = sale["category"]

        if category in grouped_sales:
            grouped_sales[category] += sale["price"]
        else:
            grouped_sales[category] = sale["price"]

    return grouped_sales


print(get_total_by_category(products))

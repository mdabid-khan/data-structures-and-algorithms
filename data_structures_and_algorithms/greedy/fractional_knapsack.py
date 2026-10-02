def frac_knap(capacity, items):
    items.sort(key=lambda item: item['profit'] / item['weight'], reverse=True)

    total_profit = 0

    for item in items:
        if capacity >= item['weight']:
            capacity -= item['weight']
            total_profit += item['profit']
        else:
            fraction = capacity / item['weight']
            total_profit += item['profit'] * fraction
            capacity = 0
            break

    return total_profit


kachabazar_list = [
    {'profit': 10, 'weight': 2},
    {'profit': 5, 'weight': 3},
    {'profit': 15, 'weight': 5},
    {'profit': 7, 'weight': 7},
    {'profit': 6, 'weight': 1},
    {'profit': 10, 'weight': 2}
]

bazarbag_cap = 15

max_profit = frac_knap(bazarbag_cap, kachabazar_list)

print(f"Maximum profit: {max_profit}")
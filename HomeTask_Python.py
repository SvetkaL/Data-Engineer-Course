purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
#item — название товара,
#category — категория товара,
#price — цена за единицу товара,
#quantity — количество единиц, купленных за один раз

#1 total_revenue(purchases): Рассчитайте и верните общую выручку (цена * количество для всех записей).
#2 items_by_category(purchases): Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории
#3 expensive_purchases(purchases, min_price): Выведите все покупки, где цена товара больше или равна min_price.
#4 average_price_by_category(purchases): Рассчитайте среднюю цену товаров по каждой категории.
#5 most_frequent_category(purchases): Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity)


def total_revenue(kwargs):
    prices = [kwargs[i]['price'] for i in range(len(kwargs))]
    quantities = [kwargs[i]['quantity'] for i in range(len(kwargs))]
    return sum([prices[i]*quantities[i] for i in range(len(kwargs))])

def items_by_category(kwargs):
    dt = {}
    for i in range(len(kwargs)):
        if kwargs[i]['category'] not in dt.keys():
            dt[kwargs[i]['category']] = [kwargs[i]['item']]
        else:
            dt[kwargs[i]['category']].append(kwargs[i]['item'])
    return dt

def expensive_purchases(kwargs, min_price):
    ls = []
    for i in range(len(kwargs)):
        if kwargs[i]['price'] >= min_price:
            ls.append(kwargs[i])
    return ls

def average_price_by_category(kwargs):
    dt = {}
    for i in range(len(kwargs)):
        if kwargs[i]['category'] not in dt.keys():
            dt[kwargs[i]['category']] = [kwargs[i]['price']]
        else:
            dt[kwargs[i]['category']].append(kwargs[i]['price'])
    dt_avg = {}
    for k, v in dt.items():
        dt_avg[k] = sum(v) / len(v)
    return dt_avg

def most_frequent_category(kwargs):
    dt = {}
    for i in range(len(kwargs)):
        if kwargs[i]['category'] not in dt.keys():
            dt[kwargs[i]['category']] = kwargs[i]['quantity']
        else:
            dt[kwargs[i]['category']] += kwargs[i]['quantity']
    sort_dt = sorted(dt.items(), key=lambda item: item[1], reverse=True)
    return sort_dt[0][0]

print(total_revenue(purchases))
print(items_by_category(purchases))
print(expensive_purchases(purchases, 1.5))
print(average_price_by_category(purchases))
print(most_frequent_category(purchases))
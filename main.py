import csv
import matplotlib.pyplot as plt


def read_sales_data(file_path):
    sales_data = []
    with open(file_path, encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            sales_data.append({
                'product_name': row[0],
                'quantity': int(row[1]),
                'price': int(row[2]),
                'date': row[3]
            })

    return sales_data


def total_sales_per_product(sales_data):
    total_sales = {}
    for item in sales_data:
        product_name = item['product_name']
        total_sales[product_name] = total_sales.get(product_name, 0) + item['quantity'] * item['price']
    return total_sales


def sales_over_time(sales_data):
    sales_by_date = {}
    for item in sales_data:
        date = item['date']
        sales_by_date[date] = sales_by_date.get(date, 0) + item['quantity'] * item['price']
    return sales_by_date


def plot_total_sales_per_product(total_sales):
    products = list(total_sales.keys())
    sales = list(total_sales.values())

    plt.figure(figsize=(10, 5))
    plt.bar(products, sales, color='blue')
    plt.xlabel('Продукт')
    plt.ylabel('Сумма продаж')
    plt.title('График общей суммы продаж по каждому продукту')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_sales_over_time(sales_by_date):
    dates = sorted(sales_by_date.keys())
    sales = [sales_by_date[date] for date in dates]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, sales, marker='o', linestyle='-', color='green')
    plt.xlabel('Дата')
    plt.ylabel('Сумма продаж в день')
    plt.title('График общей суммы продаж по дням')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main(file_path):
    sales_data = read_sales_data(file_path)

    total_sales = total_sales_per_product(sales_data)
    sales_by_date = sales_over_time(sales_data)

    max_product = max(total_sales.items(), key=lambda item: item[1])[0]
    max_date = max(sales_by_date.items(), key=lambda item: item[1])[0]

    print(f'Наибольшую выручку принес продукт: {max_product}')
    print(f'Наибольшая выручка была {max_date}')

    plot_total_sales_per_product(total_sales)
    plot_sales_over_time(sales_by_date)


if __name__ == '__main__':
    main('./products.csv')

import sqlite3

conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

def display_stores():
    cursor.execute("SELECT store_id, title FROM store")
    stores = cursor.fetchall()
    print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")

def display_products(store_id):
    cursor.execute("""
        SELECT p.title, c.title, p.unit_price, p.stock_quantity 
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    """, (store_id,))
    products = cursor.fetchall()
    for product in products:
        print(f"Название продукта: {product[0]}")
        print(f"Категория: {product[1]}")
        print(f"Цена: {product[2]}")
        print(f"Количество на складе: {product[3]}")
        print()

while True:
    display_stores()
    choice = int(input())
    if choice == 0:
        break
    display_products(choice)

conn.close()

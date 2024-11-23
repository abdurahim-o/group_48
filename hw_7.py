import sqlite3

def create_database():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
            price REAL NOT NULL DEFAULT 0.0 CHECK(price >= 0.0),
            quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0)
        )
    ''')

    conn.commit()
    conn.close()

def add_products():
    products = [
        ("Мыло", 25.5, 10),
        ("Шампунь", 150.0, 5),
        ("Зубная паста", 80.0, 20),
        ("Лосьон", 200.0, 8),
        ("Крем для рук", 120.0, 15),
        ("Гель для душа", 180.0, 7),
        ("Бритва", 300.0, 10),
        ("Зубная щетка", 60.0, 30),
        ("Пена для бритья", 210.0, 6),
        ("Дезодорант", 150.0, 12),
        ("Крем для лица", 250.0, 9),
        ("Маска для лица", 90.0, 11),
        ("Тоник", 110.0, 13),
        ("Лак для волос", 140.0, 5),
        ("Мусс для укладки", 190.0, 4)
    ]

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)
    ''', products)

    conn.commit()
    conn.close()

def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE products
        SET quantity = ?
        WHERE id = ?
    ''', (new_quantity, product_id))

    conn.commit()
    conn.close()

def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE products
        SET price = ?
        WHERE id = ?
    ''', (new_price, product_id))

    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM products
        WHERE id = ?
    ''', (product_id,))

    conn.commit()
    conn.close()

def select_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()

def select_products_below_price_and_above_quantity(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM products
        WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()

def search_products_by_title(search_term):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM products
        WHERE product_title LIKE ?
    ''', ('%' + search_term + '%',))
    products = cursor.fetchall()

    for product in products:
        print(product)

    conn.close()


create_database()
add_products()
print("Initial Products:")
select_all_products()

update_quantity(1, 15)
update_price(1, 30.0)
print("\nAfter Updates:")
select_all_products()

delete_product(3)
print("\nAfter Deletion:")
select_all_products()

print("\nProducts below price limit and above quantity limit:")
select_products_below_price_and_above_quantity(100, 5)

print("\nSearch products by title 'мыло':")
search_products_by_title("мыло")

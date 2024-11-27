#import sqlite3

#conn = sqlite3.connect('school.db')
#cursor = conn.cursor()

#cursor.execute('''
#CREATE TABLE countries (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    title TEXT NOT NULL
#)
#''')

#countries_data = [('Кыргызстан'), ('Германия'), ('Китай')]
#cursor.executemany('INSERT INTO countries (title) VALUES (?)', [(title,) for title in countries_data])

#cursor.execute('''
#CREATE TABLE cities (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    title TEXT NOT NULL,
#    area REAL DEFAULT 0,
#    country_id INTEGER,
#    FOREIGN KEY (country_id) REFERENCES countries(id)
#)
#''')


#cities_data = [
#    ('Бишкек', 200.0, 1),
#    ('Ош', 150.0, 1),
#    ('Берлин', 891.8, 2),
#    ('Гамбург', 755.0, 2),
#    ('Пекин', 16410.54, 3),
#    ('Шанхай', 6340.5, 3),
#    ('Тяньцзинь', 11760.0, 3)
#]
#cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities_data)


#cursor.execute('''
#CREATE TABLE students (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    first_name TEXT NOT NULL,
#    last_name TEXT NOT NULL,
#    city_id INTEGER,
#    FOREIGN KEY (city_id) REFERENCES cities(id)
#)
#''')

#students_data = [
#    ('Нурлан', 'Токтобеков', 1),
#    ('Садыр', 'Жапаров', 1),
#    ('Алексей', 'Бондарев', 2),
#    ('Диана', 'Смирнова', 2),
#    ('Томас', 'Мюллер', 3),
#    ('Клаус', 'Шмидт', 3),
#    ('Таня', 'Лебедева', 4),
#    ('Томас', 'Мюллер', 4),
#]
#cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)', students_data)

#conn.commit()
#conn.close()

import sqlite3


def main():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()


    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    cursor.execute('SELECT id, title FROM cities')
    cities = cursor.fetchall()

    for city in cities:
        print(f"{city[0]}: {city[1]}")

    while True:

        city_id = int(input("Введите id города: "))

        if city_id == 0:
            print("Вы вышли из программы.")
            break

        cursor.execute('''
            SELECT s.first_name, s.last_name, c.title, co.title, c.area
            FROM students s
            JOIN cities c ON s.city_id = c.id
            JOIN countries co ON c.country_id = co.id
            WHERE c.id = ?
        ''', (city_id,))

        students = cursor.fetchall()

        if students:
            print(f"\nСписок учеников из города с id {city_id}:")
            for student in students:
                print(
                    f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[3]}, Город: {student[2]}, Площадь города: {student[4]}")
        else:
            print("Нет учеников в этом городе.")

    conn.close()


if __name__ == '__main__':
    main()

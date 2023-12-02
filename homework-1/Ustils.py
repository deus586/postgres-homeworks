import csv
import psycopg2


def writer(path, create_table):
    """
    Подключается к базу данных и записывает таблицы
    """
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='ShAmAn5861'
    )
    try:
        with conn:
            with conn.cursor() as cur:

                # Запускаем скрипты создания таблиц
                cur.execute(create_table)

                with open(path, encoding='utf-8') as emp_file:
                    # Записываем строкой название таблицы в которую будем записывать строки
                    table = path.split('_')[1].split('/')[-1]

                    # Убираем заголовки
                    heading = next(emp_file)

                    reader_object = csv.reader(emp_file, delimiter=",")

                    for row in reader_object:
                        # цикл записи в таблицы с разным количеством столбцов
                        rows_count = "%s, " * len(row)
                        cur.execute(f"INSERT INTO {table} VALUES ({rows_count[:-2]})",
                                    tuple(row))
    finally:
        conn.close()

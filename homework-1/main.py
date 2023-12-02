"""Скрипт для заполнения данными таблиц в БД Postgres."""
from Ustils import writer


# Список скриптов для динамического создания таблиц
TABLES = ["CREATE TABLE employees ( employee_id int PRIMARY KEY, first_name varchar(100), last_name varchar(100),"
          " title varchar(100), birth_date date, notes text );",

          "CREATE TABLE customers ( customer_id varchar(100) PRIMARY KEY,"
          " company_name varchar(100), contact_name varchar(100) );",

          "CREATE TABLE orders ( order_id int PRIMARY KEY, customer_id varchar(100) REFERENCES customers(customer_id),"
          " employee_id int REFERENCES employees(employee_id), order_date date, ship_city varchar(100) );"
          ]

# Список csv файлов
files = ["north_data/employees_data.csv", "north_data/customers_data.csv", "north_data/orders_data.csv"]

# Поочерёдное подключение к csv файлам
for ind in range(len(files)):
    writer(files[ind], TABLES[ind])

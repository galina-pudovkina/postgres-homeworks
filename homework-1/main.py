"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

FILE_PATH_CUSTUMERS = "../homework-1/north_data/customers_data.csv"
FILE_PATH_EMPLOYEES = "../homework-1/north_data/employees_data.csv"
FILE_PATH_ORDERS = "../homework-1/north_data/orders_data.csv"

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='12345'
)


def insert_to_db(query, file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        data = csv.reader(f)
        next(data)
        with conn.cursor() as cur:
            cur.executemany(query, data)

query_customers = "INSERT INTO customers (customer_id,company_name,contact_name) VALUES (%s, %s, %s)"

query_employees = "INSERT INTO employees (employee_id,first_name,last_name,title,birth_date,notes)" \
                  " VALUES (%s, %s, %s, %s, %s, %s)"

query_orders = "INSERT INTO orders (order_id,customer_id,employee_id,order_date,ship_city) VALUES (%s, %s, %s, %s, %s)"

insert_to_db(query_customers, FILE_PATH_CUSTUMERS)
insert_to_db(query_employees, FILE_PATH_EMPLOYEES)
insert_to_db(query_orders, FILE_PATH_ORDERS)
conn.commit()
conn.close()

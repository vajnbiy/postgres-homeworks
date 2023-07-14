"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv
import psycopg2

with open('north_data/employees_data.csv', newline='\n') as file:
    emp_data = list(csv.reader(file, delimiter=',', quotechar='"'))

with open('north_data/customers_data.csv', newline='\n') as file:
    customer_data = list(csv.reader(file, delimiter=',', quotechar='"'))

with open('north_data/orders_data.csv', newline='\n') as file:
    orders_data = list(csv.reader(file, delimiter=',', quotechar='"'))


a = input('Password\n')

with psycopg2.connect(
    database='north',
    user='postgres',
    password=a,
    host='localhost') as conn:
    with conn.cursor() as cur:
        for entry in emp_data[1:]:
            cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                        (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))

    with conn.cursor() as cur:
        for entry in customer_data[1:]:
            cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                        (entry[0], entry[1], entry[2]))

    with conn.cursor() as cur:
        for entry in orders_data[1:]:
            cur.execute('INSERT INTO order_data VALUES (%s, %s, %s, %s, %s)',
                        (entry[0], entry[1], entry[2], entry[3], entry[4]))

conn.close()
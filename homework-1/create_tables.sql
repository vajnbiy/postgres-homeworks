-- SQL-команды для создания таблиц

CREATE TABLE employees (
	emp_id int PRIMARY KEY,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(50),
	birth_date date NOT NULL,
	notes text
);

CREATE TABLE customers (
	customer_id char(5) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(50)
);

CREATE TABLE order_data (
	order_id varchar(10) PRIMARY KEY,
	customer_id char(5) REFERENCES customers(customer_id),
	emp_id int REFERENCES employees(emp_id),
	order_date date NOT NULL,
	ship_city varchar(50)
);
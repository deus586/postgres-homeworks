-- Подключиться к БД Northwind и сделать следующие изменения:
-- 1. Добавить ограничение на поле unit_price таблицы products (цена должна быть больше 0)

ALTER TABLE products
ADD CONSTRAINT check_price
CHECK (unit_price > 0)

-- 2. Добавить ограничение, что поле discontinued таблицы products может содержать только значения 0 или 1

ALTER TABLE products
ADD CONSTRAINT check_discont
CHECK (discontinued BETWEEN 0 AND 1)

-- 3. Создать новую таблицу, содержащую все продукты, снятые с продажи (discontinued = 1)

CREATE TABLE discontinued_units(
	product_id int PRIMARY KEY,
	product_name varchar(100),
	supplier_id int,
	category_id int,
	quantity_per_unit varchar(100),
	unit_price real,
	units_in_stock int,
	units_in_order int,
	reorder_level int,
	discontinued int
);

INSERT INTO discontinued_units SELECT * FROM products WHERE discontinued = 1

-- 4. Удалить из products товары, снятые с продажи (discontinued = 1)
-- Для 4-го пункта может потребоваться удаление ограничения, связанного с foreign_key. Подумайте, как это можно решить, чтобы связь с таблицей order_details все же осталась.

ALTER TABLE order_details DROP CONSTRAINT fk_order_details_products;
DELETE FROM products WHERE discontinued = 1;
DELETE FROM order_details WHERE product_id NOT IN (SELECT product_id FROM products);
DELETE FROM orders WHERE order_id NOT IN (SELECT order_id FROM order_details);
ALTER TABLE order_details ADD CONSTRAINT fk_order_details_products FOREIGN KEY(product_id) REFERENCES products(product_id);


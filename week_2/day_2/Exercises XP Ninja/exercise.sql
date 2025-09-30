--Q1
SELECT first_name, last_name
FROM customers
ORDER BY last_name ASC, first_name ASC
LIMIT 2 OFFSET (
  (SELECT COUNT(*) FROM customers) - 2
);

-- Q2
DELETE FROM purchases
WHERE customer_id = (
    SELECT customer_id FROM customers WHERE first_name = 'Scott'
);

-- Q3

SELECT * 
FROM customers
WHERE first_name = 'Scott';

-- Q4
SELECT p.purchase_id, p.product_id, c.first_name, c.last_name
FROM purchases p
LEFT JOIN customers c ON p.customer_id = c.customer_id;

-- Q5

SELECT p.purchase_id, p.product_id, c.first_name, c.last_name
FROM purchases p
INNER JOIN customers c ON p.customer_id = c.customer_id;
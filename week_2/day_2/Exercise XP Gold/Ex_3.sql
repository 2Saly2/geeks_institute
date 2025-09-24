
CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    item_id INT REFERENCES items(id),
    quantity_purchased INT
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name='Scott' AND last_name='Scott'),
    (SELECT id FROM items WHERE item_name='Fan'),
    1
);


INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name='Melanie' AND last_name='Johnson'),
    (SELECT id FROM items WHERE item_name='Large Desk'),
    10
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name='Greg' AND last_name='Jones'),
    (SELECT id FROM items WHERE item_name='Small Desk'),
    2
);


SELECT * FROM purchases;


SELECT p.id, c.first_name, c.last_name, p.item_id, p.quantity_purchased
FROM purchases p
JOIN customers c ON p.customer_id = c.id;


SELECT * 
FROM purchases
WHERE customer_id = 5;


SELECT p.*, i.item_name
FROM purchases p
JOIN items i ON p.item_id = i.id
WHERE i.item_name IN ('Large Desk','Small Desk');


SELECT c.first_name, c.last_name, i.item_name
FROM purchases p
JOIN customers c ON p.customer_id = c.id
JOIN items i ON p.item_id = i.id;


INSERT INTO purchases (customer_id, quantity_purchased)
VALUES (3, 5);


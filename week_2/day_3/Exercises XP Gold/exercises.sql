-- Exercise 1 : DVD Rentals
-- Q1
SELECT rental_id, rental_date,inventory_id,customer_id
FROM rental
WHERE return_date IS NULL ;

-- Q2
SELECT c.customer_id, c.first_name, c.last_name,COUNT(r.rental_id) AS not_returned
FROM customer c
JOIN rental r ON c.customer_id =r.customer_id
WHERE r.return_date IS NULL
GROUP BY c.customer_id, c.first_name,c.last_naame
ORDER BY not_returned DESC;

-- Q3

SELECT f.title , a.first_name ,a.last_name,c.name AS category
FROM film 
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Action'
  AND a.first_name = 'Joe'
  AND a.last_name = 'Swank';

-- Shortcut idea
CREATE VIEW not_returned_rentals AS
SELECT rental_id, customer_id, inventory_id
FROM rental
WHERE return_date IS NULL;


-- Exercise 2 – Happy Halloween

-- Q1

SELECT s.store_id, ci.city, co.country
FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id;

-- Q2
SELECT i.store_id, SUM(f.length) AS total_minutes
FROM inventory i
JOIN film f ON i.film_id = f.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NOT NULL
GROUP BY i.store_id;

-- Q3

SELECT DISTINCT c.customer_id, c.first_name, c.last_name, ci.city
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE ci.city_id IN (
  SELECT ci.city_id
  FROM store s
  JOIN address a ON s.address_id = a.address_id
  JOIN city ci ON a.city_id = ci.city_id
);

-- Q4
SELECT DISTINCT c.customer_id, c.first_name, c.last_name, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country_id IN (
  SELECT co.country_id
  FROM store s
  JOIN address a ON s.address_id = a.address_id
  JOIN city ci ON a.city_id = ci.city_id
  JOIN country co ON ci.country_id = co.country_id
);





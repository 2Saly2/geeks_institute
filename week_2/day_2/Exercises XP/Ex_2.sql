SELECT * from customer;

SELECT CONCAT(first_name," ",last_name)
AS full_name FROM customer ;

SELECT DISTINCT create_date FROM customer;

SELECT * FROM customer 
ORDER BY first_name DESC;

SELECT film_id, title,description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

SELECT address, phone
FROM address
WHERE district = 'Texas';

SELECT *
FROM film
WHERE film_id IN (15, 150);

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'ACADEMY DINOSAUR';

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title LIKE 'AC%';

SELECT * FROM film
ORDER BY rental_rate ASC
LIMIT 10;

SELECT * FROM film
ORDER BY rental_rate ASC
LIMIT 10 OFFSET 10;

WITH RankedFilms AS (
SELECT *,
ROW_NUMBER() OVER (ORDER BY rental_rate ASC) as rn
FROM film
)
SELECT * FROM RankedFilms
WHERE rn > 10 AND rn <= 20;

SELECT
c.first_name,
c.last_name,
p.amount,
p.payment_date
FROM customer AS c
JOIN payment AS p
ON c.customer_id = p.customer_id
ORDER BY c.customer_id ASC;

SELECT f.title
FROM film AS f
LEFT JOIN inventory AS i
ON f.film_id = i.film_id
WHERE i.film_id IS NULL;

SELECT city.city, country.country
FROM city
JOIN country
ON city.country_id = country.country_id;

SELECT
c.customer_id,
c.first_name,
c.last_name,
p.amount,
p.payment_date
FROM customer AS c
JOIN payment AS p
ON c.customer_id = p.customer_id
ORDER BY p.staff_id ASC;







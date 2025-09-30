-- Q1

SELECT DISTINCT f.film_id, f.title, f.rating
FROM film 
JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE f.rating IN ('G','PG')
AND (r.rental_id IS NULL OR r.return_date IS NOT NULL);

-- Q2
CREATE TABLE waiting_list (
    waiting_id SERIAL PRIMARY KEY,
    film_id INT NOT NULL REFERENCES film(film_id),
    child_name VARCHAR(100) NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Q3

SELECT f.film_id, f.title, COUNT(w.waiting_id) AS num_waiting
FROM film f
LEFT JOIN waiting_list w ON f.film_id = w.film_id
WHERE f.rating IN ('G', 'PG')
GROUP BY f.film_id, f.title
ORDER BY num_waiting DESC;


INSERT INTO waiting_list (film_id, child_name)
VALUES (12, 'Sara'), (12, 'Amine'), (15, 'Aya');
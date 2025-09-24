SELECT rating , COUNT(*) As number_of_films
FROM film
GROUP BY rating;

SELECT film_id,title,rating
FROM film 
WHERE rating IN('G','PG-13');

SELECT *
FROM film 
WHERE rating IN('G','PG-13')
AND length < 120
AND rental_rate < 3.00
ORDER BY title ASC;

UPDATE customer 
SET first_name = 'Nouhaila',
    last_name='Ail lahssaine',
    email = 'aitlahssainenouhaila @gmail.com'
WHERE customer_id = 1 ;

SELECT address_id 
FROM customer 
WHERE customer_id =1;

UPDATE address
SET address = 'Shellalate ',
    district = 'Mohemmadia',
    postal_code = '20000',
    phone = '0674798654'
WHERE adress_id =5;






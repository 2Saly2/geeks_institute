SELECT * 
FROM language;

SELECT f.title ,f.description , l.name AS language_name 
FROM film f
JOIN language l On f.language_id = l.language_id;

SELECT f.title ,f.description , l.name AS language_name 
FROM language l
LEFT JOIN film f On f.language_id = l.language_id;

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY ,
    name VARCHAR(255) NOT NULL,
);

INSERT INTO new_film (name) 
values ('film 1'),('film 2');

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255) NOT NULL,
    score INT CHECK (score >=1 AND score <=10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customer_review(film_id , language_id,title,score,review_text)
VALUES 
(1,1,'Great Movie',9,'loved the story and acting'),
(2,1,' not bad',7,'good , but could be better');

DELETE FROM new_film
WHERE id = 1;


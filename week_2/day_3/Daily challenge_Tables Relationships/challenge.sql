-- part 1 : relationships one to one

CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);



CREATE TABLE customer_profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT false,
    customer_id INT UNIQUE REFERENCES customer(id)
);


INSERT INTO customer (first_name, last_name)
VALUES 
('Youssef', 'El Fassi'),
('Salma', 'Benali'),
('Nadia', 'Ouardi');



INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES 
(true, (SELECT id FROM customer WHERE first_name = 'Youssef')),
(false, (SELECT id FROM customer WHERE first_name = 'Salma'));



SELECT c.first_name
FROM customer c
JOIN customer_profile p ON c.id = p.customer_id
WHERE p.isLoggedIn = true;



SELECT c.first_name, p.isLoggedIn
FROM customer c
LEFT JOIN customer_profile p ON c.id = p.customer_id;


SELECT COUNT(*) AS not_logged_in_count
FROM customer c
LEFT JOIN customer_profile p ON c.id = p.customer_id
WHERE p.isLoggedIn IS DISTINCT FROM true;


-- part 2 : relationships many to many

CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);


INSERT INTO book (title, author)
VALUES
('Le Passé Simple', 'Driss Chraïbi'),
('La Civilisation, ma Mère!', 'Driss Chraïbi'),
('Le Pain Nu', 'Mohamed Choukri');



CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    age INT CHECK (age <= 15)
);


INSERT INTO student (name, age)
VALUES
('Jalal', 12),
('Laila', 11),
('Saaid', 10),
('Brahim', 14);

CREATE TABLE library (
    book_fk_id INT REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id INT REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id, borrowed_date)
);



INSERT INTO library (book_fk_id, student_fk_id, borrowed_date)
VALUES
((SELECT book_id FROM book WHERE title='Le Passé Simple'),
 (SELECT student_id FROM student WHERE name='Jalal'),
 '2022-02-15'),

((SELECT book_id FROM book WHERE title='La Civilisation, ma Mère!'),
 (SELECT student_id FROM student WHERE name='Brahim'),
 '2021-03-03'),

((SELECT book_id FROM book WHERE title='Le Passé Simple'),
 (SELECT student_id FROM student WHERE name='Laila'),
 '2021-05-23'),

((SELECT book_id FROM book WHERE title='Le Pain Nu'),
 (SELECT student_id FROM student WHERE name='Brahim'),
 '2021-08-12');


SELECT * FROM library;

SELECT s.name, b.title, l.borrowed_date
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id;


SELECT AVG(s.age) AS avg_age
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Le Passé Simple';

DELETE FROM student WHERE name = 'Brahim';



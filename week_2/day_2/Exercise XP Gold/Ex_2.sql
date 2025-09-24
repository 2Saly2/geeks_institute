
UPDATE students
SET birth_date ='1999-11-02'
WHERE (first_name = 'lea' AND last_name = 'Benichou')
  OR (first_name = 'Marc' AND last_name = 'Benichou');


UPDATE students 
SET last_name ='Guez'
WHERE ferst_name = 'David' AND last_name = 'Grez';

DELETE FROM students 
WHERE first_name = 'Lea' AND last_name = 'Benichou';

SELECT COUNT(*) As toutal_students
FROM students;

SELECT COUNT(*) AS born_after_year_2000
FROM students
WHERE birth_date > '2000-01-01';


ALTER TABLE students
ADD COLUMN math_grade INT ;


UPDATE students
SET math_grade = 80
WHERE id = 1;

UPDATE students 
SET math_grade = 90
WHERE id IN (2,4);

UPDATE students
SET math_grade = 40
WHERE id = 6;


SELECT COUNT(*) AS grande_above_83
FROM students 
WHERE math_grade >83;

INSERT INTO students (first_name, last_name, birth_date, math_grade)
VALUES ('Omer', 'Simpson', (SELECT birth_date FROM students WHERE first_name='Omer' AND last_name='Simpson' LIMIT 1), 70);


SELECT first_name, last_name, COUNT(math_grade) AS total_grade
FROM students
GROUP BY first_name, last_name;

SELECT SUM(math_grade) AS total_sum
FROM students ;




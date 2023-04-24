-- this project is continues of SQL101 course project

-- creating a new table that only has students who have a High GPA using the student table
CREATE TABLE excellent_students SELECT * FROM student WHERE GPA > 4.49;

-- creating a new table that only has students who have a low GPA using the student table
CREATE TABLE failed_students SELECT * FROM student WHERE GPA < 2;

-- retrieve student's info whose names start with an A
SELECT * FROM student WHERE student_name LIKE ("A%");

-- retrieve student's info whose names have four letters
SELECT * FROM student WHERE student_name LIKE ("____");

-- applying aggregate functions on student's GPA
SELECT AVG(GPA) from student;
SELECT MAX(GPA) from student;
SELECT MIN(GPA) from student;

-- retrieve student's info whose in 6th grade and have a GPA = 5
SELECT * FROM student where educational_level = 6 AND GPA = 5;

-- adding age column
ALTER TABLE student
ADD age INT;

-- updating age for each student
UPDATE student
SET age = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), birth_date)), '%Y') + 0;

--  retrieve student's info whose age between 15 and 16
SELECT * FROM student WHERE age BETWEEN 15 AND 16;

-- retrieve number of students whose in 2nd grade
SELECT COUNT(student_name) FROM student WHERE educational_level = 2;

-- retrieve each major once
SELECT DISTINCT major FROM student;

-- retrieve subject names in uppercase
SELECT UPPER(subject_name) FROM course;

-- display average of GPA and round it to smallest number
SELECT FLOOR(AVG(GPA)) FROM student;

-- changing gender values from "M" to "Male" and from "F" to "Female" using string functions
ALTER TABLE student MODIFY COLUMN gender varchar(10);

UPDATE student
SET gender = REPLACE(gender,"M","Male");

UPDATE student
SET gender = REPLACE(gender,"F","Female");

-- updating GPA for students whose GPA is less than 2 and increasing it by 0.5
UPDATE student
SET GPA = GPA + 0.5
WHERE GPA < 2;

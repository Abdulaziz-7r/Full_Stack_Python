-- create database for school
create database School;
-- create table for students
CREATE TABLE student (
id INT PRIMARY KEY,
name VARCHAR(225),
birth_date DATE,
gender VARCHAR(1),
enrollment_date DATE,
email VARCHAR(225),
educational_level INT,
major VARCHAR(225),
GPA DOUBLE(3,2)
);
-- create table for teachers
CREATE TABLE teacher (
id INT PRIMARY KEY,
teacher_name VARCHAR(225),
birth_date DATE,
gender VARCHAR(1),
email VARCHAR(225),
office_number INT
);
-- create table for subjects
CREATE TABLE subject (
id INT PRIMARY KEY,
subject_name VARCHAR(225)
);
-- list all tables database
SHOW TABLES;
-- adding info to student table
INSERT INTO student VALUES 
(8,"Naser","1995-03-21","M","2001-5-01","naser@gmail.com",3,"humanitarian", 2.8),
(9,"Reda","1995-03-21","M","2001-5-5","reda@gmail.com",4,"scientific", 3.6),
(10,"Mansor","1995-03-21","M","2001-8-15","mansor@gmail.com",5,"scientific", 4.1);
-- adding info to teacher table
INSERT INTO teacher VALUES 
(1,"Naser","1980-01-8","M","naser@gmail.com",5),
(2,"Nada","1985-05-6","F","nada@gmail.com",10);
-- adding info to subject table
INSERT INTO subject VALUES 
(1,"Math"),
(2,"English"),
(5,"Computer"),
(6,"Physics");
-- retrieve  content of each table 
SELECT * FROM subject, student, teacher;
-- retrieve  content of students ordered by names in ASC order
SELECT * FROM student ORDER BY student_name ASC;
-- retrieve student name columns and rename the column 
SELECT student_name AS Student FROM student;
-- edit email of student
UPDATE student
SET email = "ahmedHr@gmail.com"
WHERE id = 1;
-- edit office number of teacher
UPDATE teacher
SET office_number = 11
WHERE id = 2;
-- rename a table 
ALTER TABLE subject
RENAME TO course;
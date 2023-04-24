-- this project is continues of SQL102 course project

-- create a relation between student and teacher tables (As teacher teaches more than one student, and the student is taught by more than one teacher)
CREATE TABLE Teach_student
(
teacher_id INT,
student_id INT,
CONSTRAINT `teacher_id` FOREIGN KEY (teacher_id) REFERENCES teacher(id),
CONSTRAINT `student_id` FOREIGN KEY (student_id) REFERENCES student(id)
);

-- create a relation between course and teacher tables (As teacher teaches only one course, and course is taught by more than one teacher.)
ALTER TABLE Teacher
ADD course_id INT,
ADD CONSTRAINT `course_id` FOREIGN KEY (course_id) REFERENCES Course(id);


-- create a relation between  subject and student tables (as student studies more than one subject, and subject is studied by more than one student)
CREATE TABLE Student_enrollment
(
student_id INT,
course_id INT,
CONSTRAINT `course_id1` FOREIGN KEY (course_id) REFERENCES Course(id),
CONSTRAINT `student_id1` FOREIGN KEY (student_id) REFERENCES Student(id)
);

-- create a procedure named student_info that displays names of students and subjects and contains all data shared between subject and student tables
DELIMITER // 
CREATE PROCEDURE student_info()
BEGIN
SELECT s.student_name
, c.subject_name 
FROM Student s
INNER JOIN student_enrollment AS se
ON se.student_id = s.id
INNER JOIN Course AS c
ON c.id = se.course_id
order by s.id;
END//
DELIMITER ;

-- call student_info procedure
CALL student_info;

-- Create a view named teacher_info containing teacher's name, office number and name of subject being taught
CREATE VIEW teacher_info
AS
SELECT teacher_name, office_number, subject_name
FROM teacher
INNER JOIN course
ON course.id = teacher.course_id
;

-- query teacher_info View
SELECT * FROM teacher_info;

-- delete teacher_info View
DROP VIEW teacher_info;

-- create an index 
CREATE INDEX student_name
ON student (student_name);

-- show created index
SHOW INDEX FROM Student;

-- delete an INDEX
DROP INDEX student_name ON Student;
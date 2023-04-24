-- using foreign key 
CREATE TABLE Product
(
    product_id INT NOT NULL,
    product_name varchar(225) NOT NULL,
    company_id int,
    PRIMARY KEY (product_id),
    FOREIGN KEY (company_id) REFERENCES Company(company_id)
);

-- adding foreign key to existence table
ALTER TABLE Product
ADD FOREIGN KEY (company_id) REFERENCES Company(company_id);

-- INNER JOINS
SELECT product_id, company_name
FROM Product
INNER JOIN Company
ON Product.company_id = Company.company_id;

-- LEFT OUTER JOINS
SELECT employee_name, employee_id, product_id
FROM Employee
LEFT OUTER JOIN Project
ON employee_name = project_manager;

-- RIGHT OUTER JOINS
SELECT employee_name, employee_id, product_id, project_manager
FROM Employee
RIGHT OUTER JOIN Project
ON employee_name = project_manager;

-- CROSS JOINS
SELECT *
FROM Employee
CROSS JOIN Department;

-- NATURAL JOINS
SELECT product_name, company_name
FROM Company
NATURAL JOIN Company;

-- creating VIEW
CREATE VIEW passed_students 
AS
SELECT student_name, course, exam_result
FROM student
WHERE exam_result = "Passed";

-- delete VIEW
DROP VIEW passed_students;

-- create INDEXES
CREATE INDEX employee_name
ON Employee (employee_name);

-- show INDEXES 
SHOW INDEX FROM Employee;

-- delete INDEXES
DROP INDEX employee_name ON Employee;

-- create PROCEDURE
DELIMITER // 
CREATE PROCEDURE display_student()
BEGIN
SELECT * FROM student;
END//
DELIMITER ;

-- call PROCEDURE
CALL display_student();
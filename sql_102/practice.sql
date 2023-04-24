-- add primary key to existence table
ALTER TABLE test ADD PRIMARY KEY (id);

-- using LIKE to retrieve all info about students whose name start with an "A"
SELECT * FROM test WHERE id LIKE "A%";

-- using LIKE to retrieve all info about students whose name start with an "A" and has two letters after it 
SELECT * FROM test WHERE student_name LIKE "A__";

-- using DISTINCT to retrieve one of each different value
SELECT DISTINCT student_name FROM test;

-- the AS command is used to rename a column or table with an alias. An alias only exists for the duration of the query.
SELECT student_name AS s_name FROM test AS student;

-- copying existence table
CREATE TABLE test_1 SELECT * FROM test;

/* Aggregate functions syntax:
SELECT Aggregate_functions(column_name) FROM table_name;
Aggregate functions examples: AVG, MAX, MIN, SUM, COUNT

Numeric functions examples: POW, MOD, ABS, DIV

String functions examples: ASCII, BIN, CONCAT, HEX, LOWER, UPPER
*/

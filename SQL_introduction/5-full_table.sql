-- Prints the following description of the table in your MySQL server.
SELECT CONCAT('Table: ', TABLE_NAME. '\n', 'Create Table', CREATE_STATEMENT)
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';

# Comprehensive MySQL Command Guide

## Table of Contents
1. [Connecting to MySQL Server](#connecting-to-mysql-server)
2. [Database Management](#database-management)
3. [User Management](#user-management)
4. [Table Management](#table-management)
   - [Creating Tables](#creating-tables)
   - [Modifying Tables](#modifying-tables)
   - [Deleting Tables](#deleting-tables)
5. [Data Manipulation (CRUD)](#data-manipulation-crud)
6. [Querying Data](#querying-data)
7. [Joins](#joins)
8. [Indexing and Optimization](#indexing-and-optimization)
9. [Stored Procedures and Functions](#stored-procedures-and-functions)
10. [Triggers](#triggers)
11. [Transactions](#transactions)
12. [Backup and Restore](#backup-and-restore)
13. [Security and Privileges](#security-and-privileges)
14. [Performance and Monitoring](#performance-and-monitoring)
15. [Resetting Root Password](#resetting-root-password)

## Connecting to MySQL Server
- Connect to MySQL as root:
  ```sql
  mysql -u root -p
  ```

- Connect to MySQL with a specific user:
  ```sql
  mysql -u username -p
  ```

- Connect to a specific database:
  ```sql
  mysql -u username -p database_name
  ```

## Database Management
- Show all databases:
  ```sql
  SHOW DATABASES;
  ```

- Create a new database:
  ```sql
  CREATE DATABASE database_name;
  ```

- Select a database to use:
  ```sql
  USE database_name;
  ```

- Drop (delete) a database:
  ```sql
  DROP DATABASE database_name;
  ```

- Show currently selected database:
  ```sql
  SELECT DATABASE();
  ```

- Rename a database (requires dump and restore):
  ```sql
  mysqldump -u username -p old_database > backup.sql
  mysql -u username -p -e "CREATE DATABASE new_database;"
  mysql -u username -p new_database < backup.sql
  ```

## User Management
- Create a new user:
  ```sql
  CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
  CREATE USER 'newuser'@'%' IDENTIFIED BY 'securepassword';
  ```

- Show all users:
  ```sql
  SELECT user, host FROM mysql.user;
  SELECT User, Host, authentication_string, plugin FROM mysql.user;
  ```

- Grant privileges to a user:
  ```sql
  GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'host';
  GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost' WITH GRANT OPTION;
  ```

- Show user privileges:
  ```sql
  SHOW GRANTS FOR 'username'@'host';
  ```

- Revoke privileges from a user:
  ```sql
  REVOKE privilege_name ON database_name.* FROM 'username'@'host';
  REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'username'@'host';
  ```

- Change user password:
  ```sql
  ALTER USER 'username'@'host' IDENTIFIED BY 'new_password';
  ```

- Delete a user:
  ```sql
  DROP USER 'username'@'host';
  ```

- Apply changes:
  ```sql
  FLUSH PRIVILEGES;
  ```

## Table Management

### Creating Tables
- Show all tables in the selected database:
  ```sql
  SHOW TABLES;
  ```

- Create a new table:
  ```sql
  CREATE TABLE table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    column1_name DATATYPE,
    column2_name DATATYPE
  );
  ```

- Create a table with a primary key:
  ```sql
  CREATE TABLE table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT
  );
  ```

- Create a table with a foreign key:
  ```sql
  CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
  );
  ```

- Create a temporary table:
  ```sql
  CREATE TEMPORARY TABLE temp_table_name (
    column1_name datatype constraints,
    column2_name datatype constraints
  );
  ```

- Show the structure of a table:
  ```sql
  DESCRIBE table_name;
  DESC table_name;
  ```

- Show table creation SQL:
  ```sql
  SHOW CREATE TABLE table_name;
  ```

### Modifying Tables
- Add a new column:
  ```sql
  ALTER TABLE table_name ADD COLUMN column_name datatype constraints;
  ```

- Modify an existing column:
  ```sql
  ALTER TABLE table_name MODIFY COLUMN column_name new_datatype constraints;
  ```

- Rename a column:
  ```sql
  ALTER TABLE table_name CHANGE old_column_name new_column_name datatype constraints;
  ```

- Remove a column:
  ```sql
  ALTER TABLE table_name DROP COLUMN column_name;
  ```

- Rename a table:
  ```sql
  RENAME TABLE old_table_name TO new_table_name;
  ALTER TABLE old_table_name RENAME TO new_table_name;
  ```

- Modify a table's character set/collation:
  ```sql
  ALTER TABLE your_table_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
  ```

- Add a primary key:
  ```sql
  ALTER TABLE table_name ADD PRIMARY KEY (column_name);
  ```

- Add a unique constraint:
  ```sql
  ALTER TABLE table_name ADD CONSTRAINT constraint_name UNIQUE (column_name);
  ```

- Add a foreign key:
  ```sql
  ALTER TABLE table_name ADD CONSTRAINT constraint_name FOREIGN KEY (column_name) REFERENCES other_table(column_name);
  ```

- Remove a constraint:
  ```sql
  ALTER TABLE table_name DROP CONSTRAINT constraint_name;
  ```

### Deleting Tables
- Delete a table:
  ```sql
  DROP TABLE table_name;
  ```

- Delete multiple tables:
  ```sql
  DROP TABLE table1, table2;
  ```

- Delete a table only if it exists:
  ```sql
  DROP TABLE IF EXISTS table_name;
  ```

- Truncate (empty) a table:
  ```sql
  TRUNCATE TABLE table_name;
  ```

## Data Manipulation (CRUD)
- Insert a new row:
  ```sql
  INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2');
  ```

- Insert multiple rows:
  ```sql
  INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2'), ('value3', 'value4');
  ```

- Example from provided files:
  ```sql
  INSERT INTO Artist (Artist_Name, Up_Date) VALUES ('John Doe', '2023-01-01');
  INSERT INTO Works (Artist_ID, Title, Rating, Code, Source) VALUES (1, 'Work A', 8.5, 'ABC123', 'Source A');
  ```

- Select all rows:
  ```sql
  SELECT * FROM table_name;
  ```

- Select specific columns:
  ```sql
  SELECT column1, column2 FROM table_name;
  ```

- Select with a condition:
  ```sql
  SELECT * FROM table_name WHERE column1 = 'value';
  ```

- Update records:
  ```sql
  UPDATE table_name SET column1 = 'new_value' WHERE column2 = 'condition_value';
  ```

- Delete records:
  ```sql
  DELETE FROM table_name WHERE column1 = 'value';
  ```

## Querying Data
- Filter rows with WHERE clause:
  ```sql
  SELECT * FROM table_name WHERE column_name = 'value';
  ```

- Sort results (ascending/descending):
  ```sql
  SELECT * FROM table_name ORDER BY column1 ASC;
  SELECT * FROM table_name ORDER BY column1 DESC;
  ```

- Limit results:
  ```sql
  SELECT * FROM table_name LIMIT 10;
  ```

- Count rows:
  ```sql
  SELECT COUNT(*) FROM table_name;
  ```

- Group by a column:
  ```sql
  SELECT column1, COUNT(*) FROM table_name GROUP BY column1;
  ```

- Find unique values:
  ```sql
  SELECT DISTINCT column_name FROM table_name;
  ```

- Subqueries:
  ```sql
  SELECT column_name FROM table_name WHERE column_name IN (SELECT column_name FROM another_table);
  ```

## Joins
- Inner Join (return rows when there is a match in both tables):
  ```sql
  SELECT a.column1, b.column2 
  FROM table1 a 
  INNER JOIN table2 b ON a.id = b.id;
  ```

- Left Join (return all rows from the left table, and matching rows from the right table):
  ```sql
  SELECT a.column1, b.column2 
  FROM table1 a 
  LEFT JOIN table2 b ON a.id = b.id;
  ```

- Right Join (return all rows from the right table, and matching rows from the left table):
  ```sql
  SELECT a.column1, b.column2 
  FROM table1 a 
  RIGHT JOIN table2 b ON a.id = b.id;
  ```

- Full Outer Join (using UNION in MySQL):
  ```sql
  SELECT a.*, b.*
  FROM table1 a
  LEFT JOIN table2 b ON a.id = b.id
  UNION
  SELECT a.*, b.*
  FROM table1 a
  RIGHT JOIN table2 b ON a.id = b.id
  WHERE a.id IS NULL;
  ```

- Example from provided files:
  ```sql
  SELECT Artist.Artist_ID, Artist.Artist_Name, Artist.Up_Date,
         Works.Title, Works.Rating, Works.Code, Works.Source
  FROM Artist
  LEFT JOIN Works ON Artist.Artist_ID = Works.Artist_ID;
  ```

## Indexing and Optimization
- Create an index:
  ```sql
  CREATE INDEX index_name ON table_name (column_name);
  ```

- Create a unique index:
  ```sql
  CREATE UNIQUE INDEX index_name ON table_name (column_name);
  ```

- Show indexes:
  ```sql
  SHOW INDEX FROM table_name;
  ```

- Delete an index:
  ```sql
  DROP INDEX index_name ON table_name;
  ```

- Check the size of a table:
  ```sql
  SELECT table_name, round(((data_length + index_length) / 1024 / 1024), 2) AS size_MB 
  FROM information_schema.TABLES 
  WHERE table_schema = 'database_name';
  ```

- Analyze a table:
  ```sql
  ANALYZE TABLE table_name;
  ```

- Optimize a table:
  ```sql
  OPTIMIZE TABLE table_name;
  ```

## Stored Procedures and Functions
- Create a stored procedure:
  ```sql
  DELIMITER //
  CREATE PROCEDURE procedure_name ()
  BEGIN
    -- SQL statements here
  END //
  DELIMITER ;
  ```

- Example of a procedure with parameters:
  ```sql
  DELIMITER //
  CREATE PROCEDURE GetCustomerOrders(IN customerId INT)
  BEGIN
    SELECT * FROM orders WHERE customer_id = customerId;
  END //
  DELIMITER ;
  ```

- Call a stored procedure:
  ```sql
  CALL procedure_name();
  CALL GetCustomerOrders(123);
  ```

- Create a function:
  ```sql
  DELIMITER //
  CREATE FUNCTION function_name(param1 DATATYPE) RETURNS RETURN_TYPE
  BEGIN
    -- Function logic
    RETURN value;
  END //
  DELIMITER ;
  ```

- Example of a function:
  ```sql
  DELIMITER //
  CREATE FUNCTION CalculateDiscount(price DECIMAL(10,2), discount_rate DECIMAL(5,2)) RETURNS DECIMAL(10,2)
  BEGIN
    DECLARE discounted_price DECIMAL(10,2);
    SET discounted_price = price - (price * discount_rate / 100);
    RETURN discounted_price;
  END //
  DELIMITER ;
  ```

- Using a function:
  ```sql
  SELECT product_name, price, CalculateDiscount(price, 10) AS discounted_price FROM products;
  ```

- Drop a stored procedure:
  ```sql
  DROP PROCEDURE IF EXISTS procedure_name;
  DROP PROCEDURE IF EXISTS GetArtistDetails;
  ```

- Drop a function:
  ```sql
  DROP FUNCTION IF EXISTS function_name;
  ```

## Triggers
- Create a trigger:
  ```sql
  CREATE TRIGGER trigger_name BEFORE INSERT ON table_name
  FOR EACH ROW BEGIN
    -- SQL statements here
  END;
  ```

- Example of a trigger:
  ```sql
  DELIMITER //
  CREATE TRIGGER before_employee_update
  BEFORE UPDATE ON employees
  FOR EACH ROW
  BEGIN
    INSERT INTO employees_audit
    SET action = 'update',
        employee_id = OLD.id,
        changed_by = USER(),
        change_date = NOW();
  END //
  DELIMITER ;
  ```

- Show triggers:
  ```sql
  SHOW TRIGGERS;
  ```

- Drop a trigger:
  ```sql
  DROP TRIGGER trigger_name;
  ```

## Transactions
- Start a transaction:
  ```sql
  START TRANSACTION;
  ```

- Commit changes:
  ```sql
  COMMIT;
  ```

- Rollback changes:
  ```sql
  ROLLBACK;
  ```

- Set autocommit mode off:
  ```sql
  SET autocommit = 0;
  ```

## Backup and Restore
- Backup a database:
  ```sql
  mysqldump -u username -p database_name > backup.sql
  ```

- Backup all databases:
  ```sql
  mysqldump -u username -p --all-databases > all_databases_backup.sql
  ```

- Restore a database:
  ```sql
  mysql -u username -p database_name < backup.sql
  ```

- Restore all databases:
  ```sql
  mysql -u username -p < all_databases_backup.sql
  ```

## Security and Privileges
- Show user privileges:
  ```sql
  SHOW GRANTS FOR 'username'@'host';
  ```

- Grant a specific privilege:
  ```sql
  GRANT SELECT ON database_name.* TO 'username'@'host';
  ```

- Revoke a specific privilege:
  ```sql
  REVOKE SELECT ON database_name.* FROM 'username'@'host';
  ```

- Remove all privileges:
  ```sql
  REVOKE ALL PRIVILEGES ON database_name.* FROM 'username'@'host';
  ```

- Check current user:
  ```sql
  SELECT USER();
  ```

## Performance and Monitoring
- Show running processes:
  ```sql
  SHOW PROCESSLIST;
  ```

- Kill a query:
  ```sql
  KILL process_id;
  ```

- Show table status:
  ```sql
  SHOW TABLE STATUS;
  ```

- Show all variables:
  ```sql
  SHOW VARIABLES;
  ```

## Resetting Root Password

### Resetting Root Password on Linux (Ubuntu/Debian)
1. Stop the MySQL Service
   ```
   sudo systemctl stop mysql
   ```
   or for older versions:
   ```
   sudo service mysql stop
   ```

2. Start MySQL in Safe Mode (Skip Authentication)
   ```
   sudo mysqld_safe --skip-grant-tables --skip-networking &
   ```
   or:
   ```
   sudo mysqld --skip-grant-tables --skip-networking &
   ```

3. Log in Without a Password
   ```
   mysql -u root
   ```

4. Reset the Root Password
   For MySQL 5.7+ or MariaDB:
   ```sql
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewStrongPassword';
   FLUSH PRIVILEGES;
   ```
   For MySQL 5.6 and below:
   ```sql
   SET PASSWORD FOR 'root'@'localhost' = PASSWORD('NewStrongPassword');
   FLUSH PRIVILEGES;
   ```

5. Restart MySQL Normally
   ```
   sudo systemctl stop mysql
   sudo systemctl start mysql
   ```
   or:
   ```
   sudo service mysql restart
   ```

### Resetting Root Password on CentOS/RHEL
1. Stop MySQL Service
   ```
   sudo systemctl stop mysqld
   ```

2. Start MySQL Without Authentication
   ```
   sudo mysqld_safe --skip-grant-tables --skip-networking &
   ```

3. Reset Root Password
   ```
   mysql -u root
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewStrongPassword';
   FLUSH PRIVILEGES;
   ```

4. Restart MySQL
   ```
   sudo systemctl restart mysqld
   ```

### Resetting MySQL Root Password Using --init-file
1. Create a File with the Password Update Command
   ```
   echo "ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewStrongPassword';" > /tmp/mysql-init
   ```

2. Restart MySQL with the Init File
   ```
   sudo systemctl stop mysql
   sudo mysqld --init-file=/tmp/mysql-init --skip-networking &
   ```

3. Restart Normally
   ```
   sudo systemctl restart mysql
   ```

### Resetting Root Password on Windows
1. Stop the MySQL Service
   ```
   net stop mysql
   ```

2. Start MySQL Without Authentication
   ```
   mysqld --skip-grant-tables
   ```

3. Log in and Reset Password
   ```
   mysql -u root
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'NewStrongPassword';
   FLUSH PRIVILEGES;
   ```

4. Restart MySQL
   ```
   net start mysql
   ```
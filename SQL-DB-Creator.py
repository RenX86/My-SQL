import mysql.connector

# MySQL Configuration
HOST = "localhost"
USER = "root"  # Change as needed
PASSWORD = "password"  # Change to your MySQL password
DATABASE = "mydatabase"

def create_database():
    """Creates the database if it does not exist."""
    try:
        connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")
        print(f"Database '{DATABASE}' created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def create_tables():
    """Creates tables within the database."""
    try:
        connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
        cursor = connection.cursor()

        tables = {
            "users": """
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100) UNIQUE,
                    age INT
                )
            """,
            "products": """
                CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    price DECIMAL(10,2),
                    stock INT
                )
            """,
            "orders": """
                CREATE TABLE IF NOT EXISTS orders (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT,
                    product_id INT,
                    quantity INT,
                    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
                )
            """
        }

        for table_name, table_query in tables.items():
            cursor.execute(table_query)
            print(f"Table '{table_name}' created or already exists.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    create_database()
    create_tables()

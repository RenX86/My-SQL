import mysql.connector

# MySQL Configuration
HOST = "localhost"
USER = "root"
PASSWORD = "password"
DATABASE = "mydatabase"

def insert_data():
    """Inserts sample data into the database."""
    try:
        connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
        cursor = connection.cursor()

        # Insert users
        cursor.executemany(
            "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)",
            [("Alice", "alice@example.com", 25), ("Bob", "bob@example.com", 30)]
        )

        # Insert products
        cursor.executemany(
            "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
            [("Laptop", 799.99, 10), ("Phone", 499.99, 20)]
        )

        # Get user and product IDs
        cursor.execute("SELECT id FROM users LIMIT 1")
        user_id = cursor.fetchone()[0]

        cursor.execute("SELECT id FROM products LIMIT 1")
        product_id = cursor.fetchone()[0]

        # Insert an order
        cursor.execute("INSERT INTO orders (user_id, product_id, quantity) VALUES (%s, %s, %s)", (user_id, product_id, 1))

        # Commit changes
        connection.commit()
        print("Sample data inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

def fetch_data():
    """Fetches and displays data from tables."""
    try:
        connection = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users")
        print("Users:", cursor.fetchall())

        cursor.execute("SELECT * FROM products")
        print("Products:", cursor.fetchall())

        cursor.execute("SELECT * FROM orders")
        print("Orders:", cursor.fetchall())

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    insert_data()
    fetch_data()

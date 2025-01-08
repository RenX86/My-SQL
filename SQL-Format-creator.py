import mysql.connector
from mysql.connector import errorcode

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'Rex',
    'password': '5826'  # Replace with your MySQL root password
}

# Database and table names
DATABASE_NAME = "DoujinDB"
ARTIST_TABLE = "Artist"
WORKS_TABLE = "Works"

# SQL commands to create tables
CREATE_ARTISTS_TABLE = f"""
CREATE TABLE IF NOT EXISTS {ARTIST_TABLE} (
    ArtistID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL UNIQUE
);
"""

CREATE_WORKS_TABLE = f"""
CREATE TABLE IF NOT EXISTS {WORKS_TABLE} (
    ArtistID INT,
    Title VARCHAR(255) NOT NULL UNIQUE,
    Rating DECIMAL(2, 1) CHECK (Rating BETWEEN 0 AND 10),
    Code VARCHAR(15) UNIQUE,
    Source VARCHAR(20),
    FOREIGN KEY (ArtistID) REFERENCES {ARTIST_TABLE}(ArtistID) ON DELETE SET NULL
);
"""

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE {DATABASE_NAME}")
        print(f"Database '{DATABASE_NAME}' created successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database '{DATABASE_NAME}' already exists.")
        else:
            print(f"Error creating database: {err}")

def create_tables(cursor):
    try:
        # Switch to the newly created database
        cursor.execute(f"USE {DATABASE_NAME}")
        
        # Create Artists table
        cursor.execute(CREATE_ARTISTS_TABLE)
        print(f"Table '{ARTIST_TABLE}' created successfully.")
        
        # Create Works table
        cursor.execute(CREATE_WORKS_TABLE)
        print(f"Table '{WORKS_TABLE}' created successfully.")
    except mysql.connector.Error as err:
        print(f"Error creating tables: {err}")

def main():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Create database
        create_database(cursor)
        
        # Create tables
        create_tables(cursor)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()

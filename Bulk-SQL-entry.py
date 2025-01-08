import mysql.connector

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'Rex',
    'password': '5826',
    'database': 'xxxxxxxx'
}

def artist_exists(cursor, artist_name):
    """Check if an artist already exists in the Artist table."""
    query = "SELECT Artist_ID FROM Artist WHERE Artist_Name = %s"
    cursor.execute(query, (artist_name,))
    result = cursor.fetchone()
    return result[0] if result else None

def work_exists(cursor, artist_id, title):
    """Check if a work already exists in the Works table."""
    query = "SELECT * FROM Works WHERE Artist_ID = %s AND Title = %s"
    cursor.execute(query, (artist_id, title))
    return cursor.fetchone() is not None

def insert_artist(cursor, name, date):
    """Insert a new artist if it doesn't already exist."""
    artist_id = artist_exists(cursor, name)
    if artist_id:
        print(f"Artist '{name}' already exists with ID {artist_id}.")
        return artist_id
    else:
        query = "INSERT INTO Artist (Artist_Name, Up_Date) VALUES (%s, %s)"
        cursor.execute(query, (name, date))
        print(f"Inserted artist '{name}' with new ID {cursor.lastrowid}.")
        return cursor.lastrowid

def insert_work(cursor, artist_name, title, rating, code, source):
    """Insert a new work if it doesn't already exist."""
    artist_id = artist_exists(cursor, artist_name)
    if not artist_id:
        raise ValueError(f"Artist '{artist_name}' not found in the Artist table.")
    
    if work_exists(cursor, artist_id, title):
        print(f"Work '{title}' already exists for artist '{artist_name}'. Skipping.")
        return
    
    query = "INSERT INTO Works (Artist_ID, Title, Rating, Code, Source) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (artist_id, title, rating, code, source))
    print(f"Inserted work '{title}' for artist '{artist_name}'.")

def main():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Example: Insert artist and works
        artist_name = "xxxxx"
        Up_Date = "2025-01-01"
        artist_id = insert_artist(cursor, artist_name, Up_Date)
        
        insert_work(cursor, artist_name, "xxxxxxxxxxxxxxxxx", 6, "xxxx", "xxxxxx")
        
        # Commit changes
        conn.commit()
        print("Data insertion completed.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()

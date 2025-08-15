import mysql.connector

# 35
def connect_to_mysql():
    """Connects to the MySQL database container."""
    conn = mysql.connector.connect(
        host="localhost",
        user="user",          # The user we defined in docker-compose.yml
        password="password",  # The password we defined
        database="futurama",  # The database we defined
        port=1338             # The EXTERNAL port we mapped
    )
    cursor = conn.cursor()
    return conn, cursor

# 
def reset_table(cursor):
    """Drops the existing characters table and creates a new one."""
    cursor.execute("DROP TABLE IF EXISTS characters")
    cursor.execute("""
        CREATE TABLE characters (
            id INT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            image_url TEXT
        )
    """)
    print("Table 'characters' has been reset.")

    # 
def insert_characters(character_data, conn, cursor):
    """Inserts character data into the characters table."""
    if not character_data:
        print("No character data to insert.")
        return

    query = "INSERT INTO characters (id, first_name, last_name, image_url) VALUES (%s, %s, %s, %s)"
    
    for character in character_data:
        # Prepare the data tuple in the correct order for the query
        values = (
            character["id"],
            character["name"]["first"],
            character["name"]["last"],
            character["images"]["main"],
        )
        cursor.execute(query, values)
    
    conn.commit() # This saves all the changes to the database
    print(f"Inserted {len(character_data)} characters into MySQL.")


# 
def store_characters_in_mysql(character_data):
    """A wrapper function to connect, reset, insert, and close."""
    try:
        conn, cursor = connect_to_mysql()
        reset_table(cursor)
        insert_characters(character_data, conn, cursor)
    except mysql.connector.Error as err:
        print(f"Error with MySQL: {err}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("MySQL connection closed.")
import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="00Jacob83"
    )

    if conn.is_connected():
        cursor = conn.cursor()
        
        # Corrected SQL statement
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()

import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "00Jacob83"
    )
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXIST alx_book_store")
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(f"Error: {e}")
finally:
    if conn.is_connected():
        conn.close()
        cursor.close()
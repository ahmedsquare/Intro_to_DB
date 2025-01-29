import mysql.connector
try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='Ahmedsquare900170747'  # Replace with your MySQL password
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error:
    print(f"Error")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")


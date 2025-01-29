import mysql.connector


# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ahmedsquare900170747",
    database="alx_book_store"
)
if mydb.is_connected():
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    print("Database 'alx_book_store' created successfully!")
    
print(mydb.get_server_info())
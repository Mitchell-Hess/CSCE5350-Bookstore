import mysql.connector
from tkinter import messagebox

def get_connection():
    """Establish connection to MySQL Database."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="add_user",
            password="add_password",
            database="Bookstore"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

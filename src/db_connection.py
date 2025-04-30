import mysql.connector
from tkinter import messagebox
import tkinter as tk
import os
import json

config = "db_config.txt"

def prompt_for_login():
    """Pop up a single login window and return DB credentials."""
    creds = {}

    def submit():
        creds["host"] = host_entry.get().strip()
        creds["user"] = user_entry.get().strip()
        creds["password"] = password_entry.get().strip()
        creds["database"] = database_entry.get().strip()
        login_win.destroy()

    login_win = tk.Tk()
    login_win.title("Database Login")
    login_win.geometry("300x200")
    login_win.resizable(False, False)

    tk.Label(login_win, text="Host:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    tk.Label(login_win, text="User:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    tk.Label(login_win, text="Password:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    tk.Label(login_win, text="Database:").grid(row=3, column=0, padx=10, pady=5, sticky="e")

    host_entry = tk.Entry(login_win)
    user_entry = tk.Entry(login_win)
    password_entry = tk.Entry(login_win, show="*")
    database_entry = tk.Entry(login_win)

    host_entry.grid(row=0, column=1, padx=10, pady=5)
    user_entry.grid(row=1, column=1, padx=10, pady=5)
    password_entry.grid(row=2, column=1, padx=10, pady=5)
    database_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(login_win, text="Connect", command=submit).grid(row=4, column=0, columnspan=2, pady=15)

    login_win.mainloop()

    return creds if creds else None

def save_credentials(config_info):
    # Save the credentials
    with open(config, "w") as f:
        json.dump(config_info, f)

def load_credentials():
    # Load credentials from local file, if available.
    if os.path.exists(config):
        with open(config, "r") as f:
            return json.load(f)
    return None

def get_connection():
    """Establish connection to MySQL Database using stored or prompted credentials."""
    config_info = load_credentials()

    if not config_info:
        config_info = prompt_for_login()

    try:
        conn = mysql.connector.connect(
            host=config_info["host"],
            user=config_info["user"],
            password=config_info["password"],
            database=config_info["database"]
        )
        # Save config only after a successful connection
        if not os.path.exists(config):
            save_credentials(config_info)
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

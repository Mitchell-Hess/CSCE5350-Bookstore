import mysql.connector
from tkinter import messagebox
import tkinter as tk
import os
import json

config = "db_config.txt"

def prompt_for_login():
    """Pop up a single login window and return DB credentials, or None if cancelled."""
    creds = {}
    result = {"submitted": False}

    def submit():
        if all(e.get().strip() for e in (host_entry, user_entry, password_entry, database_entry)):
            creds["host"] = host_entry.get().strip()
            creds["user"] = user_entry.get().strip()
            creds["password"] = password_entry.get().strip()
            creds["database"] = database_entry.get().strip()
            result["submitted"] = True
            login_win.destroy()
        else:
            messagebox.showerror("Input Error", "All fields are required.")

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

    login_win.protocol("WM_DELETE_WINDOW", login_win.destroy)  # Handle window close
    login_win.mainloop()

    return creds if result["submitted"] else None


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

    while True:
        if not config_info:
            config_info = prompt_for_login()

        try:
            conn = mysql.connector.connect(
                host=config_info["host"],
                user=config_info["user"],
                password=config_info["password"],
                database=config_info["database"]
            )
            # Save credentials if valid and not yet stored
            if not os.path.exists(config):
                save_credentials(config_info)
            return conn
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Connection failed:\n{err}\n\nPlease try again.")
            config_info = None  # Clear and re-prompt

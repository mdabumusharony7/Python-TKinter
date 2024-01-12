import tkinter as tk
from tkinter import messagebox
import sqlite3


def create_table():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """
    )
    connection.commit()
    connection.close()


def register():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
    )
    connection.commit()
    connection.close()

    messagebox.showinfo("Success", "Registration successful!")


def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?", (username, password)
    )
    user = cursor.fetchone()
    connection.close()

    if user:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password.")


# Create main window
window = tk.Tk()
window.title("Login and Registration System")

# Create and initialize database table
create_table()

# Username label and entry
label_username = tk.Label(window, text="Username:")
label_username.pack(pady=10)
entry_username = tk.Entry(window)
entry_username.pack(pady=10)

# Password label and entry
label_password = tk.Label(window, text="Password:")
label_password.pack(pady=10)
entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=10)

# Register and Login buttons
btn_register = tk.Button(window, text="Register", command=register)
btn_register.pack(pady=10)
btn_login = tk.Button(window, text="Login", command=login)
btn_login.pack(pady=10)

# Start the main loop
window.mainloop()

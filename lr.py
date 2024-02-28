import tkinter as tk

# Create the main Tkinter window
root = tk.Tk()
root.title("Login")
root.geometry("300x300")


# Function to handle the registration button click
def register_clicked():
    print("Register button clicked")


# Function to handle the login button click
def login_clicked():
    print("Login button clicked")


# Create a label for the title
title_label = tk.Label(root, text="Face Recognition Login", font=("Helvetica", 16))
title_label.pack(pady=20)

# Create the Login button
login_button = tk.Button(root, text="Login", command=login_clicked)
login_button.pack(side=tk.BOTTOM, pady=20)

# Create the Register button
register_button = tk.Button(root, text="Register", command=register_clicked)
register_button.pack(side=tk.BOTTOM, pady=20)

# Start the Tkinter event loop
root.mainloop()

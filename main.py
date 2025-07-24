import tkinter as tk
from Owners_menu import owner_login
from customers_menu import customers_menu


def launch_owner():
    owner_login()


def launch_customer():
    customers_menu()


def exit_app():
    root.destroy()


# Create the main window
root = tk.Tk()
root.title("Vending Machine")
root.geometry("300x250")
root.configure(bg="#f0f0f0")

# Title label
title = tk.Label(root, text="Vending Machine Menu",
                 font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title.pack(pady=20)

# Owner Button
owner_button = tk.Button(root, text="Owner", width=20,
                         height=2, command=launch_owner)
owner_button.pack(pady=5)

# Customer Button
customer_button = tk.Button(root, text="Customer",
                            width=20, height=2, command=launch_customer)
customer_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit", width=20,
                        height=2, command=exit_app)
exit_button.pack(pady=5)

# Start the GUI loop
root.mainloop()

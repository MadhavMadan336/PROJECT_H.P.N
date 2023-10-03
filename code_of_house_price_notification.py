import tkinter as tk
from tkinter import ttk
from datetime import datetime

class House:
    def _init_(self, address, price):
        self.address = address
        self.price = price

    def notify_price(self):
        return f"The price of {self.address} has changed to ₹{self.price}"

def update_prices():
    user_date = user_date_entry.get()
    if user_date == "":
        result_text.insert(tk.END, "Please fill in the date.\n", "error")
    else:
        for house in houses:
            new_price = generate_random_price(house.price)
            if new_price != house.price:
                house.price = new_price
                result_text.insert(tk.END, house.notify_price() + "\n", "update")

def generate_random_price(current_price):
    return current_price + 10000

def start_notification():
    global houses
    houses = [
        House("HOUSE:-150,BIHAR,MAUNBEHAT,DARBHANGA", 100000),
        House("HOUSE:-169,BIHAR,LAKSHIMI SAGAR,DARBHANGA", 200000),
        House("HOUSE:-180,BIHAR,MAKRANDA,DARBHANGA", 300000),
        House("HOUSE:-160,BIHAR,BAJITPUR,DARBHANGA", 400000),
        House("HOUSE:-260,BIHAR,BEGUSARAI,BEGUSARAI", 500000),
        House("HOUSE:-143,DELHI,MAYUR VIHAR PHASE 1", 600000)
    ]
    update_prices()

def clear_result():
    result_text.delete(1.0, tk.END)
    user_date_entry.delete(0, tk.END)
    current_date = datetime.now().strftime("%Y-%m-%d")
    date_label.config(text=f"Current Date: {current_date}")

def get_user_date():
    user_date = user_date_entry.get()
    try:
        datetime.strptime(user_date, "%Y-%m-%d")
        date_label.config(text=f"User Date: {user_date}")
    except ValueError:
        date_label.config(text="Invalid Date Format")

root = tk.Tk()
root.title("House Price Notification")

frame = ttk.Frame(root, padding="30", style="My.TFrame")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

style = ttk.Style()
style.configure("My.TFrame", background='#ADD8E6')  # Light Blue

style.configure("TButton", background='#00FF00')  # Green (Update Button)
style.map("TButton", background=[('active', '#00FF00')])

start_button = ttk.Button(frame, text="Start Notifications", command=start_notification, style="TButton")
start_button.grid(row=0, column=0, pady=(0, 10))

update_button = ttk.Button(frame, text="Update Prices", command=update_prices, style="TButton")
update_button.grid(row=1, column=0, pady=(10, 10))

clear_button = ttk.Button(frame, text="Clear", command=clear_result)
clear_button.grid(row=1, column=1, pady=(10, 10))

user_date_label = ttk.Label(frame, text="Enter Date (YYYY-MM-DD):", font=("Arial", 12, "bold"))
user_date_label.grid(row=2, column=0, pady=(10, 0))

user_date_entry = ttk.Entry(frame, font=("Arial", 12))
user_date_entry.grid(row=2, column=1, pady=(10, 0))

get_user_date_button = ttk.Button(frame, text="Get User Date", command=get_user_date)
get_user_date_button.grid(row=3, column=1, pady=(10, 0))

style.configure("TButton", background='#FF0000')  # Red (Start Button)

result_text = tk.Text(frame, height=35, width=190)
result_text.grid(row=4, column=0, pady=(10, 0), columnspan=2)

# Define tag configurations
result_text.tag_configure("update", background="lightgreen", foreground="black")  # Green for update notifications
result_text.tag_configure("reset", font=('Arial', 12, 'bold'), foreground="black", background="lightblue")  # Reset tag
result_text.tag_configure("error", foreground="red")  # Red for error messages

# Add "Notification" label with tags
result_text.insert(tk.END, "Notification", "reset")

# Add date section
current_date = datetime.now().strftime("%Y-%m-%d")
date_label = ttk.Label(frame, text=f"Current Date: {current_date}", font=("Arial", 12, "bold"))
date_label.grid(row=5, column=0, pady=(10, 0), columnspan=2)

root.mainloop()

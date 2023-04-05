import requests
from tkinter import *

# Colors
main_color = "#07018d"

# Window
window = Tk()
window.title("Převod měn verze 1.0.0")
window.minsize(400, 120)
window.resizable(True, True)
window.config(bg=main_color)
window.iconbitmap("icon.ico")


# Function count currency
def count_currency():
    try:
        currency1 = drop_down_from.get()
        currency2 = drop_down_to.get()
        amount = float(user_input.get())
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency2}&from={currency1}&amount={amount}"
        payload = {}
        headers= {
        "apikey": "sdQL25eQOZxFT9gk8eCjXWaljBBaA0A7"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
        data_result = response.json()
        result_label.config(text=round(data_result["result"], 2))
        notification_label.config(text="")
    except:
        notification_label.config(text="Zadej částku.")


# User input
user_input = Entry(width=20, font=("Arial", 12), justify=CENTER)
user_input.insert(0, "0")
user_input.grid(row=0, column=0, padx=10, pady=(10, 0))

# Drop down currency 1
drop_down_from = StringVar(window)
drop_down_from.set("EUR") 
drop_down_from_option = OptionMenu(window, drop_down_from, "CZK", "EUR", "USD")
drop_down_from_option.grid(row=0, column=1, padx=10, pady=(10, 0))

# Drop down currency 2
drop_down_to = StringVar(window)
drop_down_to.set("CZK")
drop_down_to_option = OptionMenu(window, drop_down_to, "CZK", "EUR", "USD")
drop_down_to_option.grid(row=1, column=1, padx=5, pady=(10, 0))

# Button
count_button = Button(text="Přepočítej", font=("Arial", 12), command=count_currency)
count_button.grid(row=0, column=2, padx=10, pady=(10, 0))

# Laber for result
result_label = Label(text="0", bg=main_color, fg="white", font=("Arial", 12))
result_label.grid(row=1, column=0)

# Laber for notification
notification_label = Label(bg=main_color, fg="white", font=("Arial", 12))
notification_label.grid(row=2, column=0)

# Main cycle
window.mainloop()
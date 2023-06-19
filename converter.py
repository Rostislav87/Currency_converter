import requests
from tkinter import *
from api_key import api_key

# Values
main_color = "#07018d"
fg_color = "#fff"
currencies = ["CZK", "EUR", "USD", "PLN"]
font = ("Arial", 15)

# Window
window = Tk()
window.title("Převod měn verze 1.0.1")
window.geometry("420x110+500+200")
window.resizable(True, True)
window.config(bg=main_color)


# Function count currency
def count_currency():
    try:
        currency1 = drop_down_from.get()
        currency2 = drop_down_to.get()
        amount = float(user_input.get())
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency2}&from={currency1}&amount={amount}"
        payload = {}
        headers= {
        "apikey": api_key
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()
        data_result = response.json()
        result = data_result["result"]
        result_label.config(text=f"{result:,}".replace(',', ' '))
        notification_label.config(text="")
    except:
        notification_label.config(text="Zadej částku.")

# Function to delete user input and result
def delete_input_and_result():
    user_input.delete(0, END)
    result_label.config(text="0")

# User input
user_input = Entry(width=15, font=font, justify=CENTER)
user_input.insert(0, "")
user_input.grid(row=0, column=0, padx=10, pady=(10, 0))

# Drop down currency 1
drop_down_from = StringVar(window)
drop_down_from.set("EUR") 
drop_down_from_option = OptionMenu(window, drop_down_from, currencies)
drop_down_from_option.grid(row=0, column=1, padx=10, pady=(10, 0))

# Drop down currency 2
drop_down_to = StringVar(window)
drop_down_to.set("CZK")
drop_down_to_option = OptionMenu(window, drop_down_to, currencies)
drop_down_to_option.grid(row=1, column=1, padx=10, pady=(10, 0))

# Button to convert
count_button = Button(text="Přepočítej", font=font, command=count_currency)
count_button.grid(row=0, column=2, padx=10, pady=(10, 0))

# Button to delete user input and result
delete_button = Button(text="Smazat", font=font, command=delete_input_and_result)
delete_button.grid(row=1, column=2, padx=10, pady=10)

# Laber for result
result_label = Label(text="0", bg=main_color, fg=fg_color, font=font)
result_label.grid(row=1, column=0)

# Laber for notification
notification_label = Label(bg=main_color, fg=fg_color, font=font)
notification_label.grid(row=2, column=0)

# Main cycle
window.mainloop()
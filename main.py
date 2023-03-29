from tkinter import *

# Window
window = Tk()
window.title("Převod CZK na Eura")
window.minsize(300, 100)
window.resizable(False, False)
window.config(bg="#07018d")
window.iconbitmap("icon.ico")


# Function count currency
def count_currency():
    amount_eur = float(amount_input.get()) / 23.70
    result_label["text"] = round(amount_eur, 2)

# User input
amount_input = Entry(width=10, font=("Helvetica", 15))
amount_input.grid(row=0, column=0, padx=10, pady=10)

# Label CZK
czk_label = Label(text="CZK", font=("Helvetica", 15), bg="#07018d", fg="white")
czk_label.grid(row=0, column=1)

result_label = Label(text="0", font=("Helvetica", 15), bg="#07018d", fg="white")
result_label.grid(row=1, column=0)

# Label EUR
eur_label = Label(text="EUR", font=("Helvetica", 15), bg="#07018d", fg="white")
eur_label.grid(row=1, column=1)

# Button
count_button = Button(text="Přepočítej", font=("Helvetica", 15), command=count_currency)
count_button.grid(row=0, column=2, padx=10, pady=10)


# Main cycle
window.mainloop()
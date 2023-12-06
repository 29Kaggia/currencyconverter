from tkinter import Tk, Label, Entry, Button

from forex_python.converter import CurrencyRates

def convert_currency():
    c = CurrencyRates()

    from_currency = from_entry.get().upper()
    to_currency = to_entry.get().upper()
    amount = float(amount_entry.get())

    conversion_rate = c.convert(from_currency, to_currency, amount)
    result_label.config(text=f"{amount} {from_currency} = {conversion_rate} {to_currency}")

# Creating the GUI
root = Tk()
root.title("Currency Converter")

from_label = Label(root, text="From Currency:")
from_label.grid(row=0, column=0)

from_entry = Entry(root)
from_entry.grid(row=0, column=1)

to_label = Label(root, text="To Currency:")
to_label.grid(row=1, column=0)

to_entry = Entry(root)
to_entry.grid(row=1, column=1)

amount_label = Label(root, text="Amount:")
amount_label.grid(row=2, column=0)

amount_entry = Entry(root)
amount_entry.grid(row=2, column=1)

convert_button = Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2)

result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

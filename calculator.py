import tkinter

screen = tkinter.Tk()
screen.geometry("200x200")


def prati_broj(broj):
    entry.insert(tkinter.END, str(broj))


def calculator():
    a = eval(entry.get())
    entry.delete(0, tkinter.END)
    entry.insert(tkinter.END, a)

entry = tkinter.Entry()
entry.grid(row=0, column=0, columnspan=5, pady=2, padx=2)

broj_1 = tkinter.Button(text="1", command=lambda: prati_broj("1"))
broj_1.grid(row=3, column=0, pady=2, padx=2)

broj_2 = tkinter.Button(text="2", command=lambda: prati_broj("2"))
broj_2.grid(row=3, column=1, pady=2, padx=2)

broj_3 = tkinter.Button(text="3", command=lambda: prati_broj("3"))
broj_3.grid(row=3, column=2, pady=2, padx=2)

broj_4 = tkinter.Button(text="4", command=lambda: prati_broj("4"))
broj_4.grid(row=2, column=0, pady=2, padx=2)

broj_4 = tkinter.Button(text="5", command=lambda: prati_broj("5"))
broj_4.grid(row=2, column=1, pady=2, padx=2)

broj_6 = tkinter.Button(text="6", command=lambda: prati_broj("6"))
broj_6.grid(row=2, column=2, pady=2, padx=2)

broj_7 = tkinter.Button(text="7", command=lambda: prati_broj("7"))
broj_7.grid(row=1, column=0, pady=2, padx=2)

broj_8 = tkinter.Button(text="8", command=lambda: prati_broj("8"))
broj_8.grid(row=1, column=1, pady=2, padx=2)

broj_9 = tkinter.Button(text="9", command=lambda: prati_broj("9"))
broj_9.grid(row=1, column=2, pady=2, padx=2)

broj_0 = tkinter.Button(text="0", command=lambda: prati_broj("0"))
broj_0.grid(row=4, column=1, pady=2, padx=2)

sum_operator = tkinter.Button(text="+", command=lambda: prati_broj("+"))
sum_operator.grid(row=3, column=3, pady=2, padx=3)

odzemanje_operator = tkinter.Button(text="-", command=lambda: prati_broj("-"))
odzemanje_operator.grid(row=2, column=3, pady=2, padx=3)

mnozenje_operator = tkinter.Button(text="*", command=lambda: prati_broj("*"))
mnozenje_operator.grid(row=1, column=3, pady=2, padx=3)

delenje_operator = tkinter.Button(text="/", command=lambda: prati_broj("/"))
delenje_operator.grid(row=1, column=4, pady=2, padx=3)

rezultat_operator = tkinter.Button(text="=", command=lambda: calculator())
rezultat_operator.grid(row=2, column=4, rowspan=2, pady=2, padx=3)

screen.mainloop()

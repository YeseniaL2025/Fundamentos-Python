from tkinter import *
from tkinter import ttk

raiz = Tk()

estado = StringVar()

comboEstados = ttk.Combobox(raiz, textvariable=estado)  # Corregido: Combobox con b minúscula
comboEstados.grid()
comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacán")

raiz.mainloop()
from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Ejemplo de botones")

boton = ttk.Button(raiz, text="Botón solo texto") 
boton.grid()

imagen = PhotoImage(file="Link.png") 

btnImagen = ttk.Button(raiz)  
btnImagen.grid()
btnImagen['image']=imagen

btnCombinada = ttk.Button(raiz, text="Botón combinado", compound="bottom")
btnCombinada.grid()
btnCombinada['image']=imagen

chkBoton = ttk.Checkbutton(raiz, text="Opción 1")
chkBoton.grid()

raiz.mainloop()
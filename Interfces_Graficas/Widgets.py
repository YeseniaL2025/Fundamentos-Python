from tkinter import *
from tkinter import ttk

def guardar():
    # Leer datos del formulario
    nombre = nombre_var.get()
    ap_paterno = ap_paterno_var.get()
    ap_materno = ap_materno_var.get()
    correo = correo_var.get()
    movil = movil_var.get()
    ocupacion = ocupacion_var.get()
    estado = estado_var.get()

    aficiones = []
    if aficion_leer.get():
        aficiones.append("Leer")
    if aficion_musica.get():
        aficiones.append("Música")
    if aficion_videojuegos.get():
        aficiones.append("Videojuegos")
    aficiones_str = ", ".join(aficiones)

    # Crear ventana emergente
    ventana = Toplevel(raiz)
    ventana.title("Widgets")
    ventana.geometry("500x250")

    # Tabla en ventana emergente
    columnas = ("Nombre", "A. Paterno", "A. Materno", "Correo", "Móvil", "Ocupación", "Estado", "Aficiones")
    tree = ttk.Treeview(ventana, columns=columnas, show="headings")

    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # Insertar datos
    tree.insert("", "end", values=(nombre, ap_paterno, ap_materno, correo, movil, ocupacion, estado, aficiones_str))

def cancelar():
    raiz.destroy()

# Crear ventana principal
raiz = Tk()
raiz.title("Formulario de datos")
raiz.geometry("600x300")
raiz.resizable(False, False)

# Variables
ocupacion_var = StringVar(value="No especificado")
estado_var = StringVar()
nombre_var = StringVar()
ap_paterno_var = StringVar()
ap_materno_var = StringVar()
correo_var = StringVar()
movil_var = StringVar()

aficion_leer = BooleanVar()
aficion_musica = BooleanVar()
aficion_videojuegos = BooleanVar()

# Lista de estados de México
estados_mexico = (
    "Aguascalientes", "Baja California", "Baja California Sur", "Campeche",
    "Coahuila", "Colima", "Chiapas", "Chihuahua", "CDMX", "Durango",
    "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México", "Michoacán",
    "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro",
    "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco",
    "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"
)

# Frame del formulario
frame_formulario = Frame(raiz)
frame_formulario.grid(row=0, column=0, padx=10, pady=10)

# Campos del formulario
ttk.Label(frame_formulario, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky=E)
ttk.Entry(frame_formulario, textvariable=nombre_var).grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_formulario, text="A. Paterno:").grid(row=1, column=0, padx=5, pady=5, sticky=E)
ttk.Entry(frame_formulario, textvariable=ap_paterno_var).grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_formulario, text="A. Materno:").grid(row=2, column=0, padx=5, pady=5, sticky=E)
ttk.Entry(frame_formulario, textvariable=ap_materno_var).grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_formulario, text="Correo:").grid(row=3, column=0, padx=5, pady=5, sticky=E)
ttk.Entry(frame_formulario, textvariable=correo_var).grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_formulario, text="Móvil:").grid(row=4, column=0, padx=5, pady=5, sticky=E)
ttk.Entry(frame_formulario, textvariable=movil_var).grid(row=4, column=1, padx=5, pady=5)

# Aficiones
ttk.Label(frame_formulario, text="Aficiones:").grid(row=5, column=0, padx=5, pady=(10, 0), sticky=E)
frame_aficiones = Frame(frame_formulario)
frame_aficiones.grid(row=5, column=1, padx=5, pady=(10, 0), sticky=W)

Checkbutton(frame_aficiones, text="Leer", variable=aficion_leer).pack(side=LEFT, padx=5)
Checkbutton(frame_aficiones, text="Música", variable=aficion_musica).pack(side=LEFT, padx=5)
Checkbutton(frame_aficiones, text="Videojuegos", variable=aficion_videojuegos).pack(side=LEFT, padx=5)

# Botones
frame_botones = Frame(raiz)
frame_botones.grid(row=2, column=0, columnspan=2, pady=(10, 10))
ttk.Button(frame_botones, text="Guardar", command=guardar).pack(side=LEFT, padx=10)
ttk.Button(frame_botones, text="Cancelar", command=cancelar).pack(side=LEFT, padx=10)

# Frame lateral para ocupación y estado
frame_lateral = Frame(raiz)
frame_lateral.grid(row=0, column=1, padx=10, pady=10, sticky=N)

Radiobutton(frame_lateral, text="Estudiante", variable=ocupacion_var, value="Estudiante").pack(anchor=W, pady=(50, 0))
Radiobutton(frame_lateral, text="Empleado", variable=ocupacion_var, value="Empleado").pack(anchor=W)
Radiobutton(frame_lateral, text="Desempleado", variable=ocupacion_var, value="Desempleado").pack(anchor=W)

ttk.Label(frame_lateral, text="Estado:").pack(pady=(20, 0), anchor=W)
combo_estados = ttk.Combobox(frame_lateral, textvariable=estado_var, values=estados_mexico, state="readonly")
combo_estados.pack(anchor=W, pady=5)
combo_estados.current(0)

# Ejecutar
raiz.mainloop()
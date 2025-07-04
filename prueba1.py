from tkinter import Tk, ttk, IntVar

ventana = Tk()
ventana.title("Checkbutton simple")

# Variable asociada
es_estudiante = IntVar()

# Checkbutton vinculado a la variable
ttk.Checkbutton(ventana, text="Soy estudiante", variable=es_estudiante).pack()

# Función para mostrar el valor
def mostrar_estado():
    print(es_estudiante.get())  # Imprime 1 si está seleccionado, 0 si no

ttk.Button(ventana, text="Ver estado", command=mostrar_estado).pack()

ventana.mainloop()

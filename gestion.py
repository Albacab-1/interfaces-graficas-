from tkinter import Tk,  StringVar, BooleanVar, END
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as messagebox


def Gestion_personal():
    nombre = names.get().strip()
    apaterno = apaternos.get().strip()
    amaterno = amaternos.get().strip()
    correo = correos.get().strip()
    movil = e_movil.get().strip()
    ocupation_usu = ocupation.get().strip()
    afiliaciones = []
    if leer_var.get():
        afiliaciones.append("Leer")
        if musica_var.get():
            afiliaciones.append("Música")
            if videojuegos_var.get():
                afiliaciones.append("Videojuegos")
    if not (leer_var.get() or musica_var.get() or videojuegos_var.get()):
        messagebox.showerror("Error", "Debes seleccionar al menos una afiliación.")
        return
    afiliacion = ", ".join(afiliaciones)
    estado = estatebar.get().strip()

    if not nombre:
        messagebox.showerror("Error", "El campo Nombre es obligatorio.")
        return
    if not apaterno:
        messagebox.showerror("Error", "El campo Apellido Paterno es obligatorio.")
        return
    if not amaterno:
        messagebox.showerror("Error", "El campo Apellido Materno es obligatorio.")
        return
    if not correo:
        messagebox.showerror("Error", "El campo Correo es obligatorio.")
        return
    if not movil:
        messagebox.showerror("Error", "El campo Móvil es obligatorio.")
        return
    if not movil.isdigit():
        messagebox.showerror("Error", "El campo Móvil debe ser numérico.")
        return
    if not ocupation_usu:
        messagebox.showerror("Error", "Debes seleccionar una ocupación.")
        return
    if estado == "Estados(32)" or not estado:
        messagebox.showerror("Error", "Debes seleccionar un Estado.")
        return


    #guardar datos
    try:
        with open("Gestion_personal.csv","r",) as archivo:
            for linea in archivo:
                if f"Nombre: {nombre}, Apellido Paterno: {apaterno}, Apellido Materno: {amaterno}, e-mail: {correo}" in linea:
                    messagebox.showerror("Error", "Elemento ya ingresado")
                    return
    except FileNotFoundError:
        pass

    with open("Gestion_personal.csv", "a") as archivo:
        archivo.write(f"Nombre: {nombre}, Apellido Paterno: {apaterno}, Apellido Materno: {amaterno}, e-mail: {correo}, Teléfono: {movil}, Ocupación: {ocupation_usu}, Hobbies:{afiliacion},Estado: {estado}\n")
    

  # limpiar campos
    names.delete(0,END)
    apaternos.delete(0, END)
    amaternos.delete(0, END)
    correos.delete(0,END)
    e_movil.delete(0, END)
    ocupation.set("")
    leer_var.set(False)
    musica_var.set(False)
    videojuegos_var.set(False)
    estatebar.set("") 


# Crear ventana principal
ventana = Tk()
ventana.title("Control de Personal")
ventana.geometry("750x450")  # Un poco más ancha
ventana.resizable(False, False) #Evita que de redimensione
ventana.grid_columnconfigure(0, weight=1)

# Configurar el grid de la ventana para que crezca correctamente
ventana.columnconfigure(0, weight=1)

# formulario datos personales
formulario = ttk.Frame(ventana, padding=20, relief="solid")
formulario.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)


# Contenido del marco izquierdo
ttk.Label(formulario, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky="W")
ttk.Label(formulario, text="A. Paterno:").grid(row=2, column=0, padx=5, pady=5, sticky="W")
ttk.Label(formulario, text="A. Materno:").grid(row=3, column=0, padx=5, pady=5, sticky="W")
ttk.Label(formulario, text="Correo:").grid(row=4, column=0, padx=5, pady=5, sticky="W")
ttk.Label(formulario, text="Móvil:").grid(row=5, column=0, padx=5, pady=5, sticky="W")


names = ttk.Entry(formulario, width=30)
names.grid(row=1, column=1, padx=5, pady=5)

apaternos = ttk.Entry(formulario, width=30)
apaternos.grid(row=2, column=1, padx=5, pady=5)

amaternos = ttk.Entry(formulario, width=30)
amaternos.grid(row=3, column=1, padx=5, pady=5)

correos = ttk.Entry(formulario, width=30)
correos.grid(row=4, column=1, padx=5, pady=5)

e_movil = ttk.Entry(formulario, width=30)
e_movil.grid(row=5, column=1, padx=5, pady=5)

# Ocupación
ocupacion = ttk.Frame(ventana, padding=20, relief="flat")
ocupacion.grid(row=0, column=1, sticky="NS", padx=10, pady=10)  # Solo vertical

# Contenido del marco derecho

ttk.Label(ocupacion, text="Ocupación").grid(row=0, column=0, pady=(0,6))

ocupation= StringVar()

ttk.Radiobutton(ocupacion, text="Estudiante", variable=ocupation, value='Estudiante').grid(row=1, column=0, pady=5)
ttk.Radiobutton(ocupacion, text="Empleado",variable=ocupation, value='Empleado').grid(row=2, column=0, pady=5)
ttk.Radiobutton(ocupacion, text="Desempleado",variable=ocupation, value='Desempleado').grid(row=3, column=0, pady=5)

# Aficiones
hobbies = ttk.Frame(ventana, padding=10, relief="ridge")
hobbies.grid(row=2, column=0, sticky="W",padx= 10, pady=10)  # Solo vertical
ttk.Label(hobbies, text="Afiliaciones").grid(row=0, column=0, sticky="WS")

leer_var = BooleanVar()
musica_var = BooleanVar()
videojuegos_var = BooleanVar()

ancho= 55
ttk.Checkbutton(hobbies, text="Leer", variable=leer_var).grid(row=1, column=0, padx=ancho)
ttk.Checkbutton(hobbies, text="Música", variable=musica_var).grid(row=1, column=1, padx=ancho)
ttk.Checkbutton(hobbies, text="Videojuegos", variable=videojuegos_var).grid(row=1, column=2, padx=ancho)

#botones posición

botones = ttk.Frame(ventana)
botones.grid(row=3, padx=10, pady=10)
botones.columnconfigure(0, weight=1)
botones.columnconfigure(1, weight=1)
ttk.Button(botones, text="Guardar",command=Gestion_personal).grid(row=50, padx=10, sticky= "W")
ttk.Button(botones, text="Cancelar", command=ventana.quit).grid(row=50, padx = 150, sticky="W")

# Selección de estado

estatebar = StringVar()

estate= ttk.Combobox (ventana, textvariable= estatebar, state="readonly")
estate.set("Estados(32)")
estate.grid(row=2, column=1, sticky="E", padx=10, pady=10)
estate['values']= ("Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila", "Colima", "Chiapas", 
                   "Chihuahua", "Durango", "Distrito Federal", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "México", 
                   "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", 
                   "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas")

# Ejecutar la ventana
ventana.mainloop()

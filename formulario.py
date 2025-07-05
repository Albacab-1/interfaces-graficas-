import tkinter as tk
from tkinter import END

class Calculadora:
    def __init__(self, ventana):
        self.expresion = ""  #crea un elemento llamado objeto y lo inicializa, cadena vacía
        self.ventana = ventana #guarda la referencia de la ventana en Tk

        # Pantalla
        self.pantalla = tk.Entry(ventana, font=("Arial", 20), bd=5, relief="sunken", justify="right")
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Botones
        botones = [
            ('1',1,0), ('2',1,1), ('3',1,2), ('+',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
            ('7',3,0), ('8',3,1), ('9',3,2), ('*',3,3),
            ('C',4,0), ('0',4,1), ('/',4,2), ('=',4,3),
        ]

        for (texto, fila, col) in botones:
            boton = tk.Button(ventana, text=texto, font=("Arial", 20), width=4, command=lambda t=texto: self.click(t))
            boton.grid(row=fila, column=col, padx=5, pady=5)

    def click(self, tecla):
        if tecla == 'C':
            self.expresion = ""
            self.pantalla.delete(0, END)
        elif tecla == '=':
            try:
                resultado = str(eval(self.expresion))
                self.pantalla.delete(0, END)
                self.pantalla.insert(0, resultado)
                self.expresion = resultado
            except:
                self.pantalla.delete(0, END)
                self.pantalla.insert(0, "Error")
                self.expresion = ""
        else:
            self.expresion += tecla
            self.pantalla.insert(END, tecla)

# Crear ventana principal
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Calculadora")
    ventana.geometry("450x400")
    ventana.configure(bg="lightblue")

    app = Calculadora(ventana)
    ventana.mainloop()

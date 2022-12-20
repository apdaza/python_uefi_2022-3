import tkinter as tk

def funcion():
    print("La opcion es: " + variable.get())

ventana = tk.Tk()
variable = tk.StringVar()
radio1 = tk.Radiobutton(ventana, text="Opcion 1", variable=variable,
                        value=1, command=funcion)
radio2 = tk.Radiobutton(ventana, text="Opcion 2", variable=variable,
                        value=2, command=funcion)
radio1.pack()
radio2.pack()

ventana.mainloop()
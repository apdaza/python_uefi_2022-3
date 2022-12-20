import tkinter as tk

def funcion1():
    print("Boton 1")

def funcion2():
    print("Boton 2")

def funcion3():
    print("Boton 3")

ventana = tk.Tk()
ventana.geometry("300x150")
boton1 = tk.Button(ventana, text="Boton 1", command=funcion1)
boton1.pack()
boton2 = tk.Button(ventana, text="Boton 2", command=funcion2)
boton2.pack()
boton3 = tk.Button(ventana, text="Boton 3", command=funcion3)
boton3.pack()

ventana.mainloop()
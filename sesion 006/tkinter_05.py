import tkinter as tk

def comando():
    print(check_var.get())

ventana = tk.Tk()
check_var = tk.IntVar()
boton = tk.Checkbutton(ventana, text="Prueba check", variable=check_var, command=comando)
boton.pack()

ventana.mainloop()

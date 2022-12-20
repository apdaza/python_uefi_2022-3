import tkinter as tk

def nueva():
    ventana = tk.Toplevel(root)
    ventana.title("Nueva ventana")
    ventana.geometry("400x400")
    ventana.focus_set()

root = tk.Tk()
root.geometry("300x150")
boton = tk.Button(root, text="Nueva", command=nueva)
boton.pack()

root.mainloop()
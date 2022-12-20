import tkinter as tk

root = tk.Tk()
etiqueta = tk.Label(root, text="etiqueta: ")
etiqueta.pack()
texto = tk.Entry(root)
texto.pack()
root.mainloop()
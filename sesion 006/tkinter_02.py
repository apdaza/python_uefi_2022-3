import tkinter as tk

def responder():
    print("Excelente")

root = tk.Tk()
boton = tk.Button(root, text="Que te parece este ejemplo", command=responder)
boton.pack()
root.mainloop()
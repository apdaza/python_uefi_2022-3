import tkinter as tk

class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_gui()

    def init_gui(self):
        self.parent.title("Una ventana")

root = tk.Tk()
root.geometry("500x500")
ventana = GUI(parent=root)
ventana.mainloop()
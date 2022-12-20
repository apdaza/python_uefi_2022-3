from tkinter import *
from cronometro import Cronometro
from threading import *
from time import sleep


class AppCronometro(Thread):

    def __init__(self):
        self.principal = Tk()
        self.crono = Cronometro()
        self.frame = Frame(self.principal)
        self.frame.pack()
        self.estado = True

        self.valor = StringVar()
        self.display = Label(self.frame, textvariable=self.valor,
                             font=('Helvetica', 20))
        self.display.pack(side=TOP)

        self.boton_iniciar = Button(self.frame, text='Iniciar/Detener',
                                    command=self.cambiar_estado)
        self.boton_iniciar.pack(side=LEFT)

        self.boton_borrar = Button(self.frame, text='Borrar',
                                    command=self.borrar_cronometro)
        self.boton_borrar.pack(side=RIGHT)

        Thread.__init__(self)
        self.start()

        #self.principal.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.principal.mainloop()
        #print("forzado")
        #raise SystemExit()
        #self.join()
        

    def cambiar_estado(self):
        self.crono.cambiar_estado()

    def borrar_cronometro(self):
        self.crono.borrar()

    def run(self):
        while self.estado:
            if not self.crono.parado:
                self.crono.avanzar()
                sleep(0.1)
            if not self.estado:
                break
            self.valor.set(self.crono.ver_tiempo())

    def callback(self):
        print("saliendo")
        self.principal.quit()


app = AppCronometro()

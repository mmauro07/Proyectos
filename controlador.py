from tkinter import Tk
import vista

class Controlador:
    def __init__(self, root):
        self.root_controlador = root
        self.ventana = vista.Ventana(self.root_controlador)

if __name__ == "__main__":
    root_tk = Tk()
    aplicacion = Controlador(root_tk)
    aplicacion.ventana.actualizar()
    root_tk.mainloop()
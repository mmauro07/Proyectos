from tkinter import Frame, Label, StringVar, Entry, OptionMenu, Button
from tkinter import ttk
from modelo import Abmc

class Ventana:
    def __init__(self, ventana):
        self.root = ventana
        self.root.title("Lista de usarios")
        self.base = Abmc()
        
        #frame
        self.frame_1 = Frame(self.root)
        self.frame_1.config(width=500, height=250, bg="#3C3B7F")
        self.frame_1.grid(row=0, rowspan=5, column=0, columnspan=4)

        #etiquetas
        self.titulo_label = Label(self.root, text="Gestor de usuarios", font=("Arial",12), bg="#3C3B7F", fg="white")
        self.titulo_label.grid(row=0, column=0, columnspan=4, sticky="n")

        self.nombre_label = Label(self.root, text="Ingrese nombre del usuario", font=("Arial",10), bg="#3C3B7F", fg="white")
        self.nombre_label.grid(row=1, column=0)

        self.usuario_label = Label(self.root, text="Ingrese usuario", font=("Arial",10), bg="#3C3B7F", fg="white")
        self.usuario_label.grid(row=2, column=0)

        self.edad_label = Label(self.root, text="Ingrese edad del usuario", font=("Arial",10), bg="#3C3B7F", fg="white")
        self.edad_label.grid(row=3, column=0)

        self.genero_label = Label(self.root, text="Ingrese género del usuario", font=("Arial",10), bg="#3C3B7F", fg="white")
        self.genero_label.grid(row=4, column=0)

        #entradas y desplegables
        self.nombre = StringVar()
        self.entrada_nombre = Entry(self.root, textvariable=self.nombre)
        self.entrada_nombre.grid(row=1, column=1)

        self.usuario = StringVar()
        self.usuario.set("@")
        self.entrada_usuario = Entry(self.root, textvariable=self.usuario)
        self.entrada_usuario.grid(row=2, column=1)

        self.edad = StringVar()
        self.edad.set("Seleccione una opción")
        self.opciones_edad = ["18-29","30-39","40-49","50-59","60-69","70-79","80-89","90-99"]
        self.menu_edad = OptionMenu(self.root, self.edad, *self.opciones_edad)
        self.menu_edad.grid(row=3, column=1)

        self.genero = StringVar()
        self.genero.set("Seleccione una opción")
        self.opciones_genero = ["Masculino", "Femenino", "No binario"]
        self.menu_genero = OptionMenu(self.root, self.genero, *self.opciones_genero)
        self.menu_genero.grid(row=4, column=1)

        #botones
        self.boton_alta = Button(self.root, text="Registrar", command=lambda: self.alta())
        self.boton_alta.grid(row=1, column=3)

        self.boton_baja = Button(self.root, text="Eliminar", command=lambda: self.baja())
        self.boton_baja.grid(row=2, column=3)

        self.boton_modificar = Button(self.root, text="Modificar", command=lambda: self.modificar())
        self.boton_modificar.grid(row=3, column=3)

        #treeview
        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1","col2","col3","col4")
        self.tree.heading("#0", text="ID")
        self.tree.column("#0", width=50, minwidth=50)
        self.tree.heading("col1", text="Nombre")
        self.tree.column("col1", width=100, minwidth=100)
        self.tree.heading("col2", text="Usuario")
        self.tree.column("col2", width=100, minwidth=100)
        self.tree.heading("col3", text="Edad")
        self.tree.column("col3", width=100, minwidth=100)
        self.tree.heading("col4", text="Género")
        self.tree.column("col4", width=100, minwidth=100)
        self.tree.grid(row=5, column=0, columnspan=5)

    def alta(self,):
        self.base.alta(self.nombre.get(), self.usuario.get(), self.edad.get(), self.genero.get(), self.tree)
        self.nombre.set("")
        self.usuario.set("@")
        self.edad.set("Seleccione una opción")
        self.genero.set("Seleccione una opción")

    def baja(self,):
        self.base.baja(self.tree)

    def modificar(self,):
        self.base.modificar(self.nombre.get(), self.usuario.get(), self.edad.get(), self.genero.get(), self.tree)
        self.nombre.set("")
        self.usuario.set("@")
        self.edad.set("Seleccione una opción")
        self.genero.set("Seleccione una opción")

    def actualizar(self,):
        self.base.actualizar_treeview(self.tree)
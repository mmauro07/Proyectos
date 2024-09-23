from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import sqlite3

base_de_datos = sqlite3.connect("base.db")

def crear_tabla():
    cursor = base_de_datos.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, nombre TEXT, stock INTEGER, precio REAL)")
    base_de_datos.commit()

crear_tabla()

main = Tk()
main.title("Control de Stock")

titulo = Label(main, text="Control de stock", font=("Arial", 16))
titulo.grid(row=0, column=0, columnspan=4, pady=10)

producto = Label(main, text="Ingrese producto", font=("Arial", 12))
producto.grid(row=1, column=0, sticky=W)
stock = Label(main, text="Ingrese stock", font=("Arial", 12))
stock.grid(row=2, column=0, sticky=W)
precio = Label(main, text="Ingrese precio", font=("Arial", 12))
precio.grid(row=3, column=0, sticky=W)
monto_total = Label(main, text="Monto total en stock: 0.00$", font=("Arial", 12))
monto_total.grid(row=4, column=0, sticky=W)

var_producto = StringVar()
var_stock = StringVar()
var_precio = StringVar()

entrada_producto = Entry(main, textvariable=var_producto)
entrada_producto.grid(row=1, column=1)
entrada_stock = Entry(main, textvariable=var_stock)
entrada_stock.grid(row=2, column=1)
entrada_precio = Entry(main, textvariable=var_precio)
entrada_precio.grid(row=3, column=1)

tabla = ttk.Treeview(main)
tabla["columns"] = ("col1", "col2", "col3")
tabla.column("#0", width=25, minwidth=25, anchor=CENTER)
tabla.column("col1", width=100, minwidth=100, anchor=CENTER)
tabla.column("col2", width=50, minwidth=50, anchor=CENTER)
tabla.column("col3", width=50, minwidth=50, anchor=CENTER)
tabla.heading("#0", text="ID", anchor=CENTER)
tabla.heading("col1", text="Producto", anchor=CENTER)
tabla.heading("col2", text="Stock", anchor=CENTER)
tabla.heading("col3", text="Precio", anchor=CENTER)
tabla.grid(row=5, column=0, columnspan=4)

def guardar():
    if var_producto.get() != "" and var_precio.get() != "" and var_stock.get() != "":
        nombre = var_producto.get()
        stock = int(var_stock.get())
        precio = float(var_precio.get())
        cursor = base_de_datos.cursor()
        cursor.execute('INSERT INTO productos (nombre, stock, precio) VALUES (?, ?, ?)', (nombre, stock, precio))
        base_de_datos.commit()
        var_producto.set("")
        var_stock.set("")
        var_precio.set("")
        cargar_productos()
        actualizar_monto_total()
    else:
        showerror("Error", "Por favor ingrese datos en todos los campos")

def borrar():
    if tabla.focus():
        elem = tabla.focus()
        id_producto = tabla.item(elem)["text"]
        cursor = base_de_datos.cursor()
        cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
        base_de_datos.commit()
        tabla.delete(elem)
        actualizar_monto_total()
    else:
        showerror("Error", "Debe seleccionar un producto")

def modificar():
    if tabla.focus():
        elem = tabla.focus()
        id_producto = tabla.item(elem)["text"]
        stock_nuevo = var_stock.get()
        precio_nuevo = var_precio.get()
        if stock_nuevo != "" and precio_nuevo != "":
            cursor = base_de_datos.cursor()
            cursor.execute('UPDATE productos SET stock = ?, precio = ? WHERE id = ?', (int(stock_nuevo), float(precio_nuevo), id_producto))
            base_de_datos.commit()
            var_stock.set("")
            var_precio.set("")
            cargar_productos()
            actualizar_monto_total()
        else:
            showerror("Error", "Por favor ingrese nuevos valores para stock y precio")
    else:
        showerror("Error", "Debe seleccionar un producto")

def cargar_productos():
    for i in tabla.get_children():
        tabla.delete(i)
    cursor = base_de_datos.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()   
    for producto in productos:
        tabla.insert("", "end", text=producto[0], values=(producto[1], producto[2], producto[3]))

def actualizar_monto_total():
    cursor = base_de_datos.cursor()
    cursor.execute('SELECT SUM(stock * precio) FROM productos')
    total = cursor.fetchone()[0] or 0
    monto_total.config(text=f"Monto total en stock: ${total:.2f}")

cargar_productos()
actualizar_monto_total()

boton_guardar = Button(main, text="Guardar", command=guardar, bg="#4CAF50", fg="white")
boton_guardar.grid(row=1, column=3)

boton_borrar = Button(main, text="Borrar", command=borrar, bg="#F44336", fg="white")
boton_borrar.grid(row=2, column=3)

boton_modificar = Button(main, text="Modificar", command=modificar, bg="#FFEC79", fg="black")
boton_modificar.grid(row=3, column=3)

main.mainloop()
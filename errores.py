from tkinter.messagebox import showerror
from validar import Validar

class Errores():

    def error_usuario_repetido():
        showerror("Error","El usuario ya existe, por favor ingrese otro")

    def error_de_entradas(nombre, usuario, edad, genero):
        if Validar.validar_nombre(nombre) == False:
            showerror("Error","Por favor ingrese un nombre válido")
            return 1
        if Validar.validar_usuario(usuario) == False:
            showerror("Error","Por favor ingrese un usuario válido")
            return 1
        if Validar.validar_edad(edad) == False:
            showerror("Error","Seleccione una opción de edad por favor")
            return 1
        if Validar.validar_genero(genero) == False:
            showerror("Error","Seleccione una opción una opción de género por favor")
            return 1
        else:
            return 0
        
    def error_baja():
        showerror("Error","Debe seleccionar con el cursor al usuario a dar de baja")

    def error_modificar():
        showerror("Error","Debe seleccionar con el cursor al usuario a modificar")

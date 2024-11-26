import re

class Validar:

    def validar_nombre(nombre):
        validacion = 0 < len(nombre) < 15
        return validacion

    def validar_usuario(usuario):
        regex = r"^@[a-zA-Z0-9._]+$"
        coincidencia = True if re.match(regex, usuario) != None else False
        validacion = coincidencia and 1 < len(usuario) < 16
        return validacion
    
    def validar_edad(edad):
        validacion = edad != "Seleccione una opción"
        return validacion
    
    def validar_genero(genero):
        validacion = genero != "Seleccione una opción"
        return validacion
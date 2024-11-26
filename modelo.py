from peewee import SqliteDatabase, Model, CharField, IntegrityError, DoesNotExist
from errores import Errores

db = SqliteDatabase("usuarios.db")

class BaseModel(Model):
    class Meta:
        database = db

class Usuarios(BaseModel):
    nombre = CharField()
    usuario = CharField(unique=True)
    edad = CharField()
    genero = CharField()

db.connect()
db.create_tables([Usuarios])

class Abmc:

    def alta(self, nombre, usuario, edad, genero, mitreeview):
        if Errores.error_de_entradas(nombre, usuario, edad, genero) == 0:
            try:
                Usuarios.create(nombre=nombre, usuario=usuario, edad=edad, genero=genero)
                self.actualizar_treeview(mitreeview)
            except IntegrityError:
                Errores.error_usuario_repetido()


    def actualizar_treeview(self, mitreeview):
        usuarios = mitreeview.get_children()
        for dato in usuarios:
            mitreeview.delete(dato)
        for fila in Usuarios.select():
            mitreeview.insert("", 0, text = fila.id, values = (fila.nombre, fila.usuario, fila.edad, fila.genero))

    def baja(self, mitreeview):
        try:
            ex_usuario = mitreeview.focus()
            valor_id = mitreeview.item(ex_usuario)
            eliminar = Usuarios.get(Usuarios.id==valor_id["text"])
            eliminar.delete_instance()
            self.actualizar_treeview(mitreeview)
        except DoesNotExist:
            Errores.error_baja()

    def modificar(self, nombre, usuario, edad, genero, mitreeview):
        if not mitreeview.focus():
            Errores.error_modificar()
        else:
            cambio_usuario = mitreeview.focus()
            valor_id = mitreeview.item(cambio_usuario)
            if Errores.error_de_entradas(nombre, usuario, edad, genero) == 0:
                try:
                    modificar = Usuarios.update(nombre = nombre, usuario = usuario, edad = edad,
                                            genero = genero).where(Usuarios.id==valor_id["text"])
                    modificar.execute()
                    self.actualizar_treeview(mitreeview)
                except IntegrityError:
                    Errores.error_usuario_repetido()
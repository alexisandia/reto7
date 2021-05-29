from config.connection import Connection
# from bson.objectid import ObjectId

class Salon:
    def __init__(self, nombre='nombre no insertado', año_escolar='año no insertado'):
        self.nombre = nombre
        self.año_escolar = año_escolar
    
    def all_salon(self):
        try:
            conn = Connection('reto7')

            todos_cursos = conn.get_all('salones', {}, {
            'nombre': 1,
            'año_escolar':1
            })
            lista = list(todos_cursos)
            for i in lista:
                print(i)
        except Exception as e:
            print(e)

    def insert_salon(self, nombre, año_escolar):
        try:
            conn = Connection('reto7')
            curso_nuevo = Salon(nombre, año_escolar)
            conn.insert('salones',  curso_nuevo.__dict__ )
        except Exception as e:
            print(e)

    def update_salon(self,nombre_viejo, nombre_nuevo, año_nuevo):
        try:
            conn = Connection('reto7')
            conn.update('salones', {
                'nombre': {
                    '$eq': nombre_viejo
                }
            }, {
                'nombre': nombre_nuevo,
                'año_escolar': año_nuevo
            })
        except Exception as e:
            print(e)

    def eliminar_salon(self, nombre):
        conn = Connection('reto7')
        conn.delete('salones', {
            'nombre': {
            '$eq': nombre
            }
        })

#a = Salon().eliminar_salon('Los nerds')
#a.all_salon()
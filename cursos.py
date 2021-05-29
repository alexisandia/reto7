from config.connection import Connection
# from bson.objectid import ObjectId

class Curso:
    def __init__(self, nombre='nombre no insertado'):
        self.nombre = nombre
    
    def all_curso(self):
        try:
            conn = Connection('reto7')

            todos_cursos = conn.get_all('cursos', {}, {
            'nombre': 1
            })
            lista = list(todos_cursos)
            for i in lista:
                print(i)
        except Exception as e:
            print(e)

    def insert_curso(self, nombre):
        try:
            conn = Connection('reto7')
            curso_nuevo = Curso(nombre)
            conn.insert('cursos',  curso_nuevo.__dict__ )
        except Exception as e:
            print(e)

    def update_curso(self,nombre_viejo, nombre_nuevo):
        try:
            conn = Connection('reto7')
            conn.update('cursos', {
                'nombre': {
                    '$eq': nombre_viejo
                }
            }, {
                'nombre': nombre_nuevo
            })
        except Exception as e:
            print(e)

    # Eliminar Muchos
    def eliminar_curso(self, nombre):
        conn = Connection('reto7')
        conn.delete('cursos', {
            'nombre': {
            '$eq': nombre
            }
        })

#a = Curso()
#a.update_curso('Calculo 2','Circuitos electricos 1')
#Curso().eliminar_curso('Circuitos electricos 1')

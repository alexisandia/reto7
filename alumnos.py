from config.connection import Connection
# from bson.objectid import ObjectId

class Alumno:
    def __init__(self, nombre='nombre no insertado', edad='edad no insertado', correo='correo no insertada', salon='salon no insertado'):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.salon = salon

    def all_alumno(self):
        try:
            conn = Connection('reto7')

            todos_cursos = conn.get_all('alumnos', {}, {
            'nombre': 1,
            'edad':1,
            'correo':1,
            'salon':1
            })
            lista = list(todos_cursos)
            for i in lista:
                print(i)
        except Exception as e:
            print(e)

    def insert_alumno(self, nombre, edad, correo, salon):
        try:
            conn = Connection('reto7')
            curso_nuevo = Alumno(nombre, edad, correo, salon)
            conn.insert('alumnos',  curso_nuevo.__dict__ )
        except Exception as e:
            print(e)

    def update_alumno(self,nombre_viejo, nombre_nuevo, edad_nuevo, correo_nuevo, salon_nuevo):
        try:
            conn = Connection('reto7')
            conn.update('alumnos', {
                'nombre': {
                    '$eq': nombre_viejo
                }
            }, {
                'nombre': nombre_nuevo,
                'edad': edad_nuevo,
                'correo': correo_nuevo,
                'salon': salon_nuevo
            })
        except Exception as e:
            print(e)
    
    def eliminar_alumno(self, nombre):
        conn = Connection('reto7')
        conn.delete('alumnos', {
            'nombre': {
            '$eq': nombre
            }
        })

#Alumno().all_alumno()
#Alumno().eliminar_alumno('Jonathan')
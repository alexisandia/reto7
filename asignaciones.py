from config.connection import Connection
# from bson.objectid import ObjectId

class Asignacion:
    def __init__(self, salon='salon no insertado', curso='curso no insertado', profesor='profesor no insertado'):
        self.salon = salon
        self.curso = curso
        self.profesor = profesor
    
    def all_asignacion(self):
        try:
            conn = Connection('reto7')

            todos_cursos = conn.get_all('asignaciones', {}, {
            'salon': 1,
            'curso':1,
            'profesor':1
            })
            lista = list(todos_cursos)
            for i in lista:
                print(i)
        except Exception as e:
            print(e)

    def insert_asignacion(self, salon, curso, profesor):
        try:
            conn = Connection('reto7')
            curso_nuevo = Asignacion(salon, curso, profesor)
            conn.insert('asignaciones',  curso_nuevo.__dict__ )
        except Exception as e:
            print(e)

    def update_asignacion(self,salon_viejo, curso_viejo,salon_nuevo, curso_nuevo, profesor_nuevo):
        try:
            conn = Connection('reto7')
            conn.update('asignaciones', {
                'salon': {
                    '$eq': salon_viejo
                },
                'curso': {
                    '$eq': curso_viejo
                }
            }, {
                'salon': salon_nuevo,
                'curso': curso_nuevo,
                'profesor': profesor_nuevo
            })
        except Exception as e:
            print(e)

    def eliminar_asignacion(self, salon, curso):
        conn = Connection('reto7')
        conn.delete('asignaciones', {
            'salon': {
            '$eq': salon
            },
            'curso': {
            '$eq': curso
            }
        })

#a = Asignacion().eliminar_asignacion('Los malditos', 'Fisica 1')
#a.update_asignacion('Los mdsad','dsa','Los nerds','Quimica 1','Maria')
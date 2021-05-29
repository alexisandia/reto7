from config.connection import Connection
# from bson.objectid import ObjectId

class Nota:
    def __init__(self, nombre='nombre no insertado', bimestre='bimestre no insertado', nota='nota no insertada'):
        self.nombre = nombre
        self.bimestre = bimestre
        self.nota = nota

    def all_nota(self):
        try:
            conn = Connection('reto7')

            todos_cursos = conn.get_all('notas', {}, {
            'nombre': 1,
            'bimestre':1,
            'nota':1
            })
            lista = list(todos_cursos)
            for i in lista:
                print(i)
        except Exception as e:
            print(e)

    def insert_nota(self, nombre, bimestre, nota):
        try:
            conn = Connection('reto7')
            curso_nuevo = Nota(nombre, bimestre, nota)
            conn.insert('notas',  curso_nuevo.__dict__ )
        except Exception as e:
            print(e)

    def update_nota(self,nombre_viejo, bimestre_viejo, bimestre_nuevo, nota_nuevo):
        try:
            conn = Connection('reto7')
            conn.update('notas', {
                'nombre': {
                    '$eq': nombre_viejo
                },
                'bimestre': {
                    '$eq': bimestre_viejo
                }
            }, {
                'bimestre': bimestre_nuevo,
                'nota': nota_nuevo
            })
        except Exception as e:
            print(e)

    def eliminar_nota(self, nombre, bimestre):
        conn = Connection('reto7')
        conn.delete('notas', {
            'nombre': {
            '$eq': nombre
            },
            'bimestre': {
            '$eq': bimestre
            }
        })

#a = Nota().eliminar_nota('Omar', '2021-1')
#a.all_nota()

from alumnos import Alumno
from profesores import Profesor
from cursos import Curso
from notas import Nota
from salones import Salon
from asignaciones import Asignacion


class Principal:
    def __init__(self):
        self.bienvenido()
        self.interfaz()

    def bienvenido(self):
        print ('''
            ____  _                           _     _       
            |  _ \(_)                         (_)   | |      
            | |_) |_  ___ _ ____   _____ _ __  _  __| | ___  
            |  _ <| |/ _ \ '_ \ \ / / _ \ '_ \| |/ _` |/ _ \ 
            | |_) | |  __/ | | \ V /  __/ | | | | (_| | (_) |
            |____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/
                ''')

    def interfaz(self):
        while True:
            print(''' 
                ¿Ingrese una opcion?
                1) Alumno
                2) Profesor
                3) Curso
                4) Salon
                5) Notas
                6) Asigancion de cursos
                7) Salir de aplicación\n
            ''')
            opcion = input("> ")
            
            if opcion == "1":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar alumnos
                    2) Registrar alumno nuevo
                    3) Editar datos de un alumno
                    4) Eliminar un alumno
                    5) Atras\n
                    ''')
                    opcion1 = input("> ")
                    if opcion1== "1":
                        self.mostrar_alumno()
                    elif opcion1=="2":
                        self.registrar_alumno()
                    elif opcion1 == "3":
                        self.editar_alumno()
                    elif opcion1 =="4":
                        self.eliminar_alumno()
                    elif opcion1 == "5":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")
            
            if opcion == "2":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar profesores
                    2) Registrar profesor nuevo
                    3) Editar datos de un profesor
                    4) Eliminar un profesor
                    5) Atras\n
                    ''')
                    opcion2 = input("> ")
                    if opcion2== "1":
                        self.mostrar_profesor()
                    elif opcion2=="2":
                        self.registrar_profesor()
                    elif opcion2 == "3":
                        self.editar_profesor()
                    elif opcion2 == "4":
                        self.eliminar_profesor()
                    elif opcion2 == "5":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")

            if opcion == "3":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar cursos
                    2) Registrar curso nuevo
                    3) Editar datos de un curso
                    4) Eliminar un curso
                    5) Atras\n
                    ''')
                    opcion3 = input("> ")
                    if opcion3== "1":
                        self.mostrar_curso()
                    elif opcion3=="2":
                        self.registrar_curso()
                    elif opcion3 == "3":
                        self.editar_curso()
                    elif opcion3 == "4":
                        self.eliminar_curso()
                    elif opcion3 == "5":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")

            if opcion == "4":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar salones
                    2) Registrar salon nuevo
                    3) Editar datos de un salon
                    4) Eliminar un salon
                    5) Atras\n
                    ''')
                    opcion4 = input("> ")
                    if opcion4== "1":
                        self.mostrar_salon()
                    elif opcion4=="2":
                        self.registrar_salon()
                    elif opcion4 == "3":
                        self.editar_salon()
                    elif opcion4 == "4":
                        self.eliminar_salon()
                    elif opcion4 == "5":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")

            if opcion == "5":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar Notas de todos los alumnos
                    2) Registrar una nota nuevo
                    3) Editar notas de un alumno
                    4) Elimnar una nota
                    5) Atras\n
                    ''')
                    opcion5 = input("> ")
                    if opcion5== "1":
                        self.mostrar_nota()
                    elif opcion5=="2":
                        self.registrar_nota()
                    elif opcion5 == "3":
                        self.editar_nota()
                    elif opcion5 == "4":
                        self.eliminar_nota()
                    elif opcion5 == "5":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")

            if opcion == "6":
                while True:
                    print(''' 
                    ¿Ingrese una opcion?
                    1) Listar Asignaciones de todos los cursos
                    2) Registrar una nueva asignacion
                    3) Editar una asignacion
                    4) Eliminar una asignacion
                    5) Atras\n
                    ''')
                    opcion6 = input("> ")
                    if opcion6== "1":
                        self.mostrar_asignacion()
                    elif opcion6=="2":
                        self.registrar_asignacion()
                    elif opcion6 == "3":
                        self.editar_asignacion()
                    elif opcion6 == "4":
                        self.eliminar_asignacion()
                    elif opcion6 == "5":
                        break
                    else:
                        print("\nIntroduciste una opcion incorrecta")


            if opcion == "7":
                break

           
    # Metodo para de la clase alumno
    def mostrar_alumno(self):
        a = Alumno().all_alumno()
        print(a)
    def registrar_alumno(self):
        nombre = input("ingrese nombre del alumno: ")
        edad = input("ingrese la edad del alumno: ")
        correo = input("ingrese el correo del alumno: ")
        id_salon = input("ingrese el salon asociado al alumno: ")
        print("Registrando alumno...")
        Alumno().insert_alumno( nombre, edad, correo, id_salon)
        print(f"Alumnno registrado --> {nombre}")
    def editar_alumno(self):
        nombre_0 = input("ingrese el nombre del alumno a modoficar: ")
        nombre_1 = input("ingrese el nombre nuevo del alumno: ")
        edad = input("ingrese la nueva edad del alumno: ")
        correo = input("ingrese el nuevo correo del alumno: ")
        id_salon = input("ingrese el nuevo salon asociado al alumno: ")
        print("Actualizando datos del alumno...")
        Alumno().update_alumno( nombre_0, nombre_1, edad, correo, id_salon)
        print(f"Datos del alumno {nombre_1} actualizados")
    def eliminar_alumno(self):
        nombre = input("ingrese el nombre del alumno a eliminar: ")
        Alumno().eliminar_alumno( nombre)
        print(f"Se elimino al alumno {nombre}")
    
    # Metodo de la clase profesor
    def mostrar_profesor(self):
        a = Profesor().all_profesor()
        print(a)

    def registrar_profesor(self):
        nombre = input("ingrese nombre del profesor: ")
        edad = input("ingrese la edad del profesor: ")
        correo = input("ingrese el correo del profesor: ")
        id_salon = input("ingrese el salon asociado al profesor: ")
        print("Registrando profesor...")
        Profesor().insert_profesor( nombre, edad, correo, id_salon)
        print(f"Profesor registrado --> {nombre}")

    def editar_profesor(self):
        nombre_0 = input("ingrese el nombre del profesor a modoficar: ")
        nombre_1 = input("ingrese el nombre nuevo del profesor: ")
        edad = input("ingrese la nueva edad del profesor: ")
        correo = input("ingrese el nuevo correo del profesor: ")
        id_salon = input("ingrese el nuevo salon asociado al profesor: ")
        print("Actualizando datos del profesor...")
        Profesor().update_profesor( nombre_0, nombre_1, edad, correo, id_salon)
        print(f"Datos del profesor {nombre_1} actualizados")

    def eliminar_profesor(self):
        nombre = input("ingrese el nombre del profesor a eliminar: ")
        Profesor().eliminar_profesor( nombre)
        print(f"Se elimino al profesor {nombre}")

# Metodos para curso
    def mostrar_curso(self):
        a = Curso().all_curso()
        print(a)
    def registrar_curso(self):
        nombre_curso = input("ingrese el nombre del curso: ")
        print("Registrando curso...")
        Curso().insert_curso( nombre_curso)
        print(f"Curso registrado --> {nombre_curso}")
    def editar_curso(self):
        nombre_curso_0 = input("ingrese el nombre del curso a modificar: ")
        nombre_curso_1 = input("ingrese el nuevo nombre del curso : ")
        print("Actualizando curso...")
        Curso().update_curso( nombre_curso_0, nombre_curso_1)
        print(f"Curso actualizado --> {nombre_curso_1}")
    def eliminar_curso(self):
        nombre = input("ingrese el nombre del curso a eliminar: ")
        Curso().eliminar_curso( nombre)
        print(f"Se elimino el curso {nombre}")

#Metodos para salon
    def mostrar_salon(self):
        a = Salon().all_salon()
        print(a)
    def registrar_salon(self):
        nombre = input("ingrese nombre del salon: ")
        año = input("ingrese el año escolar del salon: ")
        print("Registrando salon...")
        Salon().insert_salon( nombre, año)
        print(f"Salon registrado --> {nombre}")
    def editar_salon(self):
        nombre_0 = input("ingrese nombre del salon a modificar: ")
        nombre_1 = input("ingrese nombre nuevo del salon: ")
        año = input("ingrese el nuevo año escolar del salon: ")
        print("Actualizando salon...")
        Salon().update_salon( nombre_0, nombre_1, año)
        print(f"Salon actualizado --> {nombre_1}")
    def eliminar_salon(self):
        nombre = input("ingrese el nombre del salon a eliminar: ")
        Salon().eliminar_salon( nombre)
        print(f"Se elimino el salon {nombre}")

#Metodos para asignaciones
    def mostrar_asignacion(self):
        a = Asignacion().all_asignacion()
        print(a)
    def registrar_asignacion(self):
        salon = input("ingrese nombre del salon: ")
        curso = input("ingrese el nombre del curso: ")
        profesor = input("ingrese el nombre del profesor: ")
        print("Registrando asignatura...")
        Asignacion().insert_asignacion( salon, curso, profesor)
        print(f"Asignacion registrada --> {salon},{curso},{profesor} ")
    def editar_asignacion(self):
        salon_0 = input("ingrese nombre del salon: ")
        salon_1 = input("ingrese nombre nuevo del salon: ")
        curso_0 = input("ingrese el nombre del curso: ")
        curso_1 = input("ingrese el nombre nuevo del curso: ")
        profesor = input("ingrese el nombre nuevo del profesor: ")
        print("Actualizando asignatura...")
        Asignacion().update_asignacion( salon_0, curso_0, salon_1, curso_1 , profesor)
        print(f"Asignacion actualizada --> {salon_1},{curso_1},{profesor} ")
    def eliminar_asignacion(self):
        salon = input("ingrese el nombre del salon a eliminar: ")
        curso = input ('ingrese el nombre del curso a eliminar: ')
        Asignacion().eliminar_asignacion(salon, curso)
        print(f"Se elimino la asignacion asociada al {salon} y {curso}")

        #Metodos para notas
    def mostrar_nota(self):
        a = Nota().all_nota()
        print(a)
    def registrar_nota(self):
        nombre = input("ingrese nombre del alumno: ")
        bimestre = input("ingrese el bimestre en el cual se desea registrar la nota: ")
        nota = input("ingrese la nota: ")
        print("Registrando nota...")
        Nota().insert_nota( nombre, bimestre, nota)
        print(f"Nota registrada del alumno --> {nombre} ")
    def editar_nota(self):
        nombre = input("ingrese nombre del alumno al cual desea modificar su nota: ")
        bimestre_0 = input("ingrese el bimestre: ")
        bimestre_1 = input("ingrese el bimestre nuevo: ")
        nota = input("ingrese la nueva nota: ")
        print("Actualizando nota...")
        Nota().update_nota( nombre, bimestre_0, bimestre_1, nota)
        print(f"Nota actualizada del alumno --> {nombre} ")
    def eliminar_nota(self):
        nombre = input("ingrese el nombre del alumno a eliminar: ")
        bimestre = input ('ingrese el nombre del bimestre a eliminar: ')
        Nota().eliminar_nota(nombre, bimestre)
        print(f"Se elimino la nota del alumno {nombre} asociada a al bimestre {bimestre}")

# Clase principal para correr el programa
Principal()
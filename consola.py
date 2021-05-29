class interfaz():
    def __init__(self):
        self.interfaz_inicio()
    def interfaz_inicio(self):
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
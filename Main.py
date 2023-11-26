

from Usuarios import *
from Materiales import *


materiales = [[],[],[]]
# Instanciamos los objetos con los que vamos a probar las funcionalidades

#Usuarios
estudiante1 = Estudiante("Esteban","Cardona Lopez",1021301023,"esteban@gmail.com","Ingenieria Mecatronica")
egresado1 = Egresado("María", "Gómez Pérez", 54321, "maria.gomez@example.com")
profesor1 = Profesor("Juan", "Pérez Gómez", 12345, "juan.perez@example.com", "Facultad de Ciencias", "Ocasional", "Departamento de Matemáticas")
administrativo1 = Administrativo("Carlos", "Martínez López", 9876, "carlos.martinez@example.com", "Departamento de Recursos Humanos")
usuarios = [estudiante1,egresado1,profesor1,administrativo1]

#Materiales
libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "ISBN-123456", 1954, "Editorial1")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "ISBN-789012", 1967, "Editorial2")
libro3 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "ISBN-345678", 1997, "Editorial3")
revista1 = Revista("National Geographic", "Varios autores", "ISSN-12345", 2023, 1, 50)
revista2 = Revista("Scientific American", "Varios autores", "ISSN-67890", 2023, 2, 30)
revista3 = Revista("Time", "Varios autores", "ISSN-ABCDE", 2023, 3, 100)
cd1 = Elemento_Multimedia("Impacto de las redes sociales en la sociedad moderna", "María García", "TES-2023-001", 2023,"Tesis")
cd2 = Elemento_Multimedia("Desarrollo de algoritmos de inteligencia artificial", "Juan Rodríguez", "TES-2023-002", 2023,"Tesis")
cd3 = Elemento_Multimedia("Python Programming Guide", "John Smith", "CD-12345", 2023,"Libro Digital")
cd4 = Elemento_Multimedia("Data Science Essentials", "Alice Johnson", "CD-67890", 2023,"Libro Digital")
materiales = [[libro1, libro2, libro3], [revista1, revista2, revista3], [cd1, cd2, cd3, cd4]]

#Creacion del menu

print("Bienvenido al sistema de Gestion de Prestamo de Bilbioteca.")
print("-----Usuarios Registrados-----")
#Mostramos los usuarios que se encuentran registrados
usuario_en_sesion = None
i = 0
for usuario in usuarios:
    print(f"{i+1}. {usuario}")
    i +=1
try:
    indiceAux = int(input("Seleccione el indice del usuario con el que desea ingresar: "))
    estadoFecha = False
    fechas = []
    while estadoFecha == False:
        fecha = input("Ingrese la fecha actual separada por /: ")
        contadorSlash = 0
        for letra in fecha:
            if letra == "/":
                contadorSlash +=1
        if contadorSlash == 2:
            estadoFecha = True
        else:
            print("Ingrese correctamente la fecha.")
    fechas.append(fecha)
    #Verificamos las posibles excepciones que pueden ocurrir
    try:
    #Almacenamos el usuario en sesion dentro de la variable usuario_en_sesion
        usuario_en_sesion = usuarios[indiceAux-1]
        print(f"Bienvenido {usuario_en_sesion.getNombre()} {usuario_en_sesion.getApellidos()}.")  
        opcion = -1  
        while opcion!= 0:
            print(f"Fecha actual: {fechas[len(fechas)-1]}")
            print("-----Funciones Disponibles-----")
            print("1. Hacer un prestamo")
            print("2. Hacer una devolución")
            print("3. Aplicar Sanción")
            print("4. Mostrar usuarios registrados")
            print("5. Mostrar materiales registrados")
            if(usuario_en_sesion.getTipoUsuario() == "Profesor" and usuario_en_sesion.getEstado() == False):
                print("6. Levantar sanción")
            print("0. Salir/Actualizar Fecha")
            #Verificamos las posibles excepciones que pueden ocurrir
            try:
                opcion = int(input("Seleccione la opción de la función que desea realizar: "))
                if not(opcion>=0 and opcion<=6):
                    print("Ingrese correctamente la opción.")
                    break
 
                if opcion == 1:
                    print("-----Materiales disponibles----- ")
                    if usuario_en_sesion.prestamo(materiales,fechas) == True:
                        print("El material fue prestado correctamente.")
                    
                elif opcion == 2:
                    usuario_en_sesion.devolucion()
                elif opcion == 3:
                    usuario_en_sesion.aplicarSancion()
                    print("Sanción aplicada correctamente.")
                elif opcion == 4:
                    #Mostramos los usuarios registrados
                    i=0
                    for usuario in usuarios:
                        print(f"{i+1}. {usuario}")
                        i+=1

                elif opcion == 5:
                    #Mostramos los materiales registrados
                    i=0
                    for materialAux in materiales: 
                        for material in materialAux:    
                            print(f"{i+1}. {material}")
                            i+=1

                elif opcion == 0:
                    try:
                        opcion = int(input("Escriba 0 para salir y 1 para actualizar la fecha actual: "))
                        if not(opcion>=0 and opcion<=1):
                            print("Escriba una opcion correcta")
                        else:
                            if opcion == 0:
                                print("-----Saliendo-----")
                            else:
                                estadoFecha = False
                                while estadoFecha == False:
                                    fecha = input("Ingrese la fecha actual separada por /: ")
                                    contadorSlash = 0
                                    for letra in fecha:
                                        if letra == "/":
                                            contadorSlash +=1
                                    if contadorSlash == 2:
                                        #Comprobamos que la fecha ingresada sea mayor a la fecha actual(Solo funciona para el mismo año y mes)
                                        fechaAnterior = int((fechas[len(fechas)-1].split("/"))[0])
                                        if not(int((fecha.split("/"))[0])-fechaAnterior < 1):      
                                            estadoFecha = True
                                        else:
                                            print("Ingrese correctamente la fecha.")
                                    else:
                                        print("Ingrese correctamente la fecha.")
                                fechas.append(fecha)
                                print("Fecha actualizada correctamente")
                    except ValueError:
                        print("Escriba una opcion correcta")                        
                else:
                    #Excepcion para comprobar que solo sea el "Profesor" el qué puede levantar la sanción
                    try:
                        usuario_en_sesion.levantarSancion(fechas)
                        print("Sanción levantada con exito! ")
                    except AttributeError:
                        print("Ingrese correctamente la opción.")
                        break
            except ValueError:
                print("Ingrese correctamente la opción.")
    except IndexError:
        print("Ingrese correctamente el indice del usuario con el que desea ingresar.")
except ValueError:
    print("Ingrese correctamente el indice del usuario con el que desea ingresar.")

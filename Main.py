from Usuarios import *
from Materiales import *

usuarios = []
materiales = [[],[],[]]

#Usuarios
estudiante1 = Estudiante("Esteban","Cardona Lopez",1021301023,"esteban@gmail.com","Ingenieria Mecatronica")
profesor1 = Profesor("Pepito","Perez Hernandez",1315154,"pepito@gmail.com","Ingenieria","Ocasional","Ciencias Computacion")
usuarios.append(estudiante1)
usuarios.append(profesor1)

#Materiales
libro1 = Libro("Calculo 1","Stewart",13231,1990,"Libros y Más")
revista = Revista("Revista Cientifica Ingenieria","Newton",12395858,1700,5,2)
cd1 = Elemento_Multimedia("Llantas infinitas","Desconocido",98490,2005,"Tesis")

materiales[0].append(libro1)
materiales[1].append(revista)
materiales[2].append(cd1)

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
    #Verificamos las posibles excepciones que pueden ocurrir
    try:
    #Almacenamos el usuario en sesion dentro de la variable usuario_en_sesion
        usuario_en_sesion = usuarios[indiceAux-1]
        print(f"Bienvenido {usuario_en_sesion.getNombre()} {usuario_en_sesion.getApellidos()}.")  
        opcion = -1  
        while opcion!= 0:
            print("-----Funciones Disponibles-----")
            print("1. Hacer un prestamo")
            print("2. Hacer una devolución")
            print("3. Aplicar Sanción")
            print("4. Mostrar usuarios registrados")
            print("5. Mostrar materiales registrados")
            if(usuario_en_sesion.getTipoUsuario() == "Profesor" and usuario_en_sesion.getEstado() == False):
                print("6. Levantar sanción")
            print("0. Salir")
            #Verificamos las posibles excepciones que pueden ocurrir
            try:
                opcion = int(input("Seleccione la opción de la función que desea realizar: "))
                if not(opcion>=0 and opcion<=6):
                    print("Ingrese correctamente la opción.")
                    break
 
                if opcion == 1:
                    print("-----Materiales disponibles----- ")
                    if usuario_en_sesion.prestamo(materiales) == True:
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
                    print("-----Saliendo-----")
                else:
                    #Excepcion para comprobar que solo sea el "Profesor" el qué puede levantar la sanción
                    try:
                        usuario_en_sesion.levantarSancion()
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

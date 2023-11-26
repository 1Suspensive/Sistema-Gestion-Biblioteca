from Materiales import *

# Definicion de la superclase


class Usuario:
    # Definicion "Metodo Constructor"
    def __init__(self, nombre, apellidos, id, correo):
        self._nombre = nombre
        self._apellidos = apellidos
        self._id = id
        self._correo = correo
        self._material_prestado = []
        self._estado = True
        self._tipo_usuario = ""
        self._tipo_material = [0, 0, 0]

    # Getters
    def getNombre(self):
        return self._nombre

    def getApellidos(self):
        return self._apellidos

    def getTipoUsuario(self):
        return self._tipo_usuario

    def getEstado(self):
        return self._estado

    # Metodo para prestar material
    def prestamo(self, materiales, fechas):
        # Mostramos los materiales disponibles que puede prestar
        if self._estado == True:
            if self._tipo_usuario == "Estudiante":
                if not self._tipo_material[0] >= 5:
                    print("----Libros----")
                if not self._tipo_material[1] >= 2:
                    print("----Revistas----")
                if not self._tipo_material[2] >= 1:
                    print("----Elementos multimedia----")
                print(
                    "(Recuerde que solo puede prestar 5 Libros, 2 Revistas y 1 elemento multimedia a la vez)")
            elif self._tipo_usuario == "Egresado":
                if not self._tipo_material[0] >= 2:
                    print("----Libros----")
                if not self._tipo_material[1] >= 2:
                    print("----Revistas----")
                if not self._tipo_material[2] >= 1:
                    print("----Elementos multimedia----")
                print(
                    "(Recuerde que solo puede prestar 2 Libros, 2 Revistas y 1 elemento multimedia a la vez)")

            elif self._tipo_usuario == "Profesor":
                if not self._tipo_material[0] >= 7:
                    print("----Libros----")
                if not self._tipo_material[1] >= 3:
                    print("----Revistas----")
                if not self._tipo_material[2] >= 2:
                    print("----Elementos multimedia----")
                print(
                    "(Recuerde que solo puede prestar 7 Libros, 3 Revistas y 2 elementos multimedia a la vez)")

            else:
                if not self._tipo_material[0] >= 1:
                    print("----Libros----")
                if not self._tipo_material[1] >= 1:
                    print("----Revistas----")
                print("(Recuerde que solo puede prestar 1 Libros y 1 Revista la vez)")

            materialAux = input(
                "Escriba el tipo de material que desea prestar(0 para salir): ").lower()
            if materialAux != "0":
                try:
                    # Contador para saber cuantos materiales disponibles hay
                    contadorAux = 0
                    if materialAux == "libros" or materialAux == "libro":
                        # Mostramos los libros disponibles
                        print("Libros disponibles: ")
                        for i in range(len(materiales[0])):
                            # Comprobamos que el material este disponible para prestamo
                            if materiales[0][i].getEstado() == True:
                                print(f"{i+1}. {materiales[0][i]}")
                            else:
                                contadorAux += 1
                        if contadorAux != len(materiales[0]):
                            # Guardamos el material en la variable material
                            material = materiales[0][int(
                                input("Seleccione el indice del libro que desea prestar: "))-1]
                        else:
                            print("No hay libros disponibles para prestamo.")
                            return None
                    elif materialAux == "revistas" or materialAux == "revista":
                        # Mostramos las revistas disponibles
                        print("Revistas disponibles: ")
                        for i in range(len(materiales[1])):
                            # Comprobamos que el material este disponible para prestamo
                            if materiales[1][i].getEstado() == True:
                                print(f"{i+1}. {materiales[1][i]}")
                            else:
                                contadorAux += 1
                        if contadorAux != len(materiales[1]):
                            # Guardamos el material en la variable material
                            material = materiales[1][int(
                                input("Seleccione el indice de la revista que desea prestar: "))-1]
                        else:
                            print("No hay revistas disponibles para prestamo.")
                            return None
                    elif materialAux == "elementos multimedia" or materialAux == "elemento multimedia":
                        # Mostramos los elementos multimedia disponibles
                        print("Elementos multimedia disponibles: ")
                        for i in range(len(materiales[2])):
                            # Comprobamos que el material este disponible para prestamo
                            if materiales[2][i].getEstado() == True:
                                print(f"{i+1}. {materiales[2][i]}")
                            else:
                                contadorAux += 1
                        if contadorAux != len(materiales[2]):
                            # Guardamos el material en la variable material
                            material = materiales[2][int(
                                input("Seleccione el indice del elemento multimedia que desea prestar: "))-1]
                        else:
                            print(
                                "No hay elementos multimedia disponibles para prestamo.")
                            return None
                    return material
                except IndexError:
                    print(
                        "Escriba correctamente el indice del material que desea prestar.")
                    return None
        else:
            if self.comprobarFechaSancion(fechas) == True:
                print(
                    "Su sanción ha sido levantada, vuelva a intentar realizar el prestamo.")
            else:
                print(
                    f"El {self._tipo_usuario} no está habilitado para hacer prestamos.")
            return None

    # Metodo para comprobar si ya pasaron 10 dias necesarios para levantar la sancion(Solo funcionando para fechas del mismo mes)
    def comprobarFechaSancion(self, fechas):
        fechaActual = int((fechas[len(fechas)-1].split("/"))[0])
        fechaInicial = int((fechas[0].split("/"))[0])
        if (fechaActual - fechaInicial) >= 10:
            self._estado = True
            return True
        else:
            return False

    # Metodo para hacer la devolucion del prestamo

    def devolucion(self):
        if (len(self._material_prestado) == 0):
            print("De momento no tienes materiales prestados que puedas devolver")
        else:
            # Mostramos los materiales prestados
            i = 0
            print("Materiales Prestados:")
            for material_prestado in self._material_prestado:
                print(f"{i+1}.", end="")
                print(material_prestado)
                i += 1
            try:
                devolucion = int(
                    input("Seleccione el material que desea devolver: "))
                devolucion -= 1
                if (devolucion < 0 or devolucion >= (len(self._material_prestado)+1)):
                    print(
                        "Ingrese correctamente el indice del material que desea devolver")
                    return None
            except ValueError:
                print("Ingrese correctamente el indice del material que desea devolver")
            # Cambiamos el estado del material
            self._material_prestado[devolucion].setEstado(True)
            # Actualizamos la lista de tipo de material
            if isinstance(self._material_prestado[devolucion], Libro):
                self._tipo_material[0] -= 1
            elif isinstance(self._material_prestado[devolucion], Revista):
                self._tipo_material[1] -= 1
            elif isinstance(self._material_prestado[devolucion], Elemento_Multimedia):
                self._tipo_material[2] -= 1
            # Removemos de la lista de materiales prestados el material
            self._material_prestado.pop(devolucion)

    # Metodo para aplicar sancion

    def aplicarSancion(self):
        self._estado = False

    # Metodo __str__
    def __str__(self):
        # Añadimos los materiales prestados
        materiales = "Materiales prestados:"
        if len(self._material_prestado) == 0:
            materiales += " Ninguno"
        else:
            materiales += ", ".join(str(material)
                                    for material in self._material_prestado)

        return f"{self._nombre} - {self._apellidos} - {self._id} - {self._correo} - {materiales} - {self._tipo_usuario} - {'Habilitado para prestamos' if self._estado == True else 'Deshabilitado para prestamos'}"

# Definicion subclase Estudiante


class Estudiante(Usuario):
    # Definicion "Metodo Constructor"
    def __init__(self, nombre, apellidos, id, correo, programa):
        super().__init__(nombre, apellidos, id, correo)
        self.__programa = programa
        self._tipo_usuario = "Estudiante"

    # Metodo para prestar material

    def prestamo(self, materiales, fechas):
        material = super().prestamo(materiales, fechas)
        if material != None:
            if isinstance(material, Libro):
                # Modificamos la variable tipo material
                self._tipo_material[0] += 1
            elif isinstance(material, Revista):
                # Modificamos la variable tipo material
                self._tipo_material[1] += 1
            else:
                # Modificamos la variable tipo material
                self._tipo_material[2] += 1
            # Modificamos el estado del material para que no pueda ser prestado
            material.setEstado(False)
            # Añadimos el material a la lista de materiales prestados
            self._material_prestado.append(material)
            # Comprobamos si el Estudiante no esta habilitado para hacer más prestamos
            if (self._tipo_material[0] == 5 and self._tipo_material[1] == 2 and self._tipo_material[2] == 1):
                self._estado = False
            return True
        else:
            return False

    # Metodo __str__
    def __str__(self):
        return f" {super().__str__()} - {self.__programa}"

# Definicion subclase Egresado


class Egresado(Usuario):
    def __init__(self, nombre, apellidos, id, correo):
        super().__init__(nombre, apellidos, id, correo)
        self._tipo_usuario = "Egresado"

    # Metodo para prestar material
    def prestamo(self, materiales, fechas):
        material = super().prestamo(materiales, fechas)
        if material != None:
            if isinstance(material, Libro):
                # Modificamos la variable tipo material
                self._tipo_material[0] += 1
            elif isinstance(material, Revista):
                # Modificamos la variable tipo material
                self._tipo_material[1] += 1
            elif isinstance(material, Elemento_Multimedia):
                # Modificamos la variable tipo material
                self._tipo_material[2] += 1

            # Modificamos el estado del material para que no pueda ser prestado
            material.setEstado(False)
            # Añadimos el material a la lista de materiales prestados
            self._material_prestado.append(material)
            # Comprobamos si el Egresado no esta habilitado para hacer más prestamos
            if (self._tipo_material[0] == 2 and self._tipo_material[1] == 2 and self._tipo_material[2] == 1):
                self._estado = False
            return True
        else:
            return False
    # Metodo __str__

    def __str__(self):
        return super().__str__()

# Definicion subclase Profesor


class Profesor(Usuario):
    # Definicion "Metodo Constructor"
    def __init__(self, nombre, apellidos, id, correo, facultad, tipo_contrato, departamento):
        super().__init__(nombre, apellidos, id, correo)
        self.__facultad = facultad
        self.__tipo_contrato = tipo_contrato
        self.__departamento = departamento
        self._tipo_usuario = "Profesor"

    # Metodo para prestar material
    def prestamo(self, materiales, fechas):
        material = super().prestamo(materiales, fechas)
        if material != None:
            if isinstance(material, Libro):
                # Modificamos la variable tipo material
                self._tipo_material[0] += 1
            elif isinstance(material, Revista):
                # Modificamos la variable tipo material
                self._tipo_material[1] += 1
            elif isinstance(material, Elemento_Multimedia):
                # Modificamos la variable tipo material
                self._tipo_material[2] += 1

            # Modificamos el estado del material para que no pueda ser prestado
            material.setEstado(False)
            # Añadimos el material a la lista de materiales prestados
            self._material_prestado.append(material)
            # Comprobamos si el Profesor no esta habilitado para hacer más prestamos
            if (self._tipo_material[0] == 7 and self._tipo_material[1] == 3 and self._tipo_material[2] == 2):
                self._estado = False
            return True
        else:
            return False

    # Metodo __str__
    def __str__(self):
        return f"{super().__str__()} - {self.__facultad} - {self.__tipo_contrato} - {self.__departamento}"

    # Metodo levantar sancion solo funcionando para fechas del mismo mes
    def levantarSancion(self, fechas):
        if len(fechas) == 1:
            totalAPagar = 200
        else:
            fechaActual = int((fechas[len(fechas)-1].split("/"))[0])
            fechaInicial = int((fechas[0].split("/"))[0])
            totalAPagar = 200 * (fechaActual-fechaInicial)

        print(f"A su pago se le descontara un total de {totalAPagar}")
        self._estado = True

# Definicion clase Administrativo


class Administrativo(Usuario):
    # Definicion "Metodo Constructor"
    def __init__(self, nombre, apellidos, id, correo, dependencia):
        super().__init__(nombre, apellidos, id, correo)
        self.__dependencia = dependencia
        self._tipo_usuario = "Administrativo"

    # Metodo para prestar material
    def prestamo(self, materiales, fechas):
        material = super().prestamo(materiales, fechas)
        if material != None:
            if isinstance(material, Libro):
                # Modificamos la variable tipo material
                self._tipo_material[0] += 1
            elif isinstance(material, Revista):
                # Modificamos la variable tipo material
                self._tipo_material[1] += 1
            elif isinstance(material, Elemento_Multimedia):
                # Modificamos la variable tipo material
                self._tipo_material[2] += 1

            # Modificamos el estado del material para que no pueda ser prestado
            material.setEstado(False)
            # Añadimos el material a la lista de materiales prestados
            self._material_prestado.append(material)
            # Comprobamos si el Administrativo no esta habilitado para hacer más prestamos
            if (self._tipo_material[0] == 1 and self._tipo_material[1] == 1):
                self._estado = False
            return True
        else:
            return False

    # Metodo __str__
    def __str__(self):
        return f"{super().__str__()} - {self.__dependencia}"

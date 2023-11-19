#Definicion de la superclase
class Material:
    #Definicion "Metodo Constructor"
    def __init__(self,titulo,autor,codigo,año):
        self._titulo = titulo
        self._autor = autor
        self._codigo = codigo
        self._año = año
        self._estado = True
        self._tipo = ""
    # Definicion Getters
    def getTitulo(self):
        return self._titulo
    def getAutor(self):
        return self._autor
    def getCodigo(self):
        return self._codigo
    def getAño(self):
        return self._año
    def getEstado(self):
        return self._estado
    #Definicion setter
    def setEstado(self,estado):
        self._estado = estado
    #Difinicion metodo __str__
    def __str__(self):
        return f"{self._titulo} - {self._autor} - {self._codigo} - {self._año} - {'Disponible' if self._estado else 'Prestado'} - {self._tipo}"

#Definicion subclase Libro
class Libro(Material):
    #Definicion "Metodo Constructor"
    def __init__(self, titulo, autor, codigo, año,editorial):
        super().__init__(titulo, autor, codigo, año)
        self.__editorial = editorial
        self._tipo = "Libro"
    #Difinicion metodo __str__
    def __str__(self):
         return f" {super().__str__()} - {self.__editorial}"

#Definicion subclase Revista
class Revista(Material):
    #Definicion "Metodo Constructor"
    def __init__(self, titulo, autor, codigo, año,numero,volumen):
        super().__init__(titulo, autor, codigo, año)
        self.__numero = numero
        self.__volumen = volumen
        self._tipo = "Revista"
    #Difinicion metodo __str__
    def __str__(self):
        return f"{super().__str__()} - {self.__numero} - {self.__volumen}"

#Definicion subclase Elemento_Multimedia
class Elemento_Multimedia(Material):
    def __init__(self, titulo, autor, codigo, año,tipo):
        super().__init__(titulo, autor, codigo, año)
        self._tipo = tipo

    #Difinicion metodo __str__
    def __str__(self):
        return super().__str__()
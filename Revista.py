from MaterialBiblioteca import MaterialBiblioteca

class Revista(MaterialBiblioteca):
    def __init__(self, titulo:str, autor:str, anio:int, numero_edicion:int)-> None:
        super().__init__(titulo, autor, anio)
        self._numero_edicion = numero_edicion
    #se hizo un cambio en la forma en que se obtenian los datos en material biblioteca, ahora se usan getters
    def mostrar_info(self)-> str:
        estado = "Disponible " if self.disponible else "Prestado "
        # agregar una forma de saber el estado del libro (si esta prestado o disponible) para efectos visuales
        return f" [REVISTA] {self.titulo} - {self.autor}, Año: {self.anio}, Edición: {self._numero_edicion} | Estado: {estado}"

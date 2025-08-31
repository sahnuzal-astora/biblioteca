from MaterialBiblioteca import MaterialBiblioteca

class Periodico(MaterialBiblioteca):
    def __init__(self, titulo:str, autor:str, anio:int, fecha_publicacion:str)-> None:
        super().__init__(titulo, autor, anio)
        self._fecha_publicacion = fecha_publicacion
    #se hizo un cambio en la forma en que se obtenian los datos en material biblioteca, ahora se usan getters 
    def mostrar_info(self)-> str:
        estado = "Disponible " if self.disponible else "Prestado "
        # agregar una forma de saber el estado del libro (si esta prestado o disponible) para efectos visuales
        return f" [PERIÓDICO] {self.titulo} - {self.autor}, Año: {self.anio}, Fecha: {self._fecha_publicacion} | Estado: {estado}"
from MaterialBiblioteca import MaterialBiblioteca

class Libro(MaterialBiblioteca):
    def __init__(self, titulo:str, autor:str, anio:int, genero:str, paginas:int) -> None:
        super().__init__(titulo, autor, anio)
        self._genero = genero
        self._paginas = paginas

    #se hizo un cambio en la forma en que se obtenian los datos en material biblioteca, ahora se usan getters
    def mostrar_info(self) -> str:
        estado = "Disponible " if self.disponible else "Prestado "
        # agregar una forma de saber el estado del libro (si esta prestado o disponible) para efectos visuales
        return f" [LIBRO] {self.titulo} - {self.autor}, Año: {self.anio}, Género: {self._genero}, Páginas: {self._paginas} | Estado: {estado}"
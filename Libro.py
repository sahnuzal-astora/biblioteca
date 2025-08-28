 from material_biblioteca import MaterialBiblioteca

class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, anio, genero, paginas):
        super().__init__(titulo, autor, anio)
        self._genero = genero
        self._paginas = paginas

    def mostrar_info(self):
        return f"📖 [LIBRO] {self._titulo} - {self._autor}, {self._anio}, Género: {self._genero}, Páginas: {self._paginas}"

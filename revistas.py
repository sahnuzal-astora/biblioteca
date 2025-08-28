 from material_biblioteca import MaterialBiblioteca

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, anio, numero_edicion):
        super().__init__(titulo, autor, anio)
        self._numero_edicion = numero_edicion

    def mostrar_info(self):
        return f"📰 [REVISTA] {self._titulo} - {self._autor}, {self._anio}, Edición: {self._numero_edicion}"

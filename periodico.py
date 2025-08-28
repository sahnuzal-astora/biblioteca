  from material_biblioteca import MaterialBiblioteca

class Periodico(MaterialBiblioteca):
    def __init__(self, titulo, autor, anio, fecha_publicacion):
        super().__init__(titulo, autor, anio)
        self._fecha_publicacion = fecha_publicacion

    def mostrar_info(self):
        return f"🗞️ [PERIÓDICO] {self._titulo} - {self._autor}, Fecha: {self._fecha_publicacion}"
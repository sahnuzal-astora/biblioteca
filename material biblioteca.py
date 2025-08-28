 class MaterialBiblioteca:
    def __init__(self, titulo, autor, anio):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._disponible = True

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def is_disponible(self):
        return self._disponible

    def prestar(self):
        if self._disponible:
            self._disponible = False
            print(f"✅ '{self._titulo}' ha sido prestado.")
        else:
            print(f"❌ '{self._titulo}' no está disponible.")

    def devolver(self):
        if not self._disponible:
            self._disponible = True
            print(f"📚 '{self._titulo}' ha sido devuelto.")
        else:
            print(f"ℹ️ '{self._titulo}' ya estaba en la biblioteca.")

    def mostrar_info(self):
        return f"{self._titulo} - {self._autor} ({self._anio})"
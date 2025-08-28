#correcion el llamado a clases no compilaba debido a que no se habia importado bien con el nombre
class MaterialBiblioteca:
    def __init__(self, titulo:str, autor:str, anio:int) -> None:
        self.__titulo = titulo      # correcion de la proteccion de datos usando @property usando getters, no creo necesario el setter
        self.__autor = autor        # proteccion estricta de datos
        self.__anio = anio
        self.__disponible = True

    #  @property decorador para getters
    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def autor(self) -> str:
        return self.__autor

    @property
    def anio(self)-> int:
        return self.__anio

    @property
    def disponible(self)-> bool:
        return self.__disponible

    # --- Métodos de negocio ---
    def prestar(self)-> None:
        if self.__disponible:
            self.__disponible = False
            print(f" '{self.__titulo}' ha sido prestado.")
        else:
            print(f" '{self.__titulo}' no está disponible.")

    def devolver(self)-> None:
        if not self.__disponible:
            self.__disponible = True
            print(f" '{self.__titulo}' ha sido devuelto.")
        else:
            print(f" '{self.__titulo}' ya estaba en la biblioteca.")

    def mostrar_info(self)-> str:
        estado = "Disponible " if self._disponible else "Prestado "
        # agregar una forma de saber el estado del libro (si esta prestado o disponible) para efectos visuales
        return f"{self.__titulo} - {self.__autor} ({self.__anio}) | Estado: {estado}"
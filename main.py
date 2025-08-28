from Libro import Libro
from Revista import Revista
from Periodico import Periodico

# Lista general de materiales en la biblioteca
materiales = []

def mostrar_menu():
    print("\n=====  SISTEMA DE BIBLIOTECA =====")
    print("1. Agregar Libro")
    print("2. Agregar Revista")
    print("3. Agregar Periódico")
    print("4. Mostrar Materiales")
    print("5. Prestar Material")
    print("6. Devolver Material")
    print("7. Buscar por Autor")
    print("0. Salir")

def agregar_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = input("Año: ")
    genero = input("Género: ")
    paginas = input("Número de páginas: ")
    libro = Libro(titulo, autor, anio, genero, paginas)
    materiales.append(libro)
    print(" Libro agregado.")

def agregar_revista():
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = input("Año: ")
    edicion = input("Número de edición: ")
    revista = Revista(titulo, autor, anio, edicion)
    materiales.append(revista)
    print(" Revista agregada.")

def agregar_periodico():
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = input("Año: ")
    fecha = input("Fecha de publicación: ")
    periodico = Periodico(titulo, autor, anio, fecha)
    materiales.append(periodico)
    print(" Periódico agregado.")

def mostrar_materiales():
    if not materiales:
        print(" No hay materiales registrados.")
    else:
        for i, mat in enumerate(materiales, start=1):
            print(f"{i}. {mat.mostrar_info()}")

def prestar_material():
    mostrar_materiales()
    if materiales:
        opcion = int(input("Seleccione el número del material a prestar: "))
        if 1 <= opcion <= len(materiales):
            materiales[opcion-1].prestar()
        else:
            print(" Opción inválida.")

def devolver_material():
    mostrar_materiales()
    if materiales:
        opcion = int(input("Seleccione el número del material a devolver: "))
        if 1 <= opcion <= len(materiales):
            materiales[opcion-1].devolver()
        else:
            print(" Opción inválida.")

def buscar_por_autor():
    autor = input("Ingrese el nombre del autor: ")
    encontrados = [m for m in materiales if m.get_autor().lower() == autor.lower()]
    if encontrados:
        print(" Materiales encontrados:")
        for m in encontrados:
            print(m.mostrar_info())
    else:
        print(" No se encontraron materiales de ese autor.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            agregar_revista()
        elif opcion == "3":
            agregar_periodico()
        elif opcion == "4":
            mostrar_materiales()
        elif opcion == "5":
            prestar_material()
        elif opcion == "6":
            devolver_material()
        elif opcion == "7":
            buscar_por_autor()
        elif opcion == "0":
            print(" Saliendo del sistema...")
            break
        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    main()

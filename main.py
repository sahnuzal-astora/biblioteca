from Libro import Libro
from Revista import Revista
from Periodico import Periodico

# Lista general de materiales en la biblioteca
materiales = []

# ================= VALIDADORES =================
def pedir_entero(mensaje)-> int:
    """Solicita un entero y no permite salir hasta que lo ingrese bien"""
    valor = input(mensaje)
    while not valor.isdigit():   #  valida si la entrada son solo dígitos
        print(" Error: Debe ingresar un número entero.")
        valor = input(mensaje)
    return int(valor)

def pedir_texto(mensaje)-> str:
    """Solicita un texto no vacío"""
    valor = input(mensaje).strip()
    while not valor:  # evita que quede vacío
        print(" Error: No puede estar vacío.")
        valor = input(mensaje).strip()
    return valor

# ================= MENÚ =================
def mostrar_menu()-> None:
    print("\n=====  SISTEMA DE BIBLIOTECA =====")
    print("1. Agregar Libro")
    print("2. Agregar Revista")
    print("3. Agregar Periódico")
    print("4. Mostrar Materiales")
    print("5. Prestar Material")
    print("6. Devolver Material")
    print("7. Buscar por Autor")
    print("0. Salir")

# ================= AGREGAR =================
def agregar_libro()-> None:
    titulo = pedir_texto("Título: ")   
    autor = pedir_texto("Autor: ")     
    anio = pedir_entero("Año: ")       
    genero = pedir_texto("Género: ")   
    paginas = pedir_entero("Número de páginas: ")  
    libro = Libro(titulo, autor, anio, genero, paginas)
    materiales.append(libro)
    print("  Libro agregado.")

def agregar_revista()-> None:
    titulo = pedir_texto("Título: ")   
    autor = pedir_texto("Autor: ")    
    anio = pedir_entero("Año: ")       
    edicion = pedir_entero("Número de edición: ")  
    revista = Revista(titulo, autor, anio, edicion)
    materiales.append(revista)
    print(" Revista agregada.")

def agregar_periodico()-> None:
    titulo = pedir_texto("Título: ")   
    autor = pedir_texto("Autor: ")     
    anio = pedir_entero("Año: ")       
    fecha = pedir_texto("Fecha de publicación (dd/mm/aaaa): ")  
    periodico = Periodico(titulo, autor, anio, fecha)
    materiales.append(periodico)
    print("  Periódico agregado.")

# ================= MOSTRAR =================
def mostrar_materiales()-> None:
    if not materiales:
        print(" ⚠ No hay materiales registrados.")
    else:
        for i, mat in enumerate(materiales, start=1):
            print(f"{i}. {mat.mostrar_info()}")

# ================= OPERACIONES =================
def prestar_material()-> None:
    mostrar_materiales()
    if materiales:
        opcion = pedir_entero("Seleccione el número del material a prestar: ")  
        if 1 <= opcion <= len(materiales):
            materiales[opcion-1].prestar()
        else:
            print(" ⚠ Opción inválida.")

def devolver_material()-> None:
    mostrar_materiales()
    if materiales:
        opcion = pedir_entero("Seleccione el número del material a devolver: ")  
        if 1 <= opcion <= len(materiales):
            materiales[opcion-1].devolver()
        else:
            print(" ⚠ Opción inválida.")

def buscar_por_autor()-> None:
    autor = pedir_texto("Ingrese el nombre del autor: ")  
    encontrados = [m for m in materiales if m.autor.lower() == autor.lower()]
    if encontrados:
        print(" Materiales encontrados:")
        for m in encontrados:
            print(m.mostrar_info())
    else:
        print(" ⚠ No se encontraron materiales de ese autor.")

# ================= MAIN =================
def main()-> None:
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
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
            print("  Saliendo del sistema...")
            break
        else:
            print(" ⚠ Opción inválida.")

if __name__ == "__main__":
    main()
# Sistema de Biblioteca — README

**Proyecto:** Entrega — Sistema de gestión simple para materiales de una biblioteca (libros, revistas, periódicos).

**Descripción breve**

Aplicación de consola escrita en Python que modela materiales de una biblioteca mediante Programación Orientada a Objetos (POO). Implementa una clase base `MaterialBiblioteca` y tres subclases (`Libro`, `Revista`, `Periodico`). Incluye validadores de entrada, un menú de opciones y operaciones de negocio como prestar y devolver materiales.

---

## Tabla de contenidos

1. [Estructura de archivos](#estructura-de-archivos)
2. [Requisitos](#requisitos)
3. [Ejecución](#ejecución)
4. [Explicación detallada del código](#explicación-detallada-del-código)
   - [MaterialBiblioteca](#materialbiblioteca)
   - [Libro, Revista, Periódico](#libro-revista-periódico)
   - [Lista de materiales y el flujo principal](#lista-de-materiales-y-el-flujo-principal)
   - [Validadores y menú](#validadores-y-menú)
5. [Ejemplo de uso (sesión típica)](#ejemplo-de-uso-sesión-típica)

---

## Estructura de archivos

Se recomienda la siguiente organización mínima:

```
biblioteca/
├─ MaterialBiblioteca.py   # Clase base
├─ Libro.py                # Subclase Libro
├─ Revista.py              # Subclase Revista
├─ Periodico.py            # Subclase Periodico
└─ main.py                 # Interfaz de consola (menú y funciones)
```

> En el código de ejemplo las importaciones usan `from X import X` (p. ej. `from Libro import Libro`). Mantener ese esquema o convertirlo en un paquete con `__init__.py` según prefieras.

---

## Requisitos

- Python 3.8+ (funcionará en versiones superiores). 
- No hay dependencias externas — el programa usa solo la biblioteca estándar.

---

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

El programa muestra un menú en consola para agregar materiales, listarlos, prestar, devolver y buscar por autor.

---

## Explicación detallada del código

A continuación se detalla el propósito y comportamiento de cada parte relevante del proyecto.

### MaterialBiblioteca

- **Propósito:** Clase base que encapsula los datos comunes de cualquier material de la biblioteca: `titulo`, `autor`, `anio` y `disponible`.
- **Encapsulación:** Los atributos se definen como privados con `__` (`__titulo`, `__autor`, `__anio`, `__disponible`). Esto fuerza el acceso controlado mediante *getters* provistos con `@property`.
- **Getters:** `titulo`, `autor`, `anio`, `disponible` — devuelven los valores respectivos. Se usó `@property` para proteger los datos y evitar escritura directa.
- **Métodos de negocio:**
  - `prestar()`: Si `__disponible` es `True`, lo marca como `False` y muestra un mensaje. Si ya está prestado, informa que no está disponible.
  - `devolver()`: Si `__disponible` es `False`, lo marca como `True` y muestra un mensaje. Si ya estaba disponible, informa que ya está en la biblioteca.
  - `mostrar_info()`: Devuelve una representación textual del material con su estado.

### Libro, Revista, Periódico (subclases)

- **Herencia:** Cada subclase hereda de `MaterialBiblioteca` mediante `super().__init__(...)` y añade atributos específicos:
  - `Libro`: `_genero`, `_paginas`
  - `Revista`: `_numero_edicion`
  - `Periodico`: `_fecha_publicacion`

- **Override `mostrar_info()`**: Cada subclase redefine `mostrar_info()` para incluir sus atributos propios y un prefijo que indica el tipo (`[LIBRO]`, `[REVISTA]`, `[PERIÓDICO]`). Todas usan las propiedades públicas (`self.titulo`, `self.autor`, `self.anio`, `self.disponible`) en lugar de acceder directamente a los atributos privados.

### Lista de materiales y el flujo principal

- `materiales = []` — lista global que contiene instancias de `Libro`, `Revista` y `Periodico`.
- Operaciones sobre la lista:
  - `agregar_libro()`, `agregar_revista()`, `agregar_periodico()` — piden datos al usuario, crean la instancia correspondiente y la añaden a `materiales`.
  - `mostrar_materiales()` — recorre `materiales` e imprime `mostrar_info()` de cada elemento.
  - `prestar_material()` y `devolver_material()` — muestran la lista (para que el usuario seleccione por índice) y llaman a los métodos `prestar()`/`devolver()` sobre la instancia seleccionada.
  - `buscar_por_autor()` — recibe un texto del usuario y filtra la lista comparando `m.autor.lower() == autor.lower()`.

**Comportamiento de selección:** Cuando el usuario debe elegir un material para prestar/devolver, el programa valida que el número ingresado sea entero y esté dentro del rango de la lista.

### Validadores y menú

- `pedir_entero(mensaje)`: solicita una entrada y la valida con `str.isdigit()` para asegurarse de que sea un número entero positivo. Repite hasta que la entrada sea válida.
- `pedir_texto(mensaje)`: solicita una cadena y fuerza que no esté vacía (se llama `strip()` y se repite si queda vacía).
- `mostrar_menu()`: imprime las opciones principales del sistema.
- `main()`: ciclo infinito que muestra el menú y ejecuta las funciones según la opción elegida; se rompe con la opción `0`.

---

## Ejemplo de uso (sesión típica)

1. Ejecutar `python main.py`.
2. Seleccionar `1` para agregar un libro y responder a los prompts (`Título`, `Autor`, `Año`, `Género`, `Número de páginas`).
3. Seleccionar `4` para ver la lista — se imprimirá algo como:

```
1. [LIBRO] El Principito - Antoine de Saint-Exupéry, Año: 1943, Género: Novela, Páginas: 96 | Estado: Disponible
```

4. Seleccionar `5` (Prestar Material), ingresar `1` y el sistema mostrará:

```
 'El Principito' ha sido prestado.
```

5. Volver a `4` y verás el estado `Prestado`.

---
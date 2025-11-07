# 🌳 Gestor de Árbol Binario

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

> **Implementación educativa de árbol binario usando listas de Python**  
> Proyecto desarrollado para el curso de Matemática Discreta

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Uso Rápido](#-uso-rápido)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Funcionalidades](#-funcionalidades)
- [Ejemplos](#-ejemplos)
- [Documentación](#-documentación)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

---

## 🎯 Descripción

Este proyecto implementa un **gestor interactivo de árboles binarios** utilizando listas de Python como estructura de datos. Es una herramienta educativa diseñada para:

- 📚 Aprender conceptos de estructuras de datos
- 🔍 Visualizar árboles binarios de forma clara
- 🎓 Practicar algoritmos de recorrido (preorden, inorden, postorden)
- 🧮 Calcular propiedades de árboles (altura, peso)
- 🛠️ Manipular nodos (insertar, eliminar, buscar)

**Enfoque pedagógico:** Sin dependencias externas, código limpio y bien documentado.

---

## ✨ Características

### Operaciones Básicas
- ✅ Crear y reiniciar árbol
- ✅ Insertar nodos (hijo izquierdo/derecho)
- ✅ Eliminar nodos (con restricciones)
- ✅ Buscar nodos por valor
- ✅ Listar todos los nodos

### Visualización
- 🎨 Representación gráfica en texto (ASCII art)
- 📊 Tres tipos de recorridos
- 🔢 Cálculo de propiedades

### Interfaz
- 💻 Menú interactivo en consola
- 🌐 Soporte UTF-8 (caracteres especiales)
- ⚠️ Validación de entradas
- 📝 Mensajes descriptivos

---

## 🔧 Requisitos

### Software Necesario
- **Python 3.6 o superior**
- Sistema operativo: Windows, Linux o macOS

### Verificar Instalación
```bash
python --version
# o
python3 --version
```

**Salida esperada:** `Python 3.x.x`

---

## 📥 Instalación

### 1. Clonar/Descargar el Proyecto

**Opción A: Con Git**
```bash
git clone https://github.com/tu-usuario/arbol-binario.git
cd arbol-binario
```

**Opción B: Descarga Manual**
1. Descarga los archivos del proyecto
2. Extrae en una carpeta
3. Navega a esa carpeta en la terminal

### 2. Verificar Archivos

Asegúrate de tener estos archivos:
```
arbol-binario/
│
├── arbol_listas.py          # Estructura del árbol
├── operaciones_basicas.py   # Recorridos y operaciones
├── arbol_interactivo.py     # Programa principal
├── casos_uso.py             # Ejemplos predefinidos
└── README.md                # Este archivo
```

---

## 🚀 Uso Rápido

### Ejecutar el Programa Interactivo

**Windows:**
```bash
python arbol_interactivo.py
```

**Linux/macOS:**
```bash
python3 arbol_interactivo.py
```

### Ejecutar Demo Predefinida

Para ver un ejemplo automático:

**Windows:**
```bash
python casos_uso.py
```

**Linux/macOS:**
```bash
python3 casos_uso.py
```

---

## 📂 Estructura del Proyecto

```
arbol-binario/
│
├── 📄 arbol_listas.py
│   └── Funciones básicas de creación e inserción
│       ├── crear_nodo_raiz()
│       ├── insertar_hijo_izquierdo()
│       └── insertar_hijo_derecho()
│
├── 📄 operaciones_basicas.py
│   └── Operaciones de análisis y recorrido
│       ├── visualizar_arbol()
│       ├── recorrer_preorden()
│       ├── recorrer_inorden()
│       ├── recorrer_postorden()
│       ├── altura_arbol()
│       ├── peso_arbol()
│       ├── es_arbol_binario()
│       └── valor_existe_en_arbol()
│
├── 📄 arbol_interactivo.py
│   └── Interfaz de usuario (CLI)
│       ├── Menú principal
│       ├── buscar_nodo()
│       ├── eliminar_nodo()
│       ├── agregar_hijo_con_validacion()
│       └── main()
│
├── 📄 casos_uso.py
│   └── Ejemplos de uso
│       └── Árbol predefinido con 9 nodos
│
└── 📄 README.md
    └── Este archivo
```

---

## 🎮 Funcionalidades

### Menú Principal

```
============================================================
    GESTOR DE ARBOL BINARIO - Proyecto Matematica Discreta
============================================================

1.  Crear nodo raiz
2.  Agregar hijo izquierdo a un nodo
3.  Agregar hijo derecho a un nodo
4.  Mostrar arbol
5.  Recorrido Preorden
6.  Recorrido Inorden
7.  Recorrido Postorden
8.  Calcular altura del arbol
9.  Verificar si el arbol es binario
10. Mostrar peso del arbol (cantidad de nodos)
11. Buscar nodo
12. Eliminar nodo
13. Listar todos los nodos
0.  Salir
============================================================
```

### Descripción de Funciones

| Opción | Función | Descripción |
|--------|---------|-------------|
| 1 | Crear raíz | Reinicia el árbol con un nuevo nodo raíz |
| 2 | Hijo izquierdo | Agrega nodo a la izquierda de un padre |
| 3 | Hijo derecho | Agrega nodo a la derecha de un padre |
| 4 | Visualizar | Muestra estructura gráfica del árbol |
| 5 | Preorden | Recorre: Raíz → Izq → Der |
| 6 | Inorden | Recorre: Izq → Raíz → Der |
| 7 | Postorden | Recorre: Izq → Der → Raíz |
| 8 | Altura | Calcula profundidad máxima |
| 9 | Validar | Verifica que sea árbol binario |
| 10 | Peso | Cuenta total de nodos |
| 11 | Buscar | Encuentra nodo por valor |
| 12 | Eliminar | Remueve nodo (con restricciones) |
| 13 | Listar | Muestra todos los valores |
| 0 | Salir | Cierra el programa |

---

## 💡 Ejemplos

### Ejemplo 1: Crear un Árbol Simple

```python
# Resultado esperado:
#       A
#      / \
#     B   C

Opción: 1
Valor raíz: A

Opción: 2
Padre: A
Valor: B

Opción: 3
Padre: A
Valor: C

Opción: 4
# Salida:
A
├── C
└── B
```

### Ejemplo 2: Árbol Completo

```python
# Árbol de ejemplo (casos_uso.py):
#           A
#          / \
#         B   C
#        / \ / \
#       D  E F  G
#      / \
#     H   I

# Recorridos:
Preorden:  A B D H I E C F G
Inorden:   H D I B E A F C G
Postorden: H I D E B F G C A

# Propiedades:
Altura: 3
Peso: 9 nodos
```

### Ejemplo 3: Uso Programático

```python
from arbol_listas import crear_nodo_raiz, insertar_hijo_izquierdo
from operaciones_basicas import visualizar_arbol, recorrer_preorden

# Crear árbol
arbol = crear_nodo_raiz("Raiz")
insertar_hijo_izquierdo(arbol, "Hijo1")
insertar_hijo_derecho(arbol, "Hijo2")

# Visualizar
visualizar_arbol(arbol)

# Recorrer
recorrer_preorden(arbol)  # Salida: Raiz Hijo1 Hijo2
```

---

## 📖 Documentación

### Para Usuarios

📘 **[Manual de Usuario](MANUAL_USUARIO.md)**
- Guía completa de uso
- Ejemplos prácticos
- Preguntas frecuentes
- Solución de problemas

### Para Desarrolladores

📗 **[Documentación Interna](DOCUMENTACION_INTERNA.md)**
- Arquitectura del sistema
- Algoritmos implementados
- Complejidad computacional
- Guías de extensión

### Documentación en Código

Todas las funciones incluyen **docstrings** descriptivos:

```python
def altura_arbol(arbol: list) -> int:
    """
    Calcula la altura del árbol.
    
    La altura es el número de aristas en el camino más largo 
    desde la raíz hasta una hoja.
    
    Parámetros:
    - arbol (list): Árbol en formato [valor, izq, der]
    
    Retorno:
    - int: Altura del árbol
    """
```

---

## 🔬 Conceptos Implementados

### Estructura de Datos
- Árbol binario con listas anidadas
- Representación: `[valor, hijo_izq, hijo_der]`

### Algoritmos
- **DFS (Depth-First Search):** Recorridos y búsquedas
- **Recursión:** Base de todas las operaciones
- **Validación:** Prevención de duplicados

### Complejidad Computacional
| Operación | Complejidad |
|-----------|-------------|
| Crear nodo | O(1) |
| Insertar hijo | O(1) |
| Buscar | O(n) |
| Recorridos | O(n) |
| Altura | O(n) |
| Peso | O(n) |

---

## 🎓 Casos de Uso Educativos

### 1. Árboles de Expresión
Representar expresiones matemáticas:
```
    *
   / \
  +   2
 / \
3   5

Evaluación Postorden: 3 5 + 2 * = 16
```

### 2. Árboles Genealógicos
Representar familias:
```
   Abuelo
   /    \
Padre   Tía
 /  \
Hijo1 Hijo2
```

### 3. Sistemas de Decisión
Árboles de decisión simples:
```
    ¿Llueve?
    /      \
  Sí       No
  /          \
Paraguas   Gafas
```

---

## 🛡️ Limitaciones Conocidas

### Restricciones de Diseño
- ❌ No permite valores duplicados
- ❌ No elimina nodos con 2 hijos
- ❌ Sin persistencia (no guarda datos)
- ❌ Solo acepta strings como valores
- ⚠️ Sin sistema de deshacer



## 🚧 Mejoras Futuras

### Corto Plazo
- [ ] Guardar/cargar árboles (JSON)
- [ ] Soporte para números y tipos mixtos
- [ ] Búsqueda por nivel (BFS)
- [ ] Exportar a imagen

### Mediano Plazo
- [ ] Árbol binario de búsqueda (BST)
- [ ] Balanceo automático (AVL)
- [ ] Visualización gráfica (Tkinter)
- [ ] Sistema de historial

### Largo Plazo
- [ ] Interfaz web (Flask)
- [ ] Animaciones de recorridos
- [ ] Comparación de algoritmos
- [ ] Tests unitarios completos

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para cambios importantes:

1. **Fork** el proyecto
2. Crea una **rama** para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. **Commit** tus cambios (`git commit -m 'Agregar nueva característica'`)
4. **Push** a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un **Pull Request**

### Guías de Estilo
- Seguir **PEP 8** (Python)
- Incluir **docstrings** en funciones
- Agregar **comentarios** en código complejo
- Mantener **simplicidad** educativa

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. 

```
MIT License

Copyright (c) 2025 Proyecto Matemática Discreta

Se permite el uso, copia, modificación y distribución de este software
con fines educativos y comerciales, siempre que se incluya este aviso.
```

---

## 👥 Autores

**Proyecto Matemática Discreta**
- 🎓 Curso: Matemática Discreta
- 📅 Fecha: Noviembre 2025
- 🏫 Institución: Universidad Mariano Galvez de Guatemala
- 👥 Pamela Alvarado 7690-25-16439
- 👥 Anderson Palma
- 👥 Marlon Hernandez 7690-25-19080

---

## 🙏 Agradecimientos

- El Ing. Melvin Cali por mostrar el uso correcto de Markdown
- Estudiantes que probaron el software



---



<div align="center">

**¡Gracias por usar el Gestor de Árbol Binario!** 🌳

*Hecho con sudor, y lagrimas para estudiantes de Matemática Discreta*

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Educational](https://img.shields.io/badge/purpose-educational-blue.svg)]()

[⬆ Volver arriba](#-gestor-de-árbol-binario)

</div>

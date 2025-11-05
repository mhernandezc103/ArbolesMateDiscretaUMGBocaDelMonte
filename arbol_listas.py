def crear_nodo_raiz(valor: str) -> list:
    """
    Crea y retorna un nodo raíz con el valor proporcionado.
    Estructura: [valor, hijo_izquierdo, hijo_derecho]
    """
    return [valor, [], []]


def insertar_hijo_izquierdo(arbol: list, valor: str) -> list:
    """
    Inserta un nuevo nodo como hijo izquierdo del nodo actual.
    Si ya existe un hijo izquierdo, este pasa a ser hijo izquierdo del nuevo nodo.
    """
    if not arbol:
        print("Error: Arbol vacio")
        return
    
    subarbol_izq = arbol.pop(1)
    arbol.insert(1, [valor, subarbol_izq, []])
    return arbol


def insertar_hijo_derecho(arbol: list, valor: str) -> list:
    """
    Inserta un nuevo nodo como hijo derecho del nodo actual.
    Si ya existe un hijo derecho, este pasa a ser hijo derecho del nuevo nodo.
    """
    if not arbol:
        print("Error: Arbol vacio")
        return
    
    subarbol_der = arbol.pop(2)
    arbol.insert(2, [valor, [], subarbol_der])
    return arbol
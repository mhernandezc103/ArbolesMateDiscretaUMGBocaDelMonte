def visualizar_arbol(
    arbol: list,
    prefijo: str = "",
    es_ultimo: bool = True,
    es_raiz: bool = True,
) -> None:
    """
    Visualiza el árbol en modo texto con estructura indentada.
    No utiliza librerías externas, solo caracteres Unicode.
    """
    RAMA = "├── "
    ULTIMO = "└── "
    VERTICAL = "│   "
    ESPACIO = "    "

    if arbol:
        if es_raiz:
            print(arbol[0])
            nuevo_prefijo = ""
        else:
            print(prefijo + (ULTIMO if es_ultimo else RAMA) + str(arbol[0]))
            nuevo_prefijo = prefijo + (ESPACIO if es_ultimo else VERTICAL)

        hijo_derecho = arbol[2]
        hijo_izquierdo = arbol[1]

        hijos = []
        if hijo_derecho:
            hijos.append(hijo_derecho)
        if hijo_izquierdo:
            hijos.append(hijo_izquierdo)

        for i, hijo in enumerate(hijos):
            es_ultimo_hijo = i == len(hijos) - 1
            visualizar_arbol(hijo, nuevo_prefijo, es_ultimo_hijo, False)


def recorrer_preorden(arbol: list) -> None:
    """
    Recorrido Preorden: Raiz -> Izquierdo -> Derecho
    """
    if arbol:
        print(arbol[0], end=" ")
        recorrer_preorden(arbol[1])
        recorrer_preorden(arbol[2])


def recorrer_inorden(arbol: list) -> None:
    """
    Recorrido Inorden: Izquierdo -> Raiz -> Derecho
    """
    if arbol:
        recorrer_inorden(arbol[1])
        print(arbol[0], end=" ")
        recorrer_inorden(arbol[2])


def recorrer_postorden(arbol: list) -> None:
    """
    Recorrido Postorden: Izquierdo -> Derecho -> Raiz
    """
    if arbol:
        recorrer_postorden(arbol[1])
        recorrer_postorden(arbol[2])
        print(arbol[0], end=" ")


def altura_arbol(arbol: list) -> int:
    """
    Calcula la altura del árbol.
    La altura es el número de aristas en el camino más largo desde la raíz hasta una hoja.
    """
    if not arbol:
        return 0
    
    return 1 + max(altura_arbol(arbol[1]), altura_arbol(arbol[2]))


def peso_arbol(arbol: list) -> int:
    """
    Calcula el peso del árbol (cantidad total de nodos).
    """
    if not arbol:
        return 0
    
    return 1 + peso_arbol(arbol[1]) + peso_arbol(arbol[2])


def es_arbol_binario(arbol: list) -> tuple:
    """
    Verifica si el árbol es binario (cada nodo tiene como máximo 2 hijos).
    Retorna: (es_binario: bool, explicacion: str)
    """
    if not arbol:
        return True, "El arbol esta vacio, por lo tanto es binario."
    
    hijo_izq = arbol[1] if len(arbol) > 1 else []
    hijo_der = arbol[2] if len(arbol) > 2 else []
    
    # Verificar subárboles recursivamente
    if hijo_izq:
        es_binario_izq, razon_izq = es_arbol_binario(hijo_izq)
        if not es_binario_izq:
            return False, razon_izq
    
    if hijo_der:
        es_binario_der, razon_der = es_arbol_binario(hijo_der)
        if not es_binario_der:
            return False, razon_der
    
    total_nodos = peso_arbol(arbol)
    
    return True, (
        f"Si, el arbol es binario.\n"
        f"Razon: Cada nodo tiene como maximo 2 hijos (izquierdo y derecho).\n"
        f"Estructura: [valor, hijo_izquierdo, hijo_derecho]\n"
        f"Total de nodos: {total_nodos}"
    )


def valor_existe_en_arbol(arbol: list, valor: str) -> bool:
    """
    Verifica si un valor ya existe en el árbol.
    """
    if not arbol:
        return False
    
    if arbol[0] == valor:
        return True
    
    return valor_existe_en_arbol(arbol[1], valor) or valor_existe_en_arbol(arbol[2], valor)
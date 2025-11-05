import sys
import codecs

from arbol_listas import crear_nodo_raiz, insertar_hijo_izquierdo, insertar_hijo_derecho
from operaciones_basicas import (
    visualizar_arbol,
    recorrer_preorden,
    recorrer_inorden,
    recorrer_postorden,
    altura_arbol,
    peso_arbol,
    es_arbol_binario,
)

# Configuración UTF-8 para visualización correcta de caracteres especiales
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Crear árbol de ejemplo
arbol = crear_nodo_raiz("A")
insertar_hijo_izquierdo(arbol, "B")
insertar_hijo_derecho(arbol, "C")
insertar_hijo_izquierdo(arbol[1], "D")
insertar_hijo_derecho(arbol[1], "E")
insertar_hijo_izquierdo(arbol[2], "F")
insertar_hijo_derecho(arbol[2], "G")
insertar_hijo_izquierdo(arbol[1][1], "H")
insertar_hijo_derecho(arbol[1][1], "I")

# Visualización y recorridos
print("\n=== VISUALIZACION DEL ARBOL ===\n")
visualizar_arbol(arbol)

print("\n=== RECORRIDOS ===")
print("\nPreorden:")
recorrer_preorden(arbol)
print("\n\nInorden:")
recorrer_inorden(arbol)
print("\n\nPostorden:")
recorrer_postorden(arbol)

print("\n\n=== PROPIEDADES ===")
print(f"\nAltura del arbol: {altura_arbol(arbol)}")
print(f"Peso del arbol: {peso_arbol(arbol)}")

es_binario, explicacion = es_arbol_binario(arbol)
print(f"\n{explicacion}")

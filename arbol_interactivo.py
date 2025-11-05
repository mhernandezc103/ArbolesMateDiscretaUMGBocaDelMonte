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
    valor_existe_en_arbol,
)

# Configuración UTF-8 para caracteres especiales en la visualización
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


def buscar_nodo(arbol: list, valor: str) -> list:
    """
    Busca un nodo por su valor en el árbol.
    Retorna el nodo encontrado o None.
    """
    if not arbol:
        return None
    
    if arbol[0] == valor:
        return arbol
    
    resultado = buscar_nodo(arbol[1], valor)
    if resultado:
        return resultado
    
    return buscar_nodo(arbol[2], valor)


def listar_nodos(arbol: list, nodos: list = None) -> list:
    """
    Obtiene una lista con todos los valores de los nodos.
    """
    if nodos is None:
        nodos = []
    
    if arbol:
        nodos.append(arbol[0])
        listar_nodos(arbol[1], nodos)
        listar_nodos(arbol[2], nodos)
    
    return nodos


def eliminar_nodo(arbol: list, padre: list, valor: str, es_hijo_izq: bool) -> bool:
    """
    Elimina un nodo del árbol.
    Restricción: No elimina nodos con dos hijos por simplicidad.
    """
    if not arbol:
        return False
    
    if arbol[0] == valor:
        if arbol[1] and arbol[2]:
            print("No se puede eliminar: El nodo tiene dos hijos.")
            print("Sugerencia: Elimina primero sus hijos.")
            return False
        
        hijo_restante = arbol[1] if arbol[1] else arbol[2]
        
        if padre is None:
            if hijo_restante:
                arbol[0] = hijo_restante[0]
                arbol[1] = hijo_restante[1]
                arbol[2] = hijo_restante[2]
            else:
                print("No se puede eliminar la raiz sin hijos.")
                return False
        else:
            if es_hijo_izq:
                padre[1] = hijo_restante
            else:
                padre[2] = hijo_restante
        
        return True
    
    if eliminar_nodo(arbol[1], arbol, valor, True):
        return True
    
    return eliminar_nodo(arbol[2], arbol, valor, False)


def agregar_hijo_con_validacion(arbol: list, nodo_padre: list, valor: str, tipo: str) -> bool:
    """
    Agrega un hijo validando que el valor no exista en el árbol.
    tipo: 'izquierdo' o 'derecho'
    """
    if valor_existe_en_arbol(arbol, valor):
        print(f"Error: El dato '{valor}' ya existe en el arbol.")
        return False
    
    if tipo == "izquierdo":
        if nodo_padre[1]:
            print("Advertencia: Ya existe un hijo izquierdo. Se reemplazara.")
        insertar_hijo_izquierdo(nodo_padre, valor)
    else:
        if nodo_padre[2]:
            print("Advertencia: Ya existe un hijo derecho. Se reemplazara.")
        insertar_hijo_derecho(nodo_padre, valor)
    
    return True


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n" + "="*60)
    print("GESTOR DE ARBOL BINARIO".center(60))
    print("="*60)
    print("\n1. Crear nodo raiz")
    print("2. Agregar hijo izquierdo a un nodo")
    print("3. Agregar hijo derecho a un nodo")
    print("4. Mostrar arbol")
    print("5. Recorrido Preorden")
    print("6. Recorrido Inorden")
    print("7. Recorrido Postorden")
    print("8. Calcular altura del arbol")
    print("9. Verificar si el arbol es binario")
    print("10. Mostrar peso del arbol (cantidad de nodos)")
    print("11. Buscar nodo")
    print("12. Eliminar nodo")
    print("13. Listar todos los nodos")
    print("0. Salir")
    print("="*60)


def main():
    """Función principal del programa."""
    arbol = None
    
    print("\n--- BIENVENIDO AL GESTOR DE ARBOL BINARIO ---\n")
    
    # Crear nodo raíz
    while True:
        valor_raiz = input("Ingresa el valor del nodo raiz: ").strip()
        if valor_raiz:
            arbol = crear_nodo_raiz(valor_raiz)
            print(f"Arbol creado con raiz '{valor_raiz}'")
            break
        else:
            print("El valor no puede estar vacio.")
    
    # Menú principal
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opcion: ").strip()
        
        if opcion == "1":
            # Crear nueva raíz (reiniciar árbol)
            valor_raiz = input("\nIngresa el valor del nuevo nodo raiz: ").strip()
            if valor_raiz:
                arbol = crear_nodo_raiz(valor_raiz)
                print(f"Arbol reiniciado con raiz '{valor_raiz}'")
            else:
                print("El valor no puede estar vacio.")
        
        elif opcion == "2":
            # Agregar hijo izquierdo
            nodos = listar_nodos(arbol)
            print(f"\nNodos disponibles: {', '.join(nodos)}")
            padre = input("Nodo padre: ").strip()
            nodo_padre = buscar_nodo(arbol, padre)
            
            if nodo_padre:
                valor = input("Valor del nuevo nodo: ").strip()
                if valor:
                    if agregar_hijo_con_validacion(arbol, nodo_padre, valor, "izquierdo"):
                        print(f"Nodo '{valor}' agregado como hijo izquierdo de '{padre}'")
                else:
                    print("El valor no puede estar vacio.")
            else:
                print(f"No se encontro el nodo '{padre}'")
        
        elif opcion == "3":
            # Agregar hijo derecho
            nodos = listar_nodos(arbol)
            print(f"\nNodos disponibles: {', '.join(nodos)}")
            padre = input("Nodo padre: ").strip()
            nodo_padre = buscar_nodo(arbol, padre)
            
            if nodo_padre:
                valor = input("Valor del nuevo nodo: ").strip()
                if valor:
                    if agregar_hijo_con_validacion(arbol, nodo_padre, valor, "derecho"):
                        print(f"Nodo '{valor}' agregado como hijo derecho de '{padre}'")
                else:
                    print("El valor no puede estar vacio.")
            else:
                print(f"No se encontro el nodo '{padre}'")
        
        elif opcion == "4":
            # Visualizar árbol
            print("\n--- ESTRUCTURA DEL ARBOL ---\n")
            visualizar_arbol(arbol)
        
        elif opcion == "5":
            # Recorrido Preorden
            print("\n--- RECORRIDO PREORDEN (Raiz -> Izq -> Der) ---")
            recorrer_preorden(arbol)
            print()
        
        elif opcion == "6":
            # Recorrido Inorden
            print("\n--- RECORRIDO INORDEN (Izq -> Raiz -> Der) ---")
            recorrer_inorden(arbol)
            print()
        
        elif opcion == "7":
            # Recorrido Postorden
            print("\n--- RECORRIDO POSTORDEN (Izq -> Der -> Raiz) ---")
            recorrer_postorden(arbol)
            print()
        
        elif opcion == "8":
            # Altura del árbol
            altura = altura_arbol(arbol)
            print(f"\nAltura del arbol: {altura}")
        
        elif opcion == "9":
            # Verificar si es binario
            es_binario, explicacion = es_arbol_binario(arbol)
            print(f"\n{explicacion}")
        
        elif opcion == "10":
            # Peso del árbol
            peso = peso_arbol(arbol)
            print(f"\nPeso del arbol (total de nodos): {peso}")
        
        elif opcion == "11":
            # Buscar nodo
            valor = input("\nValor del nodo a buscar: ").strip()
            nodo = buscar_nodo(arbol, valor)
            
            if nodo:
                print(f"Nodo '{valor}' encontrado")
                tiene_izq = "Si" if nodo[1] else "No"
                tiene_der = "Si" if nodo[2] else "No"
                print(f"  Tiene hijo izquierdo: {tiene_izq}")
                print(f"  Tiene hijo derecho: {tiene_der}")
            else:
                print(f"Nodo '{valor}' no encontrado")
        
        elif opcion == "12":
            # Eliminar nodo
            nodos = listar_nodos(arbol)
            print(f"\nNodos disponibles: {', '.join(nodos)}")
            valor = input("Nodo a eliminar: ").strip()
            
            if eliminar_nodo(arbol, None, valor, False):
                print(f"Nodo '{valor}' eliminado")
            else:
                print(f"No se pudo eliminar el nodo '{valor}'")
        
        elif opcion == "13":
            # Listar todos los nodos
            nodos = listar_nodos(arbol)
            print(f"\nNodos del arbol ({len(nodos)} total): {', '.join(nodos)}")
        
        elif opcion == "0":
            # Salir
            print("\nGracias por usar el Gestor de Arbol Binario.\n")
            break
        
        else:
            print("\nOpcion no valida.")
        
        input("\nPresiona ENTER para continuar...")


if __name__ == "__main__":
    main()
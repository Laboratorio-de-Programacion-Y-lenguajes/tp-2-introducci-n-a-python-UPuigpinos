# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    """
    return sum(numeros)


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares.
    """
    return [n for n in numeros if n % 2 == 0]


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    return lista[::-1]


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    return list(dict.fromkeys(lista))


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    resultado = []
    for sublista in lista:
        for item in sublista:
            resultado.append(item)
    return resultado

def promedio(lista: list) -> float:
    """
    Retorna el promedio de la lista. 
    Si está vacía, retorna 0.0.
    """
    if not lista:
        return 0.0
    return sum(lista) / len(lista)

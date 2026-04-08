# ============================================================
# MÓDULO 6: Funciones
# ============================================================


from functools import cache


def aplicar_funcion(lista: list, func) -> list:
    """
    Aplica func a cada elemento de la lista y retorna la nueva lista.
    """
    return [func(x) for x in lista]


def componer(f, g):
    """
    Retorna una nueva función que aplica g y luego f.
    Ejemplo: componer(f, g)(x) == f(g(x))
    """
    return lambda x: f(g(x))


def memoizar(func):
    """
    Retorna una versión de func que cachea sus resultados.
    Si se llama con los mismos argumentos, retorna el resultado cacheado.
    """
    cache = {}
    def wrapper(x):
        if x not in cache:
            cache[x] = func(x)
        return cache[x]
    return wrapper

def reducir(lista: list, func, inicial):
    """
    Aplica func acumulativamente a los elementos de lista,
    comenzando con inicial.
    Ejemplo: reducir([1,2,3], lambda a,b: a+b, 0) -> 6
    NO uses functools.reduce
    """
    resultado = inicial
    for elemento in lista:
        resultado = func(resultado, elemento)
    return resultado
def contar_palabra(texto: str, palabra: str) -> int:
    """
    Cuenta cuántas veces aparece una palabra en un texto (case-insensitive).
    """
    palabras = texto.lower().split()
    return palabras.count(palabra.lower())

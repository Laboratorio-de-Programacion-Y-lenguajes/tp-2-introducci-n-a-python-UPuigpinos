# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    return limpio == limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    return texto.title()


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    vocales = "aeiouáéíóú"
    return sum(1 for letra in texto.lower() if letra in vocales)


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Determinamos si es mayúscula o minúscula para el valor ASCII base
            base = ord('A') if char.isupper() else ord('a')
            # Aplicamos la fórmula del cifrado César
            nuevo_char = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado += nuevo_char
        else:
            resultado += char
    return resultado
def operaciones(a: float, b: float) -> dict:
    """
    Realiza suma, resta, multiplicación y división.
    Maneja la división por cero con excepciones.
    """
    res = {
        "suma": a + b,
        "resta": a - b,
        "multiplicacion": a * b
    }
    try:
        res["division"] = a / b
    except ZeroDivisionError:
        res["division"] = "Error: división por cero"
    return res

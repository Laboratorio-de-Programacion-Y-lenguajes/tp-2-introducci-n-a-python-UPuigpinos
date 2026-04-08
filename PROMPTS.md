# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**:  Gemini pro

**Prompt usado**:
> Soy estudiante de ingeniería y estoy con un TP de Python. Me pasás una receta paso a paso para armar una función armar_mensaje(nombre, edad, ciudad)? Necesito que pida los datos por consola, chequee que la edad sea un entero y después me devuelva un f-string tipo: 'Soy [nombre], tengo [edad] años y vivo en [ciudad]'. Explicame los pasos

**Resultado obtenido**:
Me dio una explicación de cómo usar f-strings y cómo Python maneja los tipos de datos. Me sugirió usar type().__name__ para obtener el nombre del tipo de dato de forma limpia, que es justo lo que pedía la función tipo_de_dato.

**¿Lo usaste tal cual o lo modificaste?**
Lo usé igual, pero la función tipo_de_dato la cambie para que sea una sola línea usando __name__
---

### 2 - condicionales.py

**Herramienta**: Gemini pro

**Prompt usado**: 
> estoy haciendo un TP para la facu en Python 3.13 y necesito armar una función calificar_numero(n: int) -> str. La idea es que me diga si el número es negativo, cero, o si es positivo (diferenciando par de impar).

**Resultado obtenido**:
La IA me preguntó: 1. ¿Qué texto exacto devolver si es cero? 2. ¿Si es positivo, qué va primero, la paridad o el signo? 3. ¿Cómo manejar el caso de los negativos (si también se separan en par/impar)?


**¿Lo usaste tal cual o lo modificaste?**
lo use tal cual porque era un codigo sencillo y luego de responder lo de par o impar.

---

### 3 - listas.py

**Herramienta**: Gemini Pro

**Prompt usado**:
> Estoy haciendo un ejercicio de listas en Python para la facu. Tengo que armar funciones para sumar, sacar promedios, filtrar pares y aplanar listas de listas. ¿Podés actuar como mi verificador cognitivo? No me des el código todavía, decime qué errores típicos se suelen cometer en estos ejercicios (como los problemas con las listas vacías o modificar la original) y tirame 3 casos de prueba para ver si mi lógica está bien encaminada

**Resultado obtenido**:
La IA me advirtió sobre el ZeroDivisionError al calcular el promedio si la lista está vacía y me sugirió manejarlo con un if. También me explicó que para invertir una lista sin tocar la original lo mejor es usar slicing [::-1]. Me dio ejemplos de tests con listas de un solo elemento.

**¿Lo usaste tal cual o lo modificaste?**
lo use tal cual debido a que era un codigo sencillo, utilizando el if para abarcar los casos donde la lista esta vacia
---

### 4 - diccionarios.py

**Herramienta**: Gemini Pro

**Prompt usado**:
>  Necesito generar unos 8 ejemplos de diccionarios en Python que representen personas. Cada uno tiene que tener las claves: nombre, apellido, edad y mail. Después de los ejemplos, mostrame cómo quedarían formateados en un solo string tipo: '[nombre] [apellido] ([edad]) - [mail]'. con el objetivo de programar una función mostrar_datos(dic) que haga eso mismo con cualquier persona."

**Resultado obtenido**:
Me dio una lista larga de diccionarios de prueba y me mostró el patrón del f-string para concatenar los valores. Me explicó que lo más seguro es usar las claves directas del diccionario dentro de las llave []


**¿Lo usaste tal cual o lo modificaste?**
lo use tal cual

---

### 5 - loops.py

**Herramienta**:  Gemini Pro

**Prompt usado**:
> Necesito armar una función repetir_palabra(palabra, cantidad) en Python para un TP, pero quiero que sea sólida. Antes de darme el código, ¿podrías hacerme un par de preguntas para refinar lo que necesito? Especialmente sobre cómo manejar números negativos o qué tipo de dato devolver, así no me manda ninguna en el pytest.

**Resultado obtenido**:
La IA me preguntó: 1. ¿Qué debería devolver si la cantidad es 0 o negativa (una lista vacía o un error)? 2. ¿La palabra tiene que estar en una lista o ser un solo string largo? 3. ¿Hay algún límite de memoria que deba considerar?

**¿Lo usaste tal cual o lo modificaste?**
lo use como referencia, ya que me dio una idea y luego me recordo sobre el caso borde y sus errores

---

### 6 - funciones.py

**Herramienta**: Gemini Pro

**Prompt usado**:
> Necesito una función para contar cuántas veces aparece una palabra exacta en un texto, pero que no importe si está en mayúsculas o minúsculas. Despues de varias preguntas me dio varias opciones para usar y en base a ello decidi usar una, donde me explico las ventajas y deventajas de usar uno o el otro

**Resultado obtenido**:
Me explicó que regex es muy pesado para algo simple y que un for manual es más largo de escribir. Me recomendó .split() y .count() porque es lo más legible y eficiente en Python para este caso. También me dio una mano con la lógica de memoizar usando un diccionario como cache.

**¿Lo usaste tal cual o lo modificaste?**
Lo use como base para empezar pero sin utilizar biblotecas.

---

### 7 - operaciones.py

**Herramienta**: Gemini Pro 

**Prompt usado**:
> Necesito hacer una función operaciones(a, b) que me devuelva un diccionario con la suma, resta, multiplicación y división de dos números. Pero tengo un problema: si b es cero, la división explota. Me podés dar dos formas de resolver esto? Una usando un if común y otra usando try/except de Python.

**Resultado obtenido**:
La IA me mostró ambos enfoques. Me explicó que el if es "preventivo", pero que en Python se prefiere el try/except porque es más robusto. También me dio la lógica para el Cifrado César usando la función ord() y chr().

**¿Lo usaste tal cual o lo modificaste?**
Elegí el enfoque de try/except para la división, porque así cumplo con lo que se pide  en manejo de excepciones. Para el Cifrado César, seguí la lógica matemática que me pasó para que el desplazamiento siempre se mantenga dentro del abecedario.

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?

- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?

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

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?

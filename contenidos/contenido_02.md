**Pregunta 1: Variables y Operadores**
    
**Pregunta:** ¿Cuál es el valor final de la variable `resultado` después de ejecutar el siguiente código?

```python
a = 5
b = 2
resultado = a * b + 3
```

**Respuesta:** El valor de `resultado` será 13.

---

**Pregunta 2: Estructuras Condicionales**

**Pregunta:** Escribe un programa en Python que solicite al usuario ingresar un número y luego imprima "Es positivo" si el número es mayor que cero, y "Es negativo" si es menor que cero.

**Respuesta:**

```python
numero = float(input("Ingresa un número: "))
if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es cero")
```

---

**Pregunta 3: Listas y Ciclos**

**Pregunta:** Crea una lista con los primeros cinco números primos y luego imprime cada número elevado al cuadrado.

**Respuesta:**

```python
numeros_primos = [2, 3, 5, 7, 11]
for numero in numeros_primos:
    print(numero ** 2)
```

---

**Pregunta 4: Funciones**

**Pregunta:** Define una función llamada `es_par` que tome un número como argumento y devuelva True si es par y False si es impar.

**Respuesta:**

```python
def es_par(numero):
    return numero % 2 == 0

# Ejemplo de uso
print(es_par(4))  # Imprime True
print(es_par(7))  # Imprime False
```

---

**Pregunta 5: Manejo de Cadenas**

**Pregunta:** Dada la cadena "Python es divertido", imprime solo las palabras que tienen más de 5 letras.

**Respuesta:**

```python
frase = "Python es divertido"
palabras = frase.split()
for palabra in palabras:
    if len(palabra) > 5:
        print(palabra)
```

---

**Pregunta 6: Diccionarios**

**Pregunta:** Crea un diccionario que represente información sobre una persona (nombre, edad, ciudad) y luego imprime cada clave y su valor.

**Respuesta:**

```python
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

---

**Pregunta 7: Manejo de Archivos**

**Pregunta:** Escribe un programa que lea un archivo de texto llamado "datos.txt" y cuente la cantidad de líneas que contiene.

**Respuesta:**

```python
with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()
    cantidad_lineas = len(lineas)
    print(f"El archivo tiene {cantidad_lineas} líneas.")
```

---

**Pregunta 8: Excepciones**

**Pregunta:** Modifica el siguiente código para manejar la excepción y evitar que el programa se bloquee.

```python
numero = int(input("Ingresa un número: "))
resultado = 10 / numero
print("El resultado es:", resultado)
```

**Respuesta:**

```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Debes ingresar un número entero.")
```

---

**Pregunta 9: Programación Orientada a Objetos**

**Pregunta:** Crea una clase llamada `Rectangulo` con métodos para calcular el área y el perímetro. Crea una instancia de la clase y muestra los resultados.

**Respuesta:**

```python
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Ejemplo de uso
mi_rectangulo = Rectangulo(5, 3)
print("Área:", mi_rectangulo.calcular_area())
print("Perímetro:", mi_rectangulo.calcular_perimetro())
```

---

**Pregunta 10: Módulos y Librerías**

**Pregunta:** Importa el módulo `random` y genera un número aleatorio entre 1 y 100. Luego, pide al usuario que adivine el número y proporciona pistas si es demasiado alto o demasiado bajo.

**Respuesta:**

```python
import random

numero_secreto = random.randint(1, 100)

while True:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    if intento == numero_secreto:
        print("¡Correcto! ¡Has adivinado!")
        break
    elif intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")
```

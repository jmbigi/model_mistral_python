### Pregunta 1:

**Problema:**
Escribe un programa en Python que imprima los números del 1 al 10 en una línea.

**Respuesta:**
```python
for i in range(1, 11):
    print(i, end=' ')
```

---

### Pregunta 2:

**Problema:**
Define una función llamada `calcular_promedio` que tome una lista de números como argumento y devuelva el promedio de esos números.

**Respuesta:**
```python
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)
```

---

### Pregunta 3:

**Problema:**
Escribe una expresión lambda para calcular el cuadrado de un número.

**Respuesta:**
```python
cuadrado = lambda x: x ** 2
```

---

### Pregunta 4:

**Problema:**
Crea una clase llamada `Circulo` que tenga un método para calcular el área. El radio del círculo debe proporcionarse al crear una instancia de la clase.

**Respuesta:**
```python
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2
```

---

### Pregunta 5:

**Problema:**
Escribe una función que tome una cadena como entrada y devuelva la misma cadena pero con las palabras en orden inverso.

**Respuesta:**
```python
def invertir_palabras(cadena):
    palabras = cadena.split()
    palabras_invertidas = ' '.join(reversed(palabras))
    return palabras_invertidas
```

---

### Pregunta 6:

**Problema:**
Crea un diccionario con al menos tres claves y sus respectivos valores. Luego, imprime cada par clave-valor en una línea.

**Respuesta:**
```python
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

for clave, valor in mi_diccionario.items():
    print(f'{clave}: {valor}')
```

---

### Pregunta 7:

**Problema:**
Escribe un programa que solicite al usuario un número y determine si es par o impar.

**Respuesta:**
```python
numero = int(input('Ingrese un número: '))

if numero % 2 == 0:
    print(f'{numero} es un número par.')
else:
    print(f'{numero} es un número impar.')
```

---

### Pregunta 8:

**Problema:**
Crea una lista con los primeros 5 números primos.

**Respuesta:**
```python
numeros_primos = [2, 3, 5, 7, 11]
```

---

### Pregunta 9:

**Problema:**
Escribe una función que tome una lista de números y devuelva una nueva lista con solo los números pares.

**Respuesta:**
```python
def filtrar_pares(numeros):
    return [num for num in numeros if num % 2 == 0]
```

---

### Pregunta 10:

**Problema:**
Define una función llamada `calcular_factorial` que tome un número como argumento y devuelva su factorial.

**Respuesta:**
```python
def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_factorial(numero - 1)
```

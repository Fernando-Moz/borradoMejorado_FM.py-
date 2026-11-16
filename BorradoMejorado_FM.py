# Importamos el módulo random para generar números aleatorios
import random

# ---------------------------------------------------------------
# 1. Generamos la lista de 100 notas aleatorias entre 0 y 10
#    (una lista por comprensión es más corta y rápida que un
#    while con append)
# ---------------------------------------------------------------
notas = [random.randint(0, 10) for _ in range(100)]

# Contamos los ceros una sola vez y lo mostramos con un f-string
numCeros = notas.count(0)
print(f"En mi lista tengo {numCeros} ceros.")

# ---------------------------------------------------------------
# 2. Borrado optimizado de los ceros
#
#    Versión original: notas.remove(0) dentro de un bucle.
#    Cada remove() busca el primer 0 desde el principio y luego
#    desplaza todos los elementos siguientes una posición.
#    Si hay k ceros y n elementos, el coste es del orden de n*k.
#
#    Versión mejorada: recorremos la lista UNA sola vez y nos
#    quedamos solo con los elementos distintos de 0.
#    El coste es del orden de n.
# ---------------------------------------------------------------

# Opción A: lista por comprensión (crea una lista nueva)
notas_sin_ceros = [nota for nota in notas if nota != 0]

# Opción B: igual que A, pero modifica la MISMA lista en el sitio.
# Con notas[:] = ... se reemplaza el contenido sin crear otra variable,
# útil si otras partes del programa usan esa misma lista.
notas[:] = [nota for nota in notas if nota != 0]

# Opción C: filter() con una función lambda (equivalente a A)
# notas_sin_ceros = list(filter(lambda nota: nota != 0, notas))

# ---------------------------------------------------------------
# 3. Mostramos el resultado: cuántos elementos quedan y la lista
# ---------------------------------------------------------------
print(len(notas), notas)

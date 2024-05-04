# Definir el valor de n
import random
n = 6000

# Generar los valores para cantidad de soldados (x_i)
valores_soldados = [random.randint(1, 4000) for _ in range(n)]

# Generar los valores de fuerza (f(x_i))
valores_fuerza = list(range(1, n + 1))  # Ejemplo de función lineal

with open(str(n) + '.txt', 'w') as file:
    file.write("#" + '\n')
    file.write(str(n) + '\n')
    for i in range(n):
        file.write(str(valores_soldados[i]) + '\n')
    for i in range(n):
        file.write(str(valores_fuerza[i]) + '\n')

print("Archivo generado con éxito.")
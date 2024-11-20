# Pruebas para cada uno de los circuitos e implementación de 
import machine
import time
from machine import Pin
# Prueba para Y.

entrada_a = Pin(0, Pin.OUT)
entrada_b = Pin(1, Pin.OUT)
entrada_c = Pin(2, Pin.OUT)
entrada_d =Pin(3, Pin.OUT)


# Asignar valores
def asignar_valores(valores):
    # valores es una lista como [1, 0, 1, 0]
    entrada_a.value(valores[0])
    entrada_b.value(valores[1])
    entrada_c.value(valores[2])
    entrada_d.value(valores[3])


# Secuencia para probar
valores_prueba = [
    [0, 0, 0, 0], #0
    [0, 0, 0, 1], #1
    [0, 0, 1, 0], #2
    [0, 0, 1, 1], #3
    [0, 1, 0, 0], #4
    [0, 1, 0, 1], #5
    [0, 1, 1, 0], #6
    [0, 1, 1, 1], #7
    [1, 0, 0, 0], #8
    [1, 0, 0, 1], #9
]


while True:
    for valores in valores_prueba:
        print(f"Asignando: {valores}")
        asignar_valores(valores)
        time.sleep(3)  # Espera para observar los cambios



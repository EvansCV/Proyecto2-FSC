# Pruebas para cada uno de los circuitos e implementación de 
import machine
import time
from machine import Pin
# Prueba para Y.

entrada_a = Pin(16, Pin.OUT)
entrada_b = Pin(17, Pin.OUT)
entrada_c = Pin(15, Pin.OUT)
entrada_d =Pin(14, Pin.OUT)

entrada_a_2 = Pin(18, Pin.OUT)
entrada_b_2 = Pin(19, Pin.OUT)
entrada_c_2 = Pin(13, Pin.OUT)
entrada_d_2 =Pin(12, Pin.OUT)

entrada_a_3 = Pin(20, Pin.OUT)
entrada_b_3 = Pin(21, Pin.OUT)
entrada_c_3 = Pin(11, Pin.OUT)
entrada_d_3 =Pin(10, Pin.OUT)

# Asignar valores
def asignar_valores(valores):
    # valores es una lista como [1, 0, 1, 0]
    entrada_a.value(valores[0])
    entrada_b.value(valores[1])
    entrada_c.value(valores[2])
    entrada_d.value(valores[3])
    
    # Para asignar valores a las entradas duplicadas.
    entrada_a_2.value(valores[0])
    entrada_b_2.value(valores[1])
    entrada_c_2.value(valores[2])
    entrada_d_2.value(valores[3])
    
    entrada_a_3.value(valores[0])
    entrada_b_3.value(valores[1])
    entrada_c_3.value(valores[2])
    entrada_d_3.value(valores[3])


# Secuencia para probar
valores_prueba = [
    [0, 0, 0, 0], #0
    
]


while True:
    for valores in valores_prueba:
        print(f"Asignando: {valores}")
        asignar_valores(valores)
        time.sleep(5)  # Espera para observar los cambios'''
    
'''[0, 0, 0, 1], #1
    [0, 0, 1, 0], #2
    [0, 0, 1, 1], #3
    [0, 1, 0, 0], #4
    [0, 1, 0, 1], #5
    [0, 1, 1, 0], #6
    [0, 1, 1, 1], #7
    [1, 0, 0, 0], #8
    [1, 0, 0, 1], #9'''



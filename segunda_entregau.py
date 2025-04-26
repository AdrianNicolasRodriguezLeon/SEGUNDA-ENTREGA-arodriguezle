################### SEGUNDA ENTREGA PROGRAMACION
################### Estudiante: Adrian Nicolas Rodriguez Leon
## 1) Establezca el modelo matematico  que permita calcular el volumen del s olido anteriormente mostrado.

###### 

import math

def potencial(x,y):

    f= x**y
    print(f"Este es el resultado de la función: {f}")
    return f


def volumen_esfera(r1):

    V_esfera= math.pi * potencial(r1,3) * 4/3
    print("Este es el volumen de la esfera: ", V_esfera)
    return V_esfera

volumen_esfera(3)

def volumen_cono(r2,h):

    V_cono= math.pi * potencial(r2,2) * 1/3 * h
    print("Este es el volumen de la esfera: ", V_cono)
    return V_cono

volumen_cono(4, 7)

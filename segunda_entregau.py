################### SEGUNDA ENTREGA PROGRAMACION
################### Estudiante: Adrian Nicolas Rodriguez Leon
## 1) Establezca el modelo matematico  que permita calcular el volumen del s olido anteriormente mostrado.

###### 

import math

def potencial(x,y):

    f= x**y
    return f


def volumen_total(r1,r2,h):

    V_esfera= math.pi * potencial(r1,3) * 4/3
    print("Este es el volumen de la esfera: ", V_esfera)
    V_cono= math.pi * potencial(r2,2) * 1/3 * h
    print("Este es el volumen del cono: ", V_cono)
    VOLUMEN_TOTAL = V_esfera + V_cono
    return VOLUMEN_TOTAL

volumen_total(3,4,9/2)
print("El volumen total es: ", volumen_total(3,4,9/2))



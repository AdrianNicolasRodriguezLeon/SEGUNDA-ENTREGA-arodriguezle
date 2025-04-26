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
    V_cono= math.pi * potencial(r2,2) * 1/3 * h
    VOLUMEN_TOTAL = V_esfera + V_cono
    print("Este es el volumen de la esfera: ", V_esfera, " y este el volumen del cono: ", V_cono)
    print("Por lo tanto este es el volumen total: ", VOLUMEN_TOTAL)
    return VOLUMEN_TOTAL

volumen_total(3,4,9/2)

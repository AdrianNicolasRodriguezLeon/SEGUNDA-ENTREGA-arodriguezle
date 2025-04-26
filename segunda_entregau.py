################### SEGUNDA ENTREGA PROGRAMACION
################### Estudiante: Adrian Nicolas Rodriguez Leon
## 1) Establezca el modelo matematico  que permita calcular el solido anteriormente mostrado.

###### 
print("1. Volumen total del objeto.")
import math

def potencial(x,y):

    f= x**y
    return f

def volumen_total(r1,r2,h):

    V_esfera= math.pi * potencial(r1,3) * 4/3
    V_cono= math.pi * potencial(r2,2) * 1/3 * h
    VOLUMEN_TOTAL = V_esfera + V_cono
    print("Este es el volumen de la esfera: ", V_esfera,)
    print(" Y este el volumen del cono: ", V_cono)
    print("Por lo tanto:")
    print("Este es el volumen total: ", VOLUMEN_TOTAL)
    return VOLUMEN_TOTAL

volumen_total(3,4,9//2)


print(" ")
print(" ")
print("2. Area Lateral del Vagon.")
print(" ")
def area_total1(base, altura,radio3):

    area_rectangulo=  base* altura
    A_circulo= math.pi * potencial(radio3,2)
    AREA_VAGON = 2*A_circulo  + area_rectangulo
    print("El área del rectángulo es: ", area_rectangulo)
    print("El área de los círculos es: ", A_circulo)
    return AREA_VAGON

b=float(input("Base del rectángulo "))    
a=float(input("Altura del rectángulo "))
r3=float(input("Radio de los 2 círculos:"))
print("EN TOTAL:")
print("EL área Lateral del vagon es: ", area_total1(b,a,r3))

print(" ")
print(" ")

print("3. Area Total del Vagon2.")
print(" ")
def area_total2(a,b,r3,base2, altura2,segundo_radio):

    A_total_rectangulos= a*b + base2*altura2
    A_total_circulos= (math.pi * potencial(r3,2)*2) + (math.pi * potencial(segundo_radio,2)*2)
    AREA_CARRO = A_total_rectangulos + A_total_circulos
    print("Los rectangulos suman: ", A_total_rectangulos)
    print("Los círculos grandes suman: ", A_total_circulos)
    return AREA_CARRO
c=float(input("Base del segundo rectángulo "))
d=float(input("Altura del segundo rectángulo "))    
r4=float(input("Radio del segundo círculo:"))
print("EN TOTAL:")
print("EL área Lateral del carro es: ", area_total2(b,a,r3,c,d,r4))

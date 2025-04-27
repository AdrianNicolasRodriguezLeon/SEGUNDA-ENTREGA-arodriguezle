################### SEGUNDA ENTREGA PROGRAMACION
################### Estudiante: Adrian Nicolas Rodriguez Leon
## 1) Establezca el modelo matematico  que permita calcular el solido anteriormente mostrado.

###### 
print("1. Volumen total del objeto.")
print(" ")
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

print(" ")
print(" ")

print("4. Problemas.")
print(" ")
print("I. Cantidad de carne.")
print(" ")
def carne_total(gallina, gallos,poliitos):
    C_total= 6 * gallina + 7 * gallos + 1 * poliitos
    return C_total
N = int(input("numero de gallinas: "))
M = int(input("numero de gallos: "))
k = int(input("numero de pollitos: "))
print("la cantidad de carne de aves que hay en kg es:", carne_total(N,M,k), "kg")
print(" ")
print("II. Mandados.")
print(" ")

def Deuda(panes, bolsas_leche, huevos):
    a_pagar= 300 * panes + 3300 * bolsas_leche + 350 * huevos
    return a_pagar
P = int(input("numero de panes: "))
MB = int(input("numero de bolsas de leche: "))
H = int(input("numero de huevos: "))
print("El total a pagar es: $", Deuda(P,M,H))

B= int(input(" Billete que me dio mi mamá: $"))
vueltas= Deuda(P,M,H) - B
recibo=  B - Deuda(P,M,H)
if B >= Deuda(P,M,H):
    print("Las vueltas son: $", vueltas)
else:
    print("No alcanza, Faltan: $:", -1*recibo, "hoy no se fia, mañana si")
print(" ")

print("III. Intereses.")
print(" ")
def interes(tiempo, Vinicial, tasa):
    I_Compuesto = Vinicial * ((1 + tasa)**tiempo)
    return I_Compuesto


P1 = int(input("Capital inicial: $"))
print("El monto final a pagar es: $", interes(2, P1, 0.03)) 

print(" ")
print("IV. Contagios por covid.")
print(" ")

def contagios( dias, contagios_actuales):
    contagios_totales= contagios_actuales * (2**dias)
    return contagios_totales

Di = int(input("Dias que pasaron: "))
Co = int(input("Contagios actuales: "))
print("El total de contagios por covid es: ", contagios(Di, Co), "personas")

print(" ")
print("  FIN        ")
print("   ")
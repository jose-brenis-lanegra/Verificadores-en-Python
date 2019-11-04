#calculadora nro2
#hallar el perimetro y area de un cuadrado

#declaracion de variables
lado,perimetro_cuadrado,area_cuadrado=0.0,0.0,0.0

#calculadora
lado=13.06
perimetro_cuadrado=4*lado
area_cuadrado=lado**2

#mostrar datos
print("el lado es:", lado)
print("el perimetro del cuadrado es:", perimetro_cuadrado)
print("el area del cuadrado es:", area_cuadrado)

#verificacion
es_menor=perimetro_cuadrado<area_cuadrado
print("es menor:", es_menor)

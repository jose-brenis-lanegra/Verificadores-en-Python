#calculadora nro17
#hallar el area y el volumen de un octaedro

#declaracion de valores
arista,area_octaedro,volumen_octaedro=0.0,0.0,0.0

#calculadora
arista=6.17
area_octaedro=2*(3**(1/2))*(arista**2)
volumen_octaedro=((2**(1/2))*(arista**3))/3

#mostrar datos
print("la arista es:", arista)
print("el area del octaedro es:", area_octaedro)
print("el volumen del octaedro es:", volumen_octaedro)

#verificacion
menor_igual=area_octaedro<=volumen_octaedro
print("el area es menor al volumen", menor_igual)

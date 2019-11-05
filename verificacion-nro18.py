#calculadora nro18
#hallar el area y volumen de un dodecaedro

#declaracion de valores
arista,area_dodecaedro,volumen_dodecaedro=0.0,0.0,0.0

#calculadora
arista=9.34
area_dodecaedro=3*((25+10*(5**(1/2)))**(1/2))*(arista**2)
volumen_dodecaedro=((15+(7*(5**(1/2))))*(arista**3))/4

#mostrar datos
print("la arista es:", arista)
print("el area del dodecaedro es:", area_dodecaedro)
print("el volumen del dodecaedro es:", volumen_dodecaedro)

#verificacion
diferente=area_dodecaedro!=volumen_dodecaedro
print("el area es difernte al volumen", diferente)

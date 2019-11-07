#input
arista=float(input("ingrese la arista:"))

#porcessing
area_dodecaedro=3*((25+10*(5**(1/2)))**(1/2))*(arista**2)
volumen_dodecaedro=((15+(7*(5**(1/2))))*(arista**3))/4

#outpout
print("#################################################")
print("#hallar el area y volumen de un dodecaedro")
print("#################################################")
print("#")
print("#################################################")
print("#arista                             :", arista)
print("#area                               :", area_dodecaedro)
print("#volumen                            :", volumen_dodecaedro)
print("#################################################")

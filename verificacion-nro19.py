#calculdora nro19
#hallar el area y volumen de un icosaedro

#declaracion de valores
arista,area_icosaedro,volumen_icosaedro=0.0,0.0,0.0

#calculadora
arista=36.71
area_icosaedro=5*(3**(1/2))*(arista**2)
volumen_icosaedro=(5*(3+(5**(1/2)))*(arista**3))/12

#mostrar datos
print("la arista es:", arista)
print("el area del icosaedro es:", area_icosaedro)
print("el volumen del icosaedro es:", volumen_icosaedro)

#verificacion
mayor=arista>area_icosaedro
print("la arista es mayor al area", mayor)

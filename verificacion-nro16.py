#calculadora nro16
#hallar la altura y volumen de un tetraedro

#declaracion de valores
arista,altura,volumen_tetraedro=0.0,0.0,0.0

#calculadora
arista=4.67
altura=((6**(1/2))*arista)/3
volumen_tetraedro=((2**(1/2))*(arista**3))/12

#mostrar datos
print("el arista es:", arista)
print("la altura del tetraedro es:", altura)
print("el volumen del tetraedro es:", volumen_tetraedro)

#verificacion
mayor_igual=volumen_tetraedro>=arista
print("el volumen es mayor igual a la arista", mayor_igual)

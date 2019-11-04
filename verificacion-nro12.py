#calculadora nro12
#hallar el volumen de una esfera

#declaracion de variables
pi,radio,volumen_esfera=0.0,0.0,0.0

#calculadora
pi=3.1416
radio=9.30
volumen_esfera=(4*pi*(radio**3))/3

#mostrar datos
print("el radio de la esfera es:", radio)
print("el volumen de esta esfera es:", volumen_esfera)

#verificacion
diferente=radio!=volumen_esfera
print("el radio es diferente al volumen", diferente)

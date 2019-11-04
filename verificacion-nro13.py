#calculadora nro13
#hallar el area total del cilindro

#declaracion de variables
pi,altura,radio,area_total_cilindro=0.0,0.0,0.0,0.0

#calculadora
pi=3.1416
altura=4.94
radio=3.54
area_total_cilindro=2*pi*radio*(radio + altura)

#mostrar datos
print("la altura es:", altura)
print("el radio es:", radio)
print("el area total del cilindro es:", area_total_cilindro)

#verificacion
mayor=altura>area_total_cilindro
print("la altura es mayor al area", mayor)

#calculadora nro8
#calcular el area de un elipse

#declaraciones de variables
pi,semieje_menor,semieje_mayor,area_elipse=0.0,0.0,0.0,0.0

#calculadora
pi=3.1416
semieje_menor=45.54
semieje_mayor=61.93
area_elipse=pi*semieje_mayor*semieje_menor

#mostrar datos
print("el semieje menor es:", semieje_menor)
print("el semieje mayor es:", semieje_mayor)
print("el area del elipse es:", area_elipse)

#verificacion
menor=semieje_mayor<semieje_menor
print("el semieje mayor es menor al semieje menor", menor)

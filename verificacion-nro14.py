#calculadora nro14
#hallar el area lateral del cono

#declaracion de variables
pi,radio,altura,generatriz,area_lateral_cono=0.0,0.0,0.0,0.0,0.0

#calculadora
pi=3.1416
radio=9.45
altura=15.82
generatriz=(radio*2+altura*2)**(1/2)
area_lateral_cono=pi*radio*generatriz

#mostrar datos
print("el radio es:", radio)
print("la altura es:", altura)
print("la generatriz es:", generatriz)

#verificacion
menor=area_lateral_cono<generatriz
print("el area es menor a la generatriz", menor)

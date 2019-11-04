#calculadora nro6
#hallar el perimetro y area de un hexagono

#declaracion de variables
base_h,apotema,perimetro_hexagono,area_hexagono=0.0,0.0,0.0,0.0

#calculadora
base_h=7.53
apotema=5.69
perimetro_hexagono=6*base_h
area_hexagono=(perimetro_hexagono*apotema)/2

#mostar datos
print("la base del hexagono es:", base_h)
print("su apotema es:", apotema)
print("el prerimetro del hexagono es:", perimetro_hexagono)
print("el area del hexagono es:", area_hexagono)

#verificacion
diferente=area_hexagono!=apotema
print("el area es diferente al apotema", diferente)

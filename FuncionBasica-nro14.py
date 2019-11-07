#input
pi=float(input("ingrese el valor de pi:"))
radio=float(input("ingrese radio:"))
altura=float(input("ingrese altura:"))

#processing
generatriz=(radio*2+altura*2)**(1/2)
area_lateral_cono=pi*radio*generatriz

#outpout
print("#####################################")
print("#hallar el area lateral del cono")
print("#####################################")
print("#")
print("#####################################")
print("#radio                      :", radio)
print("#altura                     :", altura)
print("#generatriz                 :", generatriz)
print("#area_lateral_cono          :", area_lateral_cono)
print("#####################################")

from geometria import areas as ar
from geometria.perimetros import (
    perimetro_cuadrado,
    perimetro_rectangulo,
    perimetro_circulo
)

area = ar.area_cuadrado(4)
perimetro = perimetro_cuadrado(4)
circulo = perimetro_circulo(10)
rectangulo = perimetro_rectangulo(20,10)

print("AREA DEL CUADRADO : ",area)
print("PERIMETRO DEL CUADRADO : ",perimetro)
print("PERIMETRO DEL CIRCULO : ",round(circulo,2))
print("PERIMETRO DEL RECTANGULO : " ,rectangulo)
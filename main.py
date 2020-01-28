from math import sin, pi
import sys

orig_stdout = sys.stdout

diameter = float(input("Inserte el diámetro del tubo: "))
p = int(input("Inserte cantidad de pasadas: "))
A = (diameter/4) * 0.618
print("A = ",A)

f = open('out.gcode', 'w')
sys.stdout = f
print("(Codigo creado por Enrique Benitez y Guillermo Benitez)\n")
print("(Facultad Politecnica - Asuncion 2020)")
print("G90   (set absolute distance mode)")
print("G17   (set active plane to XY)")
print("G21   (set units to mm)")
print("F600  (velocidad para G01)")
print("G10 P0 L20 X0 (set Zero x e y )\n")
for j in range(1,p+1):
  for i in range(361):
    valor = A * sin((i*j*pi)/90)
    if valor == -0.0: valor = 0.0
    print("G01 X%d Y%5.3f"%(i*j,valor),sep='')
print("G4 P4")
print("F1600")
print("G01 X0 Y0")

sys.stdout = orig_stdout
f.close()
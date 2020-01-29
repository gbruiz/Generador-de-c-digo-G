from math import sin, pi
import sys

orig_stdout = sys.stdout 

diameter = float(input("Inserte el diámetro del tubo: "))
pasadas = int(input("Inserte cantidad de pasadas: "))
feed_rate = input("Inserte el feed rate(default: 600): ")
if feed_rate == '':
  feed_rate = int(600)
else:
  feed_rate = int(feed_rate)
print("Feed:",feed_rate)
A = (diameter/4) * 0.618
print("A = ",A)

#abrimos el fichero para guardar el código
nombre_archivo = "boca_de_pez_" + str(diameter) + "mm.gcode"
f = open(nombre_archivo, 'w')
sys.stdout = f

#Header
print("(Codigo creado por Enrique Benitez y Guillermo Benitez)\n")
print("(Facultad Politecnica - Asuncion 2020)")
print("G90   (set absolute distance mode)")
print("G17   (set active plane to XY)")
print("G21   (set units to mm)")
print("F%d  (velocidad para G01)"%(feed_rate),sep='')
print("G10 P0 L20 X0 (set Zero x e y )\n")

#Cuerpo del archivo
for j in range(1, pasadas+1):
  for i in range(361):
    valor = A * sin((i*j*pi)/90)
    if valor == -0.0: valor = 0.0
    print("G01 X%d Y%5.3f"%(i*j,valor),sep='')

#Final, delay y home
print("G4 P4")
print("F1600")
print("G01 X0 Y0")

sys.stdout = orig_stdout
f.close()
print("Código creado exitosamente.")
import math
import sys

orig_stdout = sys.stdout 

cut_size = float(input("Inserte el tamaño del corte: "))
pasadas = int(input("Inserte cantidad de pasadas: "))
feed_rate = input("Inserte el feed rate(default: 600): ")
if feed_rate == '':
  feed_rate = int(600)
else:
  feed_rate = int(feed_rate)
print("Feed:",feed_rate)
print("cut size: ",cut_size)

#abrimos el fichero para guardar el código
nombre_archivo = "cuadrado_" + str(cut_size) + "mm.gcode"
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

y = (cut_size/2)
#Cuerpo del archivo
for x in range(45,(360*pasadas)+45,45):    
    print("G01 Y%5.3f"%(y),sep='')
    print("G01 X%d"%(x),sep='')
    cut_size = - cut_size
    y = y + (cut_size)

#Final, delay y home
print("G4 P4")
print("F1600")
print("G01 X0 Y0")

sys.stdout = orig_stdout
f.close()
print("Código creado exitosamente.")
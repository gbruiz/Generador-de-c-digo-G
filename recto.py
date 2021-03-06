import sys

orig_stdout = sys.stdout 

print("Corte recto")
diameter = float(input("Inserte el diámetro del tubo: "))
pasadas = int(input("Inserte cantidad de pasadas: "))
feed_rate = input("Inserte el feed rate(default: 600): ")
if feed_rate == '':
  feed_rate = int(600)
else:
  feed_rate = int(feed_rate)
print("Feed:",feed_rate)
radio = (diameter/2)
print("Radio = ",radio)

#abrimos el fichero para guardar el código
nombre_archivo = "recto_" + str(diameter) + "mm.gcode"
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
print("M04") #Encender el laser
#Cuerpo del archivo
valor = 360*pasadas
if valor == -0.0: valor = 0.0
print("G01 X%d\n"%(valor),sep='')

#Final, delay y home
print("M03")
print("F1600")
print("G01 X0 Y0")

sys.stdout = orig_stdout
f.close()
print("Código creado exitosamente.")
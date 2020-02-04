(Codigo creado por Enrique Benitez y Guillermo Benitez)

(Facultad Politecnica - Asuncion 2020)
G90   (set absolute distance mode)
G17   (set active plane to XY)
G21   (set units to mm)
F600  (velocidad para G01)
G10 P0 L20 X0 (set Zero x e y )

G01 Y8.000
G01 X45
G01 Y-8.000
G01 X90
G01 Y8.000
G01 X135
G01 Y-8.000
G01 X180
G01 Y8.000
G01 X225
G01 Y-8.000
G01 X270
G01 Y8.000
G01 X315
G01 Y-8.000
G01 X360
G4 P4
F1600
G01 X0 Y0

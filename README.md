# Generador de código G
Generador de código G para distintos cortes de tubos
* Boca de pez
* Cuadrado
* Recto

Desarrollado para cortadora CNC de dos ejes, eje Y (lineal) y eje R (rotativo) 
Controlado con Arduino y GRBL0.9


Para el corte tipo boca de pez, depende del diámetro del tubo y utiliza la fórmula "y = R - sqrt( R**2 - (r*sen(x))**2))"

Para el corte cuadrado utiliza una fórmula de for anidados

Para el corte recto simplemente realiza un movimiento en el eje R

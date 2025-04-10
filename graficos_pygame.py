import pygame
import sys
import math 

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (255,255,255)
Naranja = (255,165,0)
cian = ( 0,255,255)
PI = math.pi
pygame.init()

ventana = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Dibujar formas con pygame")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

###########################
# Bucle principal del juego
###########################
while 1:
    clock.tick(50)

    # Ciclo para la deteccion de los eventos del juego
    for event in pygame.event.get():
        # Si se hace click sobre boton de cerrar de la ventana, el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    # Rellenar la ventana de color 
    ventana.fill(negro)

    # Dibujar formas con el metodo pygame.draw

    # Dibujar una linea 
    pygame.draw.line(ventana, azul,(100,100),(300,300))
    pygame.draw.line(ventana, azul,(100,300),(300,100))

    # dibujar una linea discontinua
    # True: crea un poligono
    puntos1 = [(0,0), (50,100), (100,50), (250,200), (400,400)]
    puntos2 = [(200,0),(400,200),(200,400),(0,200)]
    pygame.draw.lines(ventana, azul, True, puntos1) 
    pygame.draw.lines(ventana,rojo,True,puntos2)
    
    # Dibujar un rectangulo
    # rectangulo relleno, ubicado en la coordenada esquina superior izq (200,200),  de ancho 200 y altura 100
    pygame.draw.rect(ventana, rosado, (200,200, 200,100))

    # rectangulo sin relleno,esquina sup. izq: (100,100),esquina. inf. der: (150,200).
    pygame.draw.rect(ventana,verde,((100,100),(150,200)), 1)

    # Dibujar un poligono
    puntos3 = [(200,200), (300,325), (400,350)]
    pygame.draw.polygon(ventana, amarillo,puntos3,1)

    # dibujar un circulo
    # centro del circulo: (300,100)
    # radio del circulo: 100
    # grosor contorno circulo: 1
    pygame.draw.circle(ventana,  blanco, (300,100), 50 , 1)

    # Dibujar una elipse 
    pygame.draw.ellipse(ventana,Naranja, (100, 150, 200, 100), 1)
    # arcon de circuferencia 

    # arco de circunferencia 
    pygame.draw.arc(ventana, cian , (300, 25, 180, 150), PI/2, PI,1)

    # Actualiza la visualizacion de la ventana

    # texto
    #fuente de tipo arial, tamaño 35, negrilla y cursiva
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("Sistemas Guanenta", 1, blanco)
    ventana.blit(texto,(50,50))

    # actualiza la visualizacion de la ventana
    pygame.display.flip()
####################################
# Fin del bucle principal del juego
####################################
    
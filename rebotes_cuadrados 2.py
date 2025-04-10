import pygame
import sys
import random

rojo = (255,0,0)
azul = (0,0,255)
verde = (39, 174, 96)
morado =(108, 52, 131)
gris = (23, 32, 42 )
naranja = (214, 137, 16)

pygame.init()

ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("el cuadrado que rebota")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)
    
    XX = XX + MOVIMIENTO
    if XX >= 450:
        XX = 450
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3

    rojo1 = random.randint (0,255)
    verde1 = random.randint (0,255)
    azul1 = random.randint (0,255)
    color_aleatorio = (rojo1,verde1,azul1)
    
    

    pygame.draw.rect(ventana, verde, (XX, -4, 50 , 50))
    pygame.draw.rect(ventana, morado, (XX, 450, 50 , 50))
    pygame.draw.rect(ventana, color_aleatorio, (200, 200, 100 , 100))
    pygame.draw.rect(ventana, rojo, (0, XX, 50 , 50))
    pygame.draw.rect(ventana, naranja , (450, XX, 50 , 50))
    
    
    pygame.display.flip()    
    
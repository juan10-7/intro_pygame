

import pygame
import sys

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (225,225,225)
naranja = (255,165,0)
cian = (0, 255, 255)

pygame.init()

ancho_ventana = 500
alto_ventana = 500
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("animación de llantas")

clock = pygame.time.Clock()

rect_x = 60
rect_y = 90
rect_w = 400
rect_h = 350

rect_amarillo_y = 280
rect_amarillo_h = 150

llanta_radio = 35
llanta_velocidad = 1
llanta_y1 = rect_amarillo_y + rect_amarillo_h + llanta_radio  
llanta_y2 = rect_amarillo_y + rect_amarillo_h + llanta_radio
llanta_y3 = rect_amarillo_y + rect_amarillo_h + llanta_radio
direccion_llantas = 1

while True:
    clock.tick(30)
    ventana.fill(rosado)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("Colegio Guanenta", 1, negro)
    ventana.blit(texto, (60, 30))
    texto = fuente_arial.render("sistemas 1 ", 1, negro )
    ventana.blit(texto, (70, 70))
    texto = fuente_arial.render("juan santana", 1,negro )
    ventana.blit(texto, (70, 400))

    
    pygame.draw.rect(ventana, negro, ((rect_x, rect_y), (rect_w, rect_h)), 1)
    pygame.draw.rect(ventana, amarillo, (200, rect_amarillo_y, 200, rect_amarillo_h))
    pygame.draw.rect(ventana, naranja, (300, 200, 90,80))
    pygame.draw.rect(ventana, negro, (270, 150, 150,50))
    pygame.draw.rect(ventana, negro, (300, 130, 90,30))
    pygame.draw.rect(ventana, verde, (320, 210, 50,50))
    pygame.draw.rect(ventana, rojo, (207, 220, 55,20))
    pygame.draw.rect(ventana, negro, (215, 240, 40,40))
    pygame.draw.rect(ventana, negro, (180, 290, 20,80))
    pygame.draw.rect(ventana, cian, (150, 280, 30,100))
    pygame.draw.circle(ventana, cian, (145,330),35,70)

    
    pygame.draw.circle(ventana, negro, (390, int(llanta_y1)), llanta_radio, 70)
    pygame.draw.circle(ventana, negro, (310, int(llanta_y2)), llanta_radio, 70)
    pygame.draw.circle(ventana, negro, (230, int(llanta_y3)), llanta_radio, 70)

    
    llanta_y1 += llanta_velocidad * direccion_llantas
    llanta_y2 += llanta_velocidad * direccion_llantas
    llanta_y3 += llanta_velocidad * direccion_llantas


    borde_inferior_ventana = rect_y + rect_h
    tope_rectangulo_amarillo = rect_amarillo_y

    if llanta_y1 > borde_inferior_ventana + llanta_radio:
        direccion_llantas = -1  
    elif llanta_y1 < tope_rectangulo_amarillo + rect_amarillo_h + llanta_radio:
        direccion_llantas = 1   

    
    pygame.draw.circle(ventana, amarillo, (345, 220), 25)
    pygame.draw.circle(ventana, blanco, (340, 217), 7)
    pygame.draw.circle(ventana, blanco, (350, 217), 7)
    pygame.draw.circle(ventana, rojo, (347, 235), 7)
    pygame.draw.circle(ventana, negro, (340, 217), 4)
    pygame.draw.circle(ventana, negro, (350, 217), 4)

    pygame.display.flip()
































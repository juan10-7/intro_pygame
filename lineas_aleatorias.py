import pygame
import sys
import random

color_ventana = (0,0,0)
negro = (255,255,255)

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("lineas aleatorias")

clock = pygame.time.Clock()
while 1:
    clock.tick(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(color_ventana)
    fuente_area = pygame.font.SysFont("arial", 35, 1, 1)
    texto = fuente_area.render("Colegio  Guanenta", 1, negro)
    ventana.blit(texto, (100, 0))

    fuente_area = pygame.font.SysFont("arial", 25, 1, 1)
    texto = fuente_area.render("especialidad sistemas", 1, negro)
    ventana.blit(texto, (150, 30))

    fuente_area = pygame.font.SysFont("arial", 25, 1, 1)
    texto = fuente_area.render("Juan santana", 1, negro)
    ventana.blit(texto, (0, 475))

    pygame.draw.rect(ventana, negro, ((50, 50), (360, 350)), 1)

    for i in range(100):

        a = random.randint(50,400)
        b = random.randint(100,400)
        c = random.randint(50,400)
        d = random.randint(100,400)

        r = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        pygame.draw.line(ventana, r, (a, b), (c, d))
 
    pygame.display.flip()


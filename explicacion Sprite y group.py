import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Ejemplo de Grupo de Sprites")

# Colores
blanco = (255, 255, 255)
colores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

class Cuadrado(pygame.sprite.Sprite):
    def __init__(self, tamaño, posicion, velocidad):
        super().__init__()
        self.image = pygame.Surface([tamaño, tamaño])
        self.image.fill(random.choice(colores))
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.velocidad = velocidad

    def update(self):
        self.rect.x += self.velocidad[0]
        self.rect.y += self.velocidad[1]

        # Hacer que los cuadrados reboten en los bordes
        if self.rect.left < 0 or self.rect.right > ancho_pantalla:
            self.velocidad = (-self.velocidad[0], self.velocidad[1])
        if self.rect.top < 0 or self.rect.bottom > alto_pantalla:
            self.velocidad = (self.velocidad[0], -self.velocidad[1])

# Crear un grupo para todos los cuadrados
todos_los_sprites = pygame.sprite.Group()

# Crear varios cuadrados y añadirlos al grupo
for _ in range(10):
    tamaño = random.randint(20, 50)
    x = random.randint(0, ancho_pantalla - tamaño)
    y = random.randint(0, alto_pantalla - tamaño)
    velocidad_x = random.randint(1, 5) * random.choice([-1, 1])
    velocidad_y = random.randint(1, 5) * random.choice([-1, 1])
    cuadrado = Cuadrado(tamaño, (x, y), (velocidad_x, velocidad_y))
    todos_los_sprites.add(cuadrado)

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(blanco)

    # Actualizar la posición de todos los sprites en el grupo
    todos_los_sprites.update()

    # Dibujar todos los sprites del grupo en la pantalla
    todos_los_sprites.draw(pantalla)

    pygame.display.flip()

pygame.quit()

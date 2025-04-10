# estructura de un juego en pygame

## inicializacion

- como en todo programa en python, se debe importar los modulos o librerias a utilizar
`import pygame`

-inicilizar pygame usando al funcion init(). inicializa todos los modulos de pygame importados.
`pygame.init()`

## visualizacion de l ventana

`ventana = pygame.display.set_mode((6OO,400))`
- set mode() es la fucion encargada de definir el tamaño de la ventana. En elejemplo, se esta definiendo una ventana de 600 px de ancho, por 400 px de alto.

'pygame display.set_caption( 'mi ventana' )'
- set_caption() es la funcion que añade un titulo a la ventana.

### funcion set_mode()

`set_mode(size =(0,0), flags = 0 , display=0)`

- size = (600,400) : define el tamaño de la ventana.

   - valores:
      - pygame.FULLSCREEN
      - pygame.RESISTABLE
   - ejemplo
     - flag = pygame.FULLSCREEN | pygame.RESISTABLE : pantalla completa, dimensiones modificables

## bucle de juego o game loop
- bucle infinito que se interrumpe al cumplir cciertos criterios.

- reloj interno

- en cada iteracion de bucle del juego podemos mover un personaje, o tener en cuenta que un objeto a alcanzado a otro,o que se han cruzado la linea de llegada quiere decir que a partida ha terminado

- cada iteracion es una oportunidad para actualizar todos los datos relacionados con el estado actual dela partida

- en cada iteracion se realizan ls siguentes tareas:
    1. comprobar que no se alcanzan las condicones de parada, en cuyo caso se interrumpe el bucle.
    2. actualizar los recursos necesarios para la iteracion actual
    3. obtener las entradas de sistemas, o de interaccion del jugador
    4. actualizar todas las identidades que caracterizan el  juego
    5. refrescar la pantalla.

## superficies pygame 
- superficie: 
    - elemento geometrico
    - linea, poligono, imagen, texto que se muestra en la pantalla 
    - el poligono se puede o no rellenar de color 
    - las superficies se cean de diferente manera dependiendo del tipo:
        - image: image.load()
        - texto: font.render()
        - suoerficie generica: pygame.surface()
        - ventana de juego: pygame.display.set_mode()



         ejemplo de la bandera de colombia

```

# importamos la libreria pygames

import pygame


# inicializamos los modulos de pygame 

pygame.init()

# establecer titulo a la ventana 
pygame.display.set_caption("Surface")

# establecemos las dimensiones de la ventana 
ventana = pygame.display.set_mode((400,400))

# definimos un color 

amarillo= (255,255,0)

azul = (0,0,250)

rojo = (255,0,0)



# crear una superficie 

amarillo_Superficie = pygame.Surface((400,200))

azul_Superficie = pygame.Surface((400,100))

rojo_Superficie = pygame.Surface((400,100))


# rellenamos la superficie del color
amarillo_Superficie.fill(amarillo)
azul_Superficie.fill(azul)
rojo_Superficie.fill(rojo)


# inserto o muevo la ventana  la superficie en la ventana
ventana.blit(amarillo_Superficie, (0,0))
ventana.blit(azul_Superficie, (0,200))
ventana.blit(rojo_Superficie, (0,300))



# actualiza la visualizacion de la ventana 
pygame.display.flip()
# bucle del juego
while True: 
    event = pygame.event.wait()
    if event == pygame.QUIT: 
        break 

pygame.quit() 

```

![bandera](screen.jpg)


## gestion de tiempo y los eventos

### modulo time

- este modulo ofrece varias funciones que permiten cronometrar la sesion actual (desde el init) o pausar, la ejecucion,por ejemplo:
- funciones:
     - pygame.time.get_ticks
     - pygame.time.waitpygame.time.delay

- Objeto clock
    - la funcion tick permite actulizar el  reloj asociado con el juego actual.
    - se llama cada vez que se actualiza la pantalla del juego.
    - permite especificar el numero maximo de fotogramas que se muestran por segundo,y por lo tanto,limitar y controlar la velocidad de ejecucion del juego.
    - si insertamos en un bucle de juego la siguiente linea, garantizamos que nunca se ira mas rapido de 50 fotogramas por segundo: `Clock.tick(50)`

### gestion de eventos
- hay diferentes formas para que el programa sepa que se ha desencadenado un evento.
- es esencial que los programas puedan conocer inmediatamente las acciones del jugador a traves del teclado, el mouse, el joystick o cualquier otro periferico.

#### funcion pygame.event.get
- permite obtener todos los eventos en espera de ser procesados y que estan disponibles en una cola.
- si no hay niguno entonces se obtiene una coleccion vacia.
```Python
# usamos un bucle for para recorre todos los eventos de la collecion obtenida al llamar la funcion get.
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            PARAR_JUEGO = True
```
### funcion pyygame.event.wait
- esta funcion espera que ocurra un evento, y en cuanto sucede esta disponible.

```Python
while True
    event = pygame.event.wait()
    if event == pygame.QUIT: 
        break
```

### funcion pygame.event.poll

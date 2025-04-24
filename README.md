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
- devuelve solo uno de los eventos que estan en la cola de espera


## sonidos en pygame
- pygame.mixer: modulo que permite la gestion de sonido

- music: submodulo que gestiona la musica de fondo. necesariamente solo hay uno a la vez

- Sound: objeto de mixer, que se puede instanciar varias veces para usarlo en los efectos del sonido del juego.

### Archivo de sonido
- se recomienda usar dos formatos,principalmente:
    - formato WAV (Waveform audio file Format)
    - formato bierto y grtuito OGG


### chnne (canal) en pygame
- un juego tiene varios canales de sonido.
- se puede asignar un solo sonido al canal numero 1 y otro diferente al numero 2.
- entonces es posible

## sprites
- objeto u soci un ubiccion, un representacion grafica (esta o aquella imagen, por ejemplo) y un conjunto de propiedades.
- estas propiedades pueden ser un nombre, un texto, valores booleanos que caracterizan el objeto en cuestion (por ejemplo si el objeto se puede mover o no)
- una posible traduccion del termino sprite podria ser "imagen-objeto" que se actualiza con cada iteracion del bucle del juego.
- cuando mas complejo es el juego,mas objetos graficos tiene que gestionar y actualizar lo que puede ser tedioso.
- pygame usa no solo la nocon de sprite, sino la nocion de grupo de sprites (group)
- la nocion de grupo permite agrupar los objetos del mismo tipo. ejemplo : todos los soldados de un ejercito lo que se entiende como una colceccion de instancias de una clase Soldado 

- un determindado proceso se puede aplicaar a un conjunto o subconjunto de sprites. Ejemplo: cambiar el color de todos los enemigos o hacer invisibles algunos objetos

 ### Sprite explicacion
 ¿Qué es la clase Sprite?

En esencia, la clase Sprite es una clase base diseñada para contener la información gráfica y la posición de un objeto en tu juego. Al heredar de esta clase, puedes dotar a tus objetos de funcionalidades integradas para la gestión de imágenes, rectángulos de colisión y pertenencia a grupos.

## ventajas del Sprite

- Organización: Encapsula la información gráfica y la posición de un objeto en un solo lugar, facilitando la gestión del código.

Gestión de Rectángulos: El atributo rect simplifica el manejo de la posición y las colisiones. Pygame proporciona métodos eficientes para trabajar con rectángulos.

Integración con Grupos de Sprites: La clase Sprite está diseñada para funcionar perfectamente con la clase pygame.sprite.Group. Los grupos permiten gestionar múltiples sprites de manera eficiente (dibujarlos todos a la vez, verificar colisiones entre grupos, etc.).

## el group
es lo que utilizamos para agrupar los Sprite





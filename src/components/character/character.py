from src.config import (SCREEN_WIDTH, SCREEN_HEIGHT,
                        PLAYER_WIDTH, PLAYER_HEIGHT,
                        GRAVITY, JUMP_STRENGHT,
                        STANDARD_X)
from src.scenes.sound import (jump_sound)
import pygame
from src.components.obstacle.obstacle import Obstacle
from typing import Union


# Clase del Jugador
class Player(pygame.sprite.Sprite):
    def __init__(self, color, keys):
        super().__init__()

        # Tamaño Jugador
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(color)  # Color Jugador
        self.rect = self.image.get_rect()  # Mostrar
        # Renderizar en la mitad de la pantalla
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Fisica
        self.vel_y = 0  # Velocidad vertical por defecto
        self.vel_x = 0  # Velocidad horizontal por defecto
        self.gravity = GRAVITY  # Valor de la gravedad
        self.jump_strength = JUMP_STRENGHT  # Potencia del salto
        self.jump_available = True  # ¿Esta permitido el salto?

        # Colisiones

        # Controles personalizados
        self.keys = keys

    def update(self, all_sprites: list[Union['Obstacle', 'Player']] = []):
        self.vel_x = 0
        keys = pygame.key.get_pressed()  # Saber que tecla se presiono
        if keys[self.keys['left']]:
            self.vel_x = -STANDARD_X  # Moverse 5 pixeles a la Izquierda
        if keys[self.keys['right']]:
            self.vel_x = STANDARD_X  # Moverse 5 pixeles a la derecha
        if keys[self.keys['jump']] and self.jump_available:
            self.jump()  # Funcion

        # Movimiento en x
        self.rect.x += self.vel_x

        # Aplicar gravedad
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Limitar con la pantalla
        self.bordes()

        # Posibles choques
        self.choque(all_sprites)

    def bordes(self):
        # Limitar al suelo
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0
            self.jump_available = True
        # Limitar el borde izquierdo
        if self.rect.left < 0:
            self.rect.left = 0
        # Limitar el borde derecho
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def choque(self, sprites: list[Union['Obstacle', 'Player']] = []):

        # Funcion para verificar que un spite character no este tocando a otro.
        def inside(fun_izq: callable, fun_der: callable):
            # Borde dereccho dentro
            # Direccion Izq -> Der
            if (self.rect.right > sprite.rect.left and
                    self.rect.right < sprite.rect.right):
                # Realiza Funcion der
                fun_der()
            # Borde izquiero dentro
            # Direccion Der -> Izq
            elif (self.rect.left < sprite.rect.right and
                    self.rect.left > sprite.rect.left):
                # Realiza funcion izq
                fun_izq()

        # Detectar colisión
        for sprite in sprites:
            # Evitar colisionar consigo mismo
            if sprite == self:
                continue

            # Verifica la colisión con cualquier sprite
            if self.rect.colliderect(sprite.rect):

                # ✅ Colisión con el mismo tipo
                # Permite empuje a menos que tambien lo esten empujando
                if isinstance(sprite, type(self)):
                    # Empuje lateral
                    # Verifica igualdad de altura
                    if (self.rect.centery == sprite.rect.centery):
                        # Yo me muevo pero el otro esta quieto
                        if (self.vel_x != 0 and
                                sprite.vel_x == 0):
                            # LLamada funcion
                            inside(
                                # Setear el atributo
                                # Right -> Left del que se mueve
                                lambda: setattr(sprite.rect,
                                                'right',
                                                self.rect.left),
                                # Setear el atributo
                                # Left -> Right del que se mueve
                                lambda: setattr(sprite.rect,
                                                'left',
                                                self.rect.right)
                            )
                        # Nos movemos en direcciones opuestas
                        # Misma velocidad
                        elif (self.vel_x == -sprite.vel_x):
                            # NINGUNO SE DEBERIA MOVER
                            # HACEMOS IGUAL FUERZA EN LADOS OPUESTOS
                            inside(
                                lambda: setattr(self.rect,
                                                'x',
                                                self.rect.x + STANDARD_X),
                                lambda: setattr(self.rect,
                                                'x',
                                                self.rect.x - STANDARD_X)
                            )

                # ✅ Si cae encima, se queda parado
                if (self.vel_y > 0 and
                        self.rect.bottom >= sprite.rect.top):
                    # fijar la parte de abajo como la parte de arriba del otro
                    self.rect.bottom = sprite.rect.top
                    # Sin velocidad de caida
                    self.vel_y = 0
                    # Establecer que se puede saltar
                    self.jump_available = True

                # 🚫 Colisión con otro tipo de sprite - bloquea el movimiento
                if not isinstance(sprite, type(self)):
                    if (self.rect.bottom != sprite.rect.top):
                        # Bloquea hacia la derecha o
                        # izquierda según la posición
                        inside(
                            lambda: setattr(self.rect,
                                            'left',
                                            sprite.rect.right),
                            lambda: setattr(self.rect,
                                            'right',
                                            sprite.rect.left)
                        )

    def jump(self):
        self.vel_y = self.jump_strength
        jump_sound.play()
        self.jump_available = False


list_players = [
    Player(color=(0, 255, 0),
           keys={'left': pygame.K_a,
                 'right': pygame.K_d,
                 'jump': pygame.K_w}),
    Player(color=(0, 0, 255),
           keys={'left': pygame.K_LEFT,
                 'right': pygame.K_RIGHT,
                 'jump': pygame.K_UP})
]

players = pygame.sprite.Group()
for player in list_players:
    players.add(player)

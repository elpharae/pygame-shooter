import pygame
import numpy 
import math
from typing import Tuple 

pygame.init()

width, height = 640, 400 
flags = None # pygame.FULLSCREEN
screen = pygame.display.set_mode((width, height))
running = True
fps = 60
clock = pygame.time.Clock()

player_speed = 4 
player_size = 50

class Entity:

    def __init__(self, image_path: str, x: int, y: int):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (player_size, player_size))
        self.x = x
        self.y = y

    def move(self, direction: Tuple[int, int]):
        dir_length = math.sqrt(math.pow(direction[0], 2) + math.pow(direction[1], 2))
        if dir_length != 0:
            direction = (direction[0] / dir_length * player_speed, direction[1] / dir_length * player_speed)

        if not (player.x + direction[0] < 0 or player.x + direction[0] > width - player_size):
            self.x += direction[0]
        if not (player.y + direction[1] < 0 or player.y + direction[1] > height - player_size):
            self.y += direction[1]

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

player = Entity("./assets/player.png", width // 2, height // 2) 

while running:

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    # render
    screen.fill("white")
    player.draw(screen)

    # player input 
    player_dir: Tuple[float, float] = (0, 0)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        player_dir = (-1, player_dir[1])
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        player_dir = (1, player_dir[1])
    if key[pygame.K_UP] or key[pygame.K_w]:
        player_dir = (player_dir[0], -1)
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        player_dir = (player_dir[0], 1)
    player.move(player_dir)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()

        


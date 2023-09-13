import pygame
from config import (
    width, height, fps, vsync, flags
)
import numpy 
import math
from abc import ABC, abstractmethod 
from typing import Tuple 
from entities import (
    Player
)

pygame.init()

screen = pygame.display.set_mode((width, height))
running = True
clock = pygame.time.Clock()

player_speed = 4 
player_size = 50
player_start_x = width // 2
player_start_y = height - 100
player_hp = 100

player = Player("./assets/player.png", player_start_x, player_start_y, player_size, player_hp, player_speed) 

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    # render
    screen.fill("white")
    player.draw(screen)

    # player input and movement
    player_dir = (0, 0)
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

        


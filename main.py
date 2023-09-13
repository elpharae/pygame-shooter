import pygame
from config import (
    width, height, fps, vsync, flags
)
import numpy 
import math
from abc import ABC, abstractmethod 
from typing import Tuple 
from entities import (
    Player, Bullet
)

pygame.init()

screen = pygame.display.set_mode((width, height))
running = True
clock = pygame.time.Clock()

player_speed = 7
player_size = 40
player_start_x = width // 2
player_start_y = height - 100
player_hp = 100
player_shoot_delay = 20 
player_shoot_cooldown = 0 
player = Player("./assets/player.png", player_start_x, player_start_y, player_size, player_hp, player_speed) 

player_bullet_pool_count = 10
player_bullet_damage = 40
player_bullet_size = 10
player_bullet_speed = 10
player_bullet_pool = []

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    # render objects
    current_bullets: list = [bullet for bullet in player_bullet_pool if bullet.enabled]
    screen.fill("white") # redraw surface
    player.draw(screen)
    [bullet.draw(screen) for bullet in current_bullets]
    print(len(current_bullets))

    # player input 
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

    # bullet pool
    if key[pygame.K_SPACE] and player_shoot_cooldown <= 0:
        player_shoot_cooldown = player_shoot_delay
        if len(player_bullet_pool) < player_bullet_pool_count:
            bullet = Bullet("./assets/bullet.png", player.x + player_size // 2 - player_bullet_size // 2, player.y, player_bullet_size, player_bullet_damage, player_bullet_speed)
            player_bullet_pool.append(bullet)
        else:
            bullet: Bullet = player_bullet_pool.pop(0)
            bullet.enabled = True
            bullet.x = player.x + player_size // 2 - player_bullet_size // 2
            bullet.y = player.y
            player_bullet_pool.append(bullet)
    player_shoot_cooldown -= 1

    # move objects
    [bullet.check_oob() for bullet in current_bullets]
    [bullet.move(-1) for bullet in current_bullets]
    player.move(player_dir)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()

        


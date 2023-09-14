import pygame
from config import (
    width, height, vsync, flags
)
import numpy 
import math
from abc import ABC, abstractmethod 
from typing import Tuple 
from entities import (
    Player, Bullet
)
import time

pygame.init()

screen = pygame.display.set_mode((width, height))
running = True
clock = pygame.time.Clock()

player_speed = 350 
player_size = 40
player_start_x = width // 2
player_start_y = height - 100
player_hp = 100
player_last_shot = 0
player = Player("./assets/player.png", player_start_x, player_start_y, player_size, player_hp, player_speed) 

player_bullet_pool_count = 10
player_bullet_damage = 40
player_bullet_size = 10
player_bullet_speed = 500 
player_bullet_pool = []

previous_time = time.time()
while running:
    # delta time
    dt = time.time() - previous_time
    previous_time = time.time()

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    # debug text
    font = pygame.font.Font(pygame.font.get_default_font(), 18)
    current_time = font.render(str(time.time()), True, (0, 0, 0), (255, 255, 255))
    current_time_rect = current_time.get_rect()
    current_time_rect.left = 0
    current_time_rect.bottom = height
    last_shot = font.render(str(player_last_shot), True, (0, 0, 0), (255, 255, 255))
    last_shot_rect = current_time.get_rect()
    last_shot_rect.left = 0
    last_shot_rect.bottom = height - 20


    # render objects
    current_bullets: list = [bullet for bullet in player_bullet_pool if bullet.enabled]
    screen.fill("white") # redraw surface
    player.draw(screen)
    [bullet.draw(screen) for bullet in current_bullets]

    # text render
    screen.blit(current_time, current_time_rect)
    screen.blit(last_shot, last_shot_rect)

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
    if key[pygame.K_SPACE] and time.time() - player_last_shot > 0.2:
        if len(player_bullet_pool) < player_bullet_pool_count:
            bullet = Bullet("./assets/bullet.png", player.x + player_size // 2 - player_bullet_size // 2, player.y, player_bullet_size, player_bullet_damage, player_bullet_speed)
            player_bullet_pool.append(bullet)
        else:
            bullet: Bullet = player_bullet_pool.pop(0)
            bullet.enabled = True
            bullet.x = player.x + player_size // 2 - player_bullet_size // 2
            bullet.y = player.y
            player_bullet_pool.append(bullet)
        player_last_shot = time.time()

    # move objects
    [bullet.check_oob() for bullet in current_bullets]
    [bullet.move(-1, dt) for bullet in current_bullets]
    player.move(player_dir, dt)

    pygame.display.update()
    clock.tick(60)

pygame.quit()

        


import pygame
from abc import ABC, abstractmethod
from typing import Tuple
import math
import numpy
from config import (
    width, height
)

class Entity(ABC):

    def __init__(self, image_path: str, x: float, y: float, image_size: int):
        self.image_size = image_size
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (image_size, image_size))

    @abstractmethod
    def move(self, direction: Tuple[float, float], dt: float):
        pass

    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass

class Player(Entity):

    def __init__(self, image_path: str, x: float, y: float, image_size: int, hp: float, speed: float):
        super().__init__(image_path, x, y, image_size)
        self.hp = hp
        self.speed = speed
    
    def move(self, direction: Tuple[float, float], dt: float):
        dir_length = math.sqrt(math.pow(direction[0], 2) + math.pow(direction[1], 2))
        if dir_length != 0:
            direction = (direction[0] / dir_length * self.speed * dt, direction[1] / dir_length * self.speed * dt)

        if not (self.x + direction[0] < 0 or self.x + direction[0] > width - self.image_size):
            self.x += direction[0]
        if not (self.y + direction[1] < 0 or self.y + direction[1] > height - self.image_size):
            self.y += direction[1]

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

class Bullet(Entity):
    
    def __init__(self, image_path: str, x: float, y: float, image_size: int, damage: float, speed: float):
        super().__init__(image_path, x, y, image_size)
        self.damage = damage
        self.speed = speed
        self.enabled = True
    
    def move(self, direction: float, dt: float):
        self.y += round(direction * self.speed * dt)
        
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

    def check_oob(self):
        if self.x > width or self.x < 0 or self.y > height or self.y < 0:
            self.enabled = False
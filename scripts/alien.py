import os
import sys

import pygame


from pygame.sprite import Sprite
from pathlib import *


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        img_path = resource_path("images/alien.png")
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(
            self.image, (ai_game.screen.get_width() / 15, ai_game.screen.get_height() / 15))
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

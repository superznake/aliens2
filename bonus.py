import pathlib
import random

import pygame
from pygame.sprite import Sprite


class Bonus(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.rect = pygame.Rect(
            0, 0, ai_game.screen.get_height() / 40, ai_game.screen.get_height() / 40)

        self.y = float(self.rect.y)

        # 0 - +1 life; 1 - +1 max ammo; 2 - +1 bullet width; 3 - +0.5 ship speed
        self.type = random.randint(0, 3)

        match self.type:
            case 0:
                self.color = (255, 0, 0)
            case 1:
                self.color = (255, 255, 0)
            case 2:
                self.color = (0, 255, 0)
            case 3:
                self.color = (127, 0, 255)

    def update(self):
        self.y += self.settings.bonus_speed
        self.rect.y = self.y

    def draw_bonus(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
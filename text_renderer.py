from pygame import font
from settings import FONT_SIZE, FONT_NAME
class TextRenderer:
    def __init__(self, font_name=FONT_NAME, font_size=FONT_SIZE, color=(255, 255, 255)):
        self.font = font.SysFont(font_name, font_size)
        self.color = color

    def render(self, surface, text, position):
        text_surface = self.font.render(text, True, self.color)
        surface.blit(text_surface, position)

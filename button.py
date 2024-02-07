import pygame

class Button:
    def __init__(self, x, y, width, height, text, text_renderer, command=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_renderer = text_renderer
        self.command = command

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect)

        text_width, text_height = self.text_renderer.font.size(self.text)
        text_x = self.rect.x + (self.rect.width - text_width) // 2
        text_y = self.rect.y + (self.rect.height - text_height) // 2

        self.text_renderer.render(surface, self.text, (text_x, text_y))
    def is_clicked(self, pos):
        clicked = self.rect.collidepoint(pos)
        return clicked

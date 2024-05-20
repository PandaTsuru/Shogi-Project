import pygame

def draw_text(screen:pygame.Surface, text:str, font:pygame.font.Font, color:str, topleft:tuple[int, int]):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = topleft
    screen.blit(text_surface, text_rect)


class Label:
    pass
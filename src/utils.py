from Board.pieces import *
import pygame
import os

def notation_to_piece(notation:str):
    return {'P':Pawn, 'K':King, 'R':Rook, 'B':Bishop, 'N':Knight, 'S':Silver, 'G':Gold, 'L':Lance}[notation]

def load_image(path:str, size:tuple[int, int]):
    return pygame.transform.scale(pygame.image.load(path), size)

def generate_piece_images(asset:str, tile_size:int):
    images = {1:{}, -1:{}}
    for file in os.listdir(os.path.join('assets', 'pieces', asset)):
        path = os.path.join('assets', 'pieces', asset, file)
        notation = os.path.splitext(file)[0]
        images[-1][notation] = load_image(path, (tile_size, tile_size))
        images[1][notation] = pygame.transform.rotate(load_image(path, (tile_size, tile_size)), 180)
    return images

def draw_text(screen:pygame.Surface, text:str, font:pygame.font.Font, color:str, topleft:tuple[int, int]):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = topleft
    screen.blit(text_surface, text_rect)
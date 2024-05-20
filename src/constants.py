import ctypes
from math import ceil

user32 = ctypes.windll.user32

TILE_SIZE = (user32.GetSystemMetrics(1)-100)//12
MARGIN = TILE_SIZE//2
WIDTH = TILE_SIZE*9 + 2*MARGIN
HEIGHT = TILE_SIZE*11 + 2*MARGIN
FPS = 60


selected_asset = 'international'


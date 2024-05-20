import ctypes
from math import ceil

user32 = ctypes.windll.user32

HEIGHT = user32.GetSystemMetrics(1)-100
WIDTH = HEIGHT//11*9
FPS = 60
TILE_SIZE = ceil(HEIGHT/11)


selected_asset = 'military'


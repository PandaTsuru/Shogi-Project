import pygame
import ctypes

user32 = ctypes.windll.user32

HEIGHT = user32.GetSystemMetrics(1)*0.9
WIDTH = HEIGHT
FPS = 60


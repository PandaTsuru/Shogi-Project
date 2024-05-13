import pygame
from src.constants import WIDTH, HEIGHT, FPS
from src.scene import SceneManager
from src.config import Config
from src.game import Game



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    config = Config()
    manager = SceneManager()
    manager.set(Game(manager, config))
    run = True
    while run :
        manager.render(screen)
        manager.update()
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            manager.handle_event()
            if event.type == pygame.QUIT :
                run = False
    pygame.quit()



if __name__ == '__main__':
    main()





import pygame
from constants import WIDTH, HEIGHT, FPS
from Scenes.scene import SceneManager
from config import Config
from Scenes.game import Game



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    config = Config()
    manager = SceneManager()
    manager.set(Game(manager, config))
    run = True
    while run :
        screen.fill('black')
        manager.render(screen)
        manager.update()
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            manager.handle_event(event)
            if event.type == pygame.QUIT :
                run = False
    pygame.quit()



if __name__ == '__main__':
    main()





import pygame


class Game(pygame.Surface):
    def __init__(self):
        BLACK = (0, 0, 0)
        GREEN = (2, 123, 14, 0.95)

        pygame.init()
        interface = pygame.display.set_mode((600, 500))
        interface.fill(color=GREEN)
        pygame.display.update()
        pygame.display.set_caption('Sn4keG4me by gu1lhemlcb')

        wall = Wall(color=BLACK, width=5, height=400)
        interface.blit(wall.wall, (10, 60))
        pygame.display.flip()

        is_running = True

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    @ staticmethod
    def create_arena(self):
        pass


class Wall(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        # wall = pygame.sprite.Group()
        self.wall = pygame.Surface([width, height])
        self.wall.fill(color)
        self.rect = self.wall.get_rect()


game = Game()

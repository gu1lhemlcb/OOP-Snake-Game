import pygame
import random

from pygame.locals import *
from random import sample


class Game(pygame.Surface):
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        interface = pygame.display.set_mode((600, 500))
        interface.fill(color=self.BLACK)
        pygame.display.update()
        pygame.display.set_caption('Sn4keG4me by gu1lhemlcb')
        self.create_arena(interface)
        apple = Apple()
        pygame.display.flip()

        left_value, top_value = 40, 200
        left_increase, top_increase = 0, 0
        is_running = True
        clock = pygame.time.Clock()

        points = 0
        while is_running:
            clock.tick(35)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        is_running = False
                    elif event.key == K_LEFT:
                        left_increase = -2
                        top_increase = 0
                    elif event.key == K_RIGHT:
                        left_increase = 2
                        top_increase = 0
                    elif event.key == K_UP:
                        top_increase = -2
                        left_increase = 0
                    elif event.key == K_DOWN:
                        top_increase = 2
                        left_increase = 0
            left_value += left_increase
            top_value += top_increase

            # By filling again, we update the background and
            # delete the previous snake
            interface.fill(color=self.BLACK)
            self.create_arena(interface)
            snake = Snake(left_value, top_value)
            snake.add_to_interface(interface)
            apple.add_to_interface(interface)

            if snake.is_eating_apple(apple):
                apple.reset_position()
                interface.fill(color=self.BLACK)
                self.create_arena(interface)
                snake = Snake(left_value, top_value)
                snake.grow()
                snake.color
                snake.add_to_interface(interface)
                apple.add_to_interface(interface)
                points += 15
                print(points)

            if snake.is_out(560, 420):
                print('You lost sucker')

            pygame.display.update()

    def create_arena(self, interface):
        return pygame.draw.rect(interface, (255, 0, 0),
                                pygame.Rect(20, 60, 560, 420),  4)

    # def update_display(self, interface, apple, left_value, top_value):
    #     interface.fill(color=self.BLACK)
    #     self.create_arena(interface)
    #     snake = Snake(left_value, top_value)
    #     snake.add_to_interface(interface)
    #     apple.add_to_interface(interface)


class Apple(pygame.Rect):
    color = (27, 255, 0, 0.85)
    left_pos = random.randrange(25, 500, 2)
    top_pos = random.randrange(100, 450, 2)
    width_pos = 10
    height_pos = 10

    def __init__(self):
        pygame.Rect.__init__(self, self.left_pos, self.top_pos,
                             self.width_pos, self.height_pos)

    def add_to_interface(self, interface):
        return pygame.draw.rect(interface, self.color, self, 5)

    def reset_position(self):
        self.left_pos = random.randrange(25, 500, 2)
        self.top_pos = random.randrange(100, 450, 2)
        pygame.Rect.__init__(self, self.left_pos, self.top_pos,
                             self.width_pos, self.height_pos)


class Snake(pygame.Rect):
    color = (0, 62, 247, 1)
    left_pos = 0
    top_pos = 0
    width_pos = 15
    height_pos = 15
    body = [(15, 15)]

    def __init__(self, left_value, top_value):
        self.left_pos = left_value
        self.top_pos = top_value
        pygame.Rect.__init__(self, self.left_pos, self.top_pos,
                             self.width_pos, self.height_pos)

    def add_to_interface(self, interface):
        return pygame.draw.rect(interface, self.color, self, 5)

    def is_eating_apple(self, apple):
        return self.collidepoint(apple.left_pos, apple.top_pos)

    def is_out(self, arena_left_pos, arena_top_pos):
        if self.collidepoint(arena_left_pos, arena_top_pos):
            return True

    def grow(self):
        # Chaque rectangle qui suit devra tourner au même moment ou celui qui le precede a tourné, sauvegarder les positions ?
        # cf pygame.Rect.inflate en fait non car car galere quand on va tourner,
        # il vaut mieux dupliquer les rect
        return self.body.append((15, 15))

    # @staticmethod
    # def create_timer():
    #     clock = pygame.time.Clock()
    #     clock.tick(1)
    #     return pygame.time.set_timer()


game = Game()

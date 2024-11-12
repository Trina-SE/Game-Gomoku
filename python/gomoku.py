import numpy
import pygame

PVP = "PlayerVsPlayer"
PVA = "PlayerVsAI"
AVA = "AIVsAI"


class GoMokuUI():
    
    def __init__(self, size, mode="PlayerVsAI"):
        pygame.init()
        pygame.display.set_caption("GOMOKU")

        self.screen = pygame.display.set_mode((30 * size + 30, 30 * size + 30 + 150))
        self.mode = mode
        self.going = True
        self.clock = pygame.time.Clock()

        board = Board(size=size)


    
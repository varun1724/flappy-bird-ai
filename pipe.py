import random
import pygame
import constant

class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(constant.PIPE_IMG, False, True)
        self.PIPE_BOTTOM = constant.PIPE_IMG

        self.passed = False
        self.set_height()


    def set_height(self):
        self.height = random.randrange(40, 450)

        # set the top of where you want to draw the pipe at a negative value 
        self.top = self.height - self.PIPE_TOP.get_height()

        self.bottom = self.height + self.GAP


    def move(self):
        self.x -= self.VEL


    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))


    def collide(self, bird) -> bool:
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True
        
        return False

"""
    display.py

"""

# Imports #########################################################################################
import pygame
###################################################################################################

class Display():
    def __init__(self):
        self.size = [64, 32]
        self.ratio = 12
        self.resolution = [self.size[0]*self.ratio, self.size[1]*self.ratio]
        self.color = (0, 255, 0)
        self.background_color = (0, 0, 0)
        self.screen = None
        self.running = False
        self.matrix = [0x0000000000000000]*32
        self.buffer = [0xF0, 0x80, 0xF0, 0x80, 0x80]

    def start_window(self):
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode(self.resolution)

    def draw_matrix(self):
        for i in range(32):
            for j in range(64):
                if (self.matrix[i] >> j) & 0x1 == 0x1:
                    pygame.draw.rect(self.screen, self.color,
                        [((63-j)*self.ratio, i*self.ratio), (self.ratio, self.ratio)])

    def draw_buffer(self, x=0, y=10):
        for i in range(len(self.buffer)):
            row = (self.buffer[i] << x)
            print(bin(row << 8))
            self.matrix[i+y] = (self.matrix[i] & ~row) | (~self.matrix[i] & row)

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.screen.fill(self.background_color)
        self.draw_buffer()
        self.draw_matrix()
        pygame.display.flip()


display = Display()
display.start_window()
while display.running:
    display.run()


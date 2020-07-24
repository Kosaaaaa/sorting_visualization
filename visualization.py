import pygame
import sys


class Settings:
    # Canvas settings
    WIDTH = 1000
    HEIGHT = 500
    ROWS = 40

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


class Bar:
    def __init__(self, height, row, color):
        self.height = height
        self.row = row
        self.color = color
        self.width = Settings.WIDTH // Settings.ROWS

    def draw(self, surface):
        pass


class Visualization:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Sorting Visualization By Kosaaaaa')
        self.width = Settings.WIDTH
        self.height = Settings.HEIGHT
        self.rows = Settings.ROWS
        self.screen = pygame.display.set_mode((self.width, self.width))

    def draw_grid(self, surface):
        sizeBtwn = self.width // self.rows

        x = 0
        y = 0

        for i in range(self.rows):
            x = x + sizeBtwn
            y = y + sizeBtwn

            pygame.draw.line(surface, Settings.WHITE, (x, 0), (x, self.width))
            pygame.draw.line(surface, Settings.WHITE, (0, y), (self.width, y))

    @staticmethod
    def update():
        pygame.display.update()

    def get_canvas(self):
        return self.screen

    def redraw_window(self):
        self.screen.fill(Settings.BLACK)
        self.draw_grid(self.screen)


def control():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:  # Left
                print('left')
                x, y = pygame.mouse.get_pos()
                print(x, y)

            elif event.button == 3:  # Right
                print('right')

        for key in keys:
            if keys[pygame.K_SPACE]:
                print('space')
                print('start algo')


def main():
    run = True
    start = False
    vis = Visualization()
    clock = pygame.time.Clock()
    vis.redraw_window()
    while run:
        clock.tick(30)
        vis.redraw_window()
        control()
        vis.update()


if __name__ == "__main__":
    main()

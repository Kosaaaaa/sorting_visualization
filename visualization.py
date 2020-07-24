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
    PINK = (255, 0, 153)


class Bar:
    def __init__(self, height, row, color):
        self.height = height
        self.row = row
        self.color = color
        self.width = Settings.WIDTH // Settings.ROWS

    def draw(self, surface):
        pass

class Button:
    def __init__(self, color, pos, size, text='', outline_color=None):
        self.color = color
        self.x, self.y = pos
        self.width, self.height = size
        self.text = text
        self.outline_color = outline_color

    def draw(self, surface):
        if self.outline_color:
            pygame.draw.rect(surface, self.outline_color, 
            (self.x-2,self.y-2,self.width+4,self.height+4),0)
        
        pygame.draw.rect(surface, self.color, 
        (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, Settings.WHITE)

            surface.blit(text, (self.x + (self.width//2 - text.get_width()//2), 
            self.y + (self.height//2 - text.get_height()//2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

class Visualization:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Sorting Visualization By Kosaaaaa')
        self.width = Settings.WIDTH
        self.height = Settings.HEIGHT
        self.rows = Settings.ROWS
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    def draw_menu(self, surface):
        self.buttons = {'quickSort':Button(Settings.PINK, (0, 0), (125, 50), 'Quick Sort')}

        for btn in buttons:
            buttons[btn].draw(surface)

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
        self.draw_menu(self.screen)


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

import pygame
import sys
import random
import sorting


class Settings:
    # Canvas settings
    WIDTH = 1000
    HEIGHT = 600
    ROWS = 40

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PINK = (255, 0, 153)
    GRAY = (192, 192, 192)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)


class Bar:
    def __init__(self, height, row, color):
        self.height = height
        self.row = row
        self.color = color
        self.width = Settings.WIDTH // Settings.ROWS

    def draw(self, surface):
        x = self.row * self.width + 1
        y = Settings.HEIGHT - self.height + 1
        pygame.draw.rect(
            surface,
            self.color,
            (x,
             y,
             self.width - 2,
             self.height - 2))


class Button:
    def __init__(self, color, pos, size, text='', outline_color=None):
        self.color = color
        self.x, self.y = pos
        self.width, self.height = size
        self.text = text
        self.outline_color = outline_color
        self.clicked_color = Settings.GRAY

    def draw(self, surface):
        if self.outline_color:
            pygame.draw.rect(
                surface,
                self.outline_color,
                (self.x - 2,
                 self.y - 2,
                 self.width + 4,
                 self.height + 4),
                0)

        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, Settings.WHITE)

            surface.blit(text,
                         (self.x + (self.width // 2 - text.get_width() // 2),
                          self.y + (self.height // 2 - text.get_height() // 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.color, self.clicked_color = self.clicked_color, self.color
                return True

        return False

    def reset_color(self):
        self.color, self.clicked_color = self.clicked_color, self.color


class Visualization:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Sorting Visualization By Kosaaaaa')
        self.width = Settings.WIDTH
        self.height = Settings.HEIGHT
        self.rows = Settings.ROWS
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.start = False
        self.buttons = {
            'reset': Button(
                Settings.RED, (0, 0), (125, 50), 'Reset'),
            'quickSort': Button(
                Settings.PINK, (125, 0), (125, 50), 'Quick Sort'),
            'mergeSort': Button(
                Settings.PINK, (250, 0), (125, 50), 'Merge Sort'),
        }
        self.bars = self.create_bars()
        self.sorted = False

    def draw_menu(self, surface):
        for btn in self.buttons:
            self.buttons[btn].draw(surface)

    def draw_grid(self, surface):
        sizeBtwn = self.width // self.rows

        x = 0
        y = 0

        for i in range(self.rows):
            x = x + sizeBtwn
            y = y + sizeBtwn

            # Vertical
            pygame.draw.line(surface, Settings.WHITE, (x, 0), (x, self.width))

            # Horizontal
            # pygame.draw.line(surface, Settings.WHITE, (0, y), (self.width, y))
    @staticmethod
    def create_bars():
        bars = []
        for i in range(Settings.ROWS):
            bars.append(Bar(random.randrange(1, 500), i, Settings.PINK))
        return bars

    def update_bars(self, bars=None):
        if bars is None:
            self.bars = self.create_bars()
        else:
            self.bars = bars

    def draw_bars(self, surface):
        for bar in self.bars:
            bar.draw(surface)

    def reset_bars(self):
        bars = self.create_bars()
        self.sorted = False
        self.update_bars(bars)

    @staticmethod
    def update():
        pygame.display.update()

    def get_canvas(self):
        return self.screen

    def redraw_window(self):
        self.screen.fill(Settings.BLACK)
        self.draw_grid(self.screen)
        self.draw_menu(self.screen)
        self.draw_bars(self.screen)

    def do_quick_sort(self):
        if not self.start and not self.sorted:
            self.start = True
            sorting.quickSort(self.bars, 0, len(self.bars) - 1, self)
            self.start = False
            self.sorted = True
            return True
        else:
            return False

    def do_merge_sort(self):
        if not self.start and not self.sorted:
            self.start = True
            sorting.mergeSort(self.bars, self)
            self.start = False
            self.sorted = True
            return True
        else:
            return False


def control(buttons, vis):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:  # Left
                x, y = pygame.mouse.get_pos()

                if buttons['quickSort'].isOver((x, y)):
                    print('quick')
                    vis.do_quick_sort()
                    buttons['quickSort'].reset_color()

                elif buttons['reset'].isOver((x, y)):
                    print('reset')
                    vis.reset_bars()
                    buttons['reset'].reset_color()

                elif buttons['mergeSort'].isOver((x, y)):
                    print('mergeSort')
                    vis.do_merge_sort()
                    buttons['mergeSort'].reset_color()

                else:
                    print('left')

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
    buttons = vis.buttons
    while run:
        pygame.time.delay(100)
        clock.tick(30)
        vis.redraw_window()
        control(buttons, vis)
        vis.update()


if __name__ == "__main__":
    main()

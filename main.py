#uwagi
#użyć rect do punktów !
#wybór liczby iteracji #
#wyświetlanie kolorów #
#readme domena i instrukcja

import pygame
import colorsys

width, height = 800, 800

xmin, xmax = -2.0, 2.0
ymin, ymax = -2.0, 2.0
max_iter = 255

# Initialize Pygame
pygame.init()

# text
pygame.font.init()
font_size = 15

# window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mandelbrot Set')

def get_text(xmin, xmax, ymin, ymax):
    font = pygame.font.SysFont('Helvetica', font_size)

    first_text = font.render(f'xmin: {xmin} xmax: {xmax}', True, (255, 255, 255))
    second_text = font.render(f'ymin: {ymin} ymax: {ymax}', True, (255, 255, 255))

    all_text_x = 10
    first_text_y = 10
    second_text_y = first_text_y + 1.5 * font_size

    screen.blit(first_text, (all_text_x, first_text_y))
    screen.blit(second_text, (all_text_x, second_text_y))

running = True
draw = True

left_mouse_counter = 0


class Clicker:
    def __init__(self):
        self.xmin = 0
        self.ymax = 0
        self.xmax = 0
        self.ymin = 0


clicker = Clicker()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            x = pos[0]
            y = pos[1]

            zx = x * (xmax - xmin) / (width - 1) + xmin
            zy = -(y * (ymax - ymin) / (height - 1) + ymin)

            clicker.xmin = zx
            clicker.ymax = zy

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()

                        x = pos[0]
                        y = pos[1]

                        zx = x * (xmax - xmin) / (width - 1) + xmin
                        zy = -(y * (ymax - ymin) / (height - 1) + ymin)

                        clicker.xmax = zx
                        clicker.ymin = zy

                        xmin = clicker.xmin
                        xmax = clicker.xmax
                        ymin = clicker.ymin
                        ymax = clicker.ymax
                        draw = True
                if draw:
                    break
            break


    if draw:
        # Generate the Mandelbrot set
        for x in range(width):
            for y in range(height):
                c = complex(xmin + (x / width) * (xmax - xmin),
                            ymin + (y / height) * (ymax - ymin))

                z = 0
                i = 0
                for _ in range(max_iter):
                    i += 1

                    if abs(z) > 2.0:
                        break
                    z = z * z + c

                hsl = i / max_iter
                r, g, b = colorsys.hsv_to_rgb(hsl, hsl, hsl)

                screen.set_at((x, y), (r * max_iter, g * max_iter, b * max_iter))

    draw = False

    get_text(xmin, xmax, ymin, ymax)
    pygame.display.flip()

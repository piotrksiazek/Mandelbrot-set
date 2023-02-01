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
iteration_change_step = 20

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
    third_text = font.render(f'max iterations: {max_iter}', True, (255, 255, 255))
    fourth_text = font.render(f'iteration change step: {iteration_change_step}', True, (255, 255, 255))

    all_text_x = 10
    first_text_y = 10
    second_text_y = first_text_y + 1.5 * font_size
    third_text_y = second_text_y + 1.5 * font_size
    fourth_text_y = third_text_y + 1.5 * font_size

    width = max(first_text.get_size()[0], second_text.get_size()[0], third_text.get_size()[0], fourth_text.get_size()[0])
    height = (first_text.get_size()[1] + second_text.get_size()[1] + third_text.get_size()[1] + fourth_text.get_size()[1]) * 1.6

    width = 1.2 * width

    background = pygame.Rect(0, 0, width, height)
    pygame.draw.rect(screen, (0, 0, 0), background)

    screen.blit(first_text, (all_text_x, first_text_y))
    screen.blit(second_text, (all_text_x, second_text_y))
    screen.blit(third_text, (all_text_x, third_text_y))
    screen.blit(fourth_text, (all_text_x, fourth_text_y))

running = True
draw = True

left_mouse_counter = 0


class Boundaries:
    def __init__(self):
        self.xmin = 0
        self.ymax = 0
        self.xmax = 0
        self.ymin = 0


boundaries = Boundaries()
click_count = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                max_iter += iteration_change_step
            elif event.key == pygame.K_LEFT:
                if (max_iter - iteration_change_step) > 0:
                    max_iter -= iteration_change_step
            elif event.key == pygame.K_UP:
                iteration_change_step += 20
            elif event.key == pygame.K_DOWN:
                if (iteration_change_step - 20) > 0:
                    iteration_change_step -= 20

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            x = pos[0]
            y = pos[1]

            if click_count == 1:
                zx = x * (xmax - xmin) / (width - 1) + xmin
                zy = -(y * (ymax - ymin) / (height - 1) + ymin)

                boundaries.xmax = zx
                boundaries.ymin = zy

                xmin = boundaries.xmin
                xmax = boundaries.xmax
                ymin = boundaries.ymin
                ymax = boundaries.ymax
                draw = True

            if click_count == 0:
                zx = x * (xmax - xmin) / (width - 1) + xmin
                zy = -(y * (ymax - ymin) / (height - 1) + ymin)

                boundaries.xmin = zx
                boundaries.ymax = zy

                click_count += 1


    if draw:
        # Generate the Mandelbrot set
        click_count = 0

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

                screen.set_at((x, y), (int(r * 255), int(g * 255), int(b * 255)))

    draw = False

    get_text(xmin, xmax, ymin, ymax)
    pygame.display.flip()

import pygame

# dimensions
width, height = 800, 800

# Define the properties of the Mandelbrot set
xmin, xmax = -1.0, 1.0
ymin, ymax = -1.0, 1.0
max_iter = 400
max_iter_half = max_iter * 9/10


# Initialize Pygame
pygame.init()

#text
pygame.font.init()
font_size = 15

# Create a Pygame window
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Mandelbrot Set')


def get_zoom(coordinate, zoom_factor):
    if coordinate < 0:
        return coordinate + zoom_factor
    return coordinate - zoom_factor

def get_text(xmin, xmax, ymin, ymax, zoom_factor):
    font = pygame.font.SysFont('Helvetica', font_size)

    first_text = font.render(f'xmin: {xmin} xmax: {xmax}', True, (255, 255, 255))
    second_text = font.render(f'ymin: {ymin} ymax: {ymax}', True, (255, 255, 255))
    third_text = font.render(f'zoom factor: {str(zoom_factor)[:5]}', True, (255, 255, 255))

    all_text_x = 10
    first_text_y = 10
    second_text_y = first_text_y + 1.5 * font_size
    third_text_y = second_text_y + 1.5 * font_size

    screen.blit(first_text, (all_text_x, first_text_y))
    screen.blit(second_text, (all_text_x, second_text_y))
    screen.blit(third_text, (all_text_x, third_text_y))

zoom = 0.1
step = 0.05
step_increment = 0.05

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
            print('first')
            x = pos[0]
            y = pos[1]

            #tutaj jest błąd. One najpierw powinny zostać zpróbkowane i dopiero potem
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
                        print('second')
                        x = pos[0]
                        y = pos[1]

                        # tutaj jest błąd. One najpierw powinny zostać zpróbkowane i dopiero potem
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
                for i in range(max_iter):
                    if abs(z) > 2.0:
                        break
                    z = z * z + c
                # Color the pixel red at full iteration
                if i > max_iter_half:
                    i = 0
                r, g, b = i % 128, 0, 0
                screen.set_at((x, y), (r, g, b))
        max_iter += 10

        print(f'xmin: {xmin} xmax: {xmax}')
        print(f'ymin: {ymin} ymax: {ymax}')
    draw = False

    get_text(xmin, xmax, ymin, ymax, zoom)
    pygame.display.flip()

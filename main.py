import pygame

# Create a blank image with a white background
width, height = 400, 400

# Define the properties of the Mandelbrot set
xmin, xmax = -1.0, 1.0
ymin, ymax = -1.0, 1.0
max_iter = 50
max_iter_half = max_iter * 9/10

# Initialize Pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Mandelbrot Set')

def get_new_boundaries(x, y, xmin, xmax, ymin, ymax, zoom):
    zx = x * (xmax - xmin) / (width - 1) + xmin
    zy = y * (ymax - ymin) / (height - 1) + ymin

    current_center_x = (xmin + xmax) / 2
    current_center_y = (ymin + ymax) / 2

    diff_x = abs(current_center_x - zx)
    diff_y = abs(current_center_y - zy)

    moved_left = False
    moved_up = False

    if zx < current_center_x:
        moved_left = True

    if zy > current_center_y:
        moved_up = True

    if moved_up:
        ymin += diff_y
        ymax += diff_y
    else:
        ymin -= diff_y
        ymax -= diff_y

    if moved_left:
        xmin -= diff_x
        xmax -= diff_x
    else:
        xmin += diff_x
        xmax += diff_x

    return xmin / zoom, xmax / zoom, ymin / zoom, ymax / zoom

zoom = 1.1
running = True
draw = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            xmin, xmax, ymin, ymax = get_new_boundaries(pos[0], pos[1], xmin, xmax, ymin, ymax, zoom)
            draw = True

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

        pygame.display.flip()
    draw = False
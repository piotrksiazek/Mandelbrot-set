import pygame

# dimensions
width, height = 800, 800

# Define the properties of the Mandelbrot set
xmin, xmax = -1.0, 1.0
ymin, ymax = -1.0, 1.0
max_iter = 50
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

    smallest_coordinate = min([abs(xmin), abs(xmax), abs(ymin), abs(ymax)])
    zoom_factor = smallest_coordinate/2

    xmin = get_zoom(xmin, zoom_factor)
    xmax = get_zoom(xmax, zoom_factor)
    ymin = get_zoom(ymin, zoom_factor)
    ymax = get_zoom(ymax, zoom_factor)

    return xmin, xmax, ymin, ymax

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


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            xmin, xmax, ymin, ymax = get_new_boundaries(pos[0], pos[1], xmin, xmax, ymin, ymax, zoom)
            draw = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
                zoom -= step
            if event.key == pygame.K_RIGHT:
                zoom += step
            if event.key == pygame.K_UP:
                step += step_increment
            if event.key == pygame.K_DOWN:
                step -= step_increment

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

        print(f'xmin: {xmin} xmax: {xmax}')
        print(f'ymin: {ymin} ymax: {ymax}')
    draw = False

    get_text(xmin, xmax, ymin, ymax, zoom)
    pygame.display.flip()

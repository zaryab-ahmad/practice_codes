import pygame

# Initialize Pygame
pygame.init()

# Set up the canvas
canvas_width = 500
canvas_height = 500
canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Spider-Man Drawing")

# Colors
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

def draw_spiderman():
    # Draw Spider-Man's head
    pygame.draw.circle(canvas, red, (250, 250), 100)

    # Draw Spider-Man's eyes
    pygame.draw.circle(canvas, white, (210, 230), 20)
    pygame.draw.circle(canvas, white, (290, 230), 20)

    # Draw Spider-Man's eyes (black pupils)
    pygame.draw.circle(canvas, black, (220, 230), 10)
    pygame.draw.circle(canvas, black, (300, 230), 10)

    # Draw Spider-Man's body
    pygame.draw.rect(canvas, blue, (225, 250, 50, 100))

    # Draw Spider-Man's arms
    pygame.draw.line(canvas, blue, (200, 300), (175, 400), 10)
    pygame.draw.line(canvas, blue, (300, 300), (325, 400), 10)

    # Draw Spider-Man's legs
    pygame.draw.line(canvas, blue, (225, 350), (200, 450), 10)
    pygame.draw.line(canvas, blue, (275, 350), (300, 450), 10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the canvas with a white background
    canvas.fill(white)

    # Draw Spider-Man
    draw_spiderman()

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

# CASE WHERE ACHILLE NEVER GET TO THE TURTLE
import pygame
import sys

# Pygame initialization
pygame.init()

# Window settings
window_width = 1500
window_height = 1000
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Course entre Achille et la Tortue")

# Load images for background, Achille, and the turtle
background_image = pygame.image.load("Forest1.jpg")
achille_image = pygame.image.load("achille.png")
turtle_image = pygame.image.load("turtle.png")

new_size = (100, 100)
resize_img = pygame.transform.scale(turtle_image, new_size)

# Define speed of Achille and the turtle
achille_speed = 1
turtle_speed = 0.5

# Initialize positions
turtle_position = 100  # Start the turtle ahead of Achille
achille_position = 0

# Simulation loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Make Achille and the turtle move based on their speed
    achille_position += achille_speed
    turtle_position += turtle_speed

    # Prevent Achille from overtaking the turtle
    if achille_position >= turtle_position:
        achille_position = turtle_position - 5

    # Check if Achille and the turtle are within the window boundaries
    if achille_position < 0:
        achille_position = 0
    if turtle_position < 0:
        turtle_position = 0
    if achille_position > window_width - achille_image.get_width():
        achille_position = window_width - achille_image.get_width()
    if turtle_position > window_width - resize_img.get_width():
        turtle_position = window_width - resize_img.get_width()

    window.blit(background_image, (0, 0))

    # Display Achille and the turtle using their images
    window.blit(achille_image, (achille_position, 500))
    window.blit(resize_img, (turtle_position, 700))

    pygame.display.flip()

# Verify who won the race
if achille_position > turtle_position:
    winner_text = "Achille has won the race!"
elif turtle_position > achille_position:
    winner_text = "The turtle won the race!"
else:
    winner_text = "It's a tie!"

font = pygame.font.Font(None, 48)
winner_surface = font.render(winner_text, True, background_image)

# Display the winner
window.blit(winner_surface, (window_width // 2 - 200, window_height // 2))
pygame.display.flip()

# Wait for the user to close the window
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False

pygame.quit()
sys.exit()


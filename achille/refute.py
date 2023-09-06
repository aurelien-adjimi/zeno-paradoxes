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

new_size = (200, 200)
resize_img = pygame.transform.scale(turtle_image, new_size)

# Define speed of Achille and the turtle by step
achille_speed = 1
turtle_speed = 0.5

# Initialise positions
turtle_position = 100
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

    window.blit(background_image, (0, 0))

    # Display Achille and the turtle using their images
    window.blit(achille_image, (achille_position, 500))
    window.blit(resize_img, (turtle_position, 700))

    pygame.display.flip()

    achille_x = achille_position
    turtle_x = turtle_position

    pygame.display.flip()

    # Check if Achille reaches the end of the window, end the race
    if achille_x >= window_width - achille_image.get_width():
        winner_text = "Achille has won the race!"
        font = pygame.font.Font(None, 48)
        winner_surface = font.render(winner_text, True, (0, 0, 0))
        window.blit(winner_surface, (window_width // 2 - 200, window_height // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Display the message for 2 seconds
        running = False 

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

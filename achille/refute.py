import pygame
import sys

# Pygame initialization
pygame.init()

# Window settings
window_width = 1500
window_height = 1000
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Course entre Achille et la Tortue")

# Fonts
font = pygame.font.Font(None, 36)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define speed of Achille and the turtle by step
achille_speed = 1
turtle_speed = 0.5

# Initialise positions
turtle_position = 100
achille_position = 0

# Simulation loop
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Make Achille and the turtle move based on their speed
    achille_position += achille_speed
    turtle_position += turtle_speed

    window.fill(white)

    achille_text = "A"
    turtle_text = "T"

    font = pygame.font.Font(None, 36)
    achille_surface = font.render(achille_text, True, black)
    turtle_surface = font.render(turtle_text, True, black)

    achille_x = achille_position
    turtle_x = turtle_position

    window.blit(achille_surface, (achille_x, 100))
    window.blit(turtle_surface, (turtle_x, 200))

    pygame.display.flip()

    # If Achille reaches the end of the window, end the race
    if achille_x >= window_width:
        break

# Verify who won the race
if achille_position > turtle_position:
    winner_text = "Achille has won the race!"
elif turtle_position > achille_position:
    winner_text = "The turtle won the race!"
else:
    winner_text = "It's a tie!"

font = pygame.font.Font(None, 48)
winner_surface = font.render(winner_text, True, black)

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

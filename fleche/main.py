import pygame
import time

# Pygame initialization
pygame.init()

# Window settings
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Simulation de la flèche de Zénon")

# Load image
arrow_image = pygame.image.load("arrow.png")
new_size = (50, 50)
resized_img = pygame.transform.scale(arrow_image, new_size)

# Initial position of the arrow
arrow_position = 0

# Distance to the target
target_distance = 800

# Arrow speed
arrow_speed = 100

# Font for displaying text
font = pygame.font.Font(None, 36)

# Simulation loop
running = True
while arrow_position < target_distance:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the distance between the arrow and the target
    distance_to_target = target_distance - arrow_position

    # Show current arrow position
    arrow_text = f"Arrow position = {arrow_position} meters, Distance to target = {distance_to_target} meters"
    arrow_surface = font.render(arrow_text, True, (0, 0, 0))

    window.fill((255, 255, 255))
    window.blit(arrow_surface, (20, 20))

    window.blit(resized_img, (arrow_position, 100))

    pygame.display.flip()

    # Update the arrow's position
    arrow_position += arrow_speed

    # Pause for 1 second to simulate the flow of time
    time.sleep(1)

pygame.quit()

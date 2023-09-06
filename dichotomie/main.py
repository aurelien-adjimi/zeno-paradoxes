import pygame
import time

# Pygame initialization
pygame.init()

# Window settings
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Simulation de la pierre de Zénon")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Total distance between Zénon and the tree
total_distance = 8.0

# Initial position of the stone
stone_position = total_distance

# Initialize dichotomie as zero
dichotomie = 0.0

# Font for displaying text
font = pygame.font.Font(None, 36)

# Define the positions for displaying the "P"
p_x = 20 

# Simulation loop
running = True
while stone_position > 0.0001:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Show current stone position
    stone_text = f"Position de la pierre : {stone_position} mètres de l'arbre"
    dichotomie_text = f"Dichotomie totale : {dichotomie} mètres"

    stone_surface = font.render(stone_text, True, black)
    dichotomie_surface = font.render(dichotomie_text, True, black)

    window.fill(white)
    window.blit(stone_surface, (20, 20))
    window.blit(dichotomie_surface, (20, 60))

    # Calculate the position of "P" based on stone_position and total_distance
    p_relative_x = int(((total_distance - stone_position) / total_distance) * (window_width - 40))
    window.blit(font.render("P", True, black), (p_x + p_relative_x, 200))

    pygame.display.flip()

    # Add the distance traveled in this iteration to dichotomie
    dichotomie += stone_position

    # Reduce the distance the stone travels (half the remaining distance)
    stone_position /= 2.0

    # Pause for 2 seconds
    time.sleep(2)

pygame.quit()

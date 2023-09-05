# Total distance between Zéno and the tree
total_distance = 8.0

# Initial position of the stone
stone_position = total_distance

# Initialize dichotomie as zero
dichotomie = 0.0

# Loop simulation
while stone_position > 0.001:  # Using a small limit value to avoid reaching the tree
    # Show current stone position
    print(f"Position de la pierre : {stone_position} mètres de l'arbre")

    # Add the distance traveled in this iteration to dichotomie
    dichotomie += stone_position

    # Reduce the distance the stone travels (half the remaining distance)
    stone_position /= 2.0

# Print the total dichotomie
print(f"Dichotomie totale : {dichotomie} mètres")



# import pygame
# import sys

# # Pygame initialization
# pygame.init()

# # Window settings
# window_width = 800
# window_height = 600
# window = pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption("Simulation de Zénon : La pierre et l'arbre")

# # Colors
# white = (255, 255, 255)
# black = (0, 0, 0)

# # Total distance between Zénon and the tree
# total_distance = 8.0

# # Font for text
# font = pygame.font.Font(None, 36)

# # Position of the "P" character
# stone_x = 10

# # Flag to control animation progress
# animation_in_progress = False

# # Function to reset animation
# def reset_animation():
#     global stone_x, stone_position, animation_in_progress
#     stone_x = 10
#     stone_position = total_distance
#     animation_in_progress = True

# # Button settings
# button_width = 100
# button_height = 40
# button_x = (window_width - button_width) // 2
# button_y = 500

# # Button text and color
# button_text = "Lancer"
# button_color = (0, 128, 255)  # Blue

# # Create a rectangle for the button
# button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# # Simulation loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             # Check if the "Lancer" button was clicked
#             if button_rect.collidepoint(event.pos):
#                 reset_animation()  # Reset animation if button is clicked

#     window.fill(white)

#     # Draw the "Lancer" button
#     pygame.draw.rect(window, button_color, button_rect)
#     button_text_surface = font.render(button_text, True, white)
#     button_text_rect = button_text_surface.get_rect(center=button_rect.center)
#     window.blit(button_text_surface, button_text_rect)

#     # Check if the animation is in progress
#     if animation_in_progress:
#         # Show current stone position
#         if stone_position > 0.001:  # Using a small limit value to avoid reaching the tree
#             stone_text = "P"
#             stone_surface = font.render(stone_text, True, black)
#             window.blit(stone_surface, (stone_x, 10))

#             # Reduce the distance the stone travels (half the remaining distance)
#             stone_position /= 2.0

#             # Update the x-coordinate for the "P" character to make it appear to move
#             stone_x += 50

#             pygame.display.flip()  # Update the display to show the "P" at its new position

#         else:
#             # Animation finished, mark it as such
#             animation_in_progress = False

#     pygame.display.flip()

# # Wait for the user to close the window
# waiting = True
# while waiting:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             waiting = False

# pygame.quit()
# sys.exit()

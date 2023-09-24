import pygame
import matplotlib.pyplot as plt
import io
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matplotlib in Pygame")

# Create a simple Matplotlib plot
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Save the plot to a BytesIO object
plot_image = io.BytesIO()
plt.savefig(plot_image, format='png')
plot_image.seek(0)

plot_surface = pygame.image.load(plot_image)
# Pygame Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Load the Matplotlib plot image onto a Pygame surface
    # plot_surface = pygame.image.load(plot_image)

    # Blit the plot surface onto the Pygame screen
    screen.blit(plot_surface, (50, 50))  # Adjust the position as needed

    pygame.display.flip()

# Clean up resources
plt.close()
plot_image.close()
pygame.quit()

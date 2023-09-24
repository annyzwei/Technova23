import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
green = (34, 139, 34)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Triangle Trees")

# Tree parameters
tree_width = 40
tree_height = 80
tree_speed = 5

# Function to draw a triangle tree
def draw_tree(x, y):
    pygame.draw.polygon(screen, green, [(x, y), (x + tree_width / 2, y - tree_height), (x + tree_width, y)])

# Initialize tree positions
trees = []
for _ in range(5):  # You can change the number of trees as needed
    x = random.randint(screen_width, screen_width * 2)
    y = screen_height - 20
    trees.append((x, y))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    for i in range(len(trees)):
        x, y = trees[i]
        draw_tree(x, y)
        x -= tree_speed
        trees[i] = (x, y)

        # Reset tree's position when it goes off the screen
        if x + tree_width < 0:
            x = screen_width + random.randint(50, 200)
            y = screen_height - 20
            trees[i] = (x, y)

    pygame.display.flip()
    clock.tick(60)  # Adjust this value to control the frame rate

pygame.quit()

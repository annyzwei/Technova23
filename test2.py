import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
AXIS_COLOR = (0, 0, 0)
LINE_COLOR = (0, 0, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 20
MARGIN = 50

# Create a Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Chart")

# Function to draw the line chart
def draw_line_chart(surface, data, x_labels, y_labels):
    # Clear the screen
    surface.fill(BACKGROUND_COLOR)

    # Calculate chart area dimensions
    chart_width = WIDTH - 2 * MARGIN
    chart_height = HEIGHT - 2 * MARGIN

    # Draw X and Y axes
    pygame.draw.line(surface, AXIS_COLOR, (MARGIN, MARGIN + chart_height), (MARGIN + chart_width, MARGIN + chart_height), 2)
    pygame.draw.line(surface, AXIS_COLOR, (MARGIN, MARGIN + chart_height), (MARGIN, MARGIN), 2)

    # Draw X and Y axis labels
    font = pygame.font.Font(None, FONT_SIZE)
    for i, label in enumerate(x_labels):
        text = font.render(label, True, FONT_COLOR)
        text_rect = text.get_rect()
        text_rect.centerx = MARGIN + (i / (len(x_labels) - 1)) * chart_width
        text_rect.centery = MARGIN + chart_height + MARGIN // 2
        surface.blit(text, text_rect)

    for i, label in enumerate(y_labels):
        text = font.render(label, True, FONT_COLOR)
        text_rect = text.get_rect()
        text_rect.centerx = MARGIN // 2
        text_rect.centery = MARGIN + chart_height - (i / (len(y_labels) - 1)) * chart_height
        surface.blit(text, text_rect)

    # Draw data points and connect with lines
    num_points = len(data)
    if num_points > 1:
        for i in range(num_points - 1):
            x1 = MARGIN + (i / (num_points - 1)) * chart_width
            x2 = MARGIN + ((i + 1) / (num_points - 1)) * chart_width
            y1 = MARGIN + chart_height - (data[i] / max(data)) * chart_height
            y2 = MARGIN + chart_height - (data[i + 1] / max(data)) * chart_height
            pygame.draw.circle(surface, LINE_COLOR, (int(x1), int(y1)), 5)
            pygame.draw.line(surface, LINE_COLOR, (x1, y1), (x2, y2), 2)

# Sample data
data = [20, 40, 30, 50, 70, 60]
x_labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
y_labels = ["0", "20", "40", "60", "80", "100"]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_line_chart(screen, data, x_labels, y_labels)

    pygame.display.flip()

# Quit Pygame
pygame.quit()

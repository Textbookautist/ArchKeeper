import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Roller")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)

# Dice Types
DICE_TYPES = [4, 6, 8, 10, 12, 20, 100]

# Button class
class Button:
    def __init__(self, x, y, text, sides):
        self.rect = pygame.Rect(x, y, 80, 30)
        self.text = text
        self.sides = sides

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        font = pygame.font.Font(None, 24)
        text_surf = font.render(self.text, True, WHITE)
        screen.blit(text_surf, (self.rect.x + 15, self.rect.y + 5))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Dice class
class Dice:
    def __init__(self, x, y, sides):
        self.x = x
        self.y = y
        self.sides = sides
        self.size = 50
        self.velocity_x = 0
        self.velocity_y = 0
        self.held = False
        self.shaking = False
        self.last_pos = (x, y)
        self.roll()

    def roll(self):
        self.value = random.randint(1, self.sides)

    def update(self):
        if not self.held:
            self.x += self.velocity_x
            self.y += self.velocity_y
            self.velocity_x *= 0.95
            self.velocity_y *= 0.95

        # Detect shaking
        movement_distance = abs(self.x - self.last_pos[0]) + abs(self.y - self.last_pos[1])
        if movement_distance > 10:  # Threshold for shaking
            self.shaking = True
        else:
            self.shaking = False
        
        self.last_pos = (self.x, self.y)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.size, self.size))
        font = pygame.font.Font(None, 36)
        text_surf = font.render(str(self.value), True, WHITE)
        screen.blit(text_surf, (self.x + 15, self.y + 10))

    def contains(self, pos):
        return self.x <= pos[0] <= self.x + self.size and self.y <= pos[1] <= self.y + self.size

# Initialize buttons
buttons = []
for i, sides in enumerate(DICE_TYPES):
    buttons.append(Button(20, 40 + i * 40, f"D{sides}", sides))

# Game loop
dice_list = []
selected_dice = None
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for btn in buttons:
                if btn.is_clicked((x, y)):
                    dice_list.append(Dice(200, 300, btn.sides))
                    break
            for dice in dice_list:
                if dice.contains((x, y)):
                    selected_dice = dice
                    selected_dice.held = True
                    break

        if event.type == pygame.MOUSEBUTTONUP:
            if selected_dice:
                selected_dice.held = False
                selected_dice.velocity_x = random.uniform(-5, 5)
                selected_dice.velocity_y = random.uniform(-5, 5)

                if selected_dice.shaking:  # Roll only if shaken
                    selected_dice.roll()

                selected_dice = None

        if event.type == pygame.MOUSEMOTION and selected_dice:
            selected_dice.x, selected_dice.y = event.pos

    # Update and draw dice
    for dice in dice_list:
        dice.update()
        dice.draw()

    # Draw buttons
    for btn in buttons:
        btn.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

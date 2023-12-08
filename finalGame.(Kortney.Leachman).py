#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 22:12:58 2023

@author: kortneyleachman
"""

import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5

# Define enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(0, 50)

    def update(self):
        self.rect.y += 3
        if self.rect.y > HEIGHT:
            self.rect.y = random.randint(0, 50)
            self.rect.x = random.randint(0, WIDTH - 30)

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create enemies
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Initialize scoreboard
score = 0
font = pygame.font.Font(None, 36)

# Display countdown
for i in range(3, 0, -1):
    screen.fill(WHITE)
    countdown_text = font.render(f"Get ready! Starting in {i}...", True, GREEN)
    screen.blit(countdown_text, (WIDTH // 4, HEIGHT // 2))
    pygame.display.flip()
    time.sleep(1)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()
    enemies.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        print("Game Over!")
        running = False
    else:
        # Increase score for each frame without collision
        score += 1

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Draw the scoreboard
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()


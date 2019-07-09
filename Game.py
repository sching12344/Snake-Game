from Opening import main_menu

import pygame
import time

pygame.init()

#Set the display screen width and height
display_height = 600
display_width = 800
game_display = pygame.display.set_mode((display_height, display_width))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

#Create the constant colours used within the game
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
grey = (166,166,166)

def main_menu():
	"""Create the main menu for the user to see when entering the game"""
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				user_quit()

		game_display.fill(white)
		pygame.display.update()
		clock.tick(15)

def user_quit():
	"""Creates a shortcut function for quitting the game"""
	pygame.quit()
	quit()

main_menu()
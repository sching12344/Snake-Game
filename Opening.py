import pygame
import time

#set the constant colours
white = (255,255,255)

#import the clock
clock = pygame.time.Clock()

def main_menu():
	"""Creates the main menu for users to see when they enter the game"""
	while True:
		for event in pygame.event.get():
			if pygame.event == pygame.QUIT:
				pygame.quit()
				quit()
		game_display.fill(white)
		pygame.display.update()
		clock.tick(15)
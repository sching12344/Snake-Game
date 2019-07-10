import pygame
import time
from Text_Object import text_object
from Draw_Snake import Snake
from Button import create_button
from Start_Game import start_game

#import the clock
clock = pygame.time.Clock()

#colours = [white, black, bright_red, red, bright_green, green, grey]
def main_menu(display_width, display_height, game_display, colours):
	"""Creates the main menu (second stack) for users to see when they enter the game. Default button size is 100 width and 50 height"""
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		large_text = pygame.font.SysFont("Times New Roman",50)
		text_surface, text_rectangle = text_object("Welcome to my Snake Game", large_text)
		text_rectangle.center = (display_width/2, display_height/3.5)

		game_display.fill(colours[0])
		game_display.blit(text_surface, text_rectangle)
		pygame.draw.circle(game_display, colours[1], (display_width//2, display_height//2), 10, 5)

		create_button("Start Game!", game_display, display_width/8, display_height*7/10, 200, 100, colours[4], colours[5], start_game)
		create_button("Quit Game!", game_display, display_width*5/8, display_height*7/10, 200, 100, colours[2], colours[3], pygame.quit)

		pygame.display.update()
		clock.tick(15)
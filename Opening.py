import pygame
import time
from Text_Object import text_object
from Draw_Snake import Snake
from Button import create_button
#set the constant colours
white = (255,255,255)
black = (0,0,0)
bright_red = (255,0,0)
red = (180,0,0)
bright_green = (0,255,0)
green = (0,180,0)

#import the clock
clock = pygame.time.Clock()

def main_menu(display_width, display_height, game_display):
	"""Creates the main menu for users to see when they enter the game. Default button size is 100 width and 50 height"""
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		large_text = pygame.font.Font("freesansbold.ttf",50)
		text_surface, text_rectangle = text_object("Welcome to my Snake Game", large_text)
		text_rectangle.center = (display_width/2, display_height/3.5)

		game_display.fill(white)
		game_display.blit(text_surface, text_rectangle)
		pygame.draw.circle(game_display, black, (display_width//2, display_height//2), 10, 5)

		create_button("Start Game!", game_display, display_width/8, display_height*7/10, 200, 100, green, bright_green)
		create_button("Quit Game!", game_display, display_width*5/8, display_height*7/10, 200, 100, red, bright_red)

		pygame.display.update()
		clock.tick(15)
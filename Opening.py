import pygame
import time
from Text_Object import text_object
from Draw_Snake import Snake
from Button import create_button
from Start_Game import start_game

#import the clock
clock = pygame.time.Clock()
pygame.font.init()

def create_background(game_display, colours, display_height, display_width):
	game_display.fill(colours[8])
	height = display_height*2//3 -50
	for a in range(height//50):
		x_position = 0
		if a%2==0:
			for i in range(display_width//50):
				if i%2==0:
					pygame.draw.rect(game_display, colours[4], (x_position,height,50,50))
				elif i%2==1:
					pygame.draw.rect(game_display, colours[6], (x_position,height,50,50))

				x_position += 50

		elif a%2==1:
			for b in range(display_width//50):
				if b%2==0:
					pygame.draw.rect(game_display, colours[6], (x_position,height,50,50))
				elif b%2==1:
					pygame.draw.rect(game_display, colours[4], (x_position, height,50,50))
				x_position +=50
		height += 50


#colours = [white, black, bright_red, red, bright_green, green, dark_green, grey, sky_blue]
def main_menu(display_width, display_height, game_display, colours):
	"""Creates the main menu (second stack) for users to see when they enter the game. Default button size is 100 width and 50 height"""
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


		create_background(game_display, colours, display_height, display_width)
		large_text = pygame.font.Font(None, 50)
		text_surface, text_rectangle = text_object("Welcome to my Snake Game", large_text)
		text_rectangle.center = (display_width/2, display_height/3.5)
		game_display.blit(text_surface, text_rectangle)
		pygame.draw.circle(game_display, colours[0], (display_width//2, display_height//2), 10, 5)

		create_button("Start Game!", game_display, display_width/8, display_height*6.5/
			10, 200, 100, colours[5], colours[4], start_game)
		create_button("Quit Game!", game_display, display_width*5/8, display_height*6.5/10, 200, 100, colours[3], colours[2], pygame.quit)

		pygame.display.update()
		clock.tick(15)
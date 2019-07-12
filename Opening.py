import pygame
import time
from Draw_Snake import *
from Button import create_button
from Start_Game import start_game
from Text_Object import text_object

#creates a clock for the game
pygame.init()
clock = pygame.time.Clock()

#Load an image of an apple for the opening menu


def create_background(game_display, colours, display_height, display_width):

	game_display.fill(colours["sky_blue"])
	height = display_height*2//3 -50
	for a in range(height//50):
		x_position = 0
		if a%2==0:
			for i in range(display_width//50):
				if i%2==0:
					pygame.draw.rect(game_display, colours["bright_green"], (x_position,height,50,50))
				elif i%2==1:
					pygame.draw.rect(game_display, colours["green"], (x_position,height,50,50))

				x_position += 50

		elif a%2==1:
			for b in range(display_width//50):
				if b%2==0:
					pygame.draw.rect(game_display, colours["green"], (x_position,height,50,50))
				elif b%2==1:
					pygame.draw.rect(game_display, colours["bright_green"], (x_position, height,50,50))
				x_position +=50
		height += 50

		

		#Load the image of the apple and snake and then blit the snake image before the apple (make it look like the snake is eating the apple)
		apple_image = pygame.image.load("new_apple.png")
		apple_image.convert_alpha()
		apple_width, apple_height = (80, 63)

		#create the image of the snake using circles
		snake_background = Snake(game_display, colours["orange"], colours["bright_orange"], display_width, display_height)
		snake_head_x, snake_head_y, radius = snake_background.create_body_background(apple_width, apple_height)
		snake_background.create_head(snake_head_x, snake_head_y, radius, colours["white"], colours["black"])
		game_display.blit(apple_image, (display_width//2-apple_width//2, display_height//2-apple_height))

#colours = [white, black, bright_red, red, bright_green, green, dark_green, grey, sky_blue]
def main_menu(display_width, display_height, game_display, colours):
	"""Creates the main menu (second stack) for users to see when they enter the game. Default button size is 100 width and 50 height"""
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		create_background(game_display, colours, display_height, display_width)

		large_text = pygame.font.Font(None, 70)
		text_surface, text_rectangle = text_object("Welcome to my Snake Game", large_text)
		text_rectangle.center = (display_width/2, display_height/5)
		game_display.blit(text_surface, text_rectangle)
		#pygame.draw.circle(game_display, colours[0], (display_width//2, display_height//2), 10, 5)
		#game_display.blit(apple_image, (display_height/2,display_width/2))

		create_button("Start Game!", game_display, display_width/8, display_height*6.5/10, 200, 100, colours["dark_green"], colours["bright_green"], start_game)
		create_button("Quit Game!", game_display, display_width*5/8, display_height*6.5/10, 200, 100, colours["red"], colours["bright_red"], pygame.quit)

		pygame.display.update()
		clock.tick(15)
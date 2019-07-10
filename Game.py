from Opening import main_menu
from Button import create_button
from Text_Object import text_object

import pygame
import time

pygame.init()

#Set the display screen width and height
display_height = 600
display_width = 800
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

#Create the constant colours used within the game
white = (255,255,255)
black = (0,0,0)
bright_red = (255,0,0)
red = (200,0,0)
bright_green = (0,255,0)
green = (0,200,0)
grey = (166,166,166)

def user_quit():
	"""Creates a shortcut function for quitting the game"""
	pygame.quit()
	quit()

main_menu(display_width, display_height, game_display)
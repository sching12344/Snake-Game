from Opening import main_menu
from Button import create_button
from Text_Object import text_object

import pygame
import time

pygame.init()


"""This is the main function of my snake game"""
display_height = 600
display_width = 800
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

#Create the constant colours used within the game [white, black, bright_red, red, bright_green, green, dark_green, grey, sky_blue]
colours = [(255,255,255), (0,0,0), (255,0,0), (200,0,0), (0,255,0), (0,180,0), (0, 140,0), (166,166,166), (132,206,250)]

def user_quit():
	"""Creates a shortcut function for quitting the game"""
	pygame.quit()
	quit()

"""List of fonts: https://docs.microsoft.com/en-us/typography/fonts/windows_10_font_list"""
main_menu(display_width, display_height, game_display, colours)
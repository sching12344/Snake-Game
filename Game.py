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

#Create the constant colours used within the game [white, black, bright_red, red, bright_green, green, dark_green, grey, sky_blue, dark_blue]
colours = {"white":(255,255,255), "black":(0,0,0), "bright_red":(255,0,0), "red":(200,0,0), "bright_green":(0,255,0), "green":(0,180,0), "dark_green":(0,140,0), "grey":(166,166,166), "sky_blue":(132,206,250), "dark_blue":(0,0,255), "bright_orange": (255,83,0), "orange":(255,140,0)}

def user_quit():
	"""Creates a shortcut function for quitting the game"""
	pygame.quit()
	quit()

"""List of fonts: https://docs.microsoft.com/en-us/typography/fonts/windows_10_font_list"""
main_menu(display_width, display_height, game_display, colours)
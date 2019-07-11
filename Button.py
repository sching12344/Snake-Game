import pygame
import time
from Text_Object import text_object

def create_button(button_message, display, x, y, width, height, inactive_colour, active_colour, action = None):
	mouse_position = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if (x + width > mouse_position[0] > x) and (y + height > mouse_position[1] > y):
		pygame.draw.rect(display, active_colour, (x, y, width, height))

		if click[0] == 1 and action != None:
			action()
	
	else:
		pygame.draw.rect(display, inactive_colour, (x, y, width, height))

	button_font = pygame.font.Font(None, 40)
	text_surface, text_rectangle = text_object(button_message, button_font)
	text_rectangle.center = ((x+width/2), (y+height/2))
	display.blit(text_surface, text_rectangle)
import pygame
import time
black = (0,0,0)

def text_object(text, font):
	text_surface = font.render(text, True, black)
	return text_surface,text_surface.get_rect()
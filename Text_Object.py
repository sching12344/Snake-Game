import pygame
import time
black = (0,0,0)
white = (255,255,255)

def text_object(text, font):
	text_surface = font.render(text, True, white)
	return text_surface,text_surface.get_rect()
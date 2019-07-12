import pygame

class Snake():

	def __init__(self, surface, first_colour, second_colour, display_width, display_height):
		self.surface = surface
		self.first_colour = first_colour
		self.second_colour = second_colour
		self.display_width = display_width
		self.display_height = display_height
		

	def create_head(self, x, y, radius, white, black):
		pygame.draw.circle(self.surface, white, (x+radius, y+radius//2), radius)
		pygame.draw.circle(self.surface, black, (x+radius+radius//2//2, y+radius//2), radius//2)

		pygame.draw.circle(self.surface, white, (x+radius, int(y+radius*2)), radius)
		pygame.draw.circle(self.surface, black, (x+radius+radius//2//2, int(y+radius*2)), radius//2)

	def create_body_background(self, apple_width, apple_height):
		#surface, colour, position, radius, width =0
		beginning_height = self.display_height*2//3 - 50
		ending_height = self.display_height//2 - apple_height
		starting_width = self.display_width//2-apple_width
		ending_width = self.display_width//2+apple_width
		first_circle_radius = 10
		next_circle = 15

		"""Create a snake that reaches to top of the apple +2 (to reach the top)"""
		last_row = (beginning_height-ending_height)//(next_circle)+1
		for k in range((beginning_height-ending_height)//(next_circle)+2):
			if k%2==0:
				beginning_width = self.display_width//2-apple_width
				if k == last_row:
					for b in range(int(ending_width-beginning_width)//next_circle//2):
						if b == (ending_width-beginning_width)//next_circle//2:
							pygame.draw.circle(self.surface, self.first_colour, (beginning_width, beginning_height), int(first_circle_radius*1.2))
							pygame.draw.circle(self.surface, self.second_colour, (beginning_width, beginning_height), int(first_circle_radius*1.2), 2)
							snake_head = (beginning_width, beginning_height-next_circle, first_circle_radius)
							return snake_head

						pygame.draw.circle(self.surface, self.first_colour, (beginning_width, beginning_height), first_circle_radius)
						pygame.draw.circle(self.surface, self.second_colour, (beginning_width, beginning_height), first_circle_radius, 2)
						beginning_width += next_circle

				else:
					for i in range((ending_width-beginning_width)//next_circle):
						pygame.draw.circle(self.surface, self.first_colour, (beginning_width, beginning_height), first_circle_radius)
						pygame.draw.circle(self.surface, self.second_colour, (beginning_width, beginning_height), first_circle_radius, 2)
						beginning_width += next_circle
			elif k == 3 or k==7:
				pygame.draw.circle(self.surface, self.first_colour, (starting_width-first_circle_radius, beginning_height), first_circle_radius)
				pygame.draw.circle(self.surface, self.second_colour, (starting_width-first_circle_radius, beginning_height), first_circle_radius, 2)
			elif k==1 or k==5 or k==9:
				pygame.draw.circle(self.surface, self.first_colour, (ending_width-next_circle, beginning_height), first_circle_radius)
				pygame.draw.circle(self.surface, self.second_colour, (ending_width-next_circle, beginning_height), first_circle_radius, 2)
			beginning_height -= next_circle
		return snake_head
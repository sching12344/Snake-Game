import pygame
import time
from Draw_Snake import *
from crashed import crashed

def create_game_background(game_display, colours, display_width, display_height):
	game_display.fill(colours["sky_blue"])
	height = 50

	for a in range(10):
		x_position = 150
		if a%2==0:
			for i in range(10):
				if i%2==0:
					pygame.draw.rect(game_display, colours["bright_green"], (x_position,height,50,50))
				elif i%2==1:
					pygame.draw.rect(game_display, colours["green"], (x_position,height,50,50))

				x_position += 50

		elif a%2==1:
			for b in range(10):
				if b%2==0:
					pygame.draw.rect(game_display, colours["green"], (x_position,height,50,50))
				elif b%2==1:
					pygame.draw.rect(game_display, colours["bright_green"], (x_position, height,50,50))
				x_position +=50
		height += 50

def arrange_turns(direction, x, y):
	new_x = int(x[1:])
	new_y = int(y[1:])

	#new implementation is incorrect please redo
	if direction == "right":
		"""if new_x <=25:
			x = int(x[0])*100+25
		elif new_x >75:
			x = (int(x[0])+1)*100+25
		elif (new_x >25 and new_x <75) or new_x==75:
			x = (int(x[0])+1)*100-25"""
		if direction == "up":
			if new_y <25:
				y = int(y[0])*100-25
			elif new_y >75:
				y = (int(y[0])+1)*100-25
			elif (new_y>=25 and new_y<75) or new_y == 75:
				y = int(y[0])*100+25
		elif direction == "down":
			if new_y <=25:
				y = int(y[0])*100+25
			elif new_y >75:
				y = (int(y[0])+1)*100+25
			elif (new_y >25 and new_y < 75) or new_y==75:
				y = (int(y[0])+1)*100-25


	elif direction == "left":
		"""if new_x <25:
			x = int(x[0])*100-25
		elif new_x >= 75:
			x = (int(x[0])+1)*100-25
		elif (new_x >=25 and new_x <75) or new_x == 25:
			x = int(x[0])*100 + 25"""
		if direction == "up":
			if new_y <25:
				y = int(y[0])*100-25
			elif new_y >75:
				y = (int(y[0])+1)*100-25
			elif (new_y>=25 and new_y<75) or new_y == 75:
				y = int(y[0])*100+25
		elif direction == "down":
			if new_y <=25:
				y = int(y[0])*100+25
			elif new_y >75:
				y = (int(y[0])+1)*100+25
			elif (new_y >25 and new_y < 75) or new_y==75:
				y = (int(y[0])+1)*100-25
					
	elif direction == "up":
		if direction == "right":
			if new_x <=25:
				x = int(x[0])*100+25
			elif new_x >75:
				x = (int(x[0])+1)*100+25
			elif (new_x >25 and new_x <75) or new_x==75:
				x = (int(x[0])+1)*100-25
		elif direction == "left":
			if new_x <25:
				x = int(x[0])*100-25
			elif new_x >= 75:
				x = (int(x[0])+1)*100-25
			elif (new_x >=25 and new_x <75) or new_x == 25:
				x = int(x[0])*100 + 25
		"""if new_y <25:
			y = int(y[0])*100-25
		elif new_y >75:
			y = (int(y[0])+1)*100-25
		elif (new_y>=25 and new_y<75) or new_y == 75:
			y = int(y[0])*100+25"""

	elif direction == "down":
		if direction == "right":
			if new_x <=25:
				x = int(x[0])*100+25
			elif new_x >75:
				x = (int(x[0])+1)*100+25
			elif (new_x >25 and new_x <75) or new_x==75:
				x = (int(x[0])+1)*100-25
		elif direction == "left":
			if new_x <25:
				x = int(x[0])*100-25
			elif new_x >= 75:
				x = (int(x[0])+1)*100-25
			elif (new_x >=25 and new_x <75) or new_x == 25:
				x = int(x[0])*100 + 25
	print(x, y)
	return (x, y)

def start_game(display_width, display_height, game_display, colours):
	clock = pygame.time.Clock()
	
	snake_body_x = 425
	snake_body_y = 550//2
	snake_body = 16
	speed = 2
	pending_turn = []

	player_snake = Snake(game_display, colours["orange"], colours["bright_orange"], display_width, display_height, snake_body_x, snake_body_y)
	not_crashed = True
	
	while not_crashed:

		if player_snake.head[0] >= 650 or player_snake.head[0] <=150 or player_snake.head[1] <= 50 or player_snake.head[1] >= 550:
			not_crashed = False

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				x = str(player_snake.head[0])
				y = str(player_snake.head[1])

				if event.key == pygame.K_LEFT and player_snake.head_direction != "right":
					player_snake.turns[arrange_turns("left", x, y)] = "left"

				elif event.key == pygame.K_RIGHT and player_snake.head_direction != "left":
					player_snake.turns[arrange_turns("right", x, y)]

				elif event.key == pygame.K_UP and player_snake.head_direction != "down":
					player_snake.turns[arrange_turns("up", x, y)] = "up"

				elif event.key == pygame.K_DOWN and player_snake.head_direction != "up":
					player_snake.turns[arrange_turns("down", x, y)] = "down"
					print(x)
					print("reached here")
					quit()


		create_game_background(game_display, colours, display_width, display_height)
		player_snake.create_snake(snake_body, colours["white"], colours["black"], colours["bright_red"], colours["sky_blue"])

		#head_x, head_y, circle_radius = player_snake.create_body_game(snake_body_x, snake_body_y)
		#player_snake.create_body_game()
			#Creating the background and the snake
			
			# create background 
			# create the snake
			# create the apple with random except the random coordinates (x, y) cannot be on top of the already blitted snake
			#move the snake
			#check keyboard movements - Rotate the snake image
			#check if crashed 1.wall 2.itself
			#create background
			#Use random.seed() to create the apple image randomly within a square


		#test for whether the player has crashed into a wall
		"""if head_x == 176 or head_x == 650 or head_y == 49 or head_y == 551:
			crashed = False
		elif (head_x, head_y) in player_snake.body:
			crashed = False"""
		
		"""player_snake.body.append((snake_body_x, snake_body_y))
		for a in range((len(player_snake.body))-2, -1, -1):
			player_snake.body[a] = player_snake.body[a+1]
		del player_snake.body[0]
		for b in range(len(player_snake.body)):
			print(player_snake.body[b])
		quit()"""

		#for b in range(len(player_snake.body)-1):
		#	player_snake.body[b] = (player_snake.body[b+1][0]*1.04, player_snake.body[b+1][])
		
		player_snake.update()
		pygame.display.update()
		clock.tick(60)

	if not_crashed == False:
		crashed()
		return
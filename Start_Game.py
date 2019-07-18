import pygame
import time
import random
from Draw_Snake import *
from crashed import crashed

def show_score(count, black, game_display):
	text = pygame.font.Font(None, 30).render("Happiness Level: {}".format(count), True, black)
	game_display.blit(text, (30,8))

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

def arrange_turns(player_snake, direction, x, y):
	new_x = int(x[1:])
	new_y = int(y[1:])
	return_x = None
	return_y = None

	if direction == "right" or direction == "left":
		if player_snake.head_direction == "up":
			if new_y <25:
				return_y = int(y[0])*100-25
			elif new_y >75:
				return_y = (int(y[0])+1)*100-25
			elif (new_y>=25 and new_y<75) or new_y == 75:
				return_y = int(y[0])*100+25
		elif player_snake.head_direction == "down":
			if new_y <=25:
				return_y = int(y[0])*100+25
			elif new_y >75:
				return_y = (int(y[0])+1)*100+25
			elif (new_y >25 and new_y < 75) or new_y==75:
				return_y = (int(y[0])+1)*100-25

					
	elif direction == "up" or direction == "down":
		if player_snake.head_direction == "right":
			if new_x <=25:
				return_x = int(x[0])*100+25
			elif new_x >75:
				return_x = (int(x[0])+1)*100+25
			elif (new_x >25 and new_x <75) or new_x==75:
				return_x = (int(x[0])+1)*100-25
		elif player_snake.head_direction == "left":
			if new_x <25:
				return_x = int(x[0])*100-25
			elif new_x >= 75:
				return_x = (int(x[0])+1)*100-25
			elif (new_x >=25 and new_x <75) or new_x == 25:
				return_x = int(x[0])*100 + 25

	if return_y == None:
		return_y = int(y)
	if return_x == None:
		return_x = int(x)

	return (return_x, return_y)

def create_apple(player_snake):
	start_width = 150
	start_height = 50
	x_position, y_position = start_width+(random.randint(0,9)*50), start_height+(random.randint(0,9)*50)
	for b in range(len(player_snake.body)):
		if (x_position, y_position) == player_snake.body[b]:
			return create_apple(player_snake)
	else:
		return (x_position+25, y_position+25), (x_position, y_position)

def start_game(display_width, display_height, game_display, colours):
	clock = pygame.time.Clock()
	
	snake_body_x = 425
	snake_body_y = 550//2
	snake_body = 16
	speed = 2
	count = 0
	pending_turn = []
	player_snake = Snake(game_display, colours["orange"], colours["bright_orange"], display_width, display_height, snake_body_x, snake_body_y)
	apple_image = pygame.image.load("new_apple.png")
	apple_image.convert_alpha()
	apple_image = pygame.transform.scale(apple_image, (50, 50))
	apple_image_two = pygame.transform.scale(apple_image, (30,30))
	hit_position, apple_position = create_apple(player_snake)

	not_crashed = True
	while not_crashed:
		# Test if the snake has crashed into itself after the recent update function has been run. for loop cannot be tested yet because snake body is not long enough.
		if player_snake.head[0] >= 650 or player_snake.head[0] <=150 or player_snake.head[1] <= 50 or player_snake.head[1] >= 550:
			not_crashed = False
		for a in range(len(player_snake.body)-1):
			if player_snake.head == player_snake.body[a]:
				not_crashed = False

		if player_snake.head == hit_position:
			hit_position, apple_position = create_apple(player_snake)
			count += 1
			print(count)


		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				x = str(player_snake.head[0])
				y = str(player_snake.head[1])

				if event.key == pygame.K_LEFT and player_snake.head_direction != "right":
					player_snake.turns[arrange_turns(player_snake, "left", x, y)] = "left"

				elif event.key == pygame.K_RIGHT and player_snake.head_direction != "left":
					player_snake.turns[arrange_turns(player_snake, "right", x, y)] = "right"

				elif event.key == pygame.K_UP and player_snake.head_direction != "down":
					player_snake.turns[arrange_turns(player_snake, "up", x, y)] = "up"

				elif event.key == pygame.K_DOWN and player_snake.head_direction != "up":
					player_snake.turns[arrange_turns(player_snake, "down", x, y)] = "down"

		create_game_background(game_display, colours, display_width, display_height)
		game_display.blit(apple_image_two, (0,0))
		show_score(count, colours["black"], game_display)
		game_display.blit(apple_image, (apple_position))
		player_snake.create_snake(snake_body, colours["white"], colours["black"], colours["bright_red"], colours["sky_blue"])

		player_snake.update()
		pygame.display.update()
		clock.tick(60)

	if not_crashed == False:
		crashed()
		return
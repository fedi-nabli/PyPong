import pygame
import random

pygame.init()

gadget_pair = 1
choice = int(input("Enter your choice for gadget pair: "))
if choice == 1:
  gadget_pair = 1
elif choice == 2:
  gadget_pair = 2

clock = pygame.time.Clock()

#INITIALS
FPS = 60000
WIDTH, HEIGHT = 1000, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PyPong')

run = True
directions = [0, 1]
angles = [0, 1, 2]

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

#BALL
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7

dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
dummy_ball_vel_x, dummy_ball_vel_y = 0.7, 0.7

#PADDLES
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
second_left_paddle_y = second_right_paddle_y = HEIGHT/2 - paddle_height/2
second_left_paddle_x, second_right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0
second_right_paddle_vel = second_left_paddle_vel = 0

#GADGETS
left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5

#main loop
while run:
  window.fill(BLACK)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        right_paddle_vel = -0.9
        second_right_paddle_vel = -0.9
      if event.key == pygame.K_DOWN:
        right_paddle_vel = 0.9
        second_right_paddle_vel = 0.9
      if event.key == pygame.K_RIGHT and right_gadget_remaining > 0:
        right_gadget = 1
      if event.key == pygame.K_LEFT and right_gadget_remaining > 0:
        right_gadget = 2
      if event.key == pygame.K_z:
        left_paddle_vel = -0.9
        scond_left_paddle_vel = -0.9
      if event.key == pygame.K_s:
        left_paddle_vel = 0.9
        second_left_paddle_vel = 0.9
      if event.key == pygame.K_d and left_gadget_remaining > 0:
        left_gadget = 1
      if event.key == pygame.K_q and left_gadget_remaining > 0:
        left_gadget == 2

    if event.type == pygame.KEYUP:
      right_paddle_vel = 0
      left_paddle_vel = 0
      second_left_paddle_vel = 0
      second_right_paddle_vel = 0

  #ball's movement controls
  if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
    ball_vel_y *= -1
  if dummy_ball_y <= 0 + radius or dummy_ball_y >= HEIGHT - radius:
    dummy_ball_vel_y *= -1
  if ball_x >= WIDTH - radius:
    ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
    dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
    second_left_paddle_y = left_paddle_y
    second_right_paddle_y = right_paddle_y
    direction = random.choice(directions)
    angle = random.choice(angles)
    if direction == 0:
      if angle == 0:
        ball_vel_y, ball_vel_x = -1.4, 0.7
        dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
      if angle == 1:
        ball_vel_y, ball_vel_x = -0.7, 0.7
        dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
      if angle == 2:
        ball_vel_y, ball_vel_x = -0.7, 1.4
        dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 1.4
    if direction == 1:
      if angle == 0:
        ball_vel_y, ball_vel_x = 1.4, 0.7
        dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
      if angle == 1:
        ball_vel_y, ball_vel_x = 0.7, 0.7
        dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 0.7
      if angle == 2:
        ball_vel_y, ball_vel_x = 0.7, 1.4
        dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 1.4
    ball_vel_x *= -1
    dummy_ball_vel_x *= -1

  if ball_x <= 0 + radius:
    ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
    dummy_ball_x, dummy_ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
    second_left_paddle_y = left_paddle_y
    second_right_paddle_y = right_paddle_y
    direction = random.choice(directions)
    angle = random.choice(angles)
    if direction == 0:
      if angle == 0:
        ball_vel_y, ball_vel_x = -1.4, 0.7
        dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
      if angle == 1:
        ball_vel_y, ball_vel_x = -0.7, 0.7
        dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
      if angle == 2:
        ball_vel_y, ball_vel_x = -0.7, 1.4
        dummy_ballall_vel_y, dummy_ballall_vel_x = -0.7, 1.4
    if direction == 1:
      if angle == 0:
        ball_vel_y, ball_vel_x = 1.4, 0.7
        dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
      if angle == 1:
        ball_vel_y, ball_vel_x = 0.7, 0.7
        dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 0.7
      if angle == 2:
        ball_vel_y, ball_vel_x = 0.7, 1.4
        dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 1.4
  
  #paddle's mouvement controls
  if left_paddle_y >= HEIGHT - paddle_height:
    left_paddle_y = HEIGHT - paddle_height
  if left_paddle_y <= 0:
    left_paddle_y = 0
  if right_paddle_y >= HEIGHT - paddle_height:
    right_paddle_y = HEIGHT - paddle_height
  if right_paddle_y <= 0:
    right_paddle_y = 0

  if second_left_paddle_y >= HEIGHT - paddle_height:
    second_left_paddle_y = HEIGHT - paddle_height
  if second_left_paddle_y <= 0:
    second_left_paddle_y = 0
  if second_right_paddle_y >= HEIGHT - paddle_height:
    second_right_paddle_y = HEIGHT - paddle_height
  if second_right_paddle_y <= 0:
    second_right_paddle_y = 0

  #collision
  #left
  if second_left_paddle_y == left_paddle_y:
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
      if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
        ball_x = left_paddle_x + paddle_width
        dummy_ball_x = left_paddle_x + paddle_width
        ball_vel_x *= -1
        dummy_ball_vel_x *= -1
  
  if second_left_paddle_y != left_paddle_y:
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
      if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
        ball_x = left_paddle_x + paddle_width
        dummy_ball_x = left_paddle_x + paddle_width
        ball_vel_x *= -1
        dummy_ball_vel_x *= -1
    
    if second_left_paddle_x <= ball_x <= second_left_paddle_x + paddle_width:
      if second_left_paddle_y <= ball_y <= second_left_paddle_y + paddle_height:
        ball_x = left_paddle_x + paddle_width
        dummy_ball_x = left_paddle_x + paddle_width
        ball_vel_x *= -1
        dummy_ball_vel_x *= -1

  #right
  if second_right_paddle_y == right_paddle_y:
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
      if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
        ball_x = right_paddle_x
        dummy_ball_x = right_paddle_x
        ball_vel_x *= -1
        dummy_ball_vel_x *= -1

  if second_right_paddle_y != right_paddle_y:
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
      if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
        ball_x = right_paddle_x
        dummy_ball_x = right_paddle_x
        ball_vel_x *= -1
        dummy_ball_vel_x *= -1

    if second_right_paddle_x <= ball_x <= second_right_paddle_x + paddle_width:
      if second_right_paddle_y <= ball_y <= second_right_paddle_y + paddle_height:
        ball_x = right_paddle_x
        dummy_ball_x = right_paddle_x
        ball_vel_x *= -1
        dummy_ball_vel_x *= -1

  #gadgets in action
  if gadget_pair == 1:
    if left_gadget == 1:
      if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
          ball_x = left_paddle_x + paddle_width
          ball_vel_x *= -3.5
          dummy_ball_vel_x *= -3.5
          left_gadget = 0
          left_gadget_remaining -= 1
    elif left_gadget == 2:
      left_paddle_y = ball_y
      left_gadget = 0
      left_gadget_remaining -= 1
    
    if right_gadget == 1:
      if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
          ball_x = right_paddle_x
          ball_vel_x *= -3.5
          dummy_ball_vel_x *= -3.5
          right_gadget = 0
          right_gadget_remaining -= 1
    elif right_gadget == 2:
      right_paddle_y = ball_y
      right_gadget = 0
      right_gadget_remaining -= 1

  elif gadget_pair == 2:
    if left_gadget == 1:
      if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
          ball_x = left_paddle_x + paddle_width
          dummy_ball_x = left_paddle_x + paddle_width
          ball_vel_x *= -1
          dummy_ball_vel_x *= -1
          dummy_ball_vel_y *= -1
          left_gadget = 0
          left_gadget_remaining -= 1

    elif left_gadget == 2:
      second_left_paddle_y = left_paddle_y + 200
      left_gadget = 0
      left_gadget_remaining -= 1
    
    if right_gadget == 1:
      if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
          ball_x = right_paddle_x
          dummy_ball_x = right_paddle_x
          ball_vel_x *= -1
          dummy_ball_vel_x *= -1
          dummy_ball_vel_y *= -1
          right_gadget = 0
          right_gadget_remaining -= 1
    
    elif right_gadget == 2:
      second_right_paddle_y = right_paddle_y + 200
      right_gadget = 0
      right_gadget_remaining -= 1

  #MOUVEMENT
  ball_x += ball_vel_x
  ball_y += ball_vel_y
  dummy_ball_x += dummy_ball_vel_x
  dummy_ball_y += dummy_ball_vel_y
  right_paddle_y += right_paddle_vel
  left_paddle_y += left_paddle_vel
  second_left_paddle_y += second_left_paddle_vel
  second_right_paddle_y += second_right_paddle_vel

  #OBJECTS
  pygame.draw.circle(window, BLUE, (ball_x, ball_y), radius)
  pygame.draw.rect(window, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
  pygame.draw.rect(window, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

  pygame.draw.circle(window, BLUE, (dummy_ball_x, dummy_ball_y), radius)

  pygame.draw.rect(window, RED, pygame.Rect(second_left_paddle_x, second_left_paddle_y, paddle_width, paddle_height))
  pygame.draw.rect(window, RED, pygame.Rect(second_right_paddle_x, second_right_paddle_y, paddle_width, paddle_height))

  if left_gadget == 1:
    pygame.draw.circle(window, WHITE, (left_paddle_x + 10, left_paddle_y + 10), 4)
  if right_gadget == 1:
    pygame.draw.circle(window, WHITE, (right_paddle_x + 10, right_paddle_y + 10), 4)

  pygame.display.update()
  #clock.tick(FPS)
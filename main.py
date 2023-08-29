import pygame

pygame.init()
clock = pygame.time.Clock()

#INITIALS
FPS = 60000
WIDTH, HEIGHT = 1000, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PyPong')

run = True

#COLORS
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

#BALL
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7

#PADDLES
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0

#main loop
while run:
  window.fill(BLACK)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        right_paddle_vel = -0.9
      if event.key == pygame.K_DOWN:
        right_paddle_vel = 0.9
      if event.key == pygame.K_z:
        left_paddle_vel = -0.9
      if event.key == pygame.K_s:
        left_paddle_vel = 0.9

    if event.type == pygame.KEYUP:
      right_paddle_vel = 0
      left_paddle_vel = 0

  #ball's movement controls
  if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
    ball_vel_y *= -1
  if ball_x >= WIDTH - radius:
    ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
    ball_vel_x *= -1
    ball_vel_y *= -1
  if ball_x <= 0 + radius:
    ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
    ball_vel_x, ball_vel_y = 0.7, 0.7
  
  #paddle's mouvement controls
  if left_paddle_y >= HEIGHT - paddle_height:
    left_paddle_y = HEIGHT - paddle_height
  if left_paddle_y <= 0:
    left_paddle_y = 0
  if right_paddle_y >= HEIGHT - paddle_height:
    right_paddle_y = HEIGHT - paddle_height
  if right_paddle_y <= 0:
    right_paddle_y = 0

  #MOUVEMENT
  ball_x += ball_vel_x
  ball_y += ball_vel_y
  right_paddle_y += right_paddle_vel
  left_paddle_y += left_paddle_vel

  #collision
  #left
  if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
    if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
      ball_x = left_paddle_x + paddle_width
      ball_vel_x *= -1
  #right
  if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
    if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
      ball_x = right_paddle_x
      ball_vel_x *= -1

  #OBJECTS
  pygame.draw.circle(window, BLUE, (ball_x, ball_y), radius)
  pygame.draw.rect(window, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
  pygame.draw.rect(window, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

  pygame.display.update()
  #clock.tick(FPS)
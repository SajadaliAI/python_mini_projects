import pygame
import random
pygame.init()

# Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screnn_width = 900
screen_height = 600

gameWindow=pygame.display.set_mode((screnn_width,screen_height))
pygame.display.set_caption("This game Iam Makking")
pygame.display.update()

game_exit = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 20
vilocity_x = 0
vilocity_y = 0
score = 0
init_velocity = 5
fps= 60
food_x = random.randint(20,int(screnn_width/2))
food_y = random.randint(20,int(screen_height/2))

clock = pygame.time.Clock()

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit =True
    
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                vilocity_x = init_velocity
                vilocity_y = 0

            if event.key==pygame.K_LEFT:
                vilocity_x = -init_velocity
                vilocity_y = 0    

            if event.key==pygame.K_UP:
                vilocity_y = -init_velocity
                vilocity_x = 0

            if event.key==pygame.K_DOWN:
                vilocity_y = init_velocity
                vilocity_x = 0 
    snake_x = snake_x + vilocity_x
    snake_y = snake_y + vilocity_y   
    if abs(snake_x - food_x)<7 and abs(snake_y - food_y)<7:
       score +=1  
       print("Score",score*10)
       food_x = random.randint(20,int(screnn_width/2))
       food_y = random.randint(20,int(screen_height/2))

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])  
    pygame.display.update()  
    clock.tick(fps)  
pygame.quit()
quit()            



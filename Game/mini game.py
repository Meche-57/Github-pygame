import pygame 
import sys

def game_timer():
    time = int(pygame.time.get_ticks()/1000) - start_time
    time_surf = font.render(f'{time}', False,'white')
    time_rect = time_surf.get_rect(topleft =(525,10))
    window.blit(time_surf,time_rect)


#window 
pygame.init()
clock = pygame.time.Clock() 
window_width = 600
window_height = 330
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Runner')

start_time = 0 


# fonts 

font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 100)
font3 = pygame.font.Font(None, 70)
font4 = pygame.font.Font(None, 40)


#surface
score = font.render('score:',False,'white')
timer = font.render('Time:',False,'white')
Over = font2.render('Game Over',False,'white')     # text information , false, colour
play_again = font3.render('Play Again?',False,'white') 
no= font4.render('No',False,'dark blue')
yes = font4.render('Yes(space for now)',False,'dark green')
fire = pygame.image.load('fire.png').convert_alpha()#removing alpha values and making the game run smoother as its easier for pygame to manage 
player = pygame.image.load('player_walk1.png').convert_alpha()
cave = pygame.image.load('cave.png').convert()
dirt = pygame.image.load('dirt2.png').convert()

# not needed anymore as we are using rect to simplify 
#fire_x_pos = 525
#fire_y_pos = 240
#player_x_pos = 200
#player_y_pos = 240

# rectangle 

player_rect = player.get_rect(midbottom = (20,0)) # adding rec around the surface # coordinate of rec too
fire_rect = fire.get_rect(bottomright= (660,320))
score_rect = score.get_rect(topleft = (10,10))
timer_rect = timer.get_rect(topleft=(400,10))
over_rect = Over.get_rect(topleft = (105,0))
play_again_rect = play_again.get_rect(topleft =(160,90))
yes_rect = yes.get_rect(topleft=(270,180))
no_rect = no.get_rect(topleft=(272,250))
player_gravity =  0

run = True
menu = False
game_start = True


while run:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    

    #if game_start: # makes avatar smoother if i place if statement here???
        
    if game_start:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_rect.bottom >= 300: #to check if player is on ground
                player_gravity = -15 # jumping illusion
                player_rect.x += 2
            if event.key == pygame.K_RIGHT:
                player_rect.x += 20
            if event.key == pygame.K_LEFT:
                player_rect.x -= 20
    
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                fire_rect.left = 600
                player_rect.left = 0
                game_start = True
                start_time = int(pygame.time.get_ticks()/ 1000)
    

    
    if game_start:
        window.blit(cave,(0,0))
        window.blit(dirt,(0,280))
        window.blit(score,score_rect)
        window.blit(timer,timer_rect)
        game_timer()
        
        # fire 
        fire_rect.left -= 2
        if fire_rect.left <= -100:
            fire_rect.left = 600 # is the screen
        window.blit(fire,fire_rect)
        
        
        player_gravity += 1 # increases gravity 
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        window.blit(player,player_rect)
        
        #fire hits player
        
        if fire_rect.colliderect(player_rect):
            game_start = False # game stops
    
    
    else:
        #game over screen soon
      
        window.fill('black')
        
        window.blit(Over,over_rect)
        window.blit(play_again, play_again_rect)
        window.blit(yes,yes_rect)
        window.blit(no,no_rect)





        
            
            
        
        
    
    



    pygame.display.update()
    clock.tick(60)


import pygame 
import sys
import time



#window 

pygame.init()
clock = pygame.time.Clock() 
window_width = 600
window_height = 330
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Runner')

def game_timer():
    time = int(pygame.time.get_ticks()/1000) - start_time
    time_surf = font.render(f'{time}', False,'white')
    time_rect = time_surf.get_rect(topleft =(300,10))
    window.blit(time_surf,time_rect)


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
player = pygame.image.load('player_1.png').convert_alpha()
cave = pygame.image.load('cave.png').convert()
dirt = pygame.image.load('dirt2.png').convert()
heart = pygame.image.load('heart.png').convert()
heart_2 = pygame.image.load('heart.png').convert()
heart_3 = pygame.image.load('heart.png').convert()



# not needed anymore as we are using rect to simplify
#fire_x_pos = 525
#fire_y_pos = 240
player_x_pos = 10
player_y_pos = 300
player_width = 37
player_height = 75

# rectangle 

player_rect = player.get_rect(bottomleft= (0,0))# adding rec around the surface # coordinate of rec too
fire_rect = fire.get_rect(bottomright= (0,280))
score_rect = score.get_rect(topleft = (10,10))
timer_rect = timer.get_rect(topleft=(200,10))
over_rect = Over.get_rect(topleft = (105,0))
play_again_rect = play_again.get_rect(topleft =(160,90))
yes_rect = yes.get_rect(topleft=(270,180))
no_rect = no.get_rect(topleft=(272,250))
heart_rect = heart.get_rect(topleft=(400,10))
heart_rect2 = heart.get_rect(topleft=(450,10))
heart_rect3 = heart.get_rect(topleft=(500,10))

heart_e = pygame.transform.scale(heart,(40,40))
heart_e2 = pygame.transform.scale(heart,(40,40))
heart_e3 = pygame.transform.scale(heart,(40,40))

player_gravity =  0


run = True
game_over = False
game_start = True



coin_image = pygame.image.load('coin.png').convert()
coin_e = pygame.transform.scale(coin_image,(40,40))

coins_rect = [
    pygame.Rect(150,100,60,60),
    pygame.Rect(50,100,60,60),
    pygame.Rect(200,100,60,60)
]


points = 0     
   

while run:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("RESETTED")
            fire_rect.left = 600
            player_rect.left = 0
            
            game_start = True
            
            start_time = int(pygame.time.get_ticks()/ 1000)
            points = 0 
            coins_rect = [
            pygame.Rect(150,100,60,60),
            pygame.Rect(50,100,60,60),
            pygame.Rect(200,100,60,60)
            ]


            for c in coins_rect: # for everY column / row in the list
                window.blit(coin_e,(c[0],c[1]))
    
            

       
    

    if game_start: # makes avatar smoother if i place if statement here???
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_rect.bottom >= 300: #to check if player is on ground
                player_gravity = -15 # jumping illusion
                player_rect.x += 10
            if event.key == pygame.K_RIGHT:
                player_rect.x += 10
            if event.key == pygame.K_LEFT:
                player_rect.x -= 10

        
            
    if game_start:
        window.blit(cave,(0,0))
        window.blit(dirt,(0,290))
        window.blit(score,score_rect)
        window.blit(timer,timer_rect)
        window.blit(player,player_rect)
        window.blit(heart_e,heart_rect)
        window.blit(heart_e2,heart_rect2)
        window.blit(heart_e3,heart_rect3)
        
        
        game_timer()
        
        for c in coins_rect: # for ever column / row in the list
            window.blit(coin_e,(c[0],c[1]))

            if c.colliderect(player_rect):
                coins_rect.remove(c)
                
                
                points = points + 1
        
        points_surf = font.render(f'{points}', False , 'white')
        points_rect = points_surf.get_rect(topleft = (100, 10))
        window.blit(points_surf,points_rect)
            
              
        
        # fire 
        fire_rect.left -= 2
        if fire_rect.left <= -100:
            fire_rect.left = 600 # is the screen
        window.blit(fire,fire_rect)
        
        
        player_gravity += 1  
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




# WHAT TO DO NEXT:
# modify size of fire_rect, probably modisize the players rect too ---> update fire ball ------------DONE 
# add image of coin and if player collide with coin score_count ___________________________DONE
# reset function 

 
 #iteration 2 
# learn how to do sprites to join the rect and surface into one class 
# spawn multiple fires using sprite 
#  work on animation for player using sprite


#updating of player
# fix problem of resetting while playing game when spacebar is pressed 
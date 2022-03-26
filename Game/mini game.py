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

start_time = 0 
player_gravity =  0
points = 0   

run = True
game_over = False
game_start = True



# fonts 

font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 100)
font3 = pygame.font.Font(None, 70)
font4 = pygame.font.Font(None, 40)



def game_timer():
    time = int(pygame.time.get_ticks()/1000) - start_time
    time_surf = font.render(f'{time}', False,'white')
    time_rect = time_surf.get_rect(topleft =(300,10))
    window.blit(time_surf,time_rect)


#surface                                                                             
score = font.render('score:',False,'white')
timer = font.render('Time:',False,'white')
Over = font2.render('Game Over',False,'white')     # text information , false, colour
play_again = font3.render('Play Again?',False,'white') 
no= font4.render('No',False,'dark blue')
yes = font4.render('Yes(press space)',False,'dark green')
fire = pygame.image.load('fire.png').convert_alpha()#removing alpha values and making the game run smoother as its easier for pygame to manage 
player = pygame.image.load('player_1.png').convert_alpha()
cave = pygame.image.load('cave.png').convert()
dirt = pygame.image.load('dirt2.png').convert()
heart = pygame.image.load('heart.png').convert()
heart_2 = pygame.image.load('heart.png').convert()
heart_3 = pygame.image.load('heart.png').convert()



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



heart_e = pygame.transform.scale(heart,(40,40)) # modificaton on image size 
heart_e2 = pygame.transform.scale(heart,(40,40))
heart_e3 = pygame.transform.scale(heart,(40,40))





# coin position using [lists]

coin_image = pygame.image.load('coin.png').convert()
coin_e = pygame.transform.scale(coin_image,(40,40))



  
   

while run:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # besides exit button you can utilize the esc key 
                pygame.quit()
                sys.exit()
        
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # As an option in gameover is pressing the SPC key to reset
            # All compenents in the level are redrawn (resetted) to 0 / original spawn place 
                                                                    
            fire_rect.left = 600
            player_rect.left = 0
            
            game_start = True # return to the main loop of game again 
            
            start_time = int(pygame.time.get_ticks()/ 1000) # /1000 to show only the seconds and minutes when increases ms show too
            
            points = 0 

            coins_rect = [
            pygame.Rect(150,100,60,60),
            pygame.Rect(50,100,60,60),
            pygame.Rect(200,100,60,60)
            ]


            for c in coins_rect: 
                window.blit(coin_e,(c[0],c[1])) # display coins 
    
            

       
    

     
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and player_rect.bottom >= 300: #to check if player is on ground
            player_gravity = -15 # replaces value 0 to -15 to go up screen
            player_rect.x += 10 # also adds to value x .... it doesnt crash with moevement to left
            print("UP") 
        if event.key == pygame.K_RIGHT:
            player_rect.x += 10
            print("Right")
        if event.key == pygame.K_LEFT:
            print("Left")
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

        coins_rect = [ 
            pygame.Rect(150,100,60,60),
            pygame.Rect(50,100,60,60),
            pygame.Rect(200,100,60,60)
            ]                                 # used a list to set multple coins and on where to place them 
            
        for c in coins_rect: # for every column / row in the list of coin_rect
            window.blit(coin_e,(c[0],c[1])) # display on screen
    
              
        
        for c in coins_rect: # for ever column / row in the list
            window.blit(coin_e,(c[0],c[1]))

            if c.colliderect(player_rect):
                coins_rect.remove(c)
                
                
                points = points + 1 # when coin is collected points increment by one 
        
        points_surf = font.render(f'{points}', False , 'white') # updates point 
        points_rect = points_surf.get_rect(topleft = (100, 10))
        window.blit(points_surf,points_rect) #display points 
            
              
        
        # fireball
        fire_rect.left -= 2 #moves the image -=2 speed 
        if fire_rect.left <= -100: # if the rect goes off screen
            fire_rect.left = 600 # returns to place 600
        window.blit(fire,fire_rect) # displays on window
        
        # when player jumps it returns to platform level

        player_gravity += 1  # when key pressed up pl
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: # when player x value exceeds 300 (which is ground) or equal to
            player_rect.bottom = 300 # player x goes back to platform
        window.blit(player,player_rect) # display player on window
        
        #collison with fireball
        
        if fire_rect.colliderect(player_rect):
            game_start = False # player dies and its game over which forwards it onto else
        
        
    
    
    else:
        #game over screen 
      
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
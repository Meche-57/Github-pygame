
import pygame
import sys
import time

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
 
# fonts used
font = pygame.font.Font(None, 100)
font_Timer= pygame.font.Font(None, 50)

#Menu options 
menu = 1
run_game = 2 
control = 3
game_over = 4


points = 0
lives = 3 

block_size = 50
coin_size = 50
fireball_size = 50
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))       
background = pygame.transform.scale(pygame.image.load("cave.jpg"),(SCREEN_WIDTH,SCREEN_HEIGHT))
heart = pygame.image.load('heart.png')
heart_2 = pygame.image.load('heart.png')
heart_3 = pygame.image.load('heart.png')
heart_e = pygame.transform.scale(heart,(40,40))
heart_e2 = pygame.transform.scale(heart_2,(40,40))
heart_e3 = pygame.transform.scale(heart_3,(40,40))
heart_rect = heart_e.get_rect(topleft=(0,10))
heart_rect2 = heart_e2.get_rect(topleft=(50,10))
heart_rect3 = heart_e3.get_rect(topleft=(100,10))


# timer 

def game_timer():

    start_time = 0
    time = int(pygame.time.get_ticks()/1000) - start_time
    time_surf = font_Timer.render(f'{time}', False,'white')
    time_rect = time_surf.get_rect(topleft =(850,10))
    timer_surf = font_Timer.render('Time:',False,'white')
    timer_rect = timer_surf.get_rect(topleft=(650,10))
    screen.blit(timer_surf,timer_rect)
    screen.blit(time_surf,time_rect)


# classes 

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.rect.topright = (x,y)

coin_group = pygame.sprite.Group() 




class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('fire.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.speed_l = -10
        
        
    def update(self):
        self.rect.x += self.speed_l # makes fireball move to left

        if self.rect.x <= -450: # when fireball goes off grid 
            
            self.rect.x = 2000 # respawns back to location 2000 which is at the far right 

         
fireball_g = pygame.sprite.Group()


platform_layout = [
    '                        ', # 0
    '                        ', # 1
    '            C  C      E  ', # 2
    '               B    ', # 3
    '        C               ', # 4
    '          B      E   C  ', # 5
    '       B    B        E         ', # 6 
    '  C  B   B        B     E ', # 7
    '                E  ', # 8 
    'C                  E      ', # 9 
    'B BBBBBBB BBBB  BBBBB BB' , ]# 10       # layout of level
    

class Level():
    

    def __init__(self, platform_layout):
        self.block_list = []
        
        row_count = 0 # location of row in block_list
        for row in platform_layout:
            col_count = 0
            for object in row:
                if object == 'C':
                    coin = Coin(col_count * coin_size , row_count * coin_size ) # coin x,y corresponding to col and row value
                    coin_group.add(coin)
                
              
                if object == 'B': 
                    dirt_surf = pygame.image.load('dirt.png') # load the image which would be the surf
                    dirt_rect = dirt_surf.get_rect() # rect is the images rect

                    dirt_rect.x = col_count * block_size # location of x 
                    dirt_rect.y = row_count * block_size # location of y block
                    block = (dirt_surf, dirt_rect) # bring both the rect and suf
                    self.block_list.append(block) # appends into the empty list of blocks

                    # if i added a class block it would dissapear when the player collides with it so i created the block variables here 
                
                if object == 'E':
                    fireball = Fireball(col_count * fireball_size, row_count * fireball_size) # block x,y corresponding to col and row value
                    fireball_g.add(fireball) # add fireball to the group


                col_count += 1 # goes through the column
            row_count += 1  # goes through the row

    def draw(self):
        
        for object in self.block_list:
                screen.blit(object[0], object[1]) # draws the obkects onto screen 
                
                

difficulty_1 = Level(platform_layout) 


class Player(pygame.sprite.Sprite):


    def __init__(self, x,y):
        super().__init__()
        self.is_animating_RIGHT = True # attribute for each animation in which is then further on used 
        self.is_animating_LEFT = True  # without them player wouldnt have any attributes 
        self.is_animating_ATTACK = True
        self.is_animating_UP = True
        

        self.gravity = 0 # creates an attribute for gravity


      
        self.sprite_U = [] # Up list

        self.sprite_U.append(pygame.image.load('player_0-4-1u.png'))
        self.sprite_U.append(pygame.image.load('player_0-4-2u.png'))
        self.sprite_U.append(pygame.image.load('player_0-4-3u.png'))
        self.sprite_U.append(pygame.image.load('player_0-4-4u.png'))

        self.current_sprite_U = 0
        self.image = self.sprite_U[self.current_sprite_U] # self.image would be whatever index the image sprite it is at 

        self.sprite_R = [] # Right list

        self.sprite_R.append(pygame.image.load('player_1-1.png'))
        self.sprite_R.append(pygame.image.load('player_1-2.png'))
        self.sprite_R.append(pygame.image.load('player_1-3.png'))
        self.sprite_R.append(pygame.image.load('player_1-4.png'))

        self.current_sprite_R = 0
        self.image = self.sprite_R[self.current_sprite_R]

        self.sprite_L = [] # LEFT list

        self.sprite_L.append(pygame.image.load('player_0-1.png'))
        self.sprite_L.append(pygame.image.load('player_0-3.png'))
        self.sprite_L.append(pygame.image.load('player_0-1.png'))
        self.sprite_L.append(pygame.image.load('player_0-3.png'))
       
        
        self.current_sprite_L = 0
        self.image = self.sprite_L[self.current_sprite_L]


        self.sprite_A = [] # Attack list

        self.sprite_A.append(pygame.image.load('player_0-1a.png'))
        self.sprite_A.append(pygame.image.load('player_0-2a.png'))
        self.sprite_A.append(pygame.image.load('player_0-3a.png'))
        self.sprite_A.append(pygame.image.load('player_0-4a.png'))
        

        self.current_sprite_A = 0
        self.image = self.sprite_A[self.current_sprite_A]


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width() # of the images when going left and colliding with a block platform
        self.height = self.image.get_height() # of the images so futher on when player colliding with blocks when it jumps up it wouldnt go straight through the block
        
    
    def animate_RIGHT(self):
        self.is_animating_RIGHT = True # THIS METHOD GETS CALLED WHEN CORRESPONDING KEY 
    
    def animate_UP(self):
        self.is_animating_UP = True # THIS METHOD GETS CALLED WHEN CORRESPONDING KEY 
        

    def animate_LEFT(self):
        self.is_animating_LEFT = True # THIS METHOD GETS CALLED WHEN CORRESPONDING KEY 
        
    def animate_ATTACK(self):
        self.is_animating_ATTACK  = True # THIS METHOD GETS CALLED WHEN CORRESPONDING KEY 
    
    
    
    

    def movement(self,speed):
        movement_x_pos = 0 # set attributes and player movements would be added onto the x and y 
        movement_y_pos = 0
        
        
        
        
        if self.is_animating_RIGHT == True:
            self.current_sprite_R += 0.1 # how fast each frame is processed 
            
            if self.current_sprite_R >= len(self.sprite_R): # if its longer than sprites appended onto list
                self.current_sprite_R = 0 # it resets to 0 
                self.is_animating_RIGHT = False # when the list of images have all been displayed it stops until animating is True
            
            self.image = self.sprite_R[int(self.current_sprite_R)]
        
        if self.is_animating_UP == True:
            self.current_sprite_U += 0.1
            
            if self.current_sprite_U>= len(self.sprite_U): 
                
                self.current_sprite_U = 0 
                self.is_animating_UP = False 
            
            self.image = self.sprite_U[int(self.current_sprite_U)]
            
            

        if self.is_animating_LEFT == True:
            self.current_sprite_L += 0.1
          
            if self.current_sprite_L >= len(self.sprite_L):
                self.current_sprite_L = 0
                self.is_animating_LEFT = False
            
            self.image = self.sprite_L[int(self.current_sprite_L)]

        if self.is_animating_ATTACK == True:
            self.current_sprite_A += 0.1

            if self.current_sprite_A >= len(self.sprite_A):
                self.current_sprite_A = 0 
                self.is_animating_ATTACK = False

            self.image = self.sprite_A[int(self.current_sprite_A)] 
        
        self.gravity += 1 # gravity is always on 
        movement_y_pos += self.gravity #movement_y_pos + gravity to pull down character when jump
         
        
        for block in difficulty_1.block_list: # difficulty_1 inherits data from difficulty_1 group which includes block_list attribute
             
            if block[1].colliderect(self.rect.x, self.rect.y + movement_y_pos, self.width, self.height):
                movement_y_pos = 0
               
               
                
                if self.gravity >= 0:
                    movement_y_pos = block[1].top - self.rect.bottom #movement_y_pos which is updated with the top of the dirtblock - the bottom of player to keep the player on block
                    self.gravity = 0 # as players.y is on block we make gravity 0 to show its on ground
                    

        print(self.gravity)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.animate_RIGHT()
                    movement_x_pos += 20
                
                
                if event.key == pygame.K_RIGHT and event.key == pygame.K_UP:
                    player.animate_UP()
                    player.animate_RIGHT()
                    movement_x_pos -= 40
                    movement_y_pos -= 50

                if event.key == pygame.K_LEFT:
                    player.animate_LEFT()
                    movement_x_pos -= 20

                if event.key == pygame.K_UP:
                        player.animate_UP()
                        movement_y_pos -= 50
                
                if event.key == pygame.K_LEFT and event.key == pygame.K_UP:
                    player.animate_UP()
                    player.animate_LEFT()
                    movement_x_pos += 40
                    movement_y_pos -= 50

                if event.key == pygame.K_e:
                    player.animate_ATTACK()
                    #player.damage = kill()
                    print("attack") 
                            
            
     
     
        self.rect.x += movement_x_pos # adds on value to move
        self.rect.y += movement_y_pos  # adds on y value to move 

        if self.rect.y > 700: # off platform through a gap
            self.rect.x = 40 
            self.rect.y = 100 # player appears back at locations given
            
    
    
player_sprite = pygame.sprite.Group()
player = Player(0,0) # location x,y constantly gets updated player such as gravity and platform collisions
player_sprite.add(player) # add player data onto player_group 


# Menu background and con

start_back = pygame.transform.scale(pygame.image.load('start_back.png'),(SCREEN_WIDTH,SCREEN_HEIGHT))
control_info = pygame.transform.scale(pygame.image.load('control.png'),(SCREEN_WIDTH,SCREEN_HEIGHT))



Game_Over = font.render('Game Over',False,'white')
Gameover_rect = Game_Over.get_rect(topleft = (300,240))




score = font_Timer.render('score:',False,'white')
score_rect = score.get_rect(bottomright = (790,590))

    
class game_status(): 
    def __init__(self):
        self.points = 0
        self.timer = 0 
    
status = game_status()

                    


while menu != run_game :

    game_start = font.render('START GAME',False,'White')    #start Game displayed on window 
    game_start_rect= game_start.get_rect(topleft = (260,90))
    screen.blit(start_back,(0,0))
    screen.blit(game_start,game_start_rect)

    Control = font.render('Controls',False,'White')      #Controls Game displayed on window      
    control_rect = Control.get_rect(topleft = (265,230))
    screen.blit(Control,control_rect)
    
    Exit = font.render('Exit',False,'White')           #Exit Game displayed on window 
    Exit_rect = Control.get_rect(topleft = (260,370))
    
    screen.blit(Exit,Exit_rect)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        
                
                
        if event.type ==  pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if control_rect.collidepoint(mouse_pos):
                menu == control
                screen.blit(control_info,(0,0))  # will display the controls menu 
            
            if Exit_rect.collidepoint(mouse_pos):
                menu == pygame.quit()             # when pressed the exit button the game closes 
        
            if game_start_rect.collidepoint(mouse_pos):
        
                start_timer = 0
                menu == run_game
            
                     # The run_game loop with start 
        
        
   
                 
            while run_game == 2:
                

                screen.blit(background,(0,0))
                game_timer()
                difficulty_1.draw()
                screen.blit(score,score_rect)

                player_sprite.draw(screen)

                fireball_g.update()
                fireball_g.draw(screen)
                coin_group.draw(screen)
                player.movement(20) # all of players movements and updates

                                    
                            
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                
                


                if pygame.sprite.spritecollide(player, coin_group, True):
                    points =  points + 1
                    print(points)
                                    
                
                points_surf = font_Timer.render(f'{points}', False , 'white')
                points_rect = points_surf.get_rect(bottomright = (850,590))
                screen.blit(points_surf,points_rect)
                
                    
            
                if lives ==  3:
                    screen.blit(heart_e,heart_rect)
                    screen.blit(heart_e2,heart_rect2)
                    screen.blit(heart_e3,heart_rect3)



                if pygame.sprite.spritecollide(player, fireball_g, True):
                    lives = lives - 1
                    


                if lives == 2:
                    screen.blit(heart_e2,heart_rect2)
                    screen.blit(heart_e3,heart_rect3)

                if lives == 1:
                    screen.blit(heart_e3,heart_rect3)

                if lives == 0:
                   
                    run_game == game_over()
                


                pygame.display.update()
                clock.tick(60)
                            
            
        pygame.display.update()
                
            

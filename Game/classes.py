
import pygame
import sys

pygame.font.init()
clock = pygame.time.Clock()
 

font = pygame.font.Font(None, 100)
font_Timer= pygame.font.Font(None, 50)

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


tile_size = 50
coin_size = 50
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



class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.rect.topright = (x,y)
    

class Fireball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('fire.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.move_l = -10
        
        
    def update(self):
        self.rect.x += self.move_l

        if self.rect.x <= -450:
            print(self.rect.x)
            self.rect.x = 2000

        

    
       
coin_group = pygame.sprite.Group()
fireball_g = pygame.sprite.Group()


level_data = [
    '                        ', # 0
    '                        ', # 1
    '            C  C      E  ', # 2
    '               B    ', # 3
    '        C               ', # 4
    '          B      E   C  ', # 5
    '       B    B        E         ', # 6 
    '  C     B        B     E ', # 7
    '     B           E  ', # 8 
    'C                  E      ', # 9 
    'B BBBBBBB BBBB  BBBBB BB' , ]# 10
    

class Level():
    

    def __init__(self, level_data):
        self.block_list = []
        

        grass_img = pygame.image.load('dirt.png')

        row_count = 0
        for row in level_data:
            col_count = 0
            for tile in row:
                if tile == 'C':
                    coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    coin_group.add(coin)
                
              


                    
                
                if tile == 'B':
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.block_list.append(tile)
                
                if tile == 'E':
                    fireball = Fireball(col_count * tile_size,row_count * tile_size + 20)
                    fireball_g.add(fireball)


                col_count += 1
            row_count += 1

    def draw(self,):
        
        for tile in self.block_list:
                screen.blit(tile[0], tile[1])
                
                
                
                
    

#Player 

world = Level(level_data) # platform set up is the surface and becomes the platform_data






class Player(pygame.sprite.Sprite):


    def __init__(self, x,y):
        super().__init__()
        self.is_animating_RIGHT = True
        self.is_animating_LEFT = True
        self.is_animating_ATTACK = True
        self.is_animating_UP = True

        self.jump = False
        self.gravity = 0 
        
       
        x = 0
        y = 0
       
        
        self.sprite_R = []
        self.sprite_L = []
        self.sprite_A = []
        self.sprite_U = []

        self.sprite_U.append(pygame.image.load('player_0-4-1u.png'))
        self.sprite_U.append(pygame.image.load('player_0-4-2u.png'))
        self.sprite_U.append(pygame.image.load('player_0-4-3u.png'))
        self.sprite_U.append(pygame.image.load('player_0-4-4u.png'))

        self.current_sprite_U = 0
        self.image = self.sprite_U[self.current_sprite_U]

        self.sprite_R.append(pygame.image.load('player_1-1.png'))
        self.sprite_R.append(pygame.image.load('player_1-2.png'))
        self.sprite_R.append(pygame.image.load('player_1-3.png'))
        self.sprite_R.append(pygame.image.load('player_1-4.png'))

        self.current_sprite_R = 0
        self.image = self.sprite_R[self.current_sprite_R]

        self.sprite_L.append(pygame.image.load('player_0-1.png'))
        self.sprite_L.append(pygame.image.load('player_0-3.png'))
        self.sprite_L.append(pygame.image.load('player_0-1.png'))
        self.sprite_L.append(pygame.image.load('player_0-3.png'))
       
        

        self.current_sprite_L = 0
        self.image = self.sprite_L[self.current_sprite_L]

        self.sprite_A.append(pygame.image.load('player_0-1a.png'))
        self.sprite_A.append(pygame.image.load('player_0-2a.png'))
        self.sprite_A.append(pygame.image.load('player_0-3a.png'))
        self.sprite_A.append(pygame.image.load('player_0-4a.png'))
        

        self.current_sprite_A = 0
        self.image = self.sprite_A[self.current_sprite_A]


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
    
    def animate_RIGHT(self):
        self.is_animating_RIGHT = True
    
    def animate_UP(self):
        self.is_animating_UP = True
        

    def animate_LEFT(self):
        self.is_animating_LEFT = True
        
    def animate_ATTACK(self):
        self.is_animating_ATTACK  = True
    
    

    def movement(self,speed):
        movement_x = 0
        movement_y = 0
        
        if self.is_animating_RIGHT == True:
            self.current_sprite_R += 0.1 # how fast each frame
            
            if self.current_sprite_R >= len(self.sprite_R):
                self.current_sprite_R = 0
                self.is_animating_RIGHT = False # when the list of images have all been displayed it stops 
            
            self.image = self.sprite_R[int(self.current_sprite_R)]
        
        if self.is_animating_UP == True:
            self.current_sprite_U += 0.1
            

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
        
        self.gravity += 1
        if self.gravity > 10:
            self.gravity = 10
        movement_y += self.gravity

        for tile in world.block_list:
           
            if tile[1].colliderect(self.rect.x + movement_x, self.rect.y, self.width, self.height):  #check for collision in x direction
                movement_x = 0
            
            if tile[1].colliderect(self.rect.x, self.rect.y + movement_y, self.width, self.height):
                movement_y = 0 #check for collision in y direction
                
                if self.gravity < 0:
                    movement_y = tile[1].bottom - self.rect.top
                    self.gravity = 1
                
                elif self.gravity >= 0:
                    movement_y = tile[1].top - self.rect.bottom
                    self.gravity = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.animate_RIGHT()
                    movement_x += 20

                if event.key == pygame.K_LEFT:
                    player.animate_LEFT()
                    movement_x -= 20

                if event.key == pygame.K_UP and self.jump == False:
                     player.animate_UP()
                     movement_y -= 20
                     self.jump == True
                
                if event.key == pygame.K_UP:
                    self.jump == False

                if event.key == pygame.K_e:
                    player.animate_ATTACK()
                    print("attack") 
                     
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
     
     
        self.rect.x += movement_x # updates both coordinates
        self.rect.y += movement_y

        if self.rect.y > 700:
            self.rect.x = 40 
            self.rect.y = 100
    
    


player_sprite = pygame.sprite.Group()
player = Player(0,575)
player_sprite.add(player)



# Coins

start_back = pygame.transform.scale(pygame.image.load('start_back.png'),(SCREEN_WIDTH,SCREEN_HEIGHT))
control_back = pygame.transform.scale(pygame.image.load('control.png'),(SCREEN_WIDTH,SCREEN_HEIGHT))



Game_Over = font.render('Game Over',False,'white')
Gameover_rect = Game_Over.get_rect(topleft = (300,240))


menu = 1
run_game = 2 
control = 3


lives = 3 

score = font_Timer.render('score:',False,'white')
score_rect = score.get_rect(bottomright = (790,590))



while menu != run_game:

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
                screen.blit(control_back,(0,0))  # will display the controls menu 
            
            if Exit_rect.collidepoint(mouse_pos):
                menu == pygame.quit()             # when pressed the exit button the game closes 
        
            if game_start_rect.collidepoint(mouse_pos):
                menu == run_game
                run_game = True                   # The run_game loop with start 
            
            
                

               
                
                while run_game:

                    
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit

                    points = 0
                    points_surf = font_Timer.render(f'{points}', False , 'white')
                    points_rect = points_surf.get_rect(bottomright = (850,590))
                    
                   

                    screen.blit(background,(0,0))
                    game_timer()
                    world.draw()
                    screen.blit(score,score_rect)
                    screen.blit(points_surf,points_rect)
                    player_sprite.draw(screen)
                    
                    fireball_g.update()
                    fireball_g.draw(screen)
                    coin_group.draw(screen)
                    player.movement(20)
                    
                   
                    
                 
                    
                    if pygame.sprite.spritecollide(player, coin_group, True):
                        points = points + 1
                        print(points)
                       
                        
                    

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
                        run_game = False

                
        


        
                    pygame.display.update()
                    clock.tick(60)
                
                else:
                    
                    
                    #game over screen soon
      
                    screen.fill('black')
                
                    screen.blit(Game_Over,Gameover_rect)
                    

        
                
        pygame.display.update()
        
    

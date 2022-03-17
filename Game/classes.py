
import pygame
import sys

pygame.font.init()
clock = pygame.time.Clock()
start_time = 0 

# timer 

def game_timer():
    time = int(pygame.time.get_ticks()/1000) - start_time
    time_surf = font_Timer.render(f'{time}', False,'white')
    time_rect = time_surf.get_rect(topleft =(750,10))
    screen.blit(time_surf,time_rect)


font = pygame.font.Font(None, 100)
font_Timer= pygame.font.Font(None, 50)
timer = font_Timer.render('Time:',False,'white')
timer_rect = timer.get_rect(topright=(700,10))


#screen stuff
platform_set_up = [
'                        ', # 0
'                        ', # 1
'                      ', # 2
'                 B    ', # 3
'           C          ', # 4
'          B             ', # 5
'       C                  ', # 6 
'     BB       B         ', # 7
'    B                  ', # 8 
' B          C      C         ', # 9 
'  BBBBBBBB  BBBBB BB' , ]# 10


tile_size = 55
coin_size = 50


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))       
background = pygame.transform.scale(pygame.image.load("cave.jpg"),(SCREEN_WIDTH,SCREEN_HEIGHT))




class Block(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('white')
  
        self.rect = self.image.get_rect(topright = pos)


class Coin(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topright = pos)


class Level:

    def __init__(self, platform_data ,surface):
        self.display_surface = surface
        self.setup_level(platform_data)
    
    def setup_level(self,setup):
        
        self.blocks = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
       
        
        for row_index ,row in enumerate(setup): #what row we have and where it is
            for col_index,col in enumerate(row): 
                if col == 'B':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    block = Block((x,y),tile_size)
                
                    self.blocks.add(block)
                
                if col == 'C':
                    x = col_index * coin_size
                    y = row_index * coin_size
                    coin = Coin((x,y),coin_size)

                    self.coins.add(coin)


        
                #print(f'{row_index},{col_index}:{col}')  #shows the coordinates of where EACH OF B in platform_set_up are located

    
    def run(self):
        self.blocks.draw(self.display_surface)
        self.coins.draw(self.display_surface)

#Player 

level = Level(platform_set_up,screen) # platform set up is the surface and becomes the platform_data

class Player(pygame.sprite.Sprite):

    


    def __init__(self, pos_x,pos_y):
        super().__init__()
        self.is_animating = True
        self.is_animating_2 = True
        self.is_animating_3 = True 
        pos_x = 0
        pos_y = 500
        self.sprite_R = []
        self.sprite_L = []
        self.sprite_A = []

        self.sprite_R.append(pygame.image.load('player_0.png'))
        self.sprite_R.append(pygame.image.load('player_1.png'))
        self.sprite_R.append(pygame.image.load('player_2.png'))
        self.sprite_R.append(pygame.image.load('player_3.png'))

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
        self.rect.bottomleft = [pos_x,pos_y]
    
    def animate(self):
        self.is_animating = True
        
        

    def animate_2(self):
        self.is_animating_2 = True
        
    def animate_3(self):
        self.is_animating_3  = True

    def update(self,speed):
        
        if self.is_animating == True:
            self.current_sprite_R += 0.1 # how fast each frame
            self.rect.right += 1
            
        
            if self.current_sprite_R >= len(self.sprite_R):
                self.current_sprite_R = 0
                self.is_animating = False # when the list of images have all been displayed it stops 
            
            self.image = self.sprite_R[int(self.current_sprite_R)]

        if self.is_animating_2 == True:
            self.current_sprite_L += 0.1
            self.rect.left -= 1
            
            
            if self.current_sprite_L >= len(self.sprite_L):
                self.current_sprite_L = 0
                self.is_animating_2 = False
            
            self.image = self.sprite_L[int(self.current_sprite_L)]

        if self.is_animating_3 == True:
            self.current_sprite_A += 0.2

            if self.current_sprite_A >= len(self.sprite_A):
                self.current_sprite_A = 0 
                self.is_animating_3 = False

            self.image = self.sprite_A[int(self.current_sprite_A)]   

player_sprite = pygame.sprite.Group()
player = Player(0,575)
player_sprite.add(player)


# Fireball

class Fireball(pygame.sprite.Sprite):# sprite is a rect and surf in one class
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('fire.png')
        self.rect = self.image.get_rect(bottomright = (750,450))
        self.x = 750
        self.y = 450
    
        
        

fire_ball= Fireball()
fire_ball_g = pygame.sprite.Group()
fire_ball_g.add(fire_ball)




control = 3
start = 2
menu = 1
# Coins

start_back = pygame.transform.scale(pygame.image.load('start_back.png'),(SCREEN_WIDTH,SCREEN_HEIGHT))
control_back = pygame.transform.scale(pygame.image.load('control.png'),(SCREEN_WIDTH,SCREEN_HEIGHT))









while menu != start:

    game_start = font.render('START GAME',False,'White') 
    game_start_rect= game_start.get_rect(topleft = (260,90))
    screen.blit(start_back,(0,0))
    screen.blit(game_start,game_start_rect)

    Control = font.render('Controls',False,'White')
    control_rect = Control.get_rect(topleft = (265,230))
    Exit = font.render('Exit',False,'White')
    Exit_rect = Control.get_rect(topleft = (260,370))
    screen.blit(Control,control_rect)
    screen.blit(Exit,Exit_rect)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
                
        if event.type ==  pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if control_rect.collidepoint(mouse_pos):
                menu == control
                screen.blit(control_back,(0,0))
            
            if Exit_rect.collidepoint(mouse_pos):
                menu == pygame.quit()
        
            if game_start_rect.collidepoint(mouse_pos):
                menu == start
            
            
                

               
                
                while start:

                    screen.blit(background,(0,0))
                    screen.blit(timer,timer_rect)
                    game_timer()
                    #mult_fireball.draw(screen)
                   


                    player_sprite.draw(screen)
                    player.update(10)
                    level.run()
                    fire_ball_g.draw(screen) # screen.blit doesnt work on sprites
                    pygame.display.update()
                    clock.tick(60)







                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RIGHT:
                                player.animate()

                            if event.key == pygame.K_LEFT:
                                player.animate_2()
                            if event.key == pygame.K_UP:
                                print("Up")
                            
                            if event.key == pygame.K_e:
                                player.animate_3()
                                print("attack")
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit
                
        pygame.display.update()
        
    

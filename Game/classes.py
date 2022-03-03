import pygame
import sys

pygame.font.init()

# timer 

def game_timer():
    time = int(pygame.time.get_ticks()/1000) - start_time
    time_surf = font.render(f'{time}', False,'white')
    time_rect = time_surf.get_rect(topleft =(750,10))
    screen.blit(time_surf,time_rect)


font = pygame.font.Font(None, 30)

timer = font.render('Time:',False,'white')
timer_rect = timer.get_rect(topright=(700,10))

 


clock = pygame.time.Clock()
start_time = 0 

#screen stuff
platform_set_up = [
'                        ', # 0
'                        ', # 1
'                  C     ', # 2
'          C              ', # 3
'                  B     ', # 4
'          B             ', # 5
'                        ', # 6 
'     BB       B         ', # 7
'    B                  ', # 8 
' B       C               ', # 9 
'   BBBBBBBB  BBBBB',
'                        ',]# 10


tile_size = 64
coin_size = 10


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = len(platform_set_up)*tile_size


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))       

background = pygame.transform.scale(pygame.image.load("cave.jpg"),(SCREEN_WIDTH,SCREEN_HEIGHT))



class Block(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        block_img = pygame.image.load('dirt.png').convert()
        self.image.fill('white')
        #self.image.append(block_img)
        self.rect = self.image.get_rect(topright = pos)

block = pygame.sprite.Group(Block((250,275),104))

#class Coin(pygame.sprite.Sprite):
    #def __init__(self,pos,size):
        #super().__init__()
        #self.image = pygame.Surface((size,size))
        #coin_img = pygame.image.load('dirt.png').convert()
        #self.image.fill('yellow')
        #self.image.append(block_img)
        #self.rect = self.image.get_rect(topright = pos)

#coin = pygame.sprite.Group((Coin(250,275),184))        


  

class Level:

    def __init__(self, level_data ,surface):
        self.display_surface = surface
        self.setup_level(level_data)
    
    def setup_level(self,setup):
        self.blocks = pygame.sprite.Group()
       
        
        for row_index ,row in enumerate(setup): #what row we have and where it is
            for col_index,col in enumerate(row): 
                if col == 'B':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    block = Block((x,y),tile_size)
                
                    self.blocks.add(block)
                #if col == 'B':
                    #x = col_index * coin_size
                    #y = row_index * coin_size
                    #coin = Coin((x,y),tile_size)

                    #self.coin.add(coin)  
                #print(f'{row_index},{col_index}:{col}')  shows the coordinates of where EACH OF B in platform_set_up are located

    
    def run(self):
        self.blocks.draw(self.display_surface)

#Player 

level = Level(platform_set_up,screen) # platform set up is the surface and becomes the level_data

class Player(pygame.sprite.Sprite):

    def __init__(self, pos_x,pos_y):
        super().__init__()
        self.is_animating = True
        self.is_animating_2 = True
        self.is_animating_3 = True 
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
        self.sprite_L.append(pygame.image.load('player_0-2.png'))
        self.sprite_L.append(pygame.image.load('player_0-3.png'))
        self.sprite_L.append(pygame.image.load('player_0-4.png'))

        self.current_sprite_L = 0
        self.image = self.sprite_L[self.current_sprite_L]

        self.sprite_A.append(pygame.image.load('player_0-1a.png'))
        self.sprite_A.append(pygame.image.load('player_0-2a.png'))
        self.sprite_A.append(pygame.image.load('player_0-3a.png'))
        self.sprite_A.append(pygame.image.load('player_0-4a.png'))
        

        self.current_sprite_A = 0
        self.image = self.sprite_A[self.current_sprite_A]


        pos_x = 300
        pos_y = 300
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
        
            if self.current_sprite_R >= len(self.sprite_R):
                self.current_sprite_R = 0
                self.is_animating = False # when the list of images have all been displayed it stops 
            
            self.image = self.sprite_R[int(self.current_sprite_R)]

        if self.is_animating_2 == True:
            self.current_sprite_L += 0.1
            
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
    
    def movement(self):

        self.x -= 2
        
        #self.poof = pygame.mixer.Sound("poof.wav")

fire_ball= Fireball()
fire_ball_g = pygame.sprite.Group()
fire_ball_g.add(fire_ball)


#multiple fireballs 
#mult_fireball = pygame.sprite.Group()

#for fire in range(5):
    #fireballs = Fireball('fire.png',random.randrange(0,screen_width),random.randrange(0,screen_height))
    #mult_fireball.add(fireballs)



# Coins

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect(topright =(150,275))
        
        

coin = Coins()
coin_g = pygame.sprite.Group()
coin_g.add(coin)

def reset():
    
    screen.blit(background,(0,0))
    screen.blit(timer,timer_rect)
    game_timer()
    #mult_fireball.draw(screen)
    fire_ball_g.draw(screen) # screen.blit doesnt work on sprites
    
    
    player_sprite.draw(screen)
    player.update(0.5)
    level.run()
    

    coin_g.draw(screen)
    
   
    pygame.display.update()

        
player_vel = 4

while True:

    reset()
    
    
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
    
    
    
    clock.tick(100)

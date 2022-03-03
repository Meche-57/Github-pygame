import pygame



class Player_info:
    player_total_points = 0 



    def __init__(self,player):
        self.player = player
    
    def add_points(cls):
        cls.player_total_points +=1
    
    def total_num_points(cls):
        return cls.player_total_points



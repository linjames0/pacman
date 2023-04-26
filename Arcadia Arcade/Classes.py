import pygame
import random

class Player:

    def __init__(self):
        self.speed = 2
        self.velocity = [0,0]
        self.origin = (300,60)
        self.pos = [self.origin[0], self.origin[1]]
        self.color = (255,255,0)

        # collision stuff
        self.sprite_size = 20
        self.hitbox = pygame.Rect(self.pos[0]-5, self.pos[1]-5, self.sprite_size/2, self.sprite_size/2)
        self.spawning = True
        self.timer = pygame.time.get_ticks()

        # game stats
        self.score = 0
        self.lives = 3

    def update(self, keys, check_boundary):
        if not self.spawning:
            if self.pos[1] % 20 == 0:
                if keys[pygame.K_LEFT] and sum(check_boundary(self.pos, [-self.speed, 0])) != 0:   # checks if pacman bumps into a wall by checking the velocity
                    self.velocity = [-self.speed, 0]
                elif keys[pygame.K_RIGHT] and sum(check_boundary(self.pos, [self.speed, 0])) != 0:  # checks if pacman bumps into a wall by checking the velocity
                    self.velocity = [self.speed, 0]
            if self.pos[0] % 20 == 0:
                if keys[pygame.K_UP] and sum(check_boundary(self.pos, [0, -self.speed])) != 0: # checks if pacman bumps into a wall by checking the velocity
                    self.velocity = [0, -self.speed]
                elif keys[pygame.K_DOWN] and sum(check_boundary(self.pos, [0, self.speed])) != 0: # checks if pacman bumps into a wall by checking the velocity
                    self.velocity = [0, self.speed]


        self.pos = [sum(x) for x in zip(self.pos, self.velocity)]
        self.hitbox.update(self.pos[0]-5, self.pos[1]-5, self.sprite_size/2, self.sprite_size/2)

        check_boundary(self.pos, self.velocity)

    def get_x_pos(self):
        return self.pos[0]
    
    def get_y_pos(self):
        return self.pos[1]
    
    def get_color(self):
        return self.color
    
    def get_sprite_size(self):
        return self.sprite_size
    
    def get_hitbox(self):
        return self.hitbox
    
    def get_origin(self):
        return self.origin
    
    def collect_points(self, collected_points):
        self.score += collected_points
    
    def get_score(self):
        return self.score
    
    def set_score(self, score):
        self.score = score
    
    def get_lives(self):
        return self.lives
    
    def set_lives(self, lives):
        self.lives = lives

    def get_spawning(self):
        return self.spawning
    
    def set_spawning(self, spawning):
        self.spawning = spawning

    def get_timer(self):
        return self.timer

    def respawn(self):
        self.lives -= 1
        self.velocity = [0,0]
        self.pos = [self.origin[0], self.origin[1]]
        self.timer = pygame.time.get_ticks()
        self.hitbox.update(self.pos[0]-5, self.pos[1]-5, self.sprite_size/2, self.sprite_size/2)
        self.spawning = True

class Enemy:
    def __init__(self, color, direction, spawn_point):
        self.speed = 2
        self.velocity = [0,0]
        self.origin = spawn_point
        self.pos = [self.origin[0], self.origin[1]]
        self.color = color

        # collision stuff
        self.sprite_size = 20
        self.hitbox = pygame.Rect(self.pos[0]-5, self.pos[1]-5, self.sprite_size/2, self.sprite_size/2)

        # relevant mutable properties
        self.is_active = False     # inactive if in spawn
        self.is_leaving = False
        self.is_vulnerable = False      # vulnerable if a special orb is collected
        self.is_controlled = False
        self.direction = direction
        self.timer = pygame.time.get_ticks()

        # game stats
        self.kills = 0
        self.deaths = 0

    def update(self, intersections, keys, check_boundary):
        if not self.is_active and not self.is_leaving:
            if self.direction == "LEFT" and sum(check_boundary(self.pos, [-self.speed, 0])) == 0:
                self.direction = "UP"

            elif self.direction == "UP" and sum(check_boundary(self.pos, [0, -self.speed])) == 0:
                self.direction = "RIGHT"

            elif self.direction == "RIGHT" and sum(check_boundary(self.pos, [self.speed, 0])) == 0:
                self.direction = "DOWN"

            elif self.direction == "DOWN" and sum(check_boundary(self.pos, [0, self.speed])) == 0:
                self.direction = "LEFT"

        elif self.is_leaving:
            if sum(check_boundary(self.pos, self.velocity)) == 0:
                self.direction = random.choice(["LEFT", "RIGHT"])
                self.is_leaving = False
                self.is_active = True

        elif self.is_active:
            if sum(check_boundary(self.pos, self.velocity)) == 0:
                if self.direction == "LEFT":
                    self.change_direction("LEFT")
                elif self.direction == "RIGHT":
                    self.change_direction("RIGHT")
                elif self.direction == "UP":
                    self.change_direction("UP")
                elif self.direction == "DOWN":
                    self.change_direction("DOWN")
            elif (self.pos[0], self.pos[1]) in intersections:
                self.change_direction()


            # if sum(check_boundary(self.pos, [-self.speed, 0])) == 0:
            #     self.change_direction("LEFT")
            # elif sum(check_boundary(self.pos, [self.speed, 0])) == 0:
            #     self.change_direction("RIGHT")
            # elif sum(check_boundary(self.pos, [0, -self.speed])) == 0:
            #     self.change_direction("UP")
            # elif sum(check_boundary(self.pos, [0, self.speed])) == 0:
            #     self.change_direction("DOWN")
            
        if self.direction == "LEFT":
            self.velocity = [-self.speed, 0]
        elif self.direction == "RIGHT":
            self.velocity = [self.speed, 0]
        elif self.direction == "UP":
            self.velocity = [0, -self.speed]
        elif self.direction == "DOWN":
            self.velocity = [0, self.speed]

        check_boundary(self.pos, self.velocity)


            # if self.pos[1] % 20 == 0:
            #     if self.direction == "LEFT" and sum(check_boundary(self.pos, [-self.speed, 0])) != 0:   # checks if pacman bumps into a wall by checking the velocity
            #         self.velocity = [-self.speed, 0]
            #     elif self.direction == "RIGHT" and sum(check_boundary(self.pos, [self.speed, 0])) != 0:  # checks if pacman bumps into a wall by checking the velocity
            #         self.velocity = [self.speed, 0]
            # if self.pos[0] % 20 == 0:
            #     if self.direction == "UP" and sum(check_boundary(self.pos, [0, -self.speed])) != 0: # checks if pacman bumps into a wall by checking the velocity
            #         self.velocity = [0, -self.speed]
            #     elif self.direction == "DOWN" and sum(check_boundary(self.pos, [0, self.speed])) != 0: # checks if pacman bumps into a wall by checking the velocity
            #         self.velocity = [0, self.speed]

       

        # player controls for the enemies
        # if self.pos[1] % 20 == 0:
        #     if keys[pygame.K_LEFT] and sum(check_boundary(self.pos, [-self.speed, 0])) != 0:   # checks if pacman bumps into a wall by checking the velocity
        #         self.velocity = [-self.speed, 0]
        #     elif keys[pygame.K_RIGHT] and sum(check_boundary(self.pos, [self.speed, 0])) != 0:  # checks if pacman bumps into a wall by checking the velocity
        #         self.velocity = [self.speed, 0]
        # if self.pos[0] % 20 == 0:
        #     if keys[pygame.K_UP] and sum(check_boundary(self.pos, [0, -self.speed])) != 0: # checks if pacman bumps into a wall by checking the velocity
        #         self.velocity = [0, -self.speed]
        #     elif keys[pygame.K_DOWN] and sum(check_boundary(self.pos, [0, self.speed])) != 0: # checks if pacman bumps into a wall by checking the velocity
        #         self.velocity = [0, self.speed]
        
        self.pos = [sum(x) for x in zip(self.pos, self.velocity)]
        self.hitbox.update(self.pos[0]-5, self.pos[1]-5, self.sprite_size/2, self.sprite_size/2)

        check_boundary(self.pos, self.velocity)

    def change_direction(self, removed_direction=""):
        directions = ["LEFT", "RIGHT", "UP", "DOWN"]
        if not removed_direction == "":
            directions.remove(removed_direction)
        self.direction = random.choice(directions)

    def get_x_pos(self):
        return self.pos[0]
    
    def get_y_pos(self):
        return self.pos[1]
    
    def get_color(self):
        return self.color
    
    def get_sprite_size(self):
        return self.sprite_size
    
    def get_hitbox(self):
        return self.hitbox
    
    def get_origin(self):
        return self.origin

    def get_timer(self):
        return self.timer
    
    # this is to start the spawn timer
    def start_timer(self):
        self.timer = pygame.time.get_ticks()  

    def respawn(self):
        self.velocity = [self.speed, 0]
        self.direction = "RIGHT"
        self.pos = [self.origin[0], self.origin[1]]
        self.timer = pygame.time.get_ticks()
        self.hitbox.update(self.pos[0]-5, self.pos[1]-5, self.sprite_size/2, self.sprite_size/2)
        self.is_active = False
        self.is_vulnerable = False

    def set_active(self, is_active):
        self.is_active = is_active
    
    def set_leaving(self, is_leaving):
        self.is_leaving = is_leaving
        if self.is_leaving:
            self.direction = "UP"

    def get_vulnerability(self):
        return self.is_vulnerable

    def set_vulnerability(self, is_vulnerable):
        self.is_vulnerable = is_vulnerable

        if self.is_vulnerable:
            self.speed = 1
        else:
            self.speed = 2

    def set_control(self, is_controlled):
        self.is_controlled = is_controlled

    

        

import pygame
from Classes import Player
from Classes import Enemy
import math

# game initialization
pygame.init()
pygame.mixer.init()

w = 600
h = 400
block_size = 20
screen = pygame.display.set_mode((w,h))
BACKGROUND_COLOR = "BLACK"
WALL_COLOR = (37, 87, 103)

orb_points = 50
fruit_points = 200
sprite_size = 20

# maze setting
maze = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

enemy_spawn = []
for y in range(260,301,20):
    for x in range(260,341,20):
        enemy_spawn.append((x,y))

# initialize Pac-Man!
pacman = Player()
pygame.mixer.music.load("Sfx/Intro.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.3)


# initialize enemies!
blinky_color = "RED"
blinky = Enemy(blinky_color, "LEFT", (300,300))
pinky_color = (246, 138, 232)
pinky = Enemy(pinky_color, "RIGHT", (300, 260))
inky_color = (114, 246, 241)
inky = Enemy(inky_color, "DOWN", (340, 280))
clyde_color = (246, 168, 54)
clyde = Enemy(clyde_color, "UP", (260, 280))

enemy_queue = [blinky, pinky, inky, clyde]
enemy_queue[0].start_timer()

active_enemies = []

characters = [pacman, blinky, pinky, inky, clyde]

no_points = [pacman.get_origin()]
for y in range(220,301,20):
    for x in range(260,341,20):
        no_points.append((x,y))

points_remaining = []
for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] == 0 and (x*block_size,y*block_size) not in no_points:
            points_remaining.append((x*block_size,y*block_size))

intersections = []
for y in range(len(maze)):
    for x in range(len(maze[0])):
        counter = 0
        if maze[y][x] == 0:
            if maze[y+1][x] == 0:
                counter += 1
            if maze[y-1][x] == 0:
                counter += 1
            if maze[y][x+1] == 0:
                counter += 1
            if maze[y][x-1] == 0:
                counter += 1
        if counter >= 3:
            intersections.append((x*block_size,y*block_size))
intersections.remove((300,220))

fps = 60
timer = 0
clock = pygame.time.Clock()

# initial screen
for char in characters:
    pygame.draw.circle(screen, char.get_color(), char.get_origin(), sprite_size/2)

pygame.display.flip()

def check_boundary(pos, velocity):
    # check left
    if maze[int(pos[1]/block_size)][int(math.ceil(pos[0]/block_size) - 1)] != 0 and velocity[0] < 0:
        velocity[0] = 0
        print("LEFT")

    # check right 
    elif maze[int(pos[1]/block_size)][int(pos[0]/block_size + 1)] != 0 and velocity[0] > 0:
        velocity[0] = 0
        print("RIGHT")

    # check up 
    elif maze[int(math.ceil(pos[1]/block_size) - 1)][int(pos[0]/block_size)] != 0 and velocity[1] < 0:
        velocity[1] = 0
        print("UP")

    # check down
    elif maze[int(pos[1]/block_size + 1)][int(pos[0]/block_size)] != 0 and velocity[1] > 0:
        velocity[1] = 0
        print("DOWN")

    return velocity

playing = True
while playing:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            playing = False
            print("Game Over!")
    
    # check key presses
    keys = pygame.key.get_pressed()
    
    # check if pacman picks up a point
    if (pacman.get_x_pos(), pacman.get_y_pos()) in points_remaining:
        points_remaining.remove((pacman.get_x_pos(), pacman.get_y_pos()))
        pacman.collect_points(orb_points)
    
    if len(points_remaining) == 0:
        playing = False
        print("GAME OVER!!")
    
    # graphics
    screen.fill(BACKGROUND_COLOR)
    for y in range(len(maze)):        # takes the y index
        for x in range(len(maze[0])): # takes the x index
            if maze[y][x] == 1:
                pygame.draw.rect(screen, WALL_COLOR, pygame.Rect(int((x-0.5)*block_size), int((y-0.5)*block_size), block_size, block_size))
            elif maze[y][x] == 0:
                if (x*block_size, y*block_size) in points_remaining:
                    pygame.draw.circle(screen, "YELLOW", (x*block_size, y*block_size), 4)

    # check on the enemy queue
    if len(enemy_queue) > 0:
        next_enemy = enemy_queue[0]
        if pygame.time.get_ticks() - next_enemy.get_timer() > 2000 and next_enemy.get_x_pos() == 300 and next_enemy.get_y_pos() == 260:
            print("Leaving home base")
            # code the enemy leaving spawn
            next_enemy.set_leaving(True)
            active_enemies.append(next_enemy)
            enemy_queue.pop(0)
            if len(enemy_queue) > 0:
                next_enemy = enemy_queue[0]
                next_enemy.start_timer()

    # collision detection
    if pygame.time.get_ticks() - timer > 100:
        timer = pygame.time.get_ticks()
        for enemy in active_enemies:
            collide = pacman.get_hitbox().colliderect(enemy.get_hitbox())
            if collide:
                if enemy.get_vulnerability():       # if the enemy is vulnerable
                    pass    # send the enemy back to base, increase the enemies death count, increase pacman's kill count and score
                elif not enemy.get_vulnerability():     # if the enemy is not vulnerable
                    pacman.respawn()
                    pygame.time.delay(1000)
                    pygame.mixer.music.load("Sfx/Death.mp3")
                    pygame.mixer.music.play()
                    print("ouch!! " + str(enemy) + " killed you!")
                
    if pacman.get_lives() == 0:

        print("GAME OVER!")
        print("Final Score: " + str(pacman.get_score()))
        
        deciding = True
        while deciding:
            print("Play Again? (Y/N)")
            choice = input()
            if choice.upper() == "Y":
                pacman.respawn()
                pacman.set_score(0)
                pacman.set_lives(3)
                deciding = False

            elif choice.upper() == "N":
                playing = False
                deciding = False
                print("Thanks for playing!")

            else:
                print("Sorry, that's not a valid choice. Please respond again.") 

    if pacman.get_spawning():
        if pygame.time.get_ticks() - pacman.get_timer() < 4500:
            if pygame.time.get_ticks() % 300 < 200:
                pygame.draw.circle(screen, pacman.get_color(), (pacman.get_x_pos(), pacman.get_y_pos()), pacman.get_sprite_size()/2)
            else:
                pygame.draw.circle(screen, BACKGROUND_COLOR, (pacman.get_x_pos(), pacman.get_y_pos()), pacman.get_sprite_size()/2)
        else:
            pacman.set_spawning(False)
            pygame.mixer.music.load("Sfx/Chomp.mp3")
            pygame.mixer.music.play(loops=-1)
    
    if not pacman.get_spawning():
        pacman.update(keys, check_boundary)
        pygame.draw.circle(screen, pacman.get_color(), (pacman.get_x_pos(), pacman.get_y_pos()), pacman.get_sprite_size()/2)
    
    # update and draw enemy characters
    for char in characters[1:]:
        char.update(intersections, keys, check_boundary)
        pygame.draw.circle(screen, char.get_color(), (char.get_x_pos(), char.get_y_pos()), char.get_sprite_size()/2)
    
    pygame.display.flip()    
    clock.tick(fps)

pygame.quit()
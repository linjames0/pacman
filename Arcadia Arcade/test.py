import pygame
pygame.init()
w = 600
h = 400
block_size = 20
screen = pygame.display.set_mode(w, h)


boundaries = [[1]*61] + [[1] + [0]*59 + [1]]*39 + [[1]*61]

running = True
while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
            print("Game Over!")


    screen.fill("BLACK")
    for y in range(len(boundaries)):        # takes the y index
        for x in range(len(boundaries[0])): # takes the x index
            if boundaries[y][x] == 1:
                pygame.draw.rect(screen, "BLUE", pygame.Rect(x*block_size, y*block_size, block_size, block_size))

    pygame.display.flip()


for row in boundaries:
    print(row)

import pygame

print("use arrow keys to apply force.\n press 'q' to quit")


def forcenil():
    force[0] = 0
    force[1] = 0


def forceadd():
    velocity[0] = velocity[0] + force[0]
    velocity[1] = velocity[1] + force[1]


def phyfor(pos, vel):
    forceadd()
    pos[0] = pos[0] + vel[0]
    pos[1] = pos[1] - vel[1]
    return pos


def phycollision(pos, dom, vel):
    if pos[0] > dom[0]:
        vel[0] = -1*vel[0]
        forcenil()
        force[0] = -.1
    elif pos[0] < 0:
        vel[0] = -1*vel[0]
        forcenil()
        force[0] = .1
    if pos[1] > dom[1]:
        vel[1] = -1*vel[1]
        forcenil()
        force[1] = -.1
    elif pos[1] < 0:
        vel[1] = -1*vel[1]
        forcenil()
        force[1] = .1
    return vel


def phydrag(vel, drag):
    vel[0] = vel[0]/drag
    vel[1] = vel[1]/drag
    return vel


def solve(pos, vel, dom, drag):
    vel = phycollision(pos, dom, vel)
    velocity = phydrag(vel, drag)
    npos = phyfor(pos, velocity)
    forcenil()
    return npos


# Pygame Configuration
pygame.init()
STEP = 10
fps = 30
global force
force = [0, 0]
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
global position
position = [screen.get_height()/2, screen.get_width()/2]
global velocity
velocity = [0, 0]
boundry = [screen.get_height(), screen.get_width()]
drag = 1.01
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_LEFT:
                force[0] = -STEP
            if event.key == pygame.K_RIGHT:
                force[0] = STEP
            if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                force[0] = 0
            if event.key == pygame.K_DOWN:
                force[1] = -STEP
            if event.key == pygame.K_UP:
                force[1] = STEP
            if event.key == pygame.K_DOWN and event.key == pygame.K_UP:
                force[1] = 0

    # clear screen to white
    position = solve(position, velocity, boundry, drag)
    # print(position, velocity, force)
    screen.fill('white')
    pygame.draw.circle(screen, "black", position, 50)
    # display content to screen
    pygame.display.flip()
    # limit fps to 60
    clock.tick(60)

pygame.quit()

# coding=utf-8
#-------------------------------------------------------------------------------------------
import pygame, random
from math import pi
import ss_2
#-------------------------------------------------------------------------------------------
#Window Form
(width, height) = (700, 700)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Spring DEM Simulation / CUCEA - MTI 2016')
#-------------------------------------------------------------------------------------------
#Particle characteristic
universe = ss_2.Environment((width, height))
universe.colour = (255,255,255)
universe.addFunctions(['move', 'bounce', 'collide', 'drag', 'accelerate'])
universe.acceleration = (pi, 0.2)
universe.mass_of_air = 0.02
#-------------------------------------------------------------------------------------------
universe.addParticles(x=10, y=10,   mass=20, size=8, speed=0, elasticity=0, colour=(255,0,0))   #1
universe.addParticles(x=10, y=110,  mass=20, size=8, speed=0, elasticity=0, colour=(255,0,0))   #2
universe.addParticles(x=110, y=10,  mass=20, size=8, speed=0, elasticity=0, colour=(5,10,10))   #3

universe.addParticles(x=50, y=50,   mass=20, size=8, speed=0, elasticity=0, colour=(155,0,0))   #1
universe.addParticles(x=50, y=160,  mass=20, size=8, speed=0, elasticity=0, colour=(155,0,0))   #2
universe.addParticles(x=160, y=50,  mass=20, size=8, speed=0, elasticity=0, colour=(15,10,10))  #3
universe.addParticles(x=200, y=200, mass=100, size=30, speed=0, elasticity=0, colour=(200,50,50))  #Impact

universe.addSpring(0,1, length=100, strength=1)
universe.addSpring(1,2, length=100, strength=1)
universe.addSpring(2,0, length=120, strength=1)

universe.addSpring(3,4, length=100, strength=1)
universe.addSpring(4,5, length=100, strength=1)
universe.addSpring(5,3, length=120, strength=1)
#-------------------------------------------------------------------------------------------
#for x in range(1):
#   universe.addParticles(mass=500, size=30, speed=0, elasticity=0, colour=(200,40,40))
#-------------------------------------------------------------------------------------------
#Mouse actions
selected_particle = None
paused = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_particle = universe.findParticle(mouseX, mouseY)
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        selected_particle.mouseMove(pygame.mouse.get_pos())
    if not paused:
        universe.update()
        
    screen.fill(universe.colour)
    
    for p in universe.particles:
        pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size, 0)
        
    for s in universe.springs:
        pygame.draw.aaline(screen, (0,0,0), (int(s.p1.x), int(s.p1.y)), (int(s.p2.x), int(s.p2.y)))

    pygame.display.flip()
#-------------------------------------------------------------------------------------------
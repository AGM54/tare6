import pygame
from pygame.locals import *
import glm
from gl import Renderer
from model import Model
from shaders import *
from obj import Obj


width = 800
height = 550

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()


rend = Renderer(screen)
rend.setShader(vertex_shader, fragmet_shader)


obj = Obj("cat.obj")

triangleModel = Model(obj.assemble())
triangleModel.loadTexture("catpro.jpg")
triangleModel.position.z = -8
triangleModel.scale = glm.vec3(0.09,0.09,0.09)
triangleModel.rotation = glm.vec3(0,0,90)

rend.scene.append(triangleModel)



isRunning = True
while isRunning:

    deltaTime = clock.tick(60) / 1000
    keys  = pygame.key.get_pressed()
    


    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
        
    
    if keys[K_a]:
        rend.camPosition.x += 5 * deltaTime
    elif keys[K_d]:
        rend.camPosition.x -= 5 * deltaTime

    
    if keys[K_w]:
        rend.camPosition.y += 5 * deltaTime
    elif keys[K_s]:
        rend.camPosition.y -= 5 * deltaTime


    if keys[K_q]:
        rend.camPosition.z += 5 * deltaTime
    elif keys[K_e]:
        rend.camPosition.z -= 5 * deltaTime

    triangleModel.rotation.y += 45 * deltaTime
    rend.elapsedTime += deltaTime
    
    
    rend.render()
    pygame.display.flip()
pygame.quit()
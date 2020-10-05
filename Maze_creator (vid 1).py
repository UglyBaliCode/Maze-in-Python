import pygame
import sys
import random
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,20)
size = 20
speed=20
red = (250,0,0)
white = (255,255,255)
blue=(0,255,0)
visited=[]
stack=[]

pygame.init()
window = pygame.display.set_mode((10+size*10,10+size*10))

def draw_grid(s):  
    for i in range (1,s):
        for j in range (1,s):
            pygame.draw.line(window,white,(i*10,j*10),(i*10,j*10+10))
            pygame.draw.line(window,white,(i*10,j*10),(i*10+10,j*10))
    pygame.draw.line(window,white,(s*10,size*10),(10,size*10))
    pygame.draw.line(window,white,(s*10,10),(s*10,s*10)) 
    pygame.display.update()

def draw_rectangle(x,y,a,b):
    pygame.draw.rect(window,white,(x+1,y+1,6,6)) 
    pygame.display.update()
    pygame.time.delay(speed)
    pygame.draw.rect(window,red,(x,y,9+a,9+b))
         
    
def backtrack(x,y):
    pygame.draw.rect(window,blue,(x+1,y+1,6,6))
    pygame.display.update()
    pygame.time.delay(speed)
    pygame.draw.rect(window,red,(x+1,y+1,6,6))
    
def move_up(x,y):
    y=y-10
    draw_rectangle(x,y,0,1)
    visited.append((x,y))
    stack.append((x,y))
    return x,y
       
def move_down(x,y):
    y=y+10
    draw_rectangle(x,y-1,0,1)
    visited.append((x,y))
    stack.append((x,y))
    return x,y
       
def move_left(x,y):
    x = x - 10
    draw_rectangle(x,y,1,0)
    visited.append((x,y))
    stack.append((x,y))
    return x,y
    
def move_right(x,y):
    x = x+10
    draw_rectangle(x-1,y,1,0)
    visited.append((x,y))
    stack.append((x,y))
    return x,y
    
def create_maze():
    sx=11
    sy=11
    pygame.time.delay(1000)
    visited.append((sx,sy))
    stack.append((sx,sy))
    
    moves=('u','d','l','r') 
    
    while len(visited)>0:
        possible_moves=[]
        move = random.choice(moves)
        if (sx,sy+10) not in visited and sy<(size*10)-10:
            possible_moves.append('d')
        if (sx,sy-10) not in visited and sy>20:
            possible_moves.append('u')
        if (sx-10,sy) not in visited and sx>11:
            possible_moves.append('l')
        if (sx+10,sy) not in visited and sx<(size*10)-10:
            possible_moves.append('r')
       # print(possible_moves)
       # print(previous)
        
        if len(possible_moves)>0:
            direction = random.choice(possible_moves)
            if direction == 'd':
                (sx,sy) = move_down(sx,sy)
            if direction == 'u':
                (sx,sy) = move_up(sx,sy)
            if direction == 'l':
                (sx,sy) = move_left(sx,sy)
            if direction == 'r':
                (sx,sy) = move_right(sx,sy)
        if len(possible_moves) < 1:
            if len(stack)>0:
                sx,sy = stack.pop()
                backtrack(sx,sy)
            if len(stack)<1:
                pygame.time.delay(3000)
                pygame.quit()
                sys.exit()
                run=False
        
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            run = False  
    draw_grid(size)
    create_maze()
        
   # run=False
pygame.quit()
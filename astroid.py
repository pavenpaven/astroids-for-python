import pygame
import math
import random

#map

class World:
  def __init__(self):
    self.world_perspective=(3, 2)
    self.world_scaler=300
    self.world_true_size= self.world_perspective[0] * self.world_scaler, self.world_perspective[1] * self.world_scaler
  def convert_to_screen(pos):
    return [pos[0]-screen_pos[0]), pos[1]-screen_pos[1]]
  def change_pos(pos, change):
    return [pos[0]+chane[0], pos[1]+change[1]]
    
world=World()

  

#graphics
tile = 250

screen_size = (3, 2)

player_size = 30

window=pygame.display.set_mode((screen_size[0]*tile, screen_size[1]*tile))
    

def player_render():
  x=(math.sin(jack.angle-0.25)*player_size+jack.x, math.cos(jack.angle-0.25)*player_size+jack.y)

  y=(math.sin(jack.angle+0.35)*player_size+jack.x, math.cos(jack.angle+0.35)*player_size+jack.y)

  z=(math.sin(jack.angle-math.pi)*player_size+jack.x, math.cos(jack.angle-math.pi)*player_size+jack.y)

  pygame.draw.polygon(window, (255, 255, 255), (z, x, y))


def graphics():
    window.fill((0, 0, 0))
    render_astroid()
    player_render()
    render_shot()
    pygame.display.update()

#

#astrodise

astroid_hitbox = 50



astroids = []

def render_astroid():
    k=0
    for i in astroids:
        #x= i[0]+i[2][0]/10*speed
        #y= i[1]+i[2][1]/10*speed

        pos=warp(astroid[k][0], astroid[k][1])

        astroids[k][0]=pos[0]
        astroids[k][1]=pos[1]
         
        pygame.draw.rect(window, (0, 255, 0), (pos[0], pos[1], astroid_hitbox, astroid_hitbox))
        k += 1

def spawn_astroid():
    cous=random.randint(0,3)
    if cous==0:
      x=0
      y = random.randint(20,tile * screen_size[1]-20)
      vol = (random.randint(3, 10), random.randint(3, 10))
    if cous==1:
      x = screen_size[0]*tile
      y = random.randint(20,tile * screen_size[1]-20)
      vol = (random.randint(0, 7)-10, random.randint(0, 20)-10)
    if cous==2:
      x= random.randint(20,tile * screen_size[0]-20) 
      y = 0
      vol = (random.randint(0, 20)-10, random.randint(3, 10))
    if cous==3:
      y = screen_size[1] * tile
      x = random.randint(20,tile * screen_size[1]-20)
      vol = (random.randint(0, 20)-10, random.randint(0, 10)-10)
    
    astroids.append([x, y, vol])

#key presses

class Player:
    def __init__(self, x, y, vol, angle):
        self.x = x
        self.y = y
        self.vol = vol
        self.angle = angle


jack = Player(screen_size[0] * tile / 2, screen_size[1] * tile / 2 , (0, 0), 0)


def check_keys(framecount, j):
  #if framecount/2==round(framecount/2):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        tut=False
    keys = pygame.key.get_pressed()
    pygame.key.set_repeat(1, 100000000)
        

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
      jack.angle+=0.03/speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
      jack.angle-=0.03/speed
    if keys[pygame.K_w]:
        calculate_vol(0.05,framecount)
    if keys[pygame.K_SPACE] and j == True:
        spawn_shot()
        j=False
    if framecount/spam == round(framecount/spam):
        j=True
    
    return j


def calculate_vol(x,framecount):
    anglevector = (math.sin(jack.angle-math.pi)/2, math.cos(jack.angle-math.pi)/2)
    jack.vol = (jack.vol[0]+anglevector[0]/4, jack.vol[1]+anglevector[1]/4)

#move


speed = 1


def warp(x,y):
  if x<0:
    x=screen_size[0] * tile - 2
  if x>screen_size[0] * tile:
    x=2
  if y<0:
    y=screen_size[1] * tile-2
  if y>screen_size[1] * tile:
    y=2
  return x, y

def move_player():
    jack.x += jack.vol[0]/speed
    jack.y += jack.vol[1]/speed
    pos=warp(jack.x, jack.y)
    jack.x = pos[0]
    jack.y = pos[1]
    
# colliction

def check_if_collide(hitbox1, hitbox2):
     for i in hitbox2:
       if i[0] > hitbox1[0][0] and i[0]<hitbox1[1][0]:
         if i[1] > hitbox1[0][1] and i[1] < hitbox1[1][1]:
           return "dead"

def player_collition(player_hitbox):
    for i in astroids:
         if check_if_collide(player_hitbox,((i[0], i[1]), (i[0] + astroid_hitbox, i[1] + astroid_hitbox))) == "dead":
              return False
    return True

def shot_collition():
    n = 0
    n1 = 0
    for a in astroids:
        for i in shots:
            if check_if_collide(((a[0], a[1]), (a[0] + astroid_hitbox, a[1] + astroid_hitbox)), ((round(i[0]), round(i[1])), (1, 1))):
                del astroids[n]
                del shots[n1]
            n1 += 1
        n1 = 0
        n += 1

# Extra
spam = 20


shots = []

speed_of_bullet = 20

bullet_size = 6


def spawn_shot():
    shots.append([jack.x, jack.y, jack.angle-math.pi])


def render_shot():
    i=0
    for n in shots:
      
      vec = math.sin(shots[i][2]), math.cos(shots[i][2])
      
      x = shots[i][0]
      y = shots[i][1]
      x += vec[0] * speed_of_bullet
      y += vec[1] * speed_of_bullet
      shots[i][0] = x
      shots[i][1] = y
      i += 1
      despawn_bullets()
      pygame.draw.rect(window, (255, 0, 0), (x, y, bullet_size, bullet_size))

def despawn_bullets():
  n=0
  for i in shots:
     if i[0]<0 or i[0]>screen_size[0]*tile or i[1]<0 or i[1]>screen_size[1]*tile:
        del shots[n] 
     n+=1
        
        
    
      
#screens

def game_over():
    while True:
        window.fill((0, 0, 0))
        pygame.l

#main loop
diff = 500
screen_pos=[0, 0];

def main_loop():
    j = False
    clock = pygame.time.Clock()
    framecount=0
    for i in range(1):
        spawn_astroid()
    game = True
    astro=3
    chance=1000
    while game:
        clock.tick(60)
        framecount+=1
        screen_pos=[jack.x-((screen_size[0]*tile)/2), jack.y-((screen_size[1]*tile)/2)]
        world.change_pos
        j=check_keys(framecount, j)
        move_player()
        graphics()
        print(clock.get_fps()) 
        player_hitbox = ((jack.x - 30, jack.y - 30), (jack.x + 30, jack.y + 30))
        game = player_collition(player_hitbox)
        shot_collition()
        if framecount/chance == round(framecount/chance):
            spawn_astroid()
        if framecount/diff == round(framecount/diff):
          chance = round(chance/ 1.25)
        

while True:
  main_loop()
  game_over()

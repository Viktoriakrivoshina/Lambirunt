from pygame import *
'''Необхідні класи'''

#клас-батько для спрайтів
class GameSprite(sprite.Sprite):
     #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивості rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#NOVE
class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
#клас-спадкоємець для спраййта-ворога (перміщається сам)
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        # катринка стіни - прямокутник потрібних розмірів та кольору 

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт повинен зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w1 = Wall(154, 205, 50, 100, 250, 10, 250)  
w2 = Wall(154, 205, 50, 100, 250, 250, 10)     
w3 = Wall(154, 205, 50, 100, 150, 250, 10)
w4 = Wall(120, 205, 100, 150, 350, 10, 250)
w5 = Wall(120, 205, 50, 150, 350, 290, 10)
w6 = Wall(154, 205, 250, 429, 100, 10, 250)
w7 = Wall(154, 205, 250, 338, 0, 10, 150)
w8 = Wall(154, 125, 50, 339, 0, 370, 10)
w9 = Wall(154, 150, 250, 550, 0, 10, 100)
w10 = Wall(154, 190, 250, 690, 0, 10, 400)
w11 = Wall(120, 225, 155, 550, 300, 250, 10)
w12 = Wall(135, 225, 155, 440, 180, 150, 10)
w13 = Wall(145, 225, 160, 430, 450, 150, 10)
#Ігрова сцена:
win_width = 700
win_height = 500


window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("Rom_m.jpg"), (win_width, win_height))

#Персонажі гри:
player = Player('HR_rr_jpg.png', 5, win_height - 80, 4)
monster = Enemy('Snake_png.png', win_width - 80, 300, 2)
final = GameSprite('Hrifindor_png.png', win_width - 120, win_height - 80, 0)

font.init()
font = font.SysFont("Arial", 80)
win = font.render('YOU WIN!',True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

game = True
clock = time.Clock()
FPS = 40
finish = False
#Музика
mixer.init()
mixer.music.load('Harry.mp3')
mixer.music.play()
dead = mixer.Sound("potter_avada_kedavra.ogg")
vin = mixer.Sound("vin.ogg")

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:

        window.blit(background,(0, 0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        final.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()

    # Ситуація "Перемога"
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11) or sprite.collide_rect(player, w12) or sprite.collide_rect(player, w13):
            finish = True
            window.blit(lose, (200, 200))
            mixer.music.stop()
            dead.play()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            mixer.music.stop()
            vin.play()

    display.update()
    clock.tick(FPS) 


    
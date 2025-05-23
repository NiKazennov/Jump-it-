
import pygame
from random import randrange, randint
import time


pygame.init()


pygame.mixer.music.load("c418-sweden-minecraft-volume-alpha.mp3")
icon = pygame.image.load('bg.png')
pygame.display.set_caption("Jump it!_Alpha")
pygame.display.set_icon(icon)


window = pygame.display.set_mode((1060, 600))


font_h1 = pygame.font.SysFont('Calibri', 90)
font_h2 = pygame.font.SysFont('Calibri', 50)
font_h3 = pygame.font.SysFont('Calibri', 30, italic=True)
font_h4=pygame.font.SysFont('Calibri', 15, italic=True)
font_h5=pygame.font.SysFont('Calibri', 50,bold=True)
font_info=pygame.font.SysFont('Calibri', 15,bold=True)
h1 = font_h1.render("Jump it!", True, (226, 160, 46))
h2 = font_h2.render("Start", True, (226, 160, 46))
h3_1 = font_h3.render("Привет !", True, (226, 160, 46))
h3_2 = font_h3.render("Лягушку зовут Роспо", True, (226, 160, 46))
h3_3 = font_h3.render("Shift дает ускорение", True, (226, 160, 46))
h3_4 = font_h3.render("Technoblade never dies!", True, (226, 160, 46))
h3_5 = font_h3.render("Игра в разработке!", True, (226, 160, 46))
h5 = font_h5.render("Спасибо за прохождение!", True, (226, 160, 46))
info_1=font_info.render("a и d - перемещение",True, (255,254,250))
info_2=font_info.render("пробел(space) - прыжок",True, (255,254,250))
info_3=font_info.render("??? - ускорение(ищите в советах)",True, (255,254,250))
bg=pygame.image.load('bg_sky.jpg')


clock = pygame.time.Clock()
slow = 5


hero_x = 300
hero_y = 520
hero_y_static = 520
random = randint(1, 5)
FPS=120
flag_ent_text=False
start_time=None

jump = False
speed=15
jumpCount = 0
jumpMax = 15
num_iter = 0
num_iter2=0
img_list_right = []
img_list2 = []
img_list_left = []
flag1 = False
flag2 = False
button_w = 300
button_h = 120
button_x = 390
button_y = 250
max=0

vol = 1.0
pygame.mixer.music.set_volume(vol)

# Класс Платформы
class Platform:
    def __init__(self, obj_x, obj_y, img):
        self.obj_x = obj_x
        self.obj_y = obj_y
        self.img = pygame.image.load(img)

    def show(self):
        window.blit(self.img, (self.obj_x, self.obj_y))
        
    def stay(self, hero_x, hero_y):
        global jump, vert_speed
        if ( self.obj_y <= hero_y + 10 <= self.obj_y + 10 and self.obj_x - 10<= hero_x <= self.obj_x + 60 ):
            jump = False      
            vert_speed = 0     
            return True
        return False

    def check_standing(self, hero_x, hero_y):
        if (self.obj_y <= hero_y + 10 <= self.obj_y + 10 and  self.obj_x -10 <= hero_x <= self.obj_x + 60):
            return True
        return False

class FinishSquare:
    def __init__(self, img,obj_x, obj_y):
        self.obj_x = obj_x
        self.obj_y = obj_y 
        self.size=20
        self.img=pygame.image.load(img)

    def draw(self):
        window.blit(self.img,(self.obj_x, self.obj_y))

    def check_collected(self, hero_x, hero_y):
        x_in_range = self.obj_x - 5 <= hero_x <= self.obj_x + self.size + 5
        y_in_range = self.obj_y - 10 <= hero_y <= self.obj_y + self.size + 10
        return x_in_range and y_in_range



platforms=[]
for i in range(15):
    platforms.append(Platform(randrange(150, 950,70), randrange(100, 490,70), 'Platform/Platform_0.png'))
finish_square_1 = None

selected_platform = randint(0, len(platforms)-1)
finish_square_1 = FinishSquare('Coin_new-1.png.png',platforms[selected_platform].obj_x + 15,platforms[selected_platform].obj_y - 15)

for i in range(6):
    img = pygame.image.load(f'Frog/Frog_0-{i+1}.png.png')
    img_list_right.append(img)
for i in range(6):
    img3=pygame.image.load(f'Frog_left/Frog_left_{i}.png')
    img_list_left.append(img3)
for i in range(6):
    img2 = pygame.image.load(f'Platform/Platform_{i}.png')
    img_list2.append(img2)

game_time_sec=0
iteration=0
run = True
while run:
    pygame.mixer.music.play(-1)
    clock.tick(60)
    time_1=clock.get_time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if not jump and event.key == pygame.K_SPACE:
                jump = True
                vert_speed = jumpMax
            if event.key == pygame.K_RETURN:
                flag2=True
                flag1=False
                start_time = pygame.time.get_ticks()
                flag_ent_text=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                flag1 = True


    keys = pygame.key.get_pressed()
    move_x = keys[pygame.K_d] - keys[pygame.K_a]
    hero_x += move_x * speed
    
    standing_on_platform = any(
        platform.check_standing(hero_x, hero_y) for platform in platforms
    )

    if keys[pygame.K_LSHIFT]:
        speed = 10
    else:
        speed = 5

    if hero_x < 0 or hero_x >= 1040:
        hero_x -= speed * move_x


    if jump:
        hero_y -= vert_speed
        if vert_speed > -jumpMax:
            vert_speed -= 1
        else:
            jump = False
    else:
        if not standing_on_platform and hero_y < hero_y_static:
            hero_y += 15
            vert_speed=0
            jump is False

    for platform in platforms:
        if platform.stay(hero_x, hero_y): 
            break  


    count = abs((hero_y_static - hero_y) // 10)
    iteration=(iteration+1)%1200
    
    if iteration%FPS == 0:
        game_time_sec+=1
    c = font_h5.render(f"{count} м", True, (4,102,2))


    window.fill((0, 0, 0))  
    window.blit(h1, (400, 20))  
    pygame.draw.rect(window, [226, 160, 46], [button_x, button_y, button_w, button_h], 10) 
    window.blit(h2, (490, 290))  


    if random == 1:
        window.blit(h3_1, (430, 500))
    elif random == 2:
        window.blit(h3_2, (430, 500))
    elif random == 3:
        window.blit(h3_3, (430, 500))
    elif random == 4:
        window.blit(h3_4, (430, 500))
    elif random == 5:
        window.blit(h3_5, (430, 500))
        
        

    if flag1:
        if (button_x <= pos[0] <= button_x + button_w and button_y <= pos[1] <= button_y + button_h):
            flag2 = True
            start_time = pygame.time.get_ticks()
    if flag2:
        window.blit(bg,(0,0))
        num_iter += 1
        num_iter2 += 1
        num_frame = num_iter // slow % 6
        if move_x == 0:
            window.blit(img_list_right[1],[hero_x,hero_y])
        num_frame2=num_iter2 // slow % 6
        pygame.draw.rect(window, (64, 64, 64), (0, 550, 1060, 50))  
        for platform in platforms:
            platform.show()          
            platform.stay(hero_x, hero_y)  
        if keys[pygame.K_d]:
            window.blit(img_list_right[num_frame], [hero_x, hero_y]) 
        if keys[pygame.K_a]:
            window.blit(img_list_left[num_frame2], [hero_x,hero_y])
        window.blit(c, (500, 20))
        finish_square_1.draw()
        window.blit(info_1,(10,10))
        window.blit(info_2,(10,30))
        window.blit(info_3,(10,50))
        if start_time:
            time_since_enter = abs(pygame.time.get_ticks() - start_time)
            if flag_ent_text:
                message = 'Вы собрали монетку за ' + str(time_since_enter/1000) + ' сек'
            else:
                message = 'Вы собрали монетку за ' + str(time_since_enter/100) + ' сек'
            if time_since_enter > max:
                max=time_since_enter
        if finish_square_1.check_collected(hero_x, hero_y):
            window.fill((0,0,0))
            window.blit(h5, (230, 250))
            window.blit(font_h5.render(message,True,(226, 160, 46)),(200, 400))
            pygame.display.flip()
            time.sleep(3.5)
            pygame.quit()


    pygame.display.flip()

pygame.quit()
exit()
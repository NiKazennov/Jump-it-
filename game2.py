import pygame
pygame.init()

pygame.mixer.music.load("c418-sweden-minecraft-volume-alpha.mp3")
icon=pygame.image.load('bg.png')
pygame.display.set_caption("Jump it!")
pygame.display.set_icon(icon)
window = pygame.display.set_mode((1060, 600))
font_h1=pygame.font.SysFont('Calibri',90)
font_h2=pygame.font.SysFont('Calibri',50)
h1=font_h1.render("Jump it!",True,(226,160,46))
h2=font_h2.render("Start",True,(226,160,46))

clock = pygame.time.Clock()
slow=5

rect = pygame.Rect(135, 220, 30, 30)

hero_x=300
vol=1.0
speed = 5
jump = False
jumpCount = 0
jumpMax = 15
obj_x=300
obj_y=450
num_iter=0
img_list=[]
img_list2=[]
img_list3=[]
flag1=False
flag2=False
button_w=300
button_h=120
button_x=390
button_y=180
hero_y=520
hero_y_static=520
pygame.mixer.music.set_volume(vol)

for i in range(6):
    img=pygame.image.load(f"Frog/Frog_0-{i+1}.png.png")
    img_list.append(img)
for i in range(6):
    img2=pygame.image.load(f"Platform/Platform_{i}.png")
    img_list2.append(img2)

run = True
while run:
    pygame.mixer.music.play(-1)
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: 
            if not jump and event.key == pygame.K_SPACE:
                jump = True
                jumpCount = jumpMax
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                flag1=True
    keys = pygame.key.get_pressed()    
    move_x=keys[pygame.K_d] - keys[pygame.K_a]
    hero_x+=move_x*speed
    if jump:
        hero_y -= jumpCount
        if jumpCount > -jumpMax:
            jumpCount -= 1
        else:
            jump = False 
    if keys[pygame.K_LSHIFT] == 1:
        speed=8
    else:
        speed=5
    if hero_x < 0 or hero_x >= 1040:
        hero_x-=speed*move_x
    count=(hero_y_static-hero_y)//10
    c=font_h2.render(f'{count} m',True,(200,200,200))
    window.fill((0,0,0))
    window.blit(h1,(400,20))
    pygame.draw.rect(window,[226,160,46],[button_x,button_y,button_w,button_h],10)
    window.blit(h2,(490,220))
    if flag1:
        if (button_x<=pos[0]<=button_x+button_w and button_y<=pos[1]<=button_y+button_h):
            flag2=True
        falg1=False
    if flag2:
        window.fill((0, 0, 64))
        num_iter+=1
        num_frame=num_iter//slow%6
    
        pygame.draw.rect(window, (64, 64, 64), (0, 550, 1060, 50))
        window.blit(img_list2[num_frame],[obj_x,obj_y])
        window.blit(img_list[num_frame],[hero_x,hero_y])
        window.blit(c,(500,20))
    pygame.display.flip()

pygame.quit()
exit() 

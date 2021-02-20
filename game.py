import pygame
import math,time,random

def draw_rect(x,y,w,h,c,z=0):
    pygame.draw.rect(screen, c, pygame.Rect(x,y,w,h),z)


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)
screen =pygame.display.set_mode((1910, 1010))
pygame.display.set_caption('HANGMAN')
words=["broadcast","wrench","economics","category","jelly","album","touch","weather","linux","ubuntu","batman"]
sand=(220,192,132)
white=225,225,225
done = False
a={pygame.K_a : 'a',pygame.K_b : 'b',pygame.K_c : 'c',
pygame.K_d : 'd',pygame.K_e : 'e',pygame.K_f : 'f',
pygame.K_g : 'g',pygame.K_h : 'h',pygame.K_i : 'i',
pygame.K_k : 'k',pygame.K_l : 'l',pygame.K_j : 'j',
pygame.K_m : 'm',pygame.K_n : 'n',pygame.K_o : 'o',
pygame.K_p : 'p',pygame.K_q : 'q',pygame.K_r : 'r',
pygame.K_s : 's',pygame.K_t : 't',pygame.K_u : 'u',
pygame.K_v : 'v',pygame.K_w : 'w',pygame.K_x : 'x',
pygame.K_y : 'y',pygame.K_z : 'z'}
i=0
j=0
ch=7
l=7
won=False
guess = myfont.render('GUESS THE WORD', False,sand,(0,0,0))
s1=words[random.randint(0,len(words)-1)]
att,cr=[],[]
c=sorted(list(set(s1)))
s=list(s1)
n=len(s)
screen.blit(guess,(900,0))
x=(1910-480)//2 - int((n-0.5)*75) +480
for d in range(n):
    draw_rect(x+2*d*75,450,75,10,sand) 
while not done:        
    for event in pygame.event.get():         
        if event.type == pygame.QUIT:                
            done = True        
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and alt_held:
                    done = True
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key in a:
                    if a[event.key] in att:
                        draw_rect(700,700,1200,100,(0,0,0))
                        warn=myfont.render("Letter has already been entered", False,(225,0,0),(0,0,0)) if not a[event.key] in s else myfont.render("Letter has already been entered", False,(0,225,0),(0,0,0))
                        screen.blit(warn,(700,700))
                        break
                    draw_rect(700,700,1200,100,(0,0,0))
                    att+=[a[event.key]]
                    if a[event.key] in s:
                        for d in range(n):
                            if s[d] == a[event.key]:
                                cr+=[s[d]]
                                lett=myfont.render(a[event.key].upper(), False,white,(0,0,0))
                                screen.blit(lett,(x+2*d*75+15,360))
                                pygame.display.flip()
                                if sorted(list(set(cr))) == c:
                                    done=True
                                    won=True
                                    time.sleep(1)
                                    break
                    else:
                        wrong=myfont.render((a[event.key].upper()), False,white,(0,0,0))
                        screen.blit(wrong,(650+(7-ch)*150,500))
                        pygame.draw.line(screen,(225,0,0),(700+(7-ch)*150,500),(650+(7-ch)*150,550),5)
                        #draw_rect(700+(7-ch)*150,500),(650+(7-ch)*150,550),5)
                        draw_rect(645+(7-ch)*150,500,60,60,sand,3)
                        if ch > 0: 
                            ch-=1 
                            l=ch
                else:
                    warn=myfont.render("Enter only alphabets", False,(225,0,0),(0,0,0))
                    screen.blit(warn,(700,700))
                    
                        
        draw_rect(477, 0, 1, 1010,sand)     #divides the screen
        draw_rect(20, 980, 350, 10,white)   #Bottom line
        draw_rect(50, 50, 10, 930,white)    #side long line
        draw_rect(50, 50, 225, 10,white)    # top line
        draw_rect(265, 50, 10, 150,white)   #rope  
        draw_rect(495,95,500,130,(0,0,0))
        draw_rect(500,100,480,120,sand,5)
        chance=myfont.render(("CHANCES : "+str(ch-1)), False,white,(0,0,0))
        screen.blit(chance,(520,130))  
        if l == 6:
            while i<= 2*3.14:
                pygame.draw.circle(screen,sand,(270+95*math.sin(i),300-95*math.cos(i)),5)
                pygame.display.flip()
                time.sleep(0.001)
                i+=0.01
            l=-1
            i=0
        if l== 5:
            while i <= 300:
                pygame.draw.circle(screen,sand,(270,395+i),5)
                pygame.display.flip()
                time.sleep(0.001)
                i+=1
            l=-1
            i=0
        if l==4 :
            while i<=100 or j <= 145:
                pygame.draw.circle(screen,sand,(270-i,545-j),5)
                time.sleep(0.001)
                pygame.display.flip()
                i+=1
                j+=1
            i,j=0,0
            l=-1
        if l==3 :
            while i<=100 or j <= 145:
                pygame.draw.circle(screen,sand,(270+i,545-j),5)
                time.sleep(0.001)
                pygame.display.flip()
                i+=1
                j+=1
            i,j=0,0
            l=-1
        if l==2 :
            while i<=120 or j <= 75:
                pygame.draw.circle(screen,sand,(270-i,695+j),5)
                time.sleep(0.001)
                pygame.display.flip()
                i+=1
                j+=1
            i,j=0,0
            l=-1
        if l==1 :
            while i<=120 or j <= 75:
                pygame.draw.circle(screen,sand,(270+i,695+j),5)
                time.sleep(0.001)
                pygame.display.flip()
                i+=1
                j+=1
            i,j=0,0
            l=-1
            done=True
            won=False
            time.sleep(1)
            break
        #pygame.draw.line(screen,sand,(270,545),(100,400)) # left arm
        #pygame.draw.line(screen,sand,(270,545),(440,400)) # right arm
        #pygame.draw.line(screen,sand,(270,795),(100,900)) # left leg
        #pygame.draw.line(screen,sand,(270,795),(440,900)) # right leg

        

        #pygame.draw.circle(screen,sand,(270,290),95,2)  #head
        #pygame.draw.rect(screen, sand, pygame.Rect(265,395,10,400))
        #pygame.draw.line(screen,brown,(477,0),(477,1010))
        pygame.display.flip()   

draw_rect(0,0,1910,1010,(0,0,0))
if won == True:
    congo=myfont.render("Congratulations!!! You Won", False,(0,225,0),(0,0,0))
    screen.blit(congo,(500,400))
else:
    congo=myfont.render("You Lost !! Try Again", False,(225,0,0),(0,0,0))
    screen.blit(congo,(600,400))
    wor=myfont.render("The Word Was : " + s1.upper(), False,(225,0,0),(0,0,0))
    screen.blit(wor,(600,600))
pygame.display.flip()  
time.sleep(2)
        
            
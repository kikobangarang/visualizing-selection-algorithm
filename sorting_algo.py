import random, pygame, time

#iniciar pygame
pygame.init()

# cores etc
white = (0, 0, 0)
black = (255, 255, 255)
RED = (255,0 ,0)
clock = pygame.time.Clock()
smallfont = pygame.font.SysFont("monospace", 35)
draging = False
sample_size = 5

#criar janela
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIN.fill(black)
pygame.display.update()
pygame.display.set_caption("sorting algorithm visualizer")


#obter width e height
width = WIN.get_width()
height = WIN.get_height()

pos_slider = [(width/2) - 150, 30]


def create_lst(n):
    lst = []
    while len(lst) != n:
        num = random.randint(1, n)
        if num not in lst:
            lst.append(num)
    WIN.fill(black)
    clock.tick(600)
    j = 1
    for i in lst:
                
        barras = pygame.Rect(width/2 + (j * 10) - (((10 * n) + 10)/2), 200, 5, 5 * lst[i-1])
        pygame.draw.rect(WIN, RED, barras)
        pygame.display.update(barras)
        clock.tick(len(lst)*10)
        j+=1
    return lst

def clear(WIN):
    rect_clear= pygame.Rect(width/2 - (((10 * len(lst)) +10)/2) , 200, width, height-200)
    pygame.draw.rect(WIN, black, rect_clear)
    pygame.display.update(rect_clear)


def selection_algorithm(lst, x):
    idx = lst.index(x)
    lst.insert(x-1, lst[idx])
    lst.pop(idx+1)
    return lst



def display_bars(lst, WIN):
    x = 1

    while x <= len(lst):

        selection_algorithm(lst,x)
        clear(WIN)
        clock.tick(600)
        j = 1
        for i in lst:      

            mouse = pygame.mouse.get_pos()  
            for ev in pygame.event.get():
                #checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:
              
                    #if the mouse is clicked on the
                    # button the game is terminated
                    if width - 300 <= mouse[0] <= width - 300 +140 and 10 <= mouse[1] <= 10+40:
                        
                        j = 1
                        clear(WIN)
                        for i in lst:
                            barras = pygame.Rect(width/2 + (j * 10) - (((10 * len(lst)) +10)/2) , 200, 5, 5 * lst[i-1])
                            pygame.draw.rect(WIN, RED, barras)
                            pygame.display.update(barras)
                            j+=1            

                        return False


            barras = pygame.Rect(width/2 + (j * 10) - (((10 * len(lst)) +10)/2) , 200, 5, 5 * lst[i-1])
            pygame.draw.rect(WIN, RED, barras)
            pygame.display.update(barras)
            clock.tick(len(lst)*10)
            j+=1
        x += 1 

    return True



text1 = smallfont.render('quit' , True , black)
text2 = smallfont.render('generate' , True , black)
text3 = smallfont.render('sort' , True , black)
text4 = smallfont.render('cancel' , True , black)
text5 = smallfont.render(str(sample_size) , True , white)

while True:
    

    text5 = smallfont.render(str(sample_size) , True , white)
    WIN.blit(text5 , ((width/2) + 300, 10))
    mouse = pygame.mouse.get_pos()  
    for ev in pygame.event.get():
        
        

        if ev.type == pygame.QUIT:
            pygame.quit()
              
        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
              
            #if the mouse is clicked on the
            # button the game is terminated
            if width - 150 <= mouse[0] <= width - 150 +140 and 10 <= mouse[1] <= 10+40:
                pygame.quit()


            #if the mouse is clicked on the
            # button the game is terminated
            if 10 <= mouse[0] <= 10 +190 and 10 <= mouse[1] <= 10+40:
                lst = create_lst(sample_size)
                sorted = False

            #if the mouse is clicked on the
            # button the game is terminated
            if pos_slider[0]-10 <= mouse[0] <= pos_slider[0]+10 and pos_slider[1]-10 <= mouse[1] <= pos_slider[1]+10:
                draging =True

        if ev.type == pygame.MOUSEBUTTONUP:
            draging = False

        if ev.type == pygame.MOUSEMOTION:
            if draging and (width/2) - 150 <= mouse[0] <= (width/2) + 150:               
                pos_slider[0] = mouse[0]
                sample_size = round((pos_slider[0] - (width/2) + 150)/2)
                if sample_size < 5:
                    sample_size = 5
                lst = create_lst(sample_size)
                sorted = False

        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if 220 <= mouse[0] <= 220 +140 and 10 <= mouse[1] <= 10+40 and sorted == False:
                sorted = True
                sorted  = display_bars(lst, WIN)
                  




    pygame.draw.rect(WIN,white,[width - 150,10,140,40])
    WIN.blit(text1 , (width-150+30,10))

    pygame.draw.rect(WIN,white,[10,10,190,40])
    WIN.blit(text2 , (10+10,10))

    pygame.draw.rect(WIN,white,[220,10,140,40])
    WIN.blit(text3 , (220+30,10))

    cancel_btn=[width - 300,10,140,40]     
    pygame.draw.rect(WIN,white,cancel_btn)
    WIN.blit(text4 , (width-300+10, 10))

    pygame.draw.rect(WIN,white,[(width/2) - 165,10,330,40])
    pygame.draw.rect(WIN,black,[(width/2) - 150,27.5,300,5])
    pygame.draw.circle(WIN, RED, pos_slider, 10)

    

    pygame.display.update()








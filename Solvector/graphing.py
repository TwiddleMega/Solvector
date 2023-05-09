import pygame
import math
import sys
from pygame import *
from math import *
from sympy import solve,Symbol
from sympy.abc import x
pygame.init()

#initialising fonts and colours
font = pygame.font.SysFont('Verdana',16) #main instruction font
font2 = pygame.font.SysFont('Serif',24) #title font
font3 = pygame.font.SysFont('Cambria Math',14)#secondary instruction/axes font
white = (255,255,255)
lightgrey = (225, 230, 235)
black = (0,0,0)
red = (255,0,0)
#graphcolour = (50,84,112) #dark blue
graphcolours = ((255,179,186),(186,255,201),(186,225,255),(255,255,186),(255,223,186))
colournames = ['red','green','blue','yellow','orange']
gridcolour = (177,227,242) #light blue
titlecolour = (59,84,138) #hued dark blue

#window settings
width, height = 500, 500
extrawidth = 600
screen = pygame.display.set_mode((width+extrawidth,height)) #dimensions
pygame.display.set_caption("Solvector - Graphing Calculator")
screen.fill(white)

#graphs
graphlist = []

#draw graph background
def graphbackground(k,graphlist):
    screen.set_clip(width,0,(width+extrawidth),height-50)#only work on instruction/equation area
    screen.fill(lightgrey)
    if True:
        screen.set_clip(0,0,width,height)#only work on graphing area
        screen.fill(white)

        #drawing gridlines
        for i in range(round(int(width/k))+1):
            gridx, gridy = k*i, k*i
            pygame.draw.line(screen, gridcolour, ((width/2)+gridx,0), ((width/2)+gridx,height), 1)
            pygame.draw.line(screen, gridcolour, ((width/2)-gridx,0), ((width/2)-gridx,height), 1)
            pygame.draw.line(screen, gridcolour, (0,(width/2)+gridy), (width,(width/2)+gridy), 1)
            pygame.draw.line(screen, gridcolour, (0,(width/2)-gridy), (width,(width/2)-gridy), 1)
            #pygame.draw.line(screen, gridcolour, (0,gridy), (width,gridy), 1)
        pygame.draw.line(screen, gridcolour, (width,0), (width,height), 5)

        #drawing axes
        midx, midy = width/(k*2), height/(k*2)
        pygame.draw.line(screen, black, (midx*k,0), (midx*k,height), 1)
        pygame.draw.line(screen, black, (0,midy*k), (width,midy*k), 1)

    screen.set_clip(None) #focus on the whole screen
        
#main program
def main(graphlist):
    
    #pixels per unit on grid
    k = 25
    screen.set_clip(width,0,(width+extrawidth),height)#fill gap in graphbackground left for post-graph
    screen.fill(lightgrey)
    graphbackground(k,graphlist)

    #instructions for use
    title = font2.render("Solvector", 1, titlecolour)
    screen.blit(title, (width+10, 20))

    instruct = font.render("Type in an equation. E.g. -3*x^2+1",1,black)
    screen.blit(instruct,(width+10,70))

    instruct = font.render('"Enter" - Graph Equation',1,black)
    screen.blit(instruct,(width+10,100))

    instruct = font.render('"Backspace" - Backspace         "Q" - Clear',1,black)
    screen.blit(instruct,(width+10,130))

    instruct = font3.render('S=sin       |       C=cos       |       T=tan       |       R=√       |       A=|  |',1,black)
    screen.blit(instruct,(width+10,180))

    instruct = font3.render('L=log₁₀       |       N=log(e)       |       E=ℯ       |       P=𝝅',1,black)
    screen.blit(instruct,(width+10,205))    

    #equation array
    equation = []
    
    done = False

    #each cycle update/quit
    active = True
    while active:
    
        #render equations
        screen.set_clip(width+10, height-30, width+extrawidth, height)
        screen.fill(lightgrey)

        eq = ''.join(equation)
        eq = eq.replace(" ","")

        eqshow = font.render("Function: y="+eq,1,black)
        screen.blit(eqshow, (width+10,height-30))

        #update screen
        pygame.display.update()

        #check for inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Exit
                active = False
                done = True
                
            elif event.type == pygame.KEYDOWN:

                #symbols
                if event.unicode == u'*':
                    equation.append('*')
                elif event.unicode == u'/':
                    equation.append('/')
                elif event.unicode == u'+':
                    equation.append('+')
                elif event.unicode == u'-':
                    equation.append('-')
                elif event.unicode == u'.':
                    equation.append('.')
                elif event.unicode == u'(':
                    equation.append('(')
                elif event.unicode == u')':
                    equation.append(')')
                elif event.unicode == u'^':
                    equation.append('**')
                
                #numbers
                elif event.key == K_0:
                    equation.append('0')
                elif event.key == K_1:
                    equation.append('1')
                elif event.key == K_2:
                    equation.append('2')
                elif event.key == K_3:
                    equation.append('3')
                elif event.key == K_4:
                    equation.append('4')
                elif event.key == K_5:
                    equation.append('5')
                elif event.key == K_6:
                    equation.append('6')
                elif event.key == K_7:
                    equation.append('7')
                elif event.key == K_8:
                    equation.append('8')
                elif event.key == K_9:
                    equation.append('9')

                #mathematical functions
                elif event.key == K_s:
                    equation.append("sin(")
                elif event.key == K_c:
                    equation.append("cos(")
                elif event.key == K_t:
                    equation.append("tan(")
                elif event.key == K_r:
                    equation.append("sqrt(")
                elif event.key == K_a:
                    equation.append("abs(")
                elif event.key == K_l:
                    equation.append("log10(")
                elif event.key == K_n:
                    equation.append("log(")
                elif event.key == K_e:
                    equation.append("e")
                elif event.key == K_p:
                    equation.append("pi")
                    
                #x variable and operations
                elif event.key == K_x:
                    equation.append('x')
                elif event.key == K_BACKSPACE:
                    try:
                        equation.pop(-1)
                    except:
                        pass
                elif event.key == K_q:
                    graphlist = []
                    main(graphlist)
                elif event.key == K_RETURN:
                    active = False

    #quit/graph 
    if done:
        pygame.quit()
    else:
        if len(graphlist) <= 6:
            graphlist.append(eq)
        screen.set_clip(width,0,width+extrawidth,height-30)
        screen.fill(lightgrey)
        screen.set_clip(None)
        
        graphequation(graphlist,k)
    sys.exit()

#draw graph equation
def graphequation(graphlist,k):
    for eq in graphlist:
        graphcolour = graphcolours[graphlist.index(eq)%5]       
        
        #graph equation for each value of x + catch domain errors
        for i in range(width):
            try:
                #Get coordinate for x value
                x = (width/2-i)/float(k)
                y = eval(eq)
                pos1 = (width/2+x*k, height/2-y*k)

                #Get coordinate for next x value
                nx = (width/2-(i+1))/float(k)
                x = nx
                ny = eval(eq)
                pos2 = (width/2+nx*k, height/2-ny*k)

                #Draw line between both coordinates and exclude asymptotic lines
                dist = sqrt(((int(pos2[1])-int(pos1[1]))**2)+((int(pos2[0])-int(pos1[0]))**2))
                if dist < 2000:
                    pygame.draw.line(screen, graphcolour, pos1, pos2, 3)
            except:
                pass

    #Compute plot information
##    x=0
##    try:
##        yint = eval(eq)
##        yint = round(yint,4)
##
##        instruct = font.render('Press "Y" to plot the intercept',1,black)
##        screen.blit(instruct,(width+10,130))
##    except:
##        yint = "N/A"
    x = Symbol("x")
    try:
        answer = solve(eq,x)
        if answer:
            instruct = font.render(f"Roots: {str(answer).strip('[]')}",1,black)
            screen.blit(instruct,(width+10, 100))
        else:
            instruct = font.render("This graph is undefined at y=0",1,black)
            screen.blit(instruct,(width+10, 100))
    except:
        instruct = font.render("Roots are not supported with this equation type",1,black)
        screen.blit(instruct,(width+10, 100))
    
    #Rerender text + plot information
    title = font2.render("Solvector", 1, titlecolour)
    screen.blit(title, (width+10, 20))  
    instruct = font.render('"Q" - Clear',1,black)
    screen.blit(instruct,(width+10,70))
##    instruct = font.render(f"y intercept = (0,{yint})",1,black)
##    screen.blit(instruct, (width+10, 100))
    instruct = font.render('"I" - zoom in | "O" - zoom out',1,black)
    screen.blit(instruct, (width+10, 130))
    instruct = font.render('"G" - Add New Graph',1,black)
    screen.blit(instruct, (width+10, 160))
    
    #Find value of function at given x
    xvalue = []
    xval = '-'
    yval = '-'
    
    #window loop
    active = True
    while active:

        #Display x and y values
        screen.set_clip(width+10,210,width+extrawidth,250)
        screen.fill(lightgrey)
        xdisplay = ''.join(xvalue)
        xdisplay = xdisplay.replace(' ','')
        plotx = font.render(f"x = {xdisplay}",1,black)
        screen.blit(plotx, (width+10, 240))
        ploty = font.render(f"({xval},{yval})",1,black)
        screen.blit(ploty, (width+210, 240))
        instruct = font.render('"Enter" - plot x value',1,black)
        screen.blit(instruct,(width+10, 210))
        instruct = font.render('Equations:',1,black)
        screen.blit(instruct,(width+10, 280))

        #Output list of graphs and colous
        for i in range(len(graphlist)):
            graphs = font.render(f'{i+1}) {graphlist[i]} - {colournames[i%5]}',1,black)
            screen.blit(graphs,(width+100,280+(i*25)))
        screen.set_clip(None)
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Exit
                active = False

            #functions and operations after graphing
            elif event.type == pygame.KEYDOWN:#Check for reset
                if event.key == K_q:
                    graphlist = []
                    main(graphlist)
                elif event.key == K_y:#Check for y intercept
                    pygame.draw.circle(screen, red, (width/2,height/2-yint*k), 4)
                elif event.key == K_i:#Zoom in
                    try:
                        k += 5
                        graphbackground(k,graphlist)
                        graphequation(graphlist,k)
                    except:
                        pass
                elif event.key == K_o:#Zoom out
                    if (k-5)>0:
                        try:
                            k -= 5
                            graphbackground(k,graphlist)
                            graphequation(graphlist,k)
                        except:
                            pass
                elif event.key == K_RETURN:#Generate plot for x-value
                    try:
                        xval = float(xdisplay)
                        x = xval
                        yval = round(eval(eq),4)
                        pygame.draw.circle(screen,red,(width/2+x*k,height/2-yval*k),4)
                        xvalue = []
                    except:
                        pass
                elif event.key == K_BACKSPACE:#Clear x-value
                    try:
                        xvalue.pop(-1)
                    except:
                        pass
                elif event.key == K_g:#Plot new graph
                    main(graphlist)
                        
                #Number/decimal entry for x and y values
                elif event.key == K_0:
                    xvalue.append('0')
                elif event.key == K_1:
                    xvalue.append('1')
                elif event.key == K_2:
                    xvalue.append('2')
                elif event.key == K_3:
                    xvalue.append('3')
                elif event.key == K_4:
                    xvalue.append('4')
                elif event.key == K_5:
                    xvalue.append('5')
                elif event.key == K_6:
                    xvalue.append('6')
                elif event.key == K_7:
                    xvalue.append('7')
                elif event.key == K_8:
                    xvalue.append('8')
                elif event.key == K_9:
                    xvalue.append('9')
                elif event.unicode == u'.':
                    xvalue.append('.')
                elif event.unicode == u'-':
                    xvalue.append('-')
        

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main(graphlist)

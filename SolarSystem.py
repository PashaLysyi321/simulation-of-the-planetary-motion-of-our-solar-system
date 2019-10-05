import pygame, math
from pygame import *
import math
import datetime

class window():
    WIN_WIDTH = 1920
    WIN_HEIGHT = 1080
    X0 = WIN_WIDTH // 2
    Y0 = WIN_HEIGHT // 2
    DISPLAY = (WIN_WIDTH,WIN_HEIGHT)

    def initwindow(self):
        pygame.init()
        pygame.display.set_caption("Solar System") 

    screen = pygame.display.set_mode(DISPLAY) 
    bg = Surface((WIN_WIDTH,WIN_HEIGHT))

    def initspace(self):   
        self.bg.fill(Color('#000022'))
        draw.circle (self.bg, Color('yellow'), (self.X0, self.Y0), 20)
        self.screen.blit(self.bg, (0, 0)) 

class motionObject(window): pass

class planet(motionObject):
    PLANET_WIDTH = 20
    PLANET_HEIGHT = 20
    NumberOfPlanet = 8

    planetsMass = [0]*NumberOfPlanet
    for i in range(len(planetsMass)):
    	planetsMass[i] = Surface((PLANET_WIDTH, PLANET_HEIGHT))

    for i in range(len(planetsMass)):
        planetsMass[i].fill(Color('#000022'))

class initobjects(planet):
    def initsun(self):
        draw.circle (self.bg, Color('yellow'), (self.X0, self.Y0), 20)
    def initplanets(self):
    	colors = ["mediumspringgreen","Aquamarine","grey","peru","darkred","blue","darkorange","Dark Olive Green"]
    	for i in range(len(colors)):
            draw.circle (self.planetsMass[i], Color(colors[i]),(self.PLANET_WIDTH // 2, self.PLANET_HEIGHT // 2), 8)
        
class contoller(planet):
    def __init__(self):
        self.textboostinform =  'Boost field'
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = pygame.Color('dodgerblue2')
        self.active = False
        self.text = ''
        self.done = False
        self.textaccesstoplanet =  'To find information about planets press on it'
        self.NowTime ='Now is '
        self.boost = 1
        self.textShow = 'textShow'
        self.days = 0
        self.positioninfo = {
                'mercury':{'x0':57.8,'y0':56.57,'t':4.09090909,'shiftX':-21.9,'shiftY':-10},
                'venus':{'x0':108.2,'y0':108.2,'t':1.60213618,'shiftX':-10.7,'shiftY':-10},
				'earth':{'x0':149.6,'y0':149.6,'t':0.98630137,'shiftX':-12.5,'shiftY':-10},
				'mars':{'x0':250,'y0':247,'t':0.524261665,'shiftX':-22.5,'shiftY':-10},
				'jupiter':{'x0':300,'y0':299,'t':0.0831036268,'shiftX':-24.615,'shiftY':-10},
				'saturn':{'x0':353.3886,'y0':353.4636,'t':0.033455839,'shiftX':-27.25,'shiftY':-10},
				'uranus':{'x0':399,'y0':399,'t':0.0117306476,'shiftX':-28.21,'shiftY':-10},
				'neptune':{'x0':450,'y0':450,'t':0.00598136311,'shiftX':-10,'shiftY':-10}
        }  
        self.planetinfo = {
                'mercury': {'name': 'Mercury','weight': '3.33022e+23', 'radius': '2439.7', 'square': '7.48e+7', 'speed': '47.36', 'period': '58.646' },
				'venus': {'name': 'Venus','weight': '4.8675e+24', 'radius': '6051.8', 'square': '4.6e+8', 'speed': '35.02', 'period': '243.023' },
				'earth': {'name': 'Earth','weight': '5.9726e+24', 'radius': '6371', 'square': '5.1e+8', 'speed': '29.783', 'period': '365.25' },
				'mars': {'name': 'Mars','weight': '6.4171e+23', 'radius': '3389.5', 'square': '1.4437e+8', 'speed': '24.077', 'period': '243.023' },
				'jupiter': {'name': 'Jupiter','weight': '1.8986e+27', 'radius': '69911', 'square': '6.21796e+10', 'speed': '12.6', 'period': '9.925' },
				'saturn': {'name': 'Saturn','weight': '5.6846e+26', 'radius': '58232', 'square': '4.272e+10', 'speed': '10.5', 'period': '4332.589' },
				'uranus': {'name': 'Uranus','weight': '8.6832e+25', 'radius': '25362', 'square': '8.1156e+9', 'speed': '2.59', 'period': '17.25' },
  				'neptune': {'name': 'Neptune','weight': '1.0243e+26', 'radius': '24622', 'square': '7.6408e+9', 'speed': '2.68', 'period': '15.95' },
 				'sun': {'name': 'Sun','weight': '1.9885e+30', 'radius': '6.9551e+8', 'square': '6.07877e+18', 'speed': '2.2e+5', 'period': '2.25e+8' }}
        self.planetss = ['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune'] 
    
    def timelastopen(self):
        f = open('C:/Users/lysyi/Desktop/Project/text.txt', 'a')
        f.write(datetime.datetime.now().ctime()+'\n')
        f.write('///////////////////////'+'\n')

    def getboost(self, text):
        while True:
            boost = text
            try:
                boost = float(boost)
                if boost < 0 :
                    print("Oops!  You need number > 0.  Try again...")
                    boost = 0
                    return boost
                elif boost > 10000 :
                    print("Oops!  You need number between 1 and 10000.  Try again...")
                    boost = 0
                    return boost
                else:
                    return boost    
            except ValueError:
                print('Are u seriously??? U need a number!')
                boost = 0
                return boost

    def countT1(self, t, period):
        return t + period

    def countX(self,radius, t, centre, shift):
        return radius*math.cos(math.radians(t))+centre+shift

    def countY(self,radius, t, centre, shift):
        return radius*math.sin(math.radians(t))+centre+shift

    def countTime(self, t, count, multiplier):
        return t+count*multiplier

    def get_deltadays(self):
        now = datetime.datetime.now()
        time = datetime.datetime(1982, 3, 10)
        delta = now - time 
        result = delta.days
        return result   

    def putsplantsontheirposition(self):
        #puts planets in the right places
        count = self.get_deltadays()
        timemass =[0]*len(self.planetss)

        while count != 0:
            for i in range(len(self.planetss)):
                timemass[i]  = self.countT1(timemass[i], self.positioninfo[self.planetss[i]]['t'])
            count = count - 1 
        return timemass
     
    def update(self):
        pygame.font.init()
        font = pygame.font.Font(None, 45)
        input_box = pygame.Rect(1630, 950, 140, 45)
        myfontforplanet = pygame.font.SysFont('Comic Sans MS', 25)
        timer = pygame.time.Clock()
        
        coordinateT = [0] *len(self.planetss)
        coordinateX = [0] *len(self.planetss)
        coordinateY = [0] *len(self.planetss)

        for i in range(len(self.planetsMass)):	
            coordinateT[i] = self.putsplantsontheirposition()[i]
        
        # do not change any data!!!!111!!! planet run!!!
        while not self.done:
            multiplier = 0.0075*self.boost
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.done = True
                    break        
                if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        self.active = not self.active
                    else:
                        self.active = False
                    if event.button == 1:
                        if(event.pos[0]>self.X0-20 and event.pos[0]<self.X0+20 and event.pos[1]>self.Y0-20 and event.pos[1]<self.Y0+20):
                            self.textShow = 'sun'
                        else:
                            for i in range(len(self.planetsMass)): 
                                if (event.pos[0]>coordinateX[i]-15 and event.pos[0]<coordinateX[i]+15 and event.pos[1]>coordinateY[i]-15 and event.pos[1]<coordinateY[i]+15):
                                    self.textShow = self.planetss[i]
                        
                # Change the current color of the input box.
                self.color = self.color_active if self.active else self.color_inactive
                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            self.text = self.getboost(self.text)
                            self.boost = int(self.text)
                            self.text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode

            # Render the current text.
            txt_surface = font.render(self.text, True, self.color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
           
            if self.textShow != 'textShow':
                info = '%s :   weight = %s kg,  radius = %s km,  square = %s km^2,  speed = %s km/c,  period = %s days' % (self.planetinfo[self.textShow]['name'],self.planetinfo[self.textShow]['weight'],self.planetinfo[self.textShow]['radius'],self.planetinfo[self.textShow]['square'],self.planetinfo[self.textShow]['speed'],self.planetinfo[self.textShow]['period'])
                textsurface =  myfontforplanet.render(info, False, (255, 255, 255))
                
            # Blit the input_box rect.
            pygame.draw.rect(self.screen, self.color, input_box, 2) 
            self.screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            pygame.display.flip()

            for i in range(len(self.planetsMass)):
            	coordinateX[i] = self.countX(self.positioninfo[self.planetss[i]]['x0'], coordinateT[i], self.X0, self.positioninfo[self.planetss[i]]['shiftX'])
            	coordinateY[i] = self.countY(self.positioninfo[self.planetss[i]]['y0'], coordinateT[i], self.Y0, self.positioninfo[self.planetss[i]]['shiftY'])
            	coordinateT[i] = self.countTime(coordinateT[i] ,self.positioninfo[self.planetss[i]]['t'],multiplier) 

            self.screen.blit(self.bg, (0, 0))	

            for i in range(len(self.planetsMass)):	
            	self.screen.blit(self.planetsMass[i], (coordinateX[i], coordinateY[i]))
            
            self.screen.blit(myfontforplanet.render(self.textboostinform, False, (47, 56, 148)),(1700,900))
            self.screen.blit(myfontforplanet.render(self.textaccesstoplanet, False, (47, 56, 148)),(20,1000))
  
            self.days = self.days + 1*multiplier
            daysconverted = round(self.days, 2)

            nowtimeD = 'Now data is %s days' % daysconverted
            yearsconverted = round(self.days/365, 2)

            nowtimeY = 'Now data is %s years' % yearsconverted
            
            self.screen.blit(myfontforplanet.render(nowtimeD, False, (47, 56, 148)),(1550,50))
            self.screen.blit(myfontforplanet.render(nowtimeY, False, (47, 56, 148)),(1550,90))
            self.screen.blit(myfontforplanet.render('From today', False, (47, 56, 148)),(1550,130))

            if self.textShow != 'textShow':
                self.screen.blit(textsurface,(250,10))  
            timer.tick()  

class run(initobjects, contoller):
    def main(self):
        wind = window()
        planets = planet()
        init = initobjects()
        planetsrun = contoller()

        wind.initwindow()
        wind.initspace()
        init.initsun()
        init.initplanets()
        planetsrun.timelastopen()
        planetsrun.update()   

if __name__ == "__main__":
    start = run()
    start.main()
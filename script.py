import sys
import math

class Unite:
    def __init__(self, entity_id  , entity_type,x,y,vx, vy  ,state):
        self.id = entity_id
        self.type = entity_type
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.state = state

def distance(objet1,objet2):
    x1=objet1.x
    y1=objet1.y
    x2=objet2.x
    y2=objet2.y
    d=((x2-x1)**2+(y2-y1)**2)**0.5
    return d

def distancei(objet1,objet2):
    x1=objet1.x+objet1.vx
    y1=objet1.y+objet1.vy
    x2=objet2.x+objet2.vx
    y2=objet2.y+objet2.vy

    d=((x2-x1)**2+(y2-y1)**2)**0.5
    return d

def proche(objet,liste_objet):
    objet0=liste_objet[0]
    d0=distancei(objet,objet0)
    for objet2 in liste_objet:
        d=distancei(objet,objet2)
        if d<d0:
            d0=d
            objet0=objet2
    return objet0



def scalaire(objet1,objet2,but):
    x1=objet1.x
    y1=objet1.y
    x2=objet2.x
    y2=objet2.y
    xbut=but.x
    ybut=but.y
    p= (x2-x1)*(xbut-x2)+(y2-y1)*(ybut-y2)
    return p

def aligne(objet1,objet2,but):
    if abs(distance(objet1,objet2)*distance(objet2,but)-scalaire(objet1,objet2,but))<100:
        return True
    else:
        return False

def ordoneebut(objet1,objet2):
    x1=objet1.x
    y1=objet1.y
    x2=objet2.x
    y2=objet2.y
    if x2-x1!=0:
        ybord=(y2-y1)/(x2-x1)*(xbut-x1)+y2
    else:
        ybord=0
    return ybord

def flip(objet,liste_objet):
    for objet2 in liste_objet:
        y=ordoneebut(objet,objet2)
        if 2150<y<5350 and (objet2.x-objet.x)*(-1)**my_team_id>0 and distance(objet,objet2)>700:
            return objet2
        else:
            return False

var1 = None
var2= 0
var3 = 0
oldsorcier1x = 0
oldsorcier1y = 0
oldsorcier2x = 0
oldsorcier2y = 0
my_team_id = int(input())  
xbut=16000*(1-my_team_id)
ybut=3750
# game loop
while True:
    
    mywizards=[]
    balls=[]
    bludgers=[]
    my_score, my_magic = [int(i) for i in input().split()]
    opponent_score, opponent_magic = [int(i) for i in input().split()]
    entities = int(input())  
    for i in range(entities):
        inputs = input().split()
        entity_id = int(inputs[0]) 
        entity_type = inputs[1]  
        x = int(inputs[2])  
        y = int(inputs[3]) 
        vx = int(inputs[4])  
        vy = int(inputs[5])  
        state = int(inputs[6])  
        objet = Unite(entity_id  , entity_type,x,y,vx, vy  ,state)
        if entity_type == "WIZARD":
            mywizards.append(objet)
        elif entity_type == "SNAFFLE":
            balls.append(objet)
        elif entity_type == "BLUDGER":
            bludgers.append(objet)

    for i in range(2):
        var3 = var3+1
        sorcier=mywizards[i]
        ballonp=proche(sorcier, balls)
        ballon=flip(sorcier,balls)
        bludger=proche(sorcier,bludgers)

        if (var3 % 2) == 0:
            oldsorcier1x = sorcier.x
            oldsorcier1y = sorcier.y
        else:
            oldsorcier2x = sorcier.x
            oldsorcier2y = sorcier.y
    for i in range(2):
        var2 = var2+1
        sorcier=mywizards[i]

        ballonp=proche(sorcier, balls)
        ballon=flip(sorcier,balls)


        bludger=proche(sorcier,bludgers)


        if sorcier.state!=0:
            if (var2 % 2) == 0:
                if my_team_id == 0:
                    if oldsorcier1x - oldsorcier2x < 0 and ((oldsorcier2x-oldsorcier1x)**2+(oldsorcier2y-oldsorcier1y)**2)**0.5 <= 4000 and ((xbut-oldsorcier1x)**2+(ybut-oldsorcier1y)**2)**0.5 >= 4000:
                        print("THROW {} {} 500 tire".format(oldsorcier2x,oldsorcier2y))
                    else:
                        print("THROW {} {} 500 tire".format(xbut,ybut))
                    
                else:
                    if oldsorcier1x - oldsorcier2x > 0 and ((oldsorcier2x-oldsorcier1x)**2+(oldsorcier2y-oldsorcier1y)**2)**0.5 >= 4000 and ((xbut-oldsorcier1x)**2+(ybut-oldsorcier1y)**2)**0.5 <= 4000:
                        print("THROW {} {} 500 tire".format(oldsorcier2x,oldsorcier2y))
                    else:
                        print("THROW {} {} 500 tire".format(xbut,ybut))
            else:
                if my_team_id == 0:
                    if oldsorcier2x - oldsorcier1x < 0 and ((oldsorcier1x-oldsorcier2x)**2+(oldsorcier1y-oldsorcier2y)**2)**0.5 <= 4000 and ((xbut-oldsorcier2x)**2+(ybut-oldsorcier2y)**2)**0.5 >= 4000:
                        print("THROW {} {} 500 tire".format(oldsorcier1x,oldsorcier1y))
                    else:
                        print("THROW {} {} 500 tire".format(xbut,ybut))
                    
                else:
                    if oldsorcier2x - oldsorcier1x > 0 and ((oldsorcier1x-oldsorcier2x)**2+(oldsorcier1y-oldsorcier2y)**2)**0.5 >= 4000 and ((xbut-oldsorcier2x)**2+(ybut-oldsorcier2y)**2)**0.5 <= 4000:
                        print("THROW {} {} 500 tire".format(oldsorcier1x,oldsorcier1y))
                    else:
                        print("THROW {} {} 500 tire".format(xbut,ybut))


        elif ballon and my_magic>=20 and sorcier.y > 1200 and sorcier.y < 6000 and ballonp.y > 1200 and ballonp.y < 6000:
            print("FLIPENDO {} flip".format(ballon.id))
            my_magic-=20

        elif my_magic>=15 and ballonp.x > 0 and  ballonp.x < 16000:
            if sorcier.x - ballonp.x > 0 and my_team_id == 0 and sorcier.x - ballonp.x > 500 and sorcier.x - ballonp.x < 6000:     
                print("ACCIO {} accio".format(ballonp.id))
                my_magic-=15
            elif sorcier.x - ballonp.x < 0 and my_team_id == 1 and sorcier.x - ballonp.x < -500 and sorcier.x - ballonp.x > -10000:
                print("ACCIO {} accio".format(ballonp.id))
                my_magic-=15
            else:
                ballonp=proche(sorcier, balls)
                print("MOVE {} {} 150 go".format(ballonp.x,ballonp.y))
       
        else:

            ballonp=proche(sorcier, balls)
            print("MOVE {} {} 150 go".format(ballonp.x,ballonp.y))
                        

        



from random import randint
class Loup():
    def __init__(self,posx,posy):
        self.force=5
        self.vit=5
        self.hpmax=randint(30,50)
        self.hp=randint(20,self.hpmax)
        self.range=5
        self.x=posx
        self.y=posy

    def deplace(self,xs,ys):
        if self.x+self.vit>30:
            self.x=(self.x+randint(-self.vit,0))%xs
        elif self.x < 0:
            self.x=(self.x +randint(0,self.vit))%xs
        if self.y+self.vit>30:
            self.y=(self.y+randint(-self.vit,0))%ys
        elif self.y < 0:
            self.y=(self.y +randint(0,self.vit))%ys
        else:
            self.x=(self.y+randint(-self.vit,self.vit))%ys
            self.y=(self.y+randint(-self.vit,self.vit))%ys



    def corpsacorps(self,autre):
        if self.hp!=0 and autre.hp!=0:
            self.hp=max(self.hp-autre.force,0)
            autre.hp=max(autre.hp-self.force,0)



        #ce déplacement est à changer, un personnage ne doit pas apparaitre sur le bord droit pour réapparaitre sur le bord gauche et le déplacement d'un loup doit être aléatoire. s'il reste sur place, il doit récupérer des hp et perdre des hp si le déplacement est important

class Archer():
    def __init__(self,posx,posy):
        self.force=1
        self.vit=1
        self.hpmax=randint(10,20)
        self.hp=randint(10,self.hpmax)
        self.range=10
        self.x=posx
        self.y=posy
        self.fleche=1

    def deplace(self,xs,ys):
        self.x=(self.x+randint(-self.vit,self.vit))%xs
        self.y=(self.y+randint(-self.vit,self.vit))%ys

    def corpsacorps(self,autre):
        if self.hp!=0 and autre.hp!=0:
            self.hp=max(self.hp-autre.force,0)
            autre.hp=max(autre.hp-self.force,0)

    def tiralarc(self,autre):
        if self.hp!=0 and autre.hp!=0:
            autre.hp=max(autre.hp-self.fleche, 0)



class Guerrier():
    def __init__(self,posx,posy):
        self.force=4
        self.vit=3
        self.hpmax=randint(20,40)
        self.hp=randint(20,self.hpmax)
        self.range=5
        self.x=posx
        self.y=posy

    def deplace(self,xs,ys):
        self.x=(self.x+randint(-self.vit,self.vit))%xs
        self.y=(self.y+randint(-self.vit,self.vit))%ys

    def corpsacorps(self,autre):
        if self.hp!=0 and autre.hp!=0:
            self.hp=max(self.hp-autre.force,0)
            autre.hp=max(autre.hp-self.force,0)

class Voleur():
    def __init__(self,posx,posy):
        self.force=1
        self.vit=4
        self.hpmax=randint(5,10)
        self.hp=randint(5,self.hpmax)
        self.range=5
        self.x=posx
        self.y=posy
        self.stealth= randint(7,10)

    def deplace(self,xs,ys):
        self.x=(self.x+randint(-self.vit,self.vit))%xs
        self.y=(self.y+randint(-self.vit,self.vit))%ys

    def corpsacorps(self,autre):
        if self.hp!=0 and autre.hp!=0:
            if randint(1,10)<self.stealth:
                self.hp=max(self.hp-autre.force,0)
                autre.hp=max(autre.hp-self.force,0)
            else:
                autre.hp=max(autre.hp-self.force,0)
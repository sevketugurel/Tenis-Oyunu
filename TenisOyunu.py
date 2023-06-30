import pygame
import random

#Pygame hazırlık
genıslık=1200
yukseklik=750
pencere=pygame.display.set_mode((genıslık,yukseklik))

#FPS işlemleri
FPS=30
saat=pygame.time.Clock()

#Sınıflar
class Oyun():
    def __init__(self) -> None:
        pass
    def update(self):
        pass
    def cizdir(self):
        pass
    def temas(self):
        pass
    def oyunDurumu(self):
        pass
    def bitir(self):
        pass
    def oyun_resetle(self):
        pass

class Oyuncu1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("/Users/sevketugurel/Tenis Oyunu/1_oyuncu.png")
        self.rect=self.image.get_rect()
        self.rect.x=0

        #Oyuncu Değişken
        self.hiz=10

    def update(self):
        tus=pygame.key.get_pressed()
        if tus[pygame.K_w] and self.rect.top>=5:
            self.rect.y-=self.hiz
        elif tus[pygame.K_s] and self.rect.bottom<=yukseklik:
            self.rect.y+=self.hiz

class Oyuncu2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("/Users/sevketugurel/Tenis Oyunu/2_oyuncu.png")
        self.rect=self.image.get_rect()
        self.rect.x=genıslık-64

        #Oyuncu değişken
        self.hiz=10

    def update(self):
        tus=pygame.key.get_pressed()
        if tus[pygame.K_UP] and self.rect.top>=5:
            self.rect.y-=self.hiz
        elif tus[pygame.K_DOWN] and self.rect.bottom<=yukseklik:
            self.rect.y+=self.hiz

class Top(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("/Users/sevketugurel/Tenis Oyunu/top.png")
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.centery=y

        #top Değişkenleri
        self.yonx=1
        self.yony=1
        self.hiz=12


    def update(self):
        self.rect.centerx+=self.hiz*self.yonx
        self.rect.centery+=self.hiz*self.yony
        if self.rect.left<=0 or self.rect.right>=genıslık:
            self.yonx*=-1
        if self.rect.top<=0 or self.rect.bottom>=yukseklik:
            self.yony*=-1

#Oyuncu1 İşlemleri
oyuncu1_group=pygame.sprite.Group()
oyuncu_1=Oyuncu1()
oyuncu1_group.add(oyuncu_1)

#Oyuncu2 İşlemleri
oyuncu2_group=pygame.sprite.Group()
oyuncu2=Oyuncu2()
oyuncu2_group.add(oyuncu2)

#Top İşlemleri
top_grup=pygame.sprite.Group()
top=Top(random.randint(200,1000),random.randint(300,yukseklik-64))
top_grup.add(top)

#Oyun Döngüsü
durum=True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False
    pencere.fill((0,0,0))

    #1. Oyuncu İşlem Devamı
    oyuncu1_group.update()
    oyuncu1_group.draw(pencere)

    #2. Oyuncu İşlem devam
    oyuncu2_group.update()
    oyuncu2_group.draw(pencere)
    
    #Top İşlem devam
    top_grup.update()
    top_grup.draw(pencere)

    pygame.display.update()
    saat.tick(FPS)
    
pygame.quit()









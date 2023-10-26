import pygame
import numpy as np
import os, inspect
import random
import pygame.surfarray as surfarray
from pygame.transform import scale
from pygame.transform import rotate

# Léna, Rémi, Raphael, Johana, Miliau


#recherche du répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"sprites")


#Sprites
    #Points
points_sprites100 = pygame.image.load(os.path.join(assets, "Points\point100.png"))
points_sprites100.set_colorkey(points_sprites100.get_at((0,0)))
points_sprites200 = pygame.image.load(os.path.join(assets, "Points\point200.png"))
points_sprites200.set_colorkey(points_sprites200.get_at((0,0)))
points_sprites500 = pygame.image.load(os.path.join(assets, "Points\point500.png"))
points_sprites500.set_colorkey(points_sprites500.get_at((0,0)))
points_sprites800 = pygame.image.load(os.path.join(assets, "Points\point800.png"))
points_sprites800.set_colorkey(points_sprites800.get_at((0,0)))

    #Tonneaux
barrel = pygame.image.load(os.path.join(assets, "barrelSprite.png"))
blueBarrel = pygame.image.load(os.path.join(assets, "blueBarrelSprite.png"))
vBarrel = pygame.image.load(os.path.join(assets, "vBarrelSprite.png"))
vBlueBarrel = pygame.image.load(os.path.join(assets, "vBlueBarrelSprite.png"))

    #Bonus
bonus_sprite = pygame.image.load(os.path.join(assets, "bonus.png"))
bonus_sprite.set_colorkey(bonus_sprite.get_at((0,0)))
bonus_x = 450
bonus_y = 40

    #Animation haut de l'echelle
mario_echelle1 = pygame.image.load(os.path.join(assets, "Mario\mario_echelle1.png"))
mario_echelle1.set_colorkey(mario_echelle1.get_at((0,0)))
mario_echelle2 = pygame.image.load(os.path.join(assets, "Mario\mario_echelle2.png"))
mario_echelle2.set_colorkey(mario_echelle2.get_at((0,0)))
mario_echelle3 = pygame.image.load(os.path.join(assets, "Mario\mario_echelle3.png"))
mario_echelle3.set_colorkey(mario_echelle3.get_at((0,0)))

    #Marteau
marteau = pygame.image.load(os.path.join(assets, "Mario\marteau.png"))
marteau.set_colorkey(marteau.get_at((0,0)))
marteau2 = pygame.image.load(os.path.join(assets, "Mario\marteau.png"))
marteau2.set_colorkey(marteau2.get_at((0,0)))

marteau_x = 500
marteau_y = 470
marteau2_x = 90
marteau2_y = 230

    #Vie de Mario
mario_vie = pygame.image.load(os.path.join(assets, "Mario\mario_vie.png"))
mario_vie.set_colorkey(mario_vie.get_at((0,0)))

    #HitBox
hitbox = pygame.image.load(os.path.join(assets, "hitbox_map.png"))
hitbox_barrel = pygame.image.load(os.path.join(assets, "hitbox_barrel.png"))

    #Mario
mario_sprites = pygame.image.load(os.path.join(assets, "Mario\mario.png"))
mario_sprites.set_colorkey(mario_sprites.get_at((0,0)))

mort1 = pygame.image.load(os.path.join(assets, "Mario\mort1.png"))
mort1.set_colorkey(mort1.get_at((0,0)))
mort2 = pygame.image.load(os.path.join(assets, "Mario\mort2.png"))
mort2.set_colorkey(mort2.get_at((0,0)))
mort3 = pygame.image.load(os.path.join(assets, "Mario\mort3.png"))
mort3.set_colorkey(mort3.get_at((0,0)))
mort4 = pygame.image.load(os.path.join(assets, "Mario\mort4.png"))
mort4.set_colorkey(mort4.get_at((0,0)))
mort5 = pygame.image.load(os.path.join(assets, "Mario\mort5.png"))
mort5.set_colorkey(mort5.get_at((0,0)))


   #BackGround
BackGsprites = pygame.image.load(os.path.join(assets, "BGSpritesNoATH.png"))
CouleurFondSprite = BackGsprites.get_at((BackGsprites.get_width()-1, BackGsprites.get_height()-1))
BackGsprites.set_colorkey(CouleurFondSprite)


      #Creation des sprites BGSprites
BGSprites = []
for i in range(8):
   spr = BackGsprites.subsurface((232*i, 0, 224,256))#un pixel de plus de ce qu'on veut dans selection du rectangle
   spr = scale(spr, (600, 600))#changement de scale
   BGSprites.append( spr )


   #Donkey
DonkeySprites = pygame.image.load(os.path.join(assets, "DonkeySprites.png"))


   #Peach et Help
peach1Sprite = pygame.image.load(os.path.join(assets, "Peach\peach1.png"))
peach2Sprite = pygame.image.load(os.path.join(assets, "Peach\peach2.png"))
peach3Sprite = pygame.image.load(os.path.join(assets, "Peach\peach3.png"))

helpSprite = pygame.image.load(os.path.join(assets, "Peach\help.png"))
helpSprite.set_colorkey((helpSprite.get_at((0, 0))))

    #Huile
huileSprite = pygame.image.load(os.path.join(assets, "HuileSprites.png"))
        #Creation des sprites BGSprites
HuileSprites = []
for i in range(5):
   spr = huileSprite.subsurface((50*i, 0, 45, 84))
   HuileSprites.append(spr)

DoHuileAnimation = False
HuileSpr = HuileSprites[0]

#Fonctions
    #Chargement des sprites mario
def ChargeSerieSprites(id, width, height,flip):
    sprite = []
    for i in range(4):
        spr = mario_sprites.subsurface((width * i, height * id, 59,32))
        spr.set_colorkey(spr.get_at((0,0)))
        test = spr.get_at((10,10))
        if ( test != (0,0,0) ):
            if flip:
                spr = pygame.transform.flip(spr, True , False)
                spr.set_colorkey(spr.get_at((0,0)))
            sprite.append( spr )
    return sprite

    #Chargement des sprites DK
def ChargeSerieDKSprites(id):
    sprite = []
    for i in range(3):
        spr = DonkeySprites.subsurface((90*i, 65*id, 90,65))
        test = spr.get_at((20,20))
        if ( test != (255, 255, 255)):#different de blanc
            spr = scale(spr, (120, 85))#changement de scale
            sprite.append( spr )
    return sprite

    #Lancement des tonneaux
def ThrowBarrel():
    global DonSpr
    global normalBarrelCount
    global DKblueBarrel
    global randAngryDK

    if(normalBarrelCount >= 2):#si on a lancé 15 barrel normal
        #if(random.randint(1, 3) == 1):#1 chance sur 3 d'en lancer un bleu
        DKblueBarrel = True

    if(DKblueBarrel):#lance un barrel bleu
        DonSpr = ThrowBBarrelDonkeySpr[DKTimeBarrel]
        normalBarrelCount = 0
    else:#lance un barrel normal
        DonSpr = ThrowNBarrelDonkeySpr[DKTimeBarrel]#animation du tonneau

    if(DKTimeBarrel==2):
        if(time10/100 >= time1000+0.05 and time10/100 <= time1000+0.09):#fait l'action qu'une seule fois
            randAngryDK = random.randint(1, 100)#change l'animation d'attente
            if(not DKblueBarrel): normalBarrelCount += 1

            NewBarrel(DKblueBarrel,False)#crée un nouveau barril bleu ou non
            print(str(len(barrelLIST)))
            DKblueBarrel = False#remet le barrel en normal

def NewBarrel(isBlue, first):
    global barrelLIST

    new_barrel = {}
    new_barrel['x'] = 144
    new_barrel['y'] = 172
    new_barrel['vy'] = 3
    new_barrel['vx'] = 3
    new_barrel['barrelYCount'] = 0
    new_barrel['blue'] = isBlue
    new_barrel['first'] = first
    new_barrel['etat'] = etatPlatform
    new_barrel['rand'] = 1
    new_barrel['marioSaut'] = False
    barrelLIST.append(new_barrel)

###################################################################################

# Initialize pygame
pygame.init()


police = pygame.font.SysFont("Arial", 25)

ROUGE = (255, 0, 0)
BLEU = (0,6,255)
VERT = (31,255,0)
NOIR = (0,0,0)
BLANC = (255,255,255)
JAUNE = (255,255,0)
CYAN = (0,255,255)
ROSE = (255,0,255)

# Définit la longueur et la largeur de l'ecran
WINDOW_SIZE = [600,600]
screen = pygame.display.set_mode(WINDOW_SIZE)

#  Définit le titre du jeu
pygame.display.set_caption("DONKEY KONG ARCADE")

# Continue de fonctionner tant que le joueur ne clique pas sur la croix pour fermer la page
done = False

# Utilisé pour gérer la vitesse à laquelle l'ecran s'actualise
clock = pygame.time.Clock()

Etat                          = 0
EtatFrappeBougeSansArme       = 100
EtatFrappeImmobileSansArme    = 200
EtatFrappeBougeAvecArme       = 300
EtatFrappeImmobileAvecArme    = 400
EtatMarche                    = 500
EtatChute                     = 600
EtatMonte                     = 700
EtatMort                      = 800
EtatImmobileEchelle           = 900
EtatHautEchelle               = 1000
EtatSaut                      = 1100


mario_x = 100
mario_y = 550
mario_speed_g = True
mario_speed_d = True
hasArme = False
score = 0
vie = 3
estMort = False
compteurMort = 0
bonus = 5000
END = False
saut = False
phaseSaut = 1
hauteurSaut = 0
tombe = False
timeMarteau = 0
timeBonus = 0
Score800 = False
Score500 = False
Score200 = False
Score100 = False

#Chargement des sprites DK, Peach (tableau)
ClimbingDonkeySpr = ChargeSerieDKSprites(0)
AngryDonkeySpr = ChargeSerieDKSprites(1)
ThrowNBarrelDonkeySpr = ChargeSerieDKSprites(2)
ThrowBBarrelDonkeySpr = ChargeSerieDKSprites(3)

   #Peach
peachSprites = [peach3Sprite, peach2Sprite, peach1Sprite]

#Variables
   #Donkey
DonkeyDone = False#animation finit ou non
Dxx = screen.get_width()/2-10
Dyy = screen.get_height()-125
yCount = 0
Dvy = -2

DonkeyShowPeach = False #affiche peach que quand donkey est en haut
BGSpriteCount = 0 #changer les background au début

randAngryDK = random.randint(1, 100)
normalBarrelCount = 0
DKblueBarrel = False

    #Barrel
barrelLIST = []
firstBarrelDone = False
firstBarrelCount = 0
firstBarrelLastColor = VERT

etatPlatform = 0
etatTakeEchelle = 1
etatContinuePlatform = 2

   #Peach
help_x = 235
help_y = 80

peach_x = 236
peach_y = 98
peach_vx = 2

PeachLCount = 0
PeachTime = -5#au début, peach bouge 1-2s après avoir été affiché
PeachFlip = False
showHelp = True




# -------- Boucle principale du programme -----------
    #Chargements des sprites mario
frappeAvecArmeImmobile     = ChargeSerieSprites(0,60,33,False)
frappeAvecArmeBouge        = ChargeSerieSprites(1,60,33,False)
immobile                   = ChargeSerieSprites(2,60,33,False)
chute                      = ChargeSerieSprites(3,60,33,False)
frappeSansArmeImmobile     = ChargeSerieSprites(4,60,33,False)
frappeSansArmeBouge        = ChargeSerieSprites(5,60,33,False)
marche                     = ChargeSerieSprites(6,60,33,False)
monte                      = ChargeSerieSprites(7,60,33,False)
immobileEchelle            = ChargeSerieSprites(8,60,33,False)
saute                      = ChargeSerieSprites(9,60,33,False)
sommetEchelle              = ChargeSerieSprites(10,60,33,False)


pygame.mouse.set_visible(1)

while not done:
    event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event

    time10 = int(pygame.time.get_ticks()/ 10)
    time80 = int( pygame.time.get_ticks() / 80)
    time200 = int(pygame.time.get_ticks() / 200)
    time300 = int(pygame.time.get_ticks() / 300)
    time500 = int( pygame.time.get_ticks() / 500)
    time1000 = int(pygame.time.get_ticks()/ 1000)

    # dessine le fond
    screen.blit(BGSprites[BGSpriteCount],(0,0))#pour la visibilité


    # gestion des évènements
    for event in pygame.event.get():  # Le joueu fait une action
        if event.type == pygame.QUIT:  # Si le joueur appuye sur la croix
            done = True  # Montre que le joueur a finit et termine la boucle

    #Boucle cinematique
    if(not DonkeyDone):
        if(Dyy == 145): #enlève l'echelle
            BGSpriteCount += 1
        if(Dyy == 115):#première étage
            BGSpriteCount += 1
        if(Dyy <= 114):#si Donkey assez haut, change de sprite et saute
            DonSpr = AngryDonkeySpr[0]
            DonkeyShowPeach = True
            Dyy += Dvy
            Dxx -= 4
            yCount += 1
            if(yCount%6==0):
                Dvy *= -1
                if(yCount%12==0):#change le fond du jeu(le étages se cassent)
                    BGSpriteCount += 1%8
            if(Dxx <= 50):#si  DK assez haut et assez à gauche
                DonkeyDone = True #animation finit
                Dxx = 50   #recale le sprite
                Dyy = 112
        else:
            DonSpr = ClimbingDonkeySpr[time200%len(ClimbingDonkeySpr)]
            Dyy -= 5

        #firstBarrel
    if(DonkeyDone  and not firstBarrelDone):
        DonSpr = ThrowBBarrelDonkeySpr[firstBarrelCount]
        if(DonSpr == ThrowBBarrelDonkeySpr[0] and (time10/100 >= time1000+0.95)): firstBarrelCount += 1
        if(DonSpr == ThrowBBarrelDonkeySpr[1] and (time10/100 >= time1000+0.95)):
            NewBarrel(True, True)
            firstBarrelDone = True


#Animation de Peach
    if(DonkeyShowPeach):
        if(time1000 >= PeachTime+10): #Si elle s'estarreté 10s
            if ( peach_x > 340 ): #si peach à droite
                peach_x = 339
                peach_vx = -abs(peach_vx)
                PeachFlip = True

            if ( peach_x < 235 ): #si peach à gauche
                PeachLCount += 1
                peach_x = 236
                peach_vx = abs(peach_vx)
                PeachFlip = False
                if(PeachLCount >= 2): #Si elle a fait 2 aller-retour
                    PeachTime = time1000 #attendra 10s
                    PeachLCount = 0


            peach_x += peach_vx
            help_x = peach_x+10

        #Message "Help" associé à Peach
        if(time1000%13 >= 5 and time1000%13 <= 8):#affiche 'Help' toute les 10 secondes pendant 3 secondes
            showHelp = True
        else: showHelp = False

#Affichage des sprites
    #Montre Peach
    peachShown = peachSprites[time300%len(peachSprites)]
    if(PeachFlip): peachShown = pygame.transform.flip(peachShown, True, False)

    peachShown.set_colorkey(peachShown.get_at((0, 0)))
    if(DonkeyShowPeach): screen.blit(peachShown,(peach_x,peach_y))
        #Montre message "Help"
    if(showHelp and DonkeyShowPeach): screen.blit(helpSprite,(help_x,help_y))

    #Montre Donkey
    DonSpr.set_colorkey(DonSpr.get_at((0, 0)))
    screen.blit(DonSpr, (Dxx, Dyy))

    ##Cinematic finit



    if DonkeyDone and firstBarrelDone:

        #Lancements des tonneaux
        DKTimeBarrel = time1000%(len(ThrowNBarrelDonkeySpr)+2)

        if(DKTimeBarrel>=3):#attend entre 2 barrel, fait différentes animations aléatoirement
            if(randAngryDK <= 65):#65% des cas
                DonSpr = AngryDonkeySpr[0]
            elif(randAngryDK <= 90):#25% des cas
                DonSpr = AngryDonkeySpr[time1000%(len(AngryDonkeySpr)-1)]
            else: DonSpr = AngryDonkeySpr[(time1000%(len(AngryDonkeySpr)-1))+1]#10% des cas

        else: #fait l'animation du tonneau
            ThrowBarrel()

        #Boucle Tonneaux
        for oneBarrel in barrelLIST:
            xx = oneBarrel['x']
            yy = oneBarrel['y']
            ColorPxG = hitbox_barrel.get_at((xx+4, yy+25))
            ColorPxD = hitbox_barrel.get_at((xx+barrel.get_width()-4, yy+25))
            vide = (ColorPxG == VERT and ColorPxG != BLEU) and ((ColorPxD == VERT and ColorPxD != BLEU))
            echelle = (hitbox_barrel.get_at((xx+4, yy+25)) == BLEU) or (hitbox_barrel.get_at((xx+4, yy+25)) == ROSE)
            etat = oneBarrel['etat']

            #déplacement du barrel
                #prend ou non l'echelle de manière aléatoire
            if(echelle and etat == etatPlatform):
                oneBarrel['rand'] = random.randint(1, 4)
                if(oneBarrel['rand'] == 1): oneBarrel['etat'] = etatTakeEchelle
                else: oneBarrel['etat'] = etatContinuePlatform
            if(not echelle):
                oneBarrel['etat'] = etatPlatform

                #Premier tonneau qui tombe tout à la verticale
            if(oneBarrel['first']):
                oneBarrel['x']=85
                oneBarrel['y']+=oneBarrel['vy']
                if(oneBarrel['vy']<= 7): oneBarrel['vy']+=1#limite sa vitesse
                if(firstBarrelLastColor != ROUGE and (ColorPxD == ROUGE or ColorPxG == ROUGE)):#ralentit sur les plateformes
                    oneBarrel['vy']=0
                    firstBarrelLastColor = ROUGE
                if(ColorPxD == VERT or ColorPxG == VERT):
                    firstBarrelLastColor = VERT

                #Autres tonneaux
            elif(vide or etat == etatTakeEchelle):
                oneBarrel['y'] += oneBarrel['vy']
                oneBarrel['barrelYCount'] += 1
                if(oneBarrel['barrelYCount'] >= 2 and oneBarrel['vy']<=7):
                    oneBarrel['vy'] += 1#tombe de plus en plus vite
                if(oneBarrel['barrelYCount'] == 3):
                    oneBarrel['vx'] *= -1
            else:
                oneBarrel['x'] += oneBarrel['vx']
                oneBarrel['barrelYCount'] = 0
                oneBarrel['vy'] = 3

                #recale le tonneau sur la dernière plateforme
                if(xx ==297 and yy >= 553):
                    oneBarrel['y'] += 3

                #faire tourner le tonneau
                if (time80%2==0):
                    barrel = rotate(barrel, 90)
                    blueBarrel = rotate(blueBarrel, 90)

            #supprime le tonneau et animation du barrel d'huile
            if(xx <= 90 and yy >= 525):#si il arrive
                barrelLIST.remove(oneBarrel)#à la fin
                DoHuileAnimation = True

            #Montre tonneau
            if(oneBarrel['first']): brl = vBlueBarrel
            elif(oneBarrel['blue'] == False and etat == etatTakeEchelle): brl = vBarrel
            elif(oneBarrel['blue'] == False and etat != etatTakeEchelle): brl = barrel
            elif(oneBarrel['blue'] == True and etat == etatTakeEchelle): brl = vBlueBarrel
            elif(oneBarrel['blue'] == True and etat != etatTakeEchelle): brl = blueBarrel
            brl.set_colorkey(brl.get_at((0,0)))
            screen.blit(brl,(oneBarrel['x'],oneBarrel['y']))

            #collision  avec mario
            if ( ( mario_x+15 - oneBarrel['x'] ) **2 + ( mario_y+10 - oneBarrel['y'] ) **2 ) < 400: # si mario touche un barrel
                if (Etat == EtatFrappeImmobileAvecArme) or (Etat == EtatFrappeBougeAvecArme): # s'il utilise son marteau, il gagne des points
                    if oneBarrel['blue'] :
                        Tscore = int(pygame.time.get_ticks()/ 1000)
                        Tscore = time1000
                        barrelLIST.remove(oneBarrel)
                        score += 800
                        Score800 = True
                    else:
                        Tscore = int(pygame.time.get_ticks()/ 1000)
                        Tscore = time1000
                        barrelLIST.remove(oneBarrel)
                        score += 500
                        Score500 = True

                else:  # sinon il meurt
                    estMort = True
                    barrelLIST.remove(oneBarrel)

            if (oneBarrel['marioSaut'] == False) and (saut == True) and (estMort == False) and (mario_y+15 < oneBarrel['y']) and  (mario_x >= oneBarrel['x']+10) and (mario_x <= oneBarrel['x']+26) and (mario_y+15 > oneBarrel['y']-35): # si mario saute au dessus d'un barrel sans le toucher
                if oneBarrel['blue']:
                    Tscore = int(pygame.time.get_ticks()/ 1000)
                    Tscore = time1000
                    score += 200
                    Score200 = True
                    oneBarrel['marioSaut'] = True
                else:
                    Tscore = int(pygame.time.get_ticks()/ 1000)
                    Tscore = time1000
                    score += 100
                    Score100 = True
                    oneBarrel['marioSaut'] = True

            #affichage d'un score lors d'une destruction de tonneau ou d'un saut au dessus d'un tonneau
            if Score800:
                screen.blit(points_sprites800,(mario_x+20,mario_y-20))
                if Tscore+1 < time1000 :
                    Score800 = False
            if Score500 :
                screen.blit(points_sprites500,(mario_x+20,mario_y-20))
                if Tscore+1 < time1000 :
                    Score500 = False
            if Score200 :
                screen.blit(points_sprites200,(mario_x+20,mario_y-20))
                if Tscore+1 < time1000 :
                    Score200 = False
            if Score100 :
                screen.blit(points_sprites100,(mario_x+20,mario_y-20))
                if Tscore+1 < time1000 :
                    Score100 = False

        #Animation du baril d'huile
        if(DoHuileAnimation):
            timeHuile = time500-2
            if(oneBarrel['first'] == True):
                HuileSpr = HuileSprites[timeHuile%len(HuileSprites)]
            else:
                HuileSpr = HuileSprites[timeHuile%len(HuileSprites)]

            if(timeHuile%len(HuileSprites) == 4):
                DoHuileAnimation = False

        #Montre baril d'huile
        HuileSpr.set_colorkey(HuileSpr.get_at((0, 0)))
        screen.blit(HuileSpr, (80, 498))



        # Gestions des transitions et du clavier
        Kp = pygame.key.get_pressed()

        if (Kp[pygame.K_SPACE] and tombe == False and Etat != EtatChute) and (Etat == EtatMarche or Etat == 0):
            saut = True       # mario est en phase de saut (montante ou descendante)


        if phaseSaut == 1 and hauteurSaut >=0 and saut == True : #si il est en phase montante
            mario_y -= 6
            hauteurSaut += 6
        elif phaseSaut == 2 and hauteurSaut <= 36 and saut == True : # si il est en phase descendante
            mario_y += 3
            hauteurSaut -= 3
            if hauteurSaut == 0 :   # moment ou on a finit le saut
                saut = False
        if hauteurSaut == 0 :   # lorsque mario a finit son saut on reset la phase
            phaseSaut = 1
        if hauteurSaut == 36 :  # lorsque mario est au point culminant de son saut on passe en phase descendante
            phaseSaut = 2

        if  Kp[pygame.K_LEFT] and mario_speed_g : # deplacement a gauche
            if (hitbox.get_at((int(mario_x+20),int(mario_y+20))) != ROSE) :
                mario_x -= 4
            frappeSansArmeImmobile = ChargeSerieSprites(4,60,33,False) # tous les sprites sont orientés vers la gauche
            frappeAvecArmeImmobile = ChargeSerieSprites(0,60,33,False)
            immobile = ChargeSerieSprites(2,60,33,False)
            saute = ChargeSerieSprites(9,60,33,False)
            if Kp[pygame.K_r] : # si on va a gauche et tape
                frappeSansArmeBouge = ChargeSerieSprites(5,60,33,False)
                frappeAvecArmeBouge = ChargeSerieSprites(1,60,33,False)
                if hasArme: # si mario recupère un marteau
                   Etat = EtatFrappeBougeAvecArme
                else:
                   Etat = EtatFrappeBougeSansArme
            elif (hitbox.get_at((int(mario_x+30),int(mario_y+15))) == BLEU): # si mario bouge en étant sur une echelle
                Etat = EtatMonte
            else: # sinon il marche
                marche = ChargeSerieSprites(6,60,33,False)
                Etat = EtatMarche

        elif Kp[pygame.K_RIGHT] and mario_speed_d : # si mario va a droite
            if (hitbox.get_at((int(mario_x+40),int(mario_y+20))) != ROSE) :
                mario_x += 4
            frappeAvecArmeImmobile = ChargeSerieSprites(0,60,33,True) # tous les sprites sont orientés vers la droite
            immobile = ChargeSerieSprites(2,60,33,True)
            frappeSansArmeImmobile = ChargeSerieSprites(4,60,33,True)
            saute = ChargeSerieSprites(9,60,33,True)
            if Kp[pygame.K_r] : # si on va a droite et tape
                frappeAvecArmeBouge = ChargeSerieSprites(1,60,33,True)
                frappeSansArmeBouge = ChargeSerieSprites(5,60,33,True)
                if hasArme:  # si mario recupère un marteau
                   Etat = EtatFrappeBougeAvecArme
                else:
                   Etat = EtatFrappeBougeSansArme
            elif (hitbox.get_at((int(mario_x+30),int(mario_y+15))) == BLEU):# si mario bouge en étant sur une echelle
                Etat = EtatMonte
            else:  # sinon il marche
                marche = ChargeSerieSprites(6,60,33,True)
                Etat = EtatMarche

        elif Kp[pygame.K_r] : # si mario tape sans bouger
           if hasArme:
               Etat = EtatFrappeImmobileAvecArme
           else:
               Etat = EtatFrappeImmobileSansArme

        elif Kp[pygame.K_UP] and (hitbox.get_at((int(mario_x+30),int(mario_y+10))) != ROSE): # si mario monte une echelle
            if (hitbox.get_at((int(mario_x+30),int(mario_y+13))) == BLEU) : # si mario est entierement dans l'echelle
                Etat = EtatMonte
                mario_y -= 2
            elif (hitbox.get_at((int(mario_x+30),int(mario_y+24))) == BLEU) and (hitbox.get_at((int(mario_x+30),int(mario_y+12))) == VERT): # si mario a le haut de la tete au dessus de l'echelle
                Etat = EtatHautEchelle
                mario_y -= 2
                screen.blit(mario_echelle1,(mario_x,mario_y))
            elif (hitbox.get_at((int(mario_x+30),int(mario_y+23))) == VERT) and (hitbox.get_at((int(mario_x+30),int(mario_y+31))) == BLEU): # si mario est presque hors de l'echelle
                Etat = EtatHautEchelle
                mario_y -= 2
                screen.blit(mario_echelle2,(mario_x,mario_y))
            elif (hitbox.get_at((int(mario_x+30),int(mario_y+35))) == BLEU) and (hitbox.get_at((int(mario_x+30),int(mario_y+30))) == VERT): #si mario est au dessus de l'echelle
                    Etat = EtatHautEchelle
                    screen.blit(mario_echelle3,(mario_x,mario_y))

        elif (Kp[pygame.K_DOWN]) and (Etat != EtatChute) : # pareil mais en descendant d'e echelle
            if (hitbox.get_at((int(mario_x+30),int(mario_y+32))) == BLEU) and (hitbox.get_at((int(mario_x+30),int(mario_y+13))) == BLEU):
                Etat = EtatMonte
                mario_y += 2
            elif (hitbox.get_at((int(mario_x+30),int(mario_y+24))) == BLEU) and (hitbox.get_at((int(mario_x+30),int(mario_y+12))) == VERT):
                Etat = EtatHautEchelle
                mario_y += 2
                screen.blit(mario_echelle1,(mario_x,mario_y))
            elif (hitbox.get_at((int(mario_x+30),int(mario_y+23))) == VERT) and (hitbox.get_at((int(mario_x+30),int(mario_y+32))) == BLEU):
                Etat = EtatHautEchelle
                mario_y += 2
                screen.blit(mario_echelle2,(mario_x,mario_y))
            elif (hitbox.get_at((int(mario_x+30),int(mario_y+35))) == BLEU) and (hitbox.get_at((int(mario_x+30),int(mario_y+30))) == VERT):
                Etat = EtatHautEchelle
                screen.blit(mario_echelle3,(mario_x,mario_y))


        else: # si on n'appuye pas sur le clavier, marrio est immobile
            if (hitbox.get_at((int(mario_x+30),int(mario_y+12))) == BLEU) and (hitbox.get_at((int(mario_x+30),int(mario_y+32))) == BLEU) and (saut == False): # quand mario est dans une echelle
                Etat = EtatImmobileEchelle
            elif (hitbox.get_at((int(mario_x+30),int(mario_y+23))) == BLEU) and (hitbox.get_at((int(mario_x+30),int(mario_y+12))) == VERT) and (saut == False):# quand il a la tete au dessus d'une echelle
                Etat = EtatHautEchelle
                screen.blit(mario_echelle1,(mario_x,mario_y))
            elif (hitbox.get_at((int(mario_x+30),int(mario_y+23))) == VERT) and (hitbox.get_at((int(mario_x+30),int(mario_y+30))) == BLEU) and (saut == False): # si mario est presque hors de l'echelle
                Etat = EtatHautEchelle
                screen.blit(mario_echelle2,(mario_x,mario_y))
            else:
                if (hitbox.get_at((int(mario_x+30),int(mario_y+35))) == BLEU) and (hitbox.get_at((int(mario_x+30),int(mario_y+30))) == VERT) and (saut == False):#si mario est au dessus de l'echelle
                    Etat = EtatHautEchelle
                    screen.blit(mario_echelle3,(mario_x,mario_y))
                else: # si mario est au sol
                    Etat = 0

        if (hitbox.get_at((int(mario_x+ 25), int(mario_y+33))) == VERT) and (hitbox.get_at((int(mario_x+ 35), int(mario_y+33))) == VERT) and (saut == False): # s'il y a le vide sous mario, il tombe
                Etat = EtatChute

        # action des etats
        if Etat != EtatChute: # monte et descendre des escalier
            if (hitbox.get_at((int(mario_x+25),int(mario_y+31))) == VERT) and (hitbox.get_at((int(mario_x+35),int(mario_y+31))) == VERT) and (hitbox.get_at((int(mario_x+18),int(mario_y+32))) == ROUGE):
                mario_y += 1
            elif (hitbox.get_at((int(mario_x+20), int(mario_y+30))) == ROUGE) or (hitbox.get_at((int(mario_x+40), int(mario_y+30))) == ROUGE) and Etat != EtatHautEchelle:
                mario_y -= 1

        if Etat == EtatChute: # si mario tombe
            mario_y += 3

        if estMort: # si mario meurt
            Etat = EtatMort

        if saut: # si mario saute
            Etat = EtatSaut

        if mario_x <= 3 : # si mario atteint le bord gauche de l'ecran
            mario_speed_g = False
        elif mario_x >= 545: # si mario atteint le bord droit de l'ecran
            mario_speed_d = False
        else:
            mario_speed_g = True
            mario_speed_d = True

        if ( ( mario_x+15 - marteau_x ) **2 + ( mario_y - marteau_y ) **2 ) < 40:  # si mario touche un marteau, il peut l'utiliser
           hasArme = True
           marteau_x = -100
        if ( ( mario_x+15 - marteau2_x ) **2 + ( mario_y - marteau2_y ) **2 ) < 40:
           hasArme = True
           marteau2_x = -100

        if hasArme: # si mario a un marteau, il peut l'utiliser pour 10 secondes
            if timeMarteau >= 200:
                hasArme = False
                timeMarteau = 0
            timeMarteau += 1


        # Gestion de l'affichage

        if Etat == 0: # si mario immobile
            screen.blit(immobile[0],(mario_x,mario_y))
        elif Etat == EtatFrappeBougeSansArme: # si mario frappe sans arme en bougeant
            screen.blit(frappeSansArmeBouge[time500%len(frappeSansArmeBouge)],(mario_x,mario_y))
        elif Etat == EtatFrappeImmobileSansArme: # si mario frappe sans arme en etant immobile
            screen.blit(frappeSansArmeImmobile[time500%len(frappeSansArmeImmobile)],(mario_x,mario_y))
        elif Etat == EtatFrappeBougeAvecArme: # si mario frappe avec une arme en bougeant
            screen.blit(frappeAvecArmeBouge[time500%len(frappeAvecArmeBouge)],(mario_x,mario_y))
        elif Etat == EtatFrappeImmobileAvecArme: # si mario frappe avec une arme en etant immobile
            screen.blit(frappeAvecArmeImmobile[time500%len(frappeAvecArmeImmobile)],(mario_x,mario_y))
        elif Etat == EtatMarche: # si mario marche
            screen.blit(marche[time80%len(marche)],(mario_x,mario_y))
        elif Etat == EtatChute: # si mario tombe
            screen.blit(chute[0],(mario_x,mario_y))
        elif Etat == EtatMonte: # si mario monte ou descend d'une echelle
            screen.blit(monte[time500%len(monte)],(mario_x,mario_y))
        elif Etat == EtatImmobileEchelle: # si mario est immobile sur une echelle
            screen.blit(immobileEchelle[time500%len(immobileEchelle)],(mario_x,mario_y))
        elif Etat == EtatSaut : # si mario saute
            screen.blit(saute[0],(mario_x,mario_y))
        elif Etat == EtatMort: # si mario meurt
            mario_speed_d = False
            mario_speed_g = False
            compteurMort += 1
            if (compteurMort >= 1) and (compteurMort < 10):
                screen.blit(mort1,(mario_x,mario_y))
            elif (compteurMort >= 10) and (compteurMort < 20):
                screen.blit(mort2,(mario_x,mario_y))
            elif (compteurMort >= 20) and (compteurMort < 30):
                screen.blit(mort3,(mario_x,mario_y))
            elif (compteurMort >= 30) and (compteurMort < 40):
                screen.blit(mort4,(mario_x,mario_y))
            elif (compteurMort >= 40) and (compteurMort < 60):
                screen.blit(mort5,(mario_x,mario_y))
            elif compteurMort >= 60:
                for oneBarrel in barrelLIST: # supprime tous les barrels et enleve une vie a mario
                    barrelLIST.clear()
                    if (vie > 1):
                        vie -= 1
                        bonus = 5000
                        mario_x = 100
                        mario_y = 550
                        marteau_x =  500
                        marteau2_x = 90
                        compteurMort = 0
                        estMort = False
                        mario_speed_d = True
                        mario_speed_g = True
                    elif vie == 1:
                        vie -= 1



        if vie == 0: # affichage en cas de defaite
            if END == False:
                score += bonus
            zone = police.render(str("GAME OVER"), True, ROUGE)
            screen.fill(NOIR)
            END = True
            screen.blit(zone,(240,290))
        if vie >= 1:
            screen.blit(mario_vie,(10,10))
        if vie >= 2:
            screen.blit(mario_vie,(30,10))
        if vie >= 3:
            screen.blit(mario_vie,(50,10))

        if (mario_x+30 > peach_x) and (mario_x+30 < peach_x+27) and (mario_y+15 > peach_y) and (mario_y+15 < peach_y+20):
            zone = police.render(str("VICTOIRE"), True, JAUNE) # affichage en cas de victoire si mario touche peach
            screen.fill(NOIR)
            if END == False:
                score += bonus
            mario_speed_d = False
            mario_speed_g = False
            peach_vx = 0
            END = True
            screen.blit(zone,(250,290))


        zone = police.render( str(score), True, BLANC) # affichage du score
        zone2 = police.render( str("HIGH SCORE"), True, ROUGE)
        screen.blit(zone,(280,23))
        screen.blit(zone2,(235,1))


        if END == False: # affichage des marteaux et du bonus
            screen.blit(marteau,(marteau_x,marteau_y))
            screen.blit(marteau2,(marteau2_x,marteau2_y))
            screen.blit(bonus_sprite,(bonus_x,bonus_y))
            zone3 = police.render( str(bonus), True, CYAN)
            screen.blit(zone3,(bonus_x+41,bonus_y+27))
            if (timeBonus >= 80):
                bonus -= 100
                timeBonus = 0
            timeBonus += 1

    clock.tick(20)

      # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
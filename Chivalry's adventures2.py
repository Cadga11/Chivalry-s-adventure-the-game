import pygame
import time

# ******************************************************************************************* #
# ******************************************************************************************* #
# ********************************** INITIALISATION ***************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #


# ***************** #
# ***INIT PYGAME*** #
# ***************** #

pygame.init()

# ******************* #
# ***ELEMENT UTILE*** #
# ******************* #

son =pygame.mixer.music.load("finalmusic.mp3")
pygame.mixer.music.play()
volume = pygame.mixer.music.get_volume() #Retourne la valeur du volume, entre 0 et 1
pygame.mixer.music.set_volume(0.5) #Met le volume à 0.5 (moitié)

# Listes pour sauvegarder les coordonnées et les images des obstacles ( MUR ET SOL)

obstacle = []                                           # Pour les coordonnées (les rectangles) des obstacles
lesimages = []                                          # Pour les images (les surfaces) des obstacles

# Listes pour sauvegarder les coordonnées et les images des pics

pics = []                                               # Pour les coordonnées (les rectangles) des pics
imagepics = []                                          # Pour les images (les surfaces) des pics

# Listes pour sauvegarder les coordonnées et les images des étoiles

etoileimage = []                                        # Pour les images (les surfaces) des étoiles
etoilerect = []                                         # Pour les coordonnées (les rectangles) des étoiles

# Listes utile pour sauvegarder des données sur les monstres (position, coordonnées, images, collisions)

rectmobs = []                                           # Pour les coordonnées (les rectangles) des monstres (= des mobs)
position_mobs = []                                      # Pour la position du monstre, savoir si il va vers la gauche ou la droite
rectmobs_initial = []                                   # Pour sauvegarder les coordonnées initiales des monstres pour comparaison lors des déplacements
blit_mobs = []                                          # Pour savoir si un mobs à été eliminé soit touché par le projectile du personnage, soit savoir si on les fait apparaître ou non

# Initialisation des coordonnées du fond et du personnage

positionperso = positionfond = (0,0)                    # positionperso = pour le peronnage, positionfond = pour le fond

# Liste pour l'eau
drapeau_rect = (0,0)




#Couleur à rendre transparent sur les images

BLANC = (255,255,255)
NOIR = (0,0,0)

# Definition de la fonction pour remplacer un element dans une liste

def remplace_list(liste,index,valeur_a_inserer) :
    del liste[index]
    liste.insert(index,valeur_a_inserer)
    return liste

# **************************** #
# ****TAILLE DE LA FENETRE**** #
# **************************** #

surfaceH = 800                                          # HAUTEUR
surfaceL = 1000                                         # LARGEUR

# **************************** #
# ****DIMENSION PERSONNAGE**** #
# **************************** #

taillepersoH = 60                                       # HAUTEUR
taillepersoL = 55                                       # LARGEUR

# **************************** #
# ******CRAETION FENETRE****** #
# **************************** #

fenetre = pygame.display.set_mode((surfaceL,surfaceH))                          # Création de la fenetre
pygame.display.set_caption("Chivalry adventure")                                          # Nom donné à la fenetre

# **************************** #
# *******HORLOGE PYGAME******* #
# **************************** #

horloge = pygame.time.Clock()

# ******************************************************************************************* #
# ******************************************************************************************* #
# ********************************* LES MENUS DU JEU **************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #

# **************************** #
# *******MENU DE DEPART******* #
# **************************** #

# IMAGE POUR LE MENU #

# < variable = pygame.image.load("destination de l'image") > : upload de l'image que l'on definit en temps que surface que l'on insere ensuite dans une variable
# < nom_de_l'image = pygame.transform.scale(nom_de_l'image,nouvelle_taille) > : redefinition de l'image, donc nouvelle surface que l'on insere dans une variable
# < variable = nom_d'une_image.get_rect() > : on definit une surface en temps que rectangle que l'on insere dans une variable. Cela permet de définir des coordonnées
# < nom_du_rectangle = nom_du_rectangle.move(x,y) > : on deplace le rectangle de x en abscisse et de y en ordonné par rapport a sa position precedente
# < nom_de_la_fenetre.blit(nom_de_l'image_soit_la_surface, nom_du_rectangle_soit_les_coordonnées) > : on applique les changement de coordonnées et/ou de surface

# Fond du menu
imagemenu = pygame.image.load("image//pour menu.png")
imagemenu = pygame.transform.scale(imagemenu,(surfaceL,surfaceH))
menu = imagemenu.get_rect()
menu = menu.move(0,0)
fenetre.blit(imagemenu,menu)

# Les épées
epee1 = pygame.image.load("image//epee.png")
rectepee1 = epee1.get_rect()
rectepee1 = rectepee1.move(-(rectepee1.right),100)

epee2 = pygame.image.load("image//epee2.png")
rectepee2 = epee2.get_rect()
rectepee2 = rectepee2.move(surfaceL,100)

# Les nuages
nuage = pygame.image.load("image//nuage menu.png")
nuage = pygame.transform.scale(nuage,(120,120))
rectnuagehaut = nuage.get_rect()
rectnuagehaut = rectnuagehaut.move(-(rectnuagehaut.right),70)

nuage2 = pygame.image.load("image//nuage menu.png")
nuage2 = pygame.transform.scale(nuage,(120,120))
rectnuagebas = nuage2.get_rect()
rectnuagebas = rectnuagebas.move(1000,650)

# DEFINITION DE LA FONCTION QUI PERMET DE CREER LA SURFACE DU TEXTE ET LE RECTANGLE #
def creaTexte(texte,police,couleur) :
    if couleur == 1 :                                                           # Si couleur = 1, alors la couleur est blanche, sinon il est noir
        surftexte = police.render(texte,True,BLANC)                             # < variable = police.render(texte,True,couleur_du_texte) > : creation de la surface du texte
    else :
        surftexte = police.render(texte,True,NOIR)
    return surftexte, surftexte.get_rect()

# DEFINITION DE LA FONCTION QUI CREER L'OMBRE DU TEXTE ET LE PLACE SUR LA FENETRE #
# < variable = pygame.font.Font("destination_de_la_police",taille_de_l'ecriture) > : On upload la police d'ecriture avec sa taille et on sauvegarde ces données dans une variable

def texte1() :
    PoliceTN = pygame.font.Font("police//impact.ttf",30)
    PoliceTK = pygame.font.Font("police//Minecrafter.ttf", 40)
    surfTN1, RectTN1 = creaTexte("Press",PoliceTN,0)
    RectTN1 = RectTN1.move(170,600)
    fenetre.blit(surfTN1,RectTN1)
    surfTN2, RectTN2 = creaTexte("to start or",PoliceTN,0)
    RectTN2 = RectTN2.move(440,600)
    fenetre.blit(surfTN2,RectTN2)
    surfTN3, RectTN3 = creaTexte("quit",PoliceTN,0)
    RectTN3 = RectTN3.move(780,600)
    fenetre.blit(surfTN3,RectTN3)
    surfTK1, RectTK1 = creaTexte("SPACE",PoliceTK,0)
    RectTK1 = RectTK1.move(260,598)
    fenetre.blit(surfTK1,RectTK1)
    surfTK2, RectTK2 = creaTexte("ESCAPE",PoliceTK,0)
    RectTK2 = RectTK2.move(590,598)
    fenetre.blit(surfTK2,RectTK2)

# DEFINITION DE LA FONCTION QUI CREER LE TEXTE ET LE PLACE SUR LA FENETRE #
def texte2() :
    PoliceTN = pygame.font.Font("police//impact.ttf",30)
    PoliceTK = pygame.font.Font("police//Minecrafter.ttf", 40)
    surfTN1, RectTN1 = creaTexte("Press",PoliceTN,1)
    RectTN1 = RectTN1.move(160,610)
    fenetre.blit(surfTN1,RectTN1)
    surfTN2, RectTN2 = creaTexte("to start or",PoliceTN,1)
    RectTN2 = RectTN2.move(440,610)
    fenetre.blit(surfTN2,RectTN2)
    surfTN3, RectTN3 = creaTexte("quit",PoliceTN,1)
    RectTN3 = RectTN3.move(790,610)
    fenetre.blit(surfTN3,RectTN3)
    surfTK1, RectTK1 = creaTexte("SPACE",PoliceTK,1)
    RectTK1 = RectTK1.move(250,608)
    fenetre.blit(surfTK1,RectTK1)
    surfTK2, RectTK2 = creaTexte("ESCAPE",PoliceTK,1)
    RectTK2 = RectTK2.move(600,608)
    fenetre.blit(surfTK2,RectTK2)

# DEFINITION DE LA FONCTION QUI PERMET D'APPLIQUER TOUS LES CHANGEMENTS EFFECTUE AUX IMAGES DU MENU DE DEPART#
def men(imagemenu,menu,epee1,epee2,rectepee1,rectepee2,nuage,rectnuagehaut,rectnuagebas,nuage2) :
    fenetre.blit(imagemenu,menu)
    fenetre.blit(nuage,rectnuagehaut)
    fenetre.blit(nuage,rectnuagebas)
    fenetre.blit(epee1,rectepee1)
    fenetre.blit(epee2,rectepee2)


# DEFINITION DE LA FONCTION QUI PERMET DE GERER LES DEPLACEMENT DES IMAGES, LES EVENEMENTS DU CLAVIER ET LA MISE EN PAGE DU MENU DE DEPART #

# < for event in pygame.event.get() : > : on compte le nombre d'evenements clavier ou souris
# < event.type > : c'est le type d'evenement. Il y a par exemple l'evenement "appuie sur une touche du clavier". Le non de l'evenement est < pygame.nom_evenement >
# < event.key > : c'est la touche qui a creer un evenement qui a pour nom < pygame.nom_de_la_touche>
# < pygame.display.flip() > : on rafraichit la fenetre

def mise_en_page_menu(imagemenu,menu,epee1,epee2,rectepee1,rectepee2,nuage,rectnuagehaut,rectnuagebas,nuage2) :
    debut = True                                                                                                    # Variable pour savoir si on est encore dans le menu de depart
    ecriture = False                                                                                                # Variable pour savoir si l'on doit afficher le texte ou non
    xm = 4                                                                                                          # Mouvement sur l'axe des abcsise pour les épées
    xnuageH = 0                                                                                                     # Mouvement sur abcsisse pour le nuage du haut
    xnuageB = 0                                                                                                     # Mouvement sur abcsisse pour le nuage du bas
    while debut :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :                                                                          # Evenement : "appuie sur croix de la fenetre"
                pygame.quit()                                                                                       # On quitte pygame
                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE : #(ESPACE)
                    debut = False                                                                                   # Debut devient faux : on sort du menu de depart
                if event.key == pygame.K_ESCAPE :#(ECHAP)
                    pygame.quit()
                    quit()
        rectepee1 = rectepee1.move(xm,0)
        rectepee2 = rectepee2.move(-xm,0)
        rectnuagehaut = rectnuagehaut.move(xnuageH,0)
        rectnuagebas = rectnuagebas.move(xnuageB,0)
        if rectnuagehaut.left > 1000 :                                                                              # Si le nuage du haut sort de la fenetre (à droite) on le replace au debut
            rectnuagehaut = rectnuagehaut.move(-(rectnuagehaut.right),0)
        if rectnuagebas.right < 0 :                                                                                 # Si le nuage du bas sort de la fenetre (à gauche) on le replace au deb
            rectnuagebas = rectnuagebas.move((1000-rectnuagebas.left),0)
        if rectepee2.left < 500 - (rectepee2.bottom/2) and rectepee1.right > 500 + (rectepee1.bottom/2) :           # Si les épée se croise, on affiche le texte et on deplace les nuages
            xm = 0
            xnuageH = 2
            xnuageB = -3
            ecriture = True
        men(imagemenu,menu,epee1,epee2,rectepee1,rectepee2,nuage,rectnuagehaut,rectnuagebas,nuage2)                 # On affiche les images
        if ecriture :                                                                                               # On affiche les textes
            texte1()
            texte2()
        pygame.display.flip()

mise_en_page_menu(imagemenu,menu,epee1,epee2,rectepee1,rectepee2,nuage,rectnuagehaut,rectnuagebas,nuage2)           # On applique la fonction

# **************************** #
# *********MENU PAUSE********* #
# **************************** #

# DEFINITION DE LA FONCTION QUI PERMET D'AFFICHER LES IMAGES #
def blit_pause(case1,case2,case3,rect1,rect2,rect3) :
    fenetre.blit(case1,rect1)
    fenetre.blit(case2,rect2)
    fenetre.blit(case3,rect3)

# DEFINITION DE LA FONCTION QUI PERMET DE GERER LA FENETRE DE PAUSE #
def menu_pause(obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau) :
    pause = True                                                                                                # Variable pour savoir si on est encore en pause
    souris = False                                                                                              # Variable pour savoir si on utilise la souris
    case = 1                                                                                                    # Cette variable revoie le numero de l'image sur laquelle on est positionné
    boutonclic = 0                                                                                              # Variable qui permet de savoir sur quel bouton de la souris on a appuyé
    coordsouris = (0,0)                                                                                         # Initialisation des coordonnées du curseur de la souris
    entrer = 0                                                                                                  # Variable qui permet de savoir si on a appuyé sur le bouton entrer
    while pause :
        horloge.tick()                                                                                          # 0 image par second du jeu (on met le jeu en pause)
        continuerFalse = pygame.image.load("image//continuer.png")
        continuerTrue = pygame.image.load("image//continuerclic.png")
        rectcontinuer  = continuerFalse.get_rect()
        rectcontinuer = rectcontinuer.move(300,200)

        recommencerFalse = pygame.image.load("image//recommencer.png")
        recommencerTrue = pygame.image.load("image//recommencerclic.png")
        rectrecommencer  = recommencerFalse.get_rect()
        rectrecommencer = rectrecommencer.move(300,400)

        quitterFalse = pygame.image.load("image//quitter.png")
        quitterTrue = pygame.image.load("image//quitterclic.png")
        rectquitter  = quitterFalse.get_rect()
        rectquitter = rectquitter.move(300,600)

        for event in pygame.event.get() :                                                                       # On repertorie les evenements
            if event.type == pygame.KEYDOWN :
                if souris :
                    souris = False
                    case = 1
                if event.key == pygame.K_ESCAPE :
                    pause = False
                if event.key == pygame.K_DOWN :
                    case += 1
                if event.key == pygame.K_UP :
                    case -= 1
                if event.key == pygame.K_RETURN :
                    entrer = 1
            elif event.type == pygame.KEYUP and not souris:
                entrer = 0
            elif event.type == pygame.MOUSEMOTION :
                souris = True
                coordsouris = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN :
                souris = True
                boutonclic = event.button                                                                       # < event.button > renvoie un numéro representant la touche de la souris qui a creer l'evenement
            elif event.type == pygame.MOUSEBUTTONUP and souris:
                boutonclic = 0
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()


        if not souris :
            if case == 4 :                                                                                      # Puisu'il y a 3 images (3 cases) si on descend en bas de la 3eme case on monte a la premiere
                case = 1
            elif case == 0:                                                                                     # Puisu'il y a 3 images (3 cases) si on monte en haut de la 1eme case on descend a la derniere
                case = 3
            if case == 1 :
                blit_pause(continuerTrue,recommencerFalse,quitterFalse,rectcontinuer,rectrecommencer,rectquitter)   # La case (l'image) sur laquelle on est positionné, a des bordures bleu
                if entrer == 1 :
                    pause = False                                                                               # Si on appuie sur entrer alors qu'on est sur la premiere case, on est plus en pause
            elif case == 2 :
                blit_pause(continuerFalse,recommencerTrue,quitterFalse,rectcontinuer,rectrecommencer,rectquitter)
                if entrer == 1 :
                    # Si on appuie sur recommencer on initialise les coordonnées de tous les rectangles du jeu
                    obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,persogauche,etoileimage,etoilerect,projectile,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau = debut(obstacle,pics,lesimages,imagepics,etoileimage,etoilerect,rectmobs,position_mobs,rectmobs_initial,blit_mobs)
                    principale(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau,False)
            elif case == 3 :
                blit_pause(continuerFalse,recommencerFalse,quitterTrue,rectcontinuer,rectrecommencer,rectquitter)
                if entrer == 1 :
                    # Si on appuie sur quitter, on quitte le jeu
                    pygame.quit()
                    quit()
            else :
                blit_pause(continuerFalse,recommencerFalse,quitterFalse,rectcontinuer,rectrecommencer,rectquitter)


        if souris :
            if rectcontinuer.left < coordsouris[0] < rectcontinuer.right and rectcontinuer.top < coordsouris[1] < rectcontinuer.bottom :
                blit_pause(continuerTrue,recommencerFalse,quitterFalse,rectcontinuer,rectrecommencer,rectquitter)
                if boutonclic == 1 :
                    pause = False
            elif rectrecommencer.left < coordsouris[0] < rectrecommencer.right and rectrecommencer.top < coordsouris[1] < rectrecommencer.bottom :
                blit_pause(continuerFalse,recommencerTrue,quitterFalse,rectcontinuer,rectrecommencer,rectquitter)
                if boutonclic == 1 :
                    obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,persogauche,etoileimage,etoilerect,projectile,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau = debut(obstacle,pics,lesimages,imagepics,etoileimage,etoilerect,rectmobs,position_mobs,rectmobs_initial,blit_mobs)
                    principale(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau,False)
            elif rectquitter.left < coordsouris[0] < rectquitter.right and rectquitter.top < coordsouris[1] < rectquitter.bottom :
                blit_pause(continuerFalse,recommencerFalse,quitterTrue,rectcontinuer,rectrecommencer,rectquitter)
                if boutonclic == 1:
                    pygame.quit()
                    quit()
            else :
                blit_pause(continuerFalse,recommencerFalse,quitterFalse,rectcontinuer,rectrecommencer,rectquitter)

        pygame.display.flip()


# **************************** #
# *******MENU GAME OVER******* #
# **************************** #

# DEFINITION DE LA FONCTION QUI CREER LE TEXTE QUI S'AFFICHE #
def message(texte) :
    PoliceGO = pygame.font.Font("police//Minecrafter.ttf", 130)
    PolicePT = pygame.font.Font("police//vgafix.fon", 300)
    surfGO, RectGO = creaTexte(texte, PoliceGO,0)
    RectGO = RectGO.move(110,250)
    fenetre.blit(surfGO,RectGO)
    surfPT, RectPT = creaTexte("Press space to continue or ECHAP to quit", PolicePT,0)
    RectPT = RectPT.move(300,400)
    fenetre.blit(surfPT,RectPT)
    pygame.display.flip()

# DEFINITION DE LA FONCTION QUI PERMET DE GERER LE MENU GAME OVER #
def Game_Over1(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau) :
    gameover = True                                                                         # Variable qui permet de savoir si le menu Game over s'affiche toujours
    while gameover == True :
        horloge.tick()
        for event in pygame.event.get() :
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_SPACE :
                    gameover = False                                                        # Si on appuie sur espace, on recommence le jeu
                if event.key == pygame.K_ESCAPE :
                    pygame.quit()
                    quit()
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
        message("Game Over")                                                                # On affiche le texte
    # On reinitialise toutes les coordonnées du jeu et on recommence le jeu
    obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,persogauche,etoileimage,etoilerect,projectile,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau = debut(obstacle,pics,lesimages,imagepics,etoileimage,etoilerect,rectmobs,position_mobs,rectmobs_initial,blit_mobs)
    principale(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau,False)


# ******************************************************************************************* #
# ******************************************************************************************* #
# ********************************* LES DECORS DU JEU *************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #

# DEFINITION DE LA FONCTION POUR FACILITER LA CREATION DES OBSTACLE ( DE LEUR SURFACE ET DE LEUR RECTANGLE ) #
def creaMur(image,listeimage,listerect,coord,changement_couleur,couleur,changement_taille,taille) :
    img = pygame.image.load(image)
    if changement_couleur :
        img.set_colorkey(couleur)
    if changement_taille :
        img = pygame.transform.scale(img,taille)
    rectangle = img.get_rect()
    rectangle = rectangle.move(coord)
    listeimage.append(img)
    listerect.append(rectangle)
    fenetre.blit(img,rectangle)
    return listeimage,listerect

# DEFINITION DE LA FONCTION POUR CREER UNE SERIE D'OBSTACLE REPETITIVE #
def creaMurSerie(image,listeimage,listerect,coordx,coordy,changement_couleur,couleur,changement_taille,taille,nombre,axe,coord_sup) :
    for i in range(0,nombre) :
        if i == 0 :
            pass
        elif i != 0 :
            if axe == "y" :
                coordy = coordy + coord_sup
            elif axe == "x" :
                coordx = coordx + coord_sup
        coord = (coordx,coordy)
        listeimage,listerect = creaMur(image,listeimage,listerect,coord,changement_couleur,couleur,changement_taille,taille)
    return listeimage,listerect

# DEFINITION DE LA FONCTION POUR UPLOAD LES IMAGE DES MONSTRES SOIT LEUR SURFACE #
def image_mobs(image,couleur,taille) :
    img = pygame.image.load(image)
    img = pygame.transform.scale(img,taille)
    img.set_colorkey(couleur)
    return img

# DEFINITION DE LA FONCTION POUR FACILITER LA CREATION DES MONSTRES #
def creaMobs(image,fonctionrect,fonctionrect_initial,coord,couleur,taille,gauche_ou_droite,position_mobs,blit_mobs) :
    img = image_mobs(image,couleur,(30,50))
    rect = img.get_rect()
    rect = rect.move(coord)
    fonctionrect.append(rect)
    fonctionrect_initial.append(rect)
    fenetre.blit(img,rect)
    if gauche_ou_droite == "gauche" :
        position_mobs.append("gauche")
    elif gauche_ou_droite == "droite" :
        position_mobs.append("droite")
    blit_mobs.append(True)
    return fonctionrect, position_mobs, fonctionrect_initial, blit_mobs

# DEFINITION DE LA FONCTION POUR INITIALISER LES COORDONNEES DE TOUS LES RECTANGLES DU JEU #
def debut(obstacle,pics,lesimages,imagepics,etoileimage,etoilerect,rectmobs,position_mobs,rectmobs_initial,blit_mobs) :
    obstacle = []
    lesimages = []
    pics = []
    imagepics = []
    etoileimage = []
    etoilerect = []
    rectmobs = []
    rectmobs_initial = []
    blit_mobs = []
    position_mobs = []

    # Mise en page de l'image de fond
    imagefond = pygame.image.load("image//fond.png").convert()
    positionfond = imagefond.get_rect()
    positionfond = positionfond.move(0,0)

    # Mise en page du personnage
    perso = pygame.image.load("image//chevalier.png")
    perso = pygame.transform.scale(perso, (taillepersoL,taillepersoH))
    persogauche = pygame.image.load("image//chevalier gauche.gif")
    persogauche = pygame.transform.scale(persogauche, (taillepersoL,taillepersoH))
    perso.set_colorkey((255,255,255))
    persogauche.set_colorkey((255,255,255))
    positionperso = perso.get_rect()
    positionperso = positionperso.move(400,500)

    # Mise en page du projetctile
    projectile = pygame.image.load("image//bouledefeu.jpg")
    projectile = pygame.transform.scale(projectile,(25,25))
    projectile.set_colorkey(BLANC)
    rectprojectile = projectile.get_rect()
    rectprojectile = rectprojectile.move(positionperso.left,positionperso.top - 20)

    # Mise en page du drapeau de fin
    image_drapeau = pygame.image.load("image//drapeau.gif")
    image_drapeau.set_colorkey(BLANC)
    drapeau_rect = image_drapeau.get_rect()
    drapeau_rect = drapeau_rect.move(5700,730)

    # Mise en page des mobs
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mob.gif",rectmobs,rectmobs_initial,(1200,730),BLANC,(30,50),"gauche",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mob.gif",rectmobs,rectmobs_initial,(2880,650),BLANC,(30,50),"gauche",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(2500,650),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(5600,700),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(6100,350),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mob.gif",rectmobs,rectmobs_initial,(6300,350),BLANC,(30,50),"gauche",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(6800,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(4800,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(4600,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(5000,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(5200,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(5400,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(6000,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(6200,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(7200,450),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(7500,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(7900,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(4050,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mobs droite.gif",rectmobs,rectmobs_initial,(4200,730),BLANC,(30,50),"droite",position_mobs,blit_mobs)
    rectmobs,position_mobs,rectmobs_initial,blit_mobs = creaMobs("image//mob.gif",rectmobs,rectmobs_initial,(3150,650),BLANC,(30,50),"gauche",position_mobs,blit_mobs)


    #Mise en page des obstacle rectangle (mur, sol)

    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(5100,320),True,BLANC,True,(30,30))

    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(3200,100),True,BLANC,True,(30,30))

    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(4050,730),True,BLANC,True,(30,30))
    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(4200,730),True,BLANC,True,(30,30))

    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(6350,350),True,BLANC,True,(30,30))
    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(7300,350),True,BLANC,True,(30,30))

    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(2800,100),True,BLANC,True,(30,30))
    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(6100,100),True,BLANC,True,(30,30))
    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(2105,50),True,BLANC,True,(30,30))
    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(3000,100),True,BLANC,True,(30,30))

    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(2750,500),True,BLANC,True,(30,30))
    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(3150,500),True,BLANC,True,(30,30))
    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(3400,500),True,BLANC,True,(30,30))

    # Mise en page des obstacle rectangle (mur, sol)
    lesimages,obstacle = creaMur("image//sol 1.jpg",lesimages,obstacle,(0,780),False,None,False,(3000,20))
    lesimages,obstacle = creaMur("image//mur 1.jpg",lesimages,obstacle,(0,0),False,None,False,None)
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(500,760),True,BLANC,False,None)



    lesimages,obstacle = creaMur("image//sol 1.jpg",lesimages,obstacle,(2000,780),False,None,True,(8000,20))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(2300,600),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(2450,450),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//mur700.jpg",lesimages,obstacle,(2650,350),False,None,True,(700,50))
    lesimages,obstacle = creaMur("image//mur100.jpg",lesimages,obstacle,(3350,350),False,None,True,(100,50))
    lesimages,obstacle = creaMur("image//mur250.jpg",lesimages,obstacle,(3550,700),False,None,True,(250,50))
    lesimages,obstacle = creaMur("image//mur150.jpg",lesimages,obstacle,(3220,750),False,None,True,(150,50))
    lesimages,obstacle = creaMur("image//mur250.jpg",lesimages,obstacle,(2450,700),False,None,True,(250,50))
    lesimages,obstacle = creaMur("image//mur250.jpg",lesimages,obstacle,(2450,750),False,None,True,(250,50))
    lesimages,obstacle = creaMur("image//mur200.jpg",lesimages,obstacle,(2880,750),False,None,True,(200,50))
    lesimages,obstacle = creaMur("image//mur200.jpg",lesimages,obstacle,(2880,700),False,None,True,(200,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(3550,470),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(2300,280),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//mur150.jpg",lesimages,obstacle,(3220,700),False,None,True,(150,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(4150,500),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//mur250.jpg",lesimages,obstacle,(3550,750),False,None,True,(250,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(4000,700),False,None,True,(50,80))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(4050,600),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(4450,700),False,None,True,(50,80))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(4350,450),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//sol 1.jpg",lesimages,obstacle,(4100,780),False,None,True,(250,20))
    lesimages,obstacle = creaMur("image//sol 1.jpg",lesimages,obstacle,(4400,780),False,None,True,(4200,20))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(4500,500),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(4650,400),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//mur700.jpg",lesimages,obstacle,(4800,350),False,None,True,(700,50))
    lesimages,obstacle = creaMur("image//mur250.jpg",lesimages,obstacle,(5500,400),False,None,True,(250,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(5550,300),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//mur200.jpg",lesimages,obstacle,(5550,300),False,None,True,(200,50))
    lesimages,obstacle = creaMur("image//mur150.jpg",lesimages,obstacle,(5600,250),False,None,True,(150,50))
    lesimages,obstacle = creaMur("image//mur100.jpg",lesimages,obstacle,(5650,200),False,None,True,(100,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(5700,150),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//mur200.jpg",lesimages,obstacle,(5550,350),False,None,True,(200,50))
    lesimages,obstacle = creaMur("image//mur100.jpg",lesimages,obstacle,(5700,100),False,None,True,(100,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(6000,100),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//mur500.jpg",lesimages,obstacle,(7500,500),False,None,True,(500,50))
    lesimages,obstacle = creaMur("image//mur700.jpg",lesimages,obstacle,(5750,400),False,None,True,(700,50))
    lesimages,obstacle = creaMur("image//mur250.jpg",lesimages,obstacle,(4750,580),False,None,True,(250,50))
    lesimages,obstacle = creaMur("image//mur250.jpg",lesimages,obstacle,(5000,580),False,None,True,(250,50))
    lesimages,obstacle = creaMur("image//mur100V.jpg",lesimages,obstacle,(5750,450),False,None,True,(50,100))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(5750,550),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//mur700.jpg",lesimages,obstacle,(5750,580),False,None,True,(700,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(6650,400),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//mur250.jpg",lesimages,obstacle,(7000,500),False,None,True,(250,50))
    lesimages,obstacle = creaMur("image//mur250.jpg",lesimages,obstacle,(7250,500),False,None,True,(250,50))
    lesimages,obstacle = creaMur("image//sol 1.jpg",lesimages,obstacle,(6900,750),False,None,True,(2250,50))
    lesimages,obstacle = creaMur("image//mur 1.jpg",lesimages,obstacle,(7950,0),False,None,True,(50,800))
    lesimages,obstacle = creaMur("image//mur100.jpg",lesimages,obstacle,(6450,580),False,None,True,(100,50))
    lesimages,obstacle = creaMur("image//mur100.jpg",lesimages,obstacle,(6850,300),False,None,True,(100,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(6450,400),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(2100,750),False,None,True,(50,50))
    lesimages,obstacle = creaMur("image//muret.jpg",lesimages,obstacle,(4300,600),False,None,True,(50,50))
    imagepics,pics = creaMur("image//pics 2.gif",imagepics,pics,(2300,650),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(2700,300),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(2850,300),True,BLANC,True,(30,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(3000,300),True,BLANC,True,(30,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(3550,420),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 4.gif",imagepics,pics,(3500,750),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 4.gif",imagepics,pics,(3500,700),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//4 pics.gif",imagepics,pics,(4300,650),True,BLANC,True,(200,50))
    imagepics,pics = creaMur("image//pics 3.gif",imagepics,pics,(4550,500),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 3.gif",imagepics,pics,(4700,400),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(3300,300),True,BLANC,True,(30,50))
    imagepics,pics = creaMur("image//pics bas.gif",imagepics,pics,(2300,330),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(7150,450),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 2.gif",imagepics,pics,(2450,500),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(5000,300),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(5200,300),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//4 pics.gif",imagepics,pics,(5750,350),True,BLANC,True,(200,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(5950,350),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(6000,350),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//4 picsV.gif",imagepics,pics,(5700,450),True,BLANC,True,(50,180))
    imagepics,pics = creaMur("image//4 picsAL.gif",imagepics,pics,(4750,630),True,BLANC,True,(200,50))
    imagepics,pics = creaMur("image//4 picsAL.gif",imagepics,pics,(5750,630),True,BLANC,True,(200,50))
    imagepics,pics = creaMur("image//pics 2.gif",imagepics,pics,(6650,450),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//4 picsAL.gif",imagepics,pics,(5950,630),True,BLANC,True,(200,50))
    imagepics,pics = creaMur("image//4 picsAL.gif",imagepics,pics,(6150,630),True,BLANC,True,(200,50))
    imagepics,pics = creaMur("image//pics 2.gif",imagepics,pics,(6350,630),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 3.gif",imagepics,pics,(6700,400),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 4.gif",imagepics,pics,(6600,400),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 2.gif",imagepics,pics,(6350,630),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//4 pics.gif",imagepics,pics,(4000,650),True,BLANC,True,(230,50))
    imagepics,pics = creaMur("image//pics 2.gif",imagepics,pics,(6400,630),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 2.gif",imagepics,pics,(6450,630),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 2.gif",imagepics,pics,(6500,630),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(3150,300),True,BLANC,True,(30,50))
    imagepics,pics = creaMur("image//pics 1.gif",imagepics,pics,(6050,350),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//4 picsAL.gif",imagepics,pics,(4950,630),True,BLANC,True,(200,50))
    imagepics,pics = creaMur("image//pics 2.gif",imagepics,pics,(5150,630),True,BLANC,True,(50,50))
    imagepics,pics = creaMur("image//pics 2.gif",imagepics,pics,(5200,630),True,BLANC,True,(50,50))


    etoileimage,etoilerect = creaMur("image//etoile.gif",etoileimage,etoilerect,(2370,370),True,BLANC,True,(30,30))


    return obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,persogauche,etoileimage,etoilerect,projectile,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau


obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,persogauche,etoileimage,etoilerect,projectile,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau = debut(obstacle,pics,lesimages,imagepics,etoileimage,etoilerect,rectmobs,position_mobs,rectmobs_initial,blit_mobs)


#Rafraichir la page initial
pygame.display.flip()


# ******************************************************************************************* #
# ******************************************************************************************* #
# *********************************** LE PERSONNAGE ***************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #

# DEFINITION DE LA FONCTION POUR AFFICHER LE PERSONNAGE #
def personnage(positionperso,pos) :
    if not pos :
        fenetre.blit(perso, positionperso)
    elif pos :
        fenetre.blit(persogauche, positionperso)


# DEFINITION DE LA FONCTION POUR GERER LE SAUT DU PERSONNAGE #
def saut(ym,xm) :
    ym = ym + 0.25
    xm = xm/2
    return ym,xm

# DEFINITION DE LA FONCTION POUR GERER LES COLLISIONS ENTRE LE PERSONNAGE ET LES OBSTACLES (MUR ET SOL) #
def collision(positionperso,xmouv,x1mouv,x2mouv,ymouv,sauter,obstacle) :
    indice = []
    surf = 0
    oby = False
    nb = len(obstacle)
    for i in range(0,nb) :
        surf = obstacle[i]
        if positionperso.colliderect(surf) :
            if xmouv < 0 and positionperso.right > surf.left and positionperso.left < surf.left - (taillepersoL - 7):
                xmouv = positionperso.right - surf.left
            elif xmouv > 0 and positionperso.left < surf.right and positionperso.right > surf.right + (taillepersoL - 7):
                xmouv = - (surf.right - positionperso.left)
            elif ymouv < 0 and positionperso.top < surf.bottom and positionperso.bottom > surf.bottom - (taillepersoH - 7):
                positionperso.top = surf.bottom
                ymouv = 0.25
                oby = True
            elif ymouv > 0 and positionperso.bottom > surf.top and positionperso.top < surf.top + (taillepersoH - 7):
                positionperso.bottom = surf.top
                sauter = False
                oby = True
    return [sauter,oby,positionperso,ymouv,xmouv]

# DEFINITION DE LA FONCTION QUI GERE LES COLLISIONS ENTRE LE PERSONNAGE ET LES PICS #
def pics_collisions(tuto1,tuto2,tuto3,positionperso,pics,imagepics,positionfond,obstacle,lesimages,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau) :
    surf = 0
    nb = len(pics)
    for i in range(0,nb) :
        surf = pics[i]
        if positionperso.colliderect(surf) :
            if i == 0 and (tuto1 or tuto2 or tuto3):
                obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,persogauche,etoileimage,etoilerect,projectile,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau = debut(obstacle,pics,lesimages,imagepics,etoileimage,etoilerect,rectmobs,position_mobs,rectmobs_initial,blit_mobs)
                principale(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau,True)
            else :
                Game_Over1(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau)
        else :
            pass

# DEFINITION DE LA FONCTION QUI PERMET DE GERER SI LE PERSONNAGE SORT DE LA FENETRE OU PAS #
def hors_map(positionperso,pics,imagepics,positionfond,obstacle,lesimages,surfaceH,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau) :
    if positionperso.bottom > surfaceH + 10 :
        Game_Over1(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau)
    else :
        pass

# DEFINITION DE LA FONCTION QUI PERMET DE GERER LES COLLISIONS ENTRE LE PERSONNAGE ET LES MONSTRES #
def collisions_mobs_avec_personnage(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau) :
    for i in range(0,len(rectmobs)) :
        if positionperso.colliderect(rectmobs[i]) :
            if blit_mobs[i] :
                Game_Over1(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau)
        else :
            pass


# ******************************************************************************************* #
# ******************************************************************************************* #
# *********************************** LES OBSTACLES ***************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #

# DEFINITION DE LA FONCTION QUI PERMET DE DEPLACER LE DECOR POUR SIMULER UN DEPLACEMENT DU PERSONNAGE #
def mouvmursol(mur,xmouv) :
    murnew = []
    for i in range(0,len(mur)) :
        surf = mur[i]
        surf = surf.move(xmouv,0)
        murnew.append(surf)
    return murnew

# DEFINITION DE LA FONCTION QUI PERMET D'AFFICHER LES OBSTACLES #
def affichagemursol(mur,lesimagesdudecor) :
    for i in range(0,len(mur)) :
        fenetre.blit(lesimagesdudecor[i],mur[i])

# ******************************************************************************************* #
# ******************************************************************************************* #
# ************************************** LE FOND ******************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #

def fond(positionfond) :
    fenetre.blit(imagefond, positionfond)


# ******************************************************************************************* #
# ******************************************************************************************* #
# ************************************* LES ETOILES ***************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #

# DEFINITION DE LA FONCTION QUI PERMET DE GERER LES COLLISIONS ENTRE LE PERSONNAGE ET LES ETOILES #
def etoile_collisions(etoileimage,etoilerect,positionperso,pointscore,blit_etoile) :
    for i in range(0,len(etoilerect)) :
        if positionperso.colliderect(etoilerect[i]) :
            if blit_etoile[i] :
                pointscore += 1
                blit_etoile = remplace_list(blit_etoile,i,False)
    return etoileimage,etoilerect,pointscore,blit_etoile

# DEFINITION DE LA FONCTION QUI PERMET D'AFFICHER LES ETOILES #
def affichage_etoile(etoilerect,etoileimage,blit_etoile) :
    for i in range(0,len(etoilerect)) :
        if blit_etoile[i] :
            fenetre.blit(etoileimage[i],etoilerect[i])
        else :
            pass

# DEFINITION DE LA FONCTION QUI PERMET D'AFFICHER LE SCORE #
def affichage_score(pointscore) :
    PoliceTexte = pygame.font.Font("police//impact.ttf",30)
    SurfTexte, RectTexte = creaTexte("Score =",PoliceTexte,0)
    RectTexte = RectTexte.move(10,10)
    fenetre.blit(SurfTexte,RectTexte)
    if pointscore == 0 :
        texte = "0"
    elif pointscore == 1 :
        texte = "1"
    elif pointscore == 2 :
        texte = "2"
    elif pointscore == 3 :
        texte = "3"
    elif pointscore == 4 :
        texte = "4"
    elif pointscore == 5 :
        texte = "5"
    elif pointscore == 6 :
        texte = "6"
    elif pointscore == 7 :
        texte = "7"
    elif pointscore == 8 :
        texte = "8"
    elif pointscore == 9 :
        texte = "9"
    elif pointscore == 10 :
        texte = "10"
    elif pointscore == 11 :
        texte = "11"
    elif pointscore == 12 :
        texte = "12"
    elif pointscore == 13 :
        texte = "13"
    elif pointscore == 14 :
        texte = "14"
    elif pointscore == 15 :
        texte = "15"


    SurfScore, RectScore = creaTexte(texte,PoliceTexte,0)
    RectScore = RectScore.move(110,10)
    fenetre.blit(SurfScore,RectScore)

# ******************************************************************************************* #
# ******************************************************************************************* #
# *********************************** LES PROJECTILES *************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #

# DEFINITION DE LA FONCTION POUR POSITIONNER LE PROJECTILE #
def position_proj(positionperso,rectprojectile) :
    rectprojectile.right = positionperso.right
    rectprojectile.top = positionperso.top + 20
    return rectprojectile

# DEFINITION DE LA FONCTION POUR DEPLACER LE PROJECTILE #
def projectile_move(position_missile,xmissile,xmouv,rectprojectile,missile,tour,positionperso) :
    if position_missile == "gauche" :
        xmissile = -6
    elif position_missile == "droite" :
        xmissile = 6
    xmissile = xmissile + xmouv
    tour = tour + 1
    rectprojectile = rectprojectile.move(xmissile,0)
    if tour == 50 and missile == True:
        missile = False
        tour = 0
        rectprojectile = position_proj(positionperso,rectprojectile)
    return rectprojectile,tour,missile

# DEFINITION DE LA FONCTION QUI PERMET DE GERER LES COLLISIONS ENTRE LES PROJECTILES ET LES OBSTACLES #
def collision_projectile(rectprojectile,obstacle,pics,tour,blit_mobs,rectmobs) :
    for i in range(0,len(obstacle)) :
        if rectprojectile.colliderect(obstacle[i]) :
            return False, 0
    for i in range(0,len(pics)) :
        if rectprojectile.colliderect(pics[i]) :
            return False, 0
    for i in range(0,len(rectmobs)) :
        if rectprojectile.colliderect(rectmobs[i]) :
            if blit_mobs[i] :
                return False, 0
    return True,tour


# DEFINITION DE LA FONCTION QUI PERMET DE GERER LES COLLISIONS ENTRE LES MONSTRES ET LE PROJECTILE #
def collisions_mobs_avec_projectile(rectprojectile,rectmobs,blit_mobs) :
    for i in range(0,len(rectmobs)) :
        rect = rectmobs[i]
        if rectprojectile.colliderect(rect) :
            blit_mobs = remplace_list(blit_mobs,i,False)
    return blit_mobs

# DEFINITION DE LA FONCTION POUR AFFICHER LE PROJECTILE #
def affichageprojectile(rectprojectile) :
    fenetre.blit(projectile,rectprojectile)

# ******************************************************************************************* #
# ******************************************************************************************* #
# ************************************ LES MONSTRES ***************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #

# DEFINITION DE LA FONCTION QUI PERMET DE DEPLACER LES LIMITES DE DEPLACEMENT DES MONSTRES #
def deplacement_de_rect_initial(rectmobs_initial,xmouv) :
    for i in range(0,len(rectmobs_initial)) :
        rect = rectmobs_initial[i]
        rect = rect.move(xmouv,0)
        rectmobs_initial = remplace_list(rectmobs_initial,i,rect)
    return rectmobs_initial

# DEFINITION DE LA FONCTION POUR DEPLACER LES RECTANGLES #
def deplacement_mobs_2(rectmobs,Rectangle,xmouv,xmobs,position_mobs,index_du_rect) :
    i = index_du_rect
    if position_mobs[i] == "droite" and xmobs < 0 :
        xmobs = - xmobs
    elif position_mobs[i] == "gauche" and xmobs > 0 :
        xmobs = - xmobs
    xmobs = xmobs + xmouv
    Rectangle = Rectangle.move(xmobs,0)
    rectmobs = remplace_list(rectmobs,i,Rectangle)
    return rectmobs

# DEFINITION DE A FONCTION QUI PERMET DE CHOISIR DE COMBIEN DE PIXELS SE DEPLACENT LES MONSTRES #
def deplacement_mobs(rectmobs,position_mobs,xmouv) :
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[0],xmouv,0,position_mobs,0)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[1],xmouv,1,position_mobs,1)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[2],xmouv,-1,position_mobs,2)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[3],xmouv,1,position_mobs,3)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[4],xmouv,-1,position_mobs,4)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[5],xmouv,1,position_mobs,5)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[6],xmouv,1,position_mobs,6)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[7],xmouv,1,position_mobs,7)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[8],xmouv,1,position_mobs,8)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[9],xmouv,1,position_mobs,9)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[10],xmouv,1,position_mobs,10)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[11],xmouv,1,position_mobs,11)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[12],xmouv,1,position_mobs,12)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[13],xmouv,1,position_mobs,13)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[14],xmouv,1,position_mobs,14)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[15],xmouv,1,position_mobs,15)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[16],xmouv,1,position_mobs,16)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[17],xmouv,1,position_mobs,17)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[18],xmouv,1,position_mobs,18)
    rectmobs = deplacement_mobs_2(rectmobs,rectmobs[19],xmouv,1,position_mobs,19)
    return rectmobs

# DEFINITION DE LA FONCTION QUI PERMET DE GERER LES COLLISIONS ENTRE LES MONSTRES ET LEUR LIMITE DE DEPLACEMENT #
def collisions_mobs_avec_position_initial(rectmobs,rectmobs_initial,position_mobs) :
    for i in range(0,len(rectmobs)) :
        rect = rectmobs_initial
        surf_gauche = rect[i]
        surf_droite = rect[i]
        surf_gauche = surf_gauche.move(-1,0)
        surf_droite = surf_droite.move(150,0)
        Rectangle = rectmobs[i]
        if Rectangle.colliderect(surf_gauche) :
            Rectangle.left = surf_gauche.right
            position_mobs = remplace_list(position_mobs,i,"droite")
            rectmobs = remplace_list(rectmobs,i,Rectangle)
        elif Rectangle.colliderect(surf_droite) :
            Rectangle.right = surf_droite.left
            position_mobs = remplace_list(position_mobs,i,"gauche")
            rectmobs = remplace_list(rectmobs,i,Rectangle)
        else :
            pass
    return rectmobs,position_mobs

# DEFINITION DE LA FONCTION QUI PERMET DE GERER L'AFFICHAGE DES MONSTRES #
def affichage_mobs(rectmobs,position_mobs,blit_mobs) :
    image_droite = pygame.image.load("image//mobs droite.gif")
    image_droite = pygame.transform.scale(image_droite,(30,50))
    image_droite.set_colorkey(BLANC)
    image_gauche = pygame.image.load("image//mob.gif")
    image_gauche = pygame.transform.scale(image_gauche,(30,50))
    image_gauche.set_colorkey(BLANC)
    for i in range(0,len(rectmobs)) :
        if blit_mobs[i] :
            if position_mobs[i] == "gauche" :
                fenetre.blit(image_gauche,rectmobs[i])
            elif position_mobs[i] == "droite" :
                fenetre.blit(image_droite,rectmobs[i])
        else :
            pass


# ******************************************************************************************* #
# ******************************************************************************************* #
# ********************************** DRAPEAU DE FIN ***************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #

# DEFINITION POUR AFFICHER LE DRAPEAU
def affichage_drapeau(drapeau_rect) :
    fenetre.blit(image_drapeau,drapeau_rect)

def blit_fin(img1,img2,img3,img4) :
    fenetre.blit(img1,(70,300))
    fenetre.blit(img2,(290,300))
    fenetre.blit(img3,(510,300))
    fenetre.blit(img4,(730,300))

def affichage_texte_fin(texte) :
    Police = pygame.font.Font("police//impact.ttf",50)
    surfTexte, RectTexte = creaTexte(texte,Police,NOIR)
    RectTexte = RectTexte.move(400,100)
    fenetre.blit(surfTexte,RectTexte)

    Police_2 = pygame.font.Font("police//impact.ttf",30)
    SurfTexte_2, RectTexte_2 = creaTexte("Appuyez sur espace pour recommencer ou echap pour quitter !",Police_2,NOIR)
    RectTexte_2 = RectTexte_2.move(100,500)
    fenetre.blit(SurfTexte_2,RectTexte_2)

def image_fin():
    etoile_vide = pygame.image.load("image//et vide.gif")
    etoile_vide = pygame.transform.scale(etoile_vide,(200,200))
    etoile_vide.set_colorkey(BLANC)
    etoile_pleine = pygame.image.load("image//et pleine.gif")
    etoile_pleine = pygame.transform.scale(etoile_pleine,(200,200))
    etoile_pleine.set_colorkey(BLANC)
    etoile_moitie = pygame.image.load("image//et moitie.gif")
    etoile_moitie = pygame.transform.scale(etoile_moitie,(200,200))
    etoile_moitie.set_colorkey(BLANC)
    etoile_quart = pygame.image.load("image//et quart.gif")
    etoile_quart = pygame.transform.scale(etoile_quart,(200,200))
    etoile_quart.set_colorkey(BLANC)
    etoile_3quart = pygame.image.load("image//et troisquart.gif")
    etoile_3quart = pygame.transform.scale(etoile_3quart,(200,200))
    etoile_3quart.set_colorkey(BLANC)
    return etoile_vide, etoile_pleine, etoile_moitie, etoile_quart, etoile_3quart

def affichage_score_fin(pointscore) :
    pourcentage_score = (pointscore/5)*100
    etoile_vide, etoile_pleine, etoile_moitie, etoile_quart, etoile_3quart = image_fin()
    if 24 < pourcentage_score :
        if 49 < pourcentage_score :
            if 74 < pourcentage_score :
                if pourcentage_score == 100 :
                    blit_fin(etoile_pleine,etoile_pleine,etoile_pleine,etoile_pleine)
                else :
                    if 74 <= pourcentage_score :
                        if 78 < pourcentage_score :
                            if 84 < pourcentage_score :
                                if 90 < pourcentage_score :
                                    blit_fin(etoile_pleine,etoile_pleine,etoile_pleine,etoile_3quart)
                                else :
                                    blit_fin(etoile_pleine,etoile_pleine,etoile_pleine,etoile_moitie)
                            else :
                                blit_fin(etoile_pleine,etoile_pleine,etoile_pleine,etoile_quart)
                        else :
                            blit_fin(etoile_pleine,etoile_pleine,etoile_pleine,etoile_vide)
            else :
                if 49 <= pourcentage_score :
                    if 54 < pourcentage_score :
                        if 60 < pourcentage_score :
                            if 66 < pourcentage_score :
                                blit_fin(etoile_pleine,etoile_pleine,etoile_3quart,etoile_vide)
                            else :
                                blit_fin(etoile_pleine,etoile_pleine,etoile_moitie,etoile_vide)
                        else :
                            blit_fin(etoile_pleine,etoile_pleine,etoile_quart,etoile_vide)
                    else :
                        blit_fin(etoile_pleine,etoile_pleine,etoile_vide,etoile_vide)
        else :
            if 24 <= pourcentage_score :
                if 28 < pourcentage_score :
                    if 33 < pourcentage_score :
                        if 42 < pourcentage_score :
                            blit_fin(etoile_pleine,etoile_3quart,etoile_vide,etoile_vide)
                        else :
                            blit_fin(etoile_pleine,etoile_moitie,etoile_vide,etoile_vide)
                    else :
                        blit_fin(etoile_pleine,etoile_quart,etoile_vide,etoile_vide)
                else :
                    blit_fin(etoile_pleine,etoile_vide,etoile_vide,etoile_vide)
    else :
        if 0 <= pourcentage_score :
            if 3 < pourcentage_score :
                if 9 < pourcentage_score :
                    if 17 < pourcentage_score :
                        blit_fin(etoile_3quart,etoile_vide,etoile_vide,etoile_vide)
                    else :
                        blit_fin(etoile_moitie,etoile_vide,etoile_vide,etoile_vide)
                else :
                    blit_fin(etoile_quart,etoile_vide,etoile_vide,etoile_vide)
            else :
                blit_fin(etoile_vide,etoile_vide,etoile_vide,etoile_vide)

def Win(texte,pointscore,obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,persogauche,etoileimage,etoilerect,projectile,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau) :
    while True :
        horloge.tick()
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,persogauche,etoileimage,etoilerect,projectile,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau = debut(obstacle,pics,lesimages,imagepics,etoileimage,etoilerect,rectmobs,position_mobs,rectmobs_initial,blit_mobs)
                    principale(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau,False)
                if event.key == pygame.K_ESCAPE :
                    pygame.quit()
                    quit()
        affichage_texte_fin(texte)
        affichage_score_fin(pointscore)
        pygame.display.flip()

def collision_drapeau_perso(pointscore,obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,persogauche,etoileimage,etoilerect,projectile,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau) :
    if positionperso.colliderect(drapeau_rect) :
        Win("Gagné",pointscore,obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,persogauche,etoileimage,etoilerect,projectile,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau)

# ******************************************************************************************* #
# ******************************************************************************************* #
# ************************************ LE TUTORIEL ****************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #

def explication(texte,texte_1,texte_2,texte_3,coord,taille) :
    Police = pygame.font.Font("police//impact.ttf",30)
    fond_ecriture = pygame.image.load("image//cadre.png")
    fond_ecriture = pygame.transform.scale(fond_ecriture,taille)
    rect = fond_ecriture.get_rect()
    rect = rect.move(coord)
    Surftexte1, Recttexte1 = creaTexte(texte,Police,0)
    Surftexte2, Recttexte2 = creaTexte(texte_1,Police,0)
    Surftexte3, Recttexte3 = creaTexte(texte_2,Police,0)
    Surftexte4, Recttexte4 = creaTexte(texte_3,Police,0)
    Recttexte1 = Recttexte1.move(rect.left+10,rect.top+10)
    Recttexte2 = Recttexte2.move(Recttexte1.left,Recttexte1.top+40)
    Recttexte3 = Recttexte3.move(Recttexte2.left,Recttexte2.top+40)
    Recttexte4 = Recttexte4.move(Recttexte3.left,Recttexte3.top+40)
    fenetre.blit(fond_ecriture,rect)
    fenetre.blit(Surftexte1,Recttexte1)
    fenetre.blit(Surftexte2,Recttexte2)
    fenetre.blit(Surftexte3,Recttexte3)
    fenetre.blit(Surftexte4,Recttexte4)
    pygame.display.flip()

def tutoriel_deplacement(move,ecriture,tuto) :
    if ecriture :
        explication("Pour pouvoir se deplacer","il suffit de","presser les bouton","fleches droite et fleche gauche",(500,200),(400,200))
    if move > 15 :
        tuto = False
    return tuto,ecriture

def tutoriel_saut(move_up,sauter,ecriture,tuto,obstacle,etape1,etape2) :
    surf = obstacle[1]
    if ecriture :
        explication("Pour pouvoir sauter","il suffit de","presser le bouton","fleche du haut",(500,200),(400,200))
    if move_up and not sauter :
        etape1 = True
    if surf.left < -450 :
        etape2 = True
    if etape1 and etape2 :
        tuto = False
    return tuto,ecriture,etape1,etape2

def tutoriel_projectile(missile,ecriture,tuto) :
    if ecriture :
        explication("Pour pouvoir lancer un","missile, il suffit de","presser le bouton","espace",(500,200),(400,200))
    if missile :
        tuto = False
    return tuto,ecriture


# ******************************************************************************************* #
# ******************************************************************************************* #
# ********************************* PARTIE PRINCIPALE *************************************** #
# ******************************************************************************************* #
# ******************************************************************************************* #

def principale(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau,TUTO) :
    x1_mouv = 0
    x2_mouv = 0
    ymouv = 8
    xmouv = 0
    tour = 0
    blit_etoile = []
    if TUTO :
        tuto = ecris_tuto1 = True
    else :
        tuto = ecris_tuto1 = False
    tuto2 = ecris_tuto2 = tuto3 = ecris_tuto3 = False
    move_up = False
    move_tuto_deplacement = 0
    tuto_saut_etape1 = tuto_saut_etape2 = False
    xmissile = 0
    pointscore = 0
    rectprojectileold = 0
    missile = False
    position_missile = "droite"
    gauche = False
    mouv = []
    oby = oby_eau = False
    sauter = False
    continuer = True
    for i in range(0,len(etoilerect)) :
        blit_etoile.append(True)
    while continuer :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE and missile == False and not tuto and not tuto2 :
                    missile = True
                    if gauche :
                        position_missile = "gauche"
                        xmissile = -6
                    elif not gauche :
                        position_missile = "droite"
                        xmissile = 6
                if event.key == pygame.K_RIGHT :
                    x1_mouv = -2
                    move_tuto_deplacement -= x1_mouv
                if event.key == pygame.K_LEFT :
                    x2_mouv = 2
                    move_tuto_deplacement += x2_mouv
                if event.key == pygame.K_UP and not sauter and not tuto:
                    if oby :
                        sauter = True
                        ymouv = -10.25
                        move_up = True
                if event.key == pygame.K_ESCAPE :
                    menu_pause(obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau)
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_RIGHT :
                    x1_mouv = 0
                if event.key == pygame.K_LEFT :
                    x2_mouv = 0
        xmouv = x1_mouv + x2_mouv
        if sauter :
            ymouv,xmouv = saut(ymouv,xmouv)
        if sauter and ymouv == 10.25 :
            sauter = False
            ymouv = 10
        if not sauter and not oby:
            ymouv = 10
        if xmouv < 0 :
            gauche = False
        elif xmouv > 0 :
            gauche = True
        positionperso = positionperso.move(0,ymouv)
        if not missile :
            rectprojectile = position_proj(positionperso,rectprojectile)
        elif missile :
            rectprojectile,tour,missile = projectile_move(position_missile,xmissile,xmouv,rectprojectile,missile,tour,positionperso)
        obstacle = mouvmursol(obstacle,xmouv)
        pics = mouvmursol(pics,xmouv)
        etoilerect = mouvmursol(etoilerect,xmouv)
        rectmobs = deplacement_mobs(rectmobs,position_mobs,xmouv)
        drapeau_rect = drapeau_rect.move(xmouv,0)
        collision_drapeau_perso(pointscore,obstacle,pics,lesimages,imagepics,positionperso,positionfond,imagefond,perso,persogauche,etoileimage,etoilerect,projectile,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau)
        mouv = collision(positionperso,xmouv,x1_mouv,x2_mouv,ymouv,sauter,obstacle)
        pics_collisions(tuto,tuto2,tuto3,positionperso,pics,imagepics,positionfond,obstacle,lesimages,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau)
        hors_map(positionperso,pics,imagepics,positionfond,obstacle,lesimages,surfaceH,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau)
        etoileimage,etoilerect,pointscore,blit_etoile = etoile_collisions(etoileimage,etoilerect,positionperso,pointscore,blit_etoile)
        rectmobs,position_mobs = collisions_mobs_avec_position_initial(rectmobs,rectmobs_initial,position_mobs)
        collisions_mobs_avec_personnage(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau)
        rectmobs_initial = deplacement_de_rect_initial(rectmobs_initial,xmouv)
        if missile :
            missile, tour = collision_projectile(rectprojectile,obstacle,pics,tour,blit_mobs,rectmobs)
            blit_mobs = collisions_mobs_avec_projectile(rectprojectile,rectmobs,blit_mobs)
        sauter = mouv[0]
        oby = mouv[1]
        positionperso = mouv[2]
        ymouv = mouv[3]
        xmouv = mouv[4]
        if not missile :
            rectprojectile = position_proj(positionperso,rectprojectile)
        obstacle = mouvmursol(obstacle,xmouv)
        pics = mouvmursol(pics,xmouv)
        etoilerect = mouvmursol(etoilerect,xmouv)
        rectmobs = deplacement_mobs(rectmobs,position_mobs,xmouv)
        rectmobs_initial = deplacement_de_rect_initial(rectmobs_initial,xmouv)
        drapeau_rect = drapeau_rect.move(xmouv,0)
        fond(positionfond)
        affichagemursol(obstacle,lesimages)
        affichagemursol(pics,imagepics)
        affichage_etoile(etoilerect,etoileimage,blit_etoile)
        affichage_score(pointscore)
        personnage(positionperso,gauche)
        affichage_drapeau(drapeau_rect)
        affichage_mobs(rectmobs,position_mobs,blit_mobs)
        if missile :
            affichageprojectile(rectprojectile)
        if not missile :
            rectprojectileold = rectprojectile
        if TUTO:
            if tuto :
                tuto,ecris_tuto1 = tutoriel_deplacement(move_tuto_deplacement,ecris_tuto1,tuto)
                if not tuto :
                    ecris_tuto2 = tuto2 = True
            if tuto2 :
                tuto2,ecris_tuto2,tuto_saut_etape1,tuto_saut_etape2 = tutoriel_saut(move_up,sauter,ecris_tuto2,tuto2,obstacle,tuto_saut_etape1,tuto_saut_etape2)
                if not tuto2 :
                    ecris_tuto3 = tuto3 = True
            if tuto3 :
                tuto3, ecris_tuto3 = tutoriel_projectile(missile,ecris_tuto3,tuto3)
                if not tuto3 :
                    TUTO = False
        else :
            pass
        pygame.time.delay(5)
        pygame.display.flip()


principale(positionfond,positionperso,obstacle,lesimages,pics,imagepics,etoileimage,etoilerect,rectprojectile,rectmobs,position_mobs,rectmobs_initial,blit_mobs,drapeau_rect,image_drapeau,True)
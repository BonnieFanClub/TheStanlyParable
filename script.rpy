# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define a = Character('???', color="#cbb89f")
define b = Character('???', color="#111111")
define c = Character('Stanly', color="#cbb89f")
define d = Character('Le narrateur', color="#e9e9e9")
define e = Character('???', color="#76d5cb")
define f = Character('???', color="#d576b7")

# Le jeu commence ici
label start:
    play music stpa
    scene 1 with Dissolve(5) :
    "Ceci est l'histoire d'un homme nommé Stanly... "
    scene 2 with Dissolve(1):
        
           
    "Stanly était un employé de bureau d'une grande entreprise dont il était le numéro # 420." 
    scene 3
    play sound camera volume 0.02
    show 3a 
    pause 0.1
    hide 3a
    show 3b 
    pause 0.1
    hide 3b
    show 3c 
    pause 0.2
    hide 3c
    show 3d 
    pause 0.1
    hide 3d
    scene 3
        
    

    "Le travail de l'employé # 420 était simple : il était assis à son bureau 420 et il appuyait sur les boutons d'un clavier."
    show 3d
    pause 0.1
    hide 3d
    show 3c 
    pause 0.2
    hide 3c
    show 3b
    pause 0.1
    hide 3b
    show 3a
    pause 0.1
    hide 3a
    stop sound 
    scene 4
        
        
    "Les ordres lui parvenaient via un moniteur sur son bureau lui indiquant quels boutons appuyer, combien de temps les appuyer et dans quel ordre."
    scene 5 with Dissolve(1):

    "C'est ce que l'employé # 420 a fait chaque jour de chaque mois de chaque année, et bien que d'autres aient pu le considérer comme déchirant,..."
    scene 6 with Dissolve(1):

    "Stanly savourait chaque instant où les commandes arrivaient, comme s'il avait été fait exactement pour ce travail."
    scene 7 with Dissolve(1):

    "Stanly était heureux..."
    stop music
    play sound bugson volume 0.5
    scene 7 with hpunch:
    
    "Hein..."
    show 7a 
    pause 0.1
    hide 7a
    show 7b
    pause 0.2
    hide 7b
    show 7c
    "Qu'EsT ce qUi Se PaSSe..."
    scene bug:
    hide textbox
    $renpy.pause()
    scene 8
    play sound bugson1 noloop fadein 5 volume 0.5 
    ""
    play sound bugson2 volume 0.5
    scene backrooms 2 with Dissolve(3)
    a "Où suis-je?"

    a "Qui suis-je?"

    "J'essayais de m'en rappeler et pourtant rien ne me venait ."

    "Meme si en y repensant plus fortement il s'agissait peut etre de..."

    $ povname = renpy.input("Mais, oui mon prénom doit sûrement etre...", length=42).strip()

    a "Je sais, je m'appele..."

    b "STANLY!!!"

    b "Tu t'appeles Stanly et TU était censé jouer à MON jeu, avec MES régles mais maintenant..."

    b "Tout est foutu, je ne sais ni où nous sommes ni qui est ce nain de jardin à coté de toi"

    c "Un nain de jardin???"
    scene backrooms 1
    play music horreur 
    show naindejardin :
        linear 50 zoom 3.0 truecenter
    show backrooms 1 red with Dissolve(20)
    show naindejardin red with Dissolve(20) :
        linear 50 zoom 3.0 truecenter
    
    ""
    
    "Ce nain de jardin est terrifiant et pourtant quelque chose de mysterieux m'attire che lui"
    menu :

        "je le prends, car en vrai il est un peu cute" :
            jump nain

        "Non, je ne le prend pas, vous-êtes des fous !!!" :
            jump non
        
label nain :
    b "tu es sur de toi, il a quand meme un petit coté terrifiant, non ?"
    jump suitea
    stop music
label non :
    b "tu es sur de toi, il a quand meme un petit coté mignon, non ?"
    jump suitea
    stop music    
    
  
label suitea :
    menu :

        "je le prends, il est vraiment trop cute" :
            jump chap1

        "Non, je le prend pas, il est vraiment terrifiant" :
            jump nona
    

    







        
label nona:
    b "j'immagine que c'est un choix commes les autres, et surtout assez logique vu la situation"
        
            
        





return

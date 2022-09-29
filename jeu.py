import random
import matplotlib.pyplot as plt
import matplotlib as mpl
from persos import *
from svgpathtools import svg2paths
from svgpath2mpl import parse_path

##########ICONE##############

"""LOUP"""
loup_path, attributes = svg2paths('loup.svg')
loup_marker = parse_path(attributes[0]['d'])
loup_marker.vertices -= loup_marker.vertices.mean(axis=0)
loup_marker = loup_marker.transformed(mpl.transforms.Affine2D().scale(-1,1))


"""ARCHER"""
archer_path, attributes = svg2paths('archer.svg')
archer_marker = parse_path(attributes[0]['d'])
archer_marker.vertices -= archer_marker.vertices.mean(axis=0)
archer_marker = archer_marker.transformed(mpl.transforms.Affine2D().scale(-1,1))


"""GUERRIER"""
guerrier_path, attributes = svg2paths('guerrier.svg')
guerrier_marker = parse_path(attributes[0]['d'])
guerrier_marker.vertices -= guerrier_marker.vertices.mean(axis=0)
guerrier_marker = guerrier_marker.transformed(mpl.transforms.Affine2D().scale(-1,1))


"""VOLEUR"""
voleur_path, attributes = svg2paths('voleur.svg')
voleur_marker = parse_path(attributes[0]['d'])
voleur_marker.vertices -= voleur_marker.vertices.mean(axis=0)
voleur_marker = voleur_marker.transformed(mpl.transforms.Affine2D().scale(-1,1))


############AFFICHAGE############


def update_plot(grass,global_plot, loup_population,  archer_population, guerrier_population,voleur_population, loup_pop_size, archer_pop_size, guerrier_pop_size, voleur_pop_size):
    """Update 2D environment plot and population line plot.

    Args:
        global_plot (tuple): Tuple with the figure container and a tuple with the two subplots even if only one is necessary here.
        grass (array): Numpy array representing the environment grass quantity doesn't change here (not nessary).
        loup_population (list): List of individuals. Each individual is an instance of the Loup class.

        archer_population (list): List of individuals. Each individual is an instance of the Archer class (to be created in the persos module).
        guerrier_population(list): List of individuals. Each individual is an instance of the Guerrier class (to be created in the persos module).
        voleur_population(list): List of individuals. Each individual is an instance of the Voleur class (to be created in the persos module).

    """

    fig = global_plot[0]
    ax1, ax2 = global_plot[1]

    # Plots
    ax1.cla()
    ax2.cla()

    ax1.imshow(grass, cmap='Greens', vmin=0, vmax=1)
    # l'herbe nous sert à avoir un terrain de taille fixe indépendant de la position des mobs.

    # affichage des loups avec le marker 4
    loups_x = []
    loups_y = []
    for idloup in range(len(loup_population)):
        loups_x.append(loup_population[idloup].x)
        loups_y.append(loup_population[idloup].y)
    ax1.scatter(loups_x, loups_y, color='k', marker=loup_marker, s=500)

    #affichage des archers avec le marker 5

    archers_x = []
    archers_y = []
    for idarcher in range(len(archer_population)):
        archers_x.append(archer_population[idarcher].x)
        archers_y.append(archer_population[idarcher].y)
    ax1.scatter(archers_x, archers_y, color='g', marker=archer_marker, s=500)

    #affichage des guerriers avec le marker 6

    guerriers_x = []
    guerriers_y = []
    for idguerrier in range(len(guerrier_population)):
        guerriers_x.append(guerrier_population[idguerrier].x)
        guerriers_y.append(guerrier_population[idguerrier].y)
    ax1.scatter(guerriers_x, guerriers_y, color='r', marker=guerrier_marker, s=500)

    #affichage des voleurs avec le marker 7

    voleurs_x = []
    voleurs_y = []
    for idvoleur in range(len(voleur_population)):
        voleurs_x.append(voleur_population[idvoleur].x)
        voleurs_y.append(voleur_population[idvoleur].y)
    ax1.scatter(voleurs_x, voleurs_y, color='slategray', marker=voleur_marker, s=500)

    #compteur
    ax2.plot(loup_pop_size, color="k")
    loup_pop_size.append(len(loup_population))
    ax2.plot(archer_pop_size, color="g")
    archer_pop_size.append(len(archer_population))
    ax2.plot(guerrier_pop_size, color="r")
    guerrier_pop_size.append(len(guerrier_population))
    ax2.plot(voleur_pop_size, color="slategray")
    voleur_pop_size.append(len(voleur_population))






    fig.canvas.flush_events()
    fig.canvas.draw()

    plt.pause(0.01)

def set_plot(width=25.6, height=13.3):
    """Initialize plot with two empty subplots.

    Args:
        width (float, optional): Width of the plot. Defaults to 25.6 (suits for 2560*1440 screen).
        height (float, optional): Height of the plot. Defaults to 13.3 (suits for 2560*1440 screen).

    Returns:
        tuple: First element of tuple is the figure container. Second element of the tuple is a tuple with the two
        subplots.
    """
    return plt.subplots(1, 2, figsize=(width, height))

def simulation(x,y, loup_init, archer_init, guerrier_init, voleur_init):
    grass = [[0]*y]*x
    archer_population = []
    for i in range(archer_init):
        archer_population.append(Archer(random.randint(0,x-1),random.randint(0,y-1)))
    loup_population = []
    for i in range(loup_init):
        loup_population.append(Loup(random.randint(0,x-1),random.randint(0,y-1)))
    guerrier_population = []
    for i in range(guerrier_init):
        guerrier_population.append(Guerrier(random.randint(0,x-1),random.randint(0,y-1)))
    voleur_population = []
    for i in range(voleur_init):
        voleur_population.append(Voleur(random.randint(0,x-1),random.randint(0,y-1)))

    loup_pop_size=[len(loup_population)]
    archer_pop_size=[len(archer_population)]
    guerrier_pop_size=[len(guerrier_population)]
    voleur_pop_size=[len(voleur_population)]

    global_plot = set_plot()

    for s in range(100):
        print(f'Tour {s}')

################DEPLACEMENT######################
        for loup in loup_population:  #LOUP
            loup.deplace(x,y)#attention à l'ordre dans lequel vont se faire les différentes actions

        for archer in archer_population:  #ARCHER
            archer.deplace(x,y)#attention à l'ordre dans lequel vont se faire les différentes actions

        for guerrier in guerrier_population:  #GUERRIER
            guerrier.deplace(x,y)#attention à l'ordre dans lequel vont se faire les différentes actions

        for voleur in voleur_population:  #VOLEUR
            voleur.deplace(x,y)#attention à l'ordre dans lequel vont se faire les différentes actions

################ATTAQUES######################
        """ARCHER TIR"""
        for archer in archer_population:
            for loup in loup_population: # TIR SUR LOUP
                if abs(loup.x-archer.x)<5 and abs(loup.y-archer.y)<5:
                    archer.tiralarc(loup)
            for guerrier in guerrier_population: # TIR SUR GUERRIER
                if abs(guerrier.x-archer.x)<5 and abs(guerrier.y-archer.y)<5:
                    archer.tiralarc(guerrier)
            for voleur in voleur_population: # TIR SUR VOLEUR
                if abs(voleur.x-archer.x)<5 and abs(voleur.y-archer.y)<5 and randint(1,10)>voleur.stealth:
                    archer.tiralarc(voleur)

        """ARCHER CAC"""

        loup_supp=[]
        """LOUP CAC"""
        for loup in loup_population:
            for archer in archer_population: #CAC LOUP SUR ARCHER
                if abs(loup.x-archer.x)<2 and abs(loup.y-archer.y)<2:
                    loup.corpsacorps(archer)
                    if archer.hp<=0: #TRANSFORMATION ARCHERS EN LOUP
                        loup_supp.append(Loup(archer.x,archer.y))
            for guerrier in guerrier_population:  #CAC LOUP SUR GUERRIER
                if abs(loup.x-guerrier.x)<2 and abs(loup.y-guerrier.y)<2:
                    loup.corpsacorps(guerrier)
            for voleur in voleur_population:  #CAC LOUP SUR VOLEUR
                if abs(loup.x-voleur.x)<2 and abs(loup.y-voleur.y)<2 and randint(1,10)>voleur.stealth:
                    loup.corpsacorps(voleur)
                    if voleur.hp<=0: #TRANSFORMATION ARCHERS EN LOUP
                        loup_supp.append(Loup(voleur.x,voleur.y))

        """GUERRIER CAC"""
        for guerrier in guerrier_population:
            for loup in loup_population: #CAC GUERRIER SUR LOUP
                if abs(guerrier.x-loup.x)<2 and abs(guerrier.y-loup.y)<2:
                    guerrier.corpsacorps(loup)
            for archer in archer_population: #CAC GUERRIER SUR ARCHER
                if abs(guerrier.x-archer.x)<2 and abs(guerrier.y-archer.y)<2:
                    guerrier.corpsacorps(archer)
            for voleur in voleur_population: #CAC GUERRIER SUR VOLEUR
                if abs(guerrier.x-voleur.x)<2 and abs(guerrier.y-voleur.y)<2 and randint(1,10)>voleur.stealth:
                    guerrier.corpsacorps(voleur)

        """VOLEUR CAC"""
        for voleur in voleur_population:
            for loup in loup_population: #CAC VOLEUR SUR LOUP
                if abs(voleur.x-loup.x)<2 and abs(voleur.y-loup.y)<2:
                    voleur.corpsacorps(loup)
            for archer in archer_population: #CAC VOLEUR SUR ARCHER
                if abs(voleur.x-archer.x)<2 and abs(voleur.y-archer.y)<2:
                    voleur.corpsacorps(archer)
            for voleur in voleur_population:  #CAC VOLEUR SUR GUERRIER
                if abs(voleur.x-guerrier.x)<2 and abs(voleur.y-guerrier.y)<2:
                    voleur.corpsacorps(guerrier)


################GESTION MORTS######################

        for i in range(len(loup_population)-1,-1,-1):
            if loup_population[i].hp<=0:
                del loup_population[i]

        for i in range(len(archer_population)-1,-1,-1):
            if archer_population[i].hp<=0:
                del archer_population[i]

        for i in range(len(guerrier_population)-1,-1,-1):
            if guerrier_population[i].hp<=0:
                del guerrier_population[i]

        for i in range(len(voleur_population)-1,-1,-1):
            if voleur_population[i].hp<=0:
                del voleur_population[i]

        loup_population = loup_population+loup_supp

        update_plot(grass,global_plot, loup_population, archer_population, guerrier_population,voleur_population, loup_pop_size,archer_pop_size, guerrier_pop_size, voleur_pop_size)

################RESULTS CONSOLE######################

        print("Nombre de loup:",str(len(loup_population)))
        print("Nombre d archer:",str(len(archer_population)))
        print("Nombre de guerrier:",str(len(guerrier_population)))
        print("Nombre de voleurs:",str(len(voleur_population)))

    plt.waitforbuttonpress()


if __name__=="__main__":
    simulation(x=30, y=30, loup_init=5, archer_init=15, guerrier_init=15, voleur_init=10)

"""Quelques idées d'amélioration et de choses à ne pas faire:
changer le visuel des markers pour des markers maison est la dernière priorité
à chaque tour visualiser le lieu où un individu est mort au tour précédent
les archers peuvent attaquer 3 fois par tour
les voleurs ne sont pas forcément repérés pour initier un combat
mettre un inventaire sur chaque perso, un voleur peut les voler
les déplacements ne sont aléatoires que pour les loups
"""

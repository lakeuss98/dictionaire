#author LK_l@ Keuss
from BibioDic import *
import json 
from pprint import *
#les fonctions externes

fichier = "dat.txt"
mboire = Mot("boire", ["avaler", "consommer"], ["cracher", "vormir"], ["mangus"], ["bois"])
manger = Mot("manger", "consommer",  "vormir", "mangus", "mange")
#dico.insererMot(manger)

dico=Dico(manger)
with open(fichier,"r") as f:
    dic = f.read().splitlines()
    print(dic)
    for mot in dic:
        mots = mot.split()
        print(mots)
        dico.lesmots[mots[0]] = {"synonymes": mots[1], "etymologie": mots[2], "antonymes": mots[3], "homonymes": mots[4]}

while( True):

    reponse = int(input(""" 
    ------------> menu de votre dictionaire <---------- \n 
        1----> Chercher un mot dans le  dictionaire 
        2----> Ajouter un mot dans le dictionaire 
        3----> Afficher le contenu du dictionaire 
        4----> Supprimer un mot du  dictionaire 
        5----> Modifier un mot du  dictionaire 
        6----> Supprimer le  dictionaire 
        7----> Enregistrer les modifications 
    """))

    if reponse == 1:
        motcherche =input(" veuillez entrez le mot que vous cherchez ou taper 0 pour rentrer au menu \n ---->")
        dico.chercherMot(motcherche)
        quit

    if reponse == 2:
        motajoute =input(" veuillez entrez le mot que vous souhaitez ajouter  ou taper 0 pour rentrer au menu \n ---->")
        dico.insererMot(motajoute)

    if reponse == 3:
        dico.affichermots()
    if reponse == 4:
        motset = input(" veuillez entrez le mot que vous souhaitez supprimer ou taper 0 pour rentrer au menu \n last word----> ")
        dico.supprimerMot(motset)
    if reponse ==5 :
        mode = input("veuillez choisir le mode de modification \n  1 --> pour complet  (tout les attributs ) \n  2 --> pour simple (rien que le nom) \n>>>>choix")
        if int(mode) == 2:
            motset =input(" veuillez entrez le mot que vous souhaitez modifier  ou taper 0 pour rentrer au menu \n last word---->")
            modef  =input("entrez votre nouveau mot  \n new word ---->")
            dico.modifierMots(motset,modef)
        if int(mode) == 1:
            motset = input(" veuillez entrez le mot que vous souhaitez modifier  ou taper 0 pour rentrer au menu \n last word---->")
            modef = input("entrez votre nouveau mot  \n new word ---->")
            s = input("entrez le nouveau synonyme   :\n")
            a = input("entrez le nouveau antonyme   :\n")
            h = input("entrez le nouveau homonyme   :\n")
            e = input("entrez le nouveau etymologie :\n")
            dico.modifierMotc(motset,modef,s,e,a,h)

    if reponse == 6:
        for dell in dico.lesmots.keys():
            dico.lesmots.pop(dell)
    if reponse == 7:
        with open(fichier, "a+") as f:
            #dic = f.read().splitlines()
            print(dic)
            for cle in dico.lesmots.keys():
                i=0
                for m in dic:
                    if m.split()[0]!=cle:
                        print(cle,m.split()[0],i,len(dic))
                        i=i+1
                if i == len(dic):
                    print("\ndictionaire mis a jour avec de nouveaux mots \n")
                    f.write(str(cle) + " " + str(dico.lesmots[cle]["synonymes"]) + " " + str(
                    dico.lesmots[cle]["etymologie"]) + " " + str(dico.lesmots[cle]["antonymes"]) + " " + str(
                    dico.lesmots[cle]["homonymes"]) + "\n")


































































































































































































        


from pprint import *
from pprint import *

class Mot():
    def __init__(self, mots, synonymes, antonymes, etymologie, homonymes):
        self.nom =  mots
        # self.at={self.nom,synonymes,antonymes,etymologie,homonymes}
        # self.attributs(synonymes,antonymes,etymologie,homonymes)
        self.syn = synonymes
        self.ant = antonymes
        self.ety = etymologie
        self.hom = homonymes

    def getmot(self):
        print([self.nom, self.syn, self.ety, self.ant, self.hom])
        return [self.nom, self.syn, self.ety, self.ant, self.hom]

    def ajoutersyn(self, syno):
        self.syn.append(syno)

    def retirersyn(self, syno):
        self.syn.remove(syno)

    def modifiersyn(self, newssyno, oldsyno):
        self.syn.remove(oldsyno)
        self.syn.append(newssyno)

    def ajouterant(self, anto):
        if not (anto in self.ant):
            self.ant.append(anto)

    def retirerant(self, anto):
        if anto in self.ant:
            self.ant.remove(anto)

    def modifierant(self, oldanto, newanto):
        self.ant.remove(oldanto)
        self.ant.append(newanto)

    def ajouterety(self, etymolo):
        if not (etymolo in self.ety):
            self.ety.append(etymolo)

    def retirerety(self, etymolo):
        self.ety.remove(etymolo)

    def modifierety(self, oldetymolo, newetymolo):
        self.ety.remove(oldetymolo)
        self.ety.append(newetymolo)

    def ajouterhom(self, homo):
        if not (homo in self.hom):
            self.hom.append(homo)

    def retirerhom(self, homo):
        if homo in self.hom:
            self.hom.remove(homo)

    def modifierhom(self, oldhomo, newhomo):
        self.hom.remove(oldhomo)
        self.hom.append(newhomo)
#(type de mots genre) et (signification) a ajouter

class Dico(Mot):
    dictionaire = {}

    def __init__(self, Mot):
        self.lesmots = {Mot.nom: {"synonymes": Mot.syn,
         "etymologie": Mot.ety,
          "antonymes": Mot.ant, 
          "homonymes": Mot.hom}
          }
        # self.ListMot = ListMot
    
    def nbrelt(self):
        return self.lesmots.__len__()
    def listeclefs(self):
        return self.lesmots.items()

    def getdico(self):
        #pprint(self.lesmots)
        return self.lesmots

    def chercherMot(self, motcherc): 
        if  motcherc in  self.lesmots.keys() :
            print(str(motcherc) ,": " ,self.lesmots[motcherc])
            return self.lesmots[motcherc]
        else:
            return print("ce mot n existe pas")
    def ChercherMot(self, titre):
        pprint(self.getmot( titre))
    
            
    def affichermots(self):
        for mo in self.lesmots.keys():
            print(mo, self.lesmots[mo])

    def insererMot(self, mo):
        if mo in self.lesmots.keys():
            print("ce mot est deja dans notre dictionaire")
        else:
            m = input("\nentrez mot        :")
            a = input("\nentrez antonyme   :")
            h = input("\nentrez homonyme   :")
            e = input("\nentrez etymologie :")
            s = input("\nentrez synonyme   :")
            adm=Mot(m, [s], [a], [e], [h])
            Dico(adm)
            self.lesmots[mo] = {"synonymes": s, "etymologie": e, "antonymes": a, "homonymes": h}
            print("votre mot a bien ete insere\n")
            self.chercherMot(mo)



    def supprimerMot(self, mo):
        if mo in self.lesmots.keys() :
            self.lesmots.pop(mo)
            print("\n !!!!!!!!!>votre mot a ete supprime avec succes<!!!!!!!")
        else:
            print("\n ce mot n 'existe pas dans le dictionaire ")

    def modifierMots(self, mo, newnom):
        if mo in self.lesmots.keys():
            self.lesmots[newnom] = self.lesmots[mo]
            self.lesmots.pop(mo)
        else:
            print("\nimpossible de modifier un mot qui n exixte pas !!!!!!!!\n")
    def modifierMotc(self,lastmo,newnom,syn,ety,ant,hom):
        if lastmo in self.lesmots.keys():
            self.lesmots[lastmo]["synonymes"] = syn
            self.lesmots[lastmo]["homonymes"] = hom
            self.lesmots[lastmo]["antonymes"] = ant
            self.lesmots[lastmo]["etymologie"] = ety
            self.lesmots[newnom] = self.lesmots[lastmo]
            self.lesmots.pop(lastmo)
            print("----->>>modification effectue avec succes!!!!!!!!!\n")
            self.chercherMot(newnom)
        else:
            print("\nimpossible de modifier un mot qui n exixte pas !!!!!!!!\n")



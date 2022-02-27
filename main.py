from BibioDic import *
from pprint import *
from json import *

boire = Mot("boire", ["avaler", "consommer"], ["cracher", "vormir"], ["mangus"], ["bois"])
manger = Mot("manger", ["avaler", "consommer"], ["cracher", "vormir"], ["mangus"], [""])
manger.getmot()
manger.ajouterant("macher")
manger.getmot()
manger.modifierant("macher", "masticoter")
manger.getmot()
manger.retirerant("masticoter")
manger.getmot()
dictionaire = Dico(manger)
dictionaire.insererMot(boire)
print(dictionaire.nbrelt())
pprint(dictionaire.lesmots)
dictionaire.chercherMot(boire)
dictionaire.modifierMot(manger, "mange")
pprint(dictionaire.lesmots)
dictionaire.supprimerMot(boire)
dictionaire.insererMot(boire)
dictionaire.insererMot(manger)
dictionaire.insererMot(boire)
pprint(dictionaire.lesmots)
print(dictionaire.nbrelt())


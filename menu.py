from time import sleep
from tkinter import*
from tkinter import ttk, Spinbox
from turtle import*
from BibioDic import *
import json 
from pprint import *
#le fonctions externes
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
def tef():
    print("test affichage ",test1)

def donothing():
    print("je ne sert a rien ")
def ecouteurtype(event):
    print("hello word")
    if 1:
        action()
def addwordtodic():
    #ajouter un mot dans le dictionaire  
    with open(fichier,"a") as f:
         dico.insererMot(mboire)
         json.dump(dico.getdico(),f)    
    pprint(dico.getdico())
    test1.mot.insert(4,dico.getdico().items()[2][1])

def addword():
    #fonction a appele sur le bouton et quiter la fenetre
    nw=appdic(200,200)
    nw.addnewwordtoapp()
    nw.lancer()


def action():
    test1.search.delete(0,20)
class appdic(Tk):
    def __init__(self, longueur, hauteur):
        self.root = Tk()
        #self.initialiser(longueur, hauteur)
        self.root.configure(bg="red")
        self.h = hauteur
        self.l = longueur
    def addnewwordtoapp(self):
        x = str("")
        Label(self.root,text="entrez votre mot",bg="red").pack(side=TOP)
        self.nom=Entry(self.root)
        self.nom.pack()
        print(self.nom.get())
        Label(self.root,text="entrez synonyme ",bg="red").pack(side=TOP)
        Entry(self.root).pack()
        Label(self.root,text="entrez homonyme",bg="red").pack(side=TOP)
        Entry(self.root).pack()
        Label(self.root,text="entrez antonyme",bg="red").pack(side=TOP)
        Entry(self.root).pack()
        Label(self.root,text="entrez etymologie",bg="red").pack(side=TOP)
        Entry(self.root).pack()
        Button(self.root,text="envoyez",bg="green",command=tef).pack()
        Button(self.root,text="annule",bg="green",command=donothing).pack()
    def initialiser(self,l, h):
        self.root.title("MON DICTIONAIRE")
        self.root.resizable(width=False, height=False)
        self.root.geometry("{}x{}+0+0".format( h,l))
        f=Frame(self.root,bg="green",width=400 ,height=50)
        menus=Frame(self.root,bg="yellow",width=120 ,height=300)
        affiche=Text(self.root,bg="blue",width=400 ,height=150)
        mots=Frame(self.root,width=280,bg="pink" ,height=300)
        self.mot=Listbox(mots,width=280,bg="pink" ,height=300)
        f.pack()
        menus.pack_configure(anchor=NW)
        Label(menus,text="search word",font="10",bg="yellow").place(relx=0.05,rely=0.015)
        self.search=Entry(menus,text="search word",width=19,justify="center",validatecommand=donothing)
        # search.delete(0,30)
        self.search.bind("<Button-1>", ecouteurtype)
        self.search.place(relx=0,rely=0.10)
        self.search.insert(1,"tape word here")
        
        btnaddword = Button(menus,bg="red",text="add new word",command=addword).place(relx=0.09,rely=0.20)
        ch= ttk.Combobox(menus,state="readonly", width=11, values=("signification","etymologie","homonyme", "synonime", "antonyme"))
        ch.place(relx=0.09,rely=0.35)
        ch.set("etymologie")
        btnadd=Button(menus,bg="green",text="add ",width=11).place(relx=0.09,rely=0.50)
        btnmov=Button(menus,bg="green",text="move ",width=11).place(relx=0.09,rely=0.65)
        btnset=Button(menus,bg="green",text="set ",width=11).place(relx=0.09,rely=0.80)
        mots.place(relx=0.3,rely=0.1)
        self.mot.place(relx=0,rely=0)
        affiche.pack_configure(anchor="s")
        Label(f,text="DICTIONAIRE MADE BY PYTHON",bg="green",foreground="red",font="14").place(relx=0.19,rely=0.25)
        self.mot.insert(1,"      kevin")
        print("test dico")
        i=1
        for (k,v) in dico.getdico().items():
            print(k)
            self.mot.insert(i,str("      ")+k)
            i=i+1
        print("fin test dico")
        
        
    def addMenu(self):
            # creons un menu nomme bar de menu que lon mettra dans notre fenetre root
        self.menu = Menu(self.root, bg="red")
        # dans ce menu creyons ces item nome filemenu
        self.filemenu = Menu(self.root, tearoff=0)
        #
        self.filemenu.add_command(label="New", command=donothing)
        self.filemenu.add_command(label="Open", command=donothing)
        self.filemenu.add_command(label="Save", command=donothing)
        self.filemenu.add_command(label="Save as...", command=donothing)
        self.filemenu.add_command(label="Close", command=self.root.quit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.winfo_exists)
        self.menu.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = Menu(self.menu, tearoff=0)
        self.editmenu.add_command(label="Undo", command=donothing)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut", command=donothing)
        self.editmenu.add_command(label="Copy", command=donothing)
        self.editmenu.add_command(label="Delete", command=donothing)
        self.editmenu.add_command(label="Paste", command=donothing)
        self.editmenu.add_command(label="Select All", command=donothing)
        self.editmenu.add_command(label="Send", command=donothing)
        self.menu.add_cascade(label="Edit", menu=self.editmenu)

        self.option = Menu(self.menu, tearoff=0)
        self.option.add_command(label="Agrandir", command=donothing)
        self.option.add_command(label="Send", command=donothing)
        self.option.add_command(label="Debuger", command=donothing)
        self.menu.add_cascade(label="Option", menu=self.option)

        self.helpmenu = Menu(self.menu, tearoff=0)
        self.helpmenu.add_command(label="help index", command=donothing)
        self.helpmenu.add_command(label="About...", command=donothing)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.root.config(menu=self.menu)

    def lancer(self):
        self.root.mainloop()

test1 = appdic(500,400)
test1.initialiser(500, 400)
test1.addMenu()
test1.lancer()

class MOT():
    def __init__(self,nom,syn,ant,ety,homo):
        self.nom = nom
        self.synonymes = syn
        self.antonymes = ant
        self.etymologie = ety
        self.homonyme = homo
    def getMOT(self):
        print([self.nom, self.synonymes, self.etymologie, self.antonymes, self.homonyme])
        return [self.nom, self.synonymes, self.etymologie, self.antonymes, self.homonyme]

class DICMOT(MOT):
    def __init__(self,MOT):
        pass

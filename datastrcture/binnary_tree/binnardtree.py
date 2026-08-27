class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None


racine = Noeud(10)

racine.gauche = Noeud(5)
racine.droite = Noeud(15)
racine.gauche.gauche = Noeud(2)
racine.gauche.droite = Noeud(7)
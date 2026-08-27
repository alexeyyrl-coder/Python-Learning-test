class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None


a = Noeud(10)
b = Noeud(20)
c = Noeud(30)

a.suivant = b
b.suivant = c

print(a.valeur)
print(a.suivant.valeur)
print(a.suivant.suivant.valeur)

actuel = a

while actuel is not None:
    print(actuel.valeur)
    actuel = actuel.suivant

text = input("entrer une chaind de forme (email-pseudo-motdepass)\n").replace("-", " ").split()
print(text)

# replace("-", " ") remplace tous les - par des espaces.
# split() découpe ensuite la chaîne sur les espaces.

import re

ttext = input("Entrer une chaine : ")

ttext = re.split(r"[- ]+", ttext)

print(ttext)

# ici on utilise le re.split
# r"..." : le r veut dire raw string ("chaîne brute"). Il sert surtout quand il y a des \, par exemple \s, \d, etc. Avec r"[- ]+", il n'est pas vraiment nécessaire, mais c'est une bonne habitude avec les regex.
# [- ] : ça veut dire un caractère parmi ceux entre crochets. Ici :
# -
# ou un espace " "
# + : ça veut dire "une ou plusieurs fois".
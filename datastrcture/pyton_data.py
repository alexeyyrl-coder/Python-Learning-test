# Liste
nombres = [10, 20, 30]

# Tuple
position = (10, 20)

# Dictionnaire / hash table
personne = {"nom": "Bob", "age": 20}

# Set
nombres_uniques = {1, 2, 3}

# Pile
pile = []
pile.append(10)
pile.append(20)
dernier = pile.pop()

# File
from collections import deque

file = deque()
file.append("A")
file.append("B")
premier = file.popleft()

count = 0
total_player = 0
online_player = ["Arcade", "jakcruzed", "miramax", "kaldariuss"]
print(online_player)
print(online_player[0])
print(online_player[len(online_player) - 1])

# modifier un valeur
online_player[0] = "L le Arcade"
print(online_player)

# ajouter entre
online_player.insert(2, "L gamer") 
print(online_player)

# modifier deux valeur
online_player[2:4] = ["kouille magiek", "Skibidy six seven"]
print(online_player)
print(online_player[len(online_player) - 2])

# ajouter des valeur
online_player.append("Gamur123")
online_player.extend(["gogbaguss", "gugussoss"])
print(online_player)

total_player = len(online_player)

while( count < total_player):
    print(online_player[count])
    count += 1

# supprimer la liste
del online_player[7]
online_player.pop(6)

online_player.remove("jakcruzed")

print(online_player)

online_player.clear()
print(online_player)


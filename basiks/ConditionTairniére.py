import random

wallet = random.randint(2000, 8000)
computer_pric = random.randint(1000, 6000)

print("vous avez " + str(wallet))
print("Le pc coutent " + str(computer_pric))

text = ("L'achat est possible", "L'achat est impossible")[computer_pric >= wallet]
print(text)

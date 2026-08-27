import statistics
import random

notes = [
    0, 15, 89, 
    10, 20, 35, 
    42, 85, 51
    ]

print(notes)
print(notes[0])

random.shuffle(notes)
print(notes)

resul = statistics.mean(notes)

print("la moyent de l'éléve est de {}".format(resul))
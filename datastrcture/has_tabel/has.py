personne = {
    "nom": "bob",
    "age": 20,
    "ville": "Paris"
}

print(personne["nom"])
print(personne["age"])

personne["score"] = 100

personne["age"] = 21

if "nom" in personne:
    print("Le nom existe")
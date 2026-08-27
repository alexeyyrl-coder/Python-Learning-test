
password = input("entré votre mot de pass ")
password_lengt = len(password)

if password_lengt <= 8 :
    print(" mot de pass trop court !")
elif password_lengt > 8 and password_lengt <= 12:
    print("mot de pass moyent")
else:
    print("mot de pass parfait !")

print (password_lengt)
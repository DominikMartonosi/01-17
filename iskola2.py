def létszám(a):
    if a > 1000:
        return True
    else:
        return False

while True:
    nev = input("Add meg az iskola nevét! ")
    letszam = int(input("Add meg a pontszámát! "))
    if nev == "":
        break
    if létszám(letszam):
        print(f"{nev} nagy létszámú iskola.")
    else:
        print(f"{nev} kis létszámú iskola.")  
    
    
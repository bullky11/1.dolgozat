"""def beker():
    szam=int(input("Kérlek adj meg egy páros számot"))
    while not (szam%2==0):
        szam=int(input(f"Kérlek adj meg egy páros számot amit megadtál {szam} nem az"))
    print(f"amit megadtál páros szám : {szam}")"""
list=[]
def beker_advanced():

    i=0
    k=1
    small=[]

    while i<3:
        szam = int(input(f"Kérem az {k}. Páros számot"))
        while not (szam % 2 == 0 ):
            szam = int(input(f"Ez nem Páros!Páros számot kérek"))
        small.append(szam)

        i+=1
        k+=1
        print(small)
    legkisebb(small)
def legkisebb(small):
    i=0
    legk=small[0]
    k=0
    while i<len(small):
        if small[i]<legk:
            k=i
            legk=small[i]
        i+=1
    print(f"{legk} ami a {k}.elem")





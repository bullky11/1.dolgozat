import random
def masodik_a():
    i=0
    list=[]
    while i<13:
        random_szamok = random.randint(-40, 150)
        print(random_szamok)
        list.append(random_szamok)
        i+=1
    print(list)
    ketjegyuek_szama(list)
    asd=paros_osszege(list)
    asd2=paratlan_osszeg(list)
    osszegzes(asd,asd2)

def ketjegyuek_szama(list):
    ketjegyu = []
    i=0
    while i<len(list):
        if list[i]>=10 or list[i]<=-10:
            ketjegyu.append(list[i])
        i+=1
    print(f"a Kétjegyűek száma:{len(ketjegyu)}")

def paros_osszege(list):
    parososszeg=0
    i=0
    while i<len(list):
        if list[i]%2==0:
            parososszeg+=list[i]
        i+=1
    print(f"a párosok összege: {parososszeg}")
    return parososszeg

def paratlan_osszeg(list):
    paratlanosszeg=0
    i=0
    while i<len(list):
        if list[i]%2!=0:
            paratlanosszeg+=list[i]
        i+=1
    print(f"a páratlanok összege:{paratlanosszeg}")
    return paratlanosszeg
def osszegzes(paratlanosszeg,parososszeg):
    if paratlanosszeg >parososszeg:
        print(f" {paratlanosszeg} a nagyobb")
    else:
        print(f"a {parososszeg} a nagyobb")













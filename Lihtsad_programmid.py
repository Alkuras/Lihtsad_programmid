from datetime import *
from calendar import *
from math import pi
#Ülesanne 1
tana=date.today()
print(f"Tere! Täna on {tana}")

# 27/12/2022
tana1 = tana.strftime("%d/%m/%Y")
print(tana1)
# December 27, 2022
tana2 = tana.strftime("%B %d, %Y")
print(tana2)
# 12/27/22
tana3 = tana.strftime("%m/%d/%y")
print(tana3)
# Dec-27-2022
tana4 = tana.strftime("%b-%d-%Y")
print(tana4)

päev =tana.day
kuu = tana.month
aasta = tana.year
print (f"Päaev on {päev},\nKuu on {kuu},\nAasta on {aasta}")

paevad=monthrange(2025,2)[1]
onjaanud=paevad-päev
print(f"Kuu lõpuni on jaanud {onjaanud} päevad")
aastalõpp=365 - (monthrange(2025,2)[1]+monthrange(2025,1)[1])
print(f"Aasta lõpuni on jaanud {aastalõpp} päevad")
try:

    sunnipaev=input("Sünnipäev: ") #YYYY-MM-DD
    sp=datetime.strptime(sunnipaev,"%Y-%m-%d")
    print(sp)
    vanus_aastades=tana.year-sp.year
    vanus_kuudes=vanus_aastades*12
    vanus_päevades=vanus_kuudes*30
    print(f"Vastus:Vanus aastades {vanus_aastades};Vanus kuudes {vanus_kuudes}; Vanus päevades {vanus_päevades}")
except:
    print("Sa pead YYYY-MM-DD format kasutada sisestamisel")
#Ülesanne 2
print("a=3 + 8 / (4 - 2) * 4")
a=3 + 8 / (4 - 2) * 4
print(a)
print("a=(3 + 8) / (4 - 2) * 4")
a=(3 + 8) / (4 - 2) * 4
print(a)
print("a=(3 + 8) / 4 - 2 * 4")
a=(3 + 8) / 4 - 2 * 4
print(a)
print("a=3 + 8 / 4 - 2 * 4")
a=3 + 8 / (4 - 2) * 4
print(a)
#Ülessanne 3
#==, !=, <,>,<=,>=


try:
    R=float(input("Sisesta R, kus R on ringi raadius:" ))
    if R<=0:
        print("Nulluga ja neg. arvudega ei ole mõtte töötada!")
    else:
        D=float( R*2)
        Sr=float(round( pi*R**2,1))
        Cr=float(round(2*pi*R,1))
        Sru=float(D*D)
        Pru=float(4*D)
        print(f"Ruudu pindala on {Pru}.\n Ruudu ümbermõõt on {Sru}.\n Ringi pindala on {Cr}. \nRingi ümbermõõt on {Sr}.")
except: 
    print("Sisesta ainult arvud!!!")

#Ülesanne 4
coin =float(25.75)
planet =float(6378000000)
planetC =2*pi*planet
coins_to_planet =float(round(planetC/coin,2))
print(f"Oleks vaja {coins_to_planet} münte.")

#Ülesanne 5
a = "kill-koll " .capitalize()
b = "killadi-koll " .capitalize()

print(2*a,b,2*a,b,4*a)
#Ülesanne 6
rong = """Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.""".upper()
print(rong)
#Ülesanne 7 
a = int(input("Sisenda ristküüliku lähiskülg 1. :"))
b = int(input("Sisenda ristküüliku lähiskülg 2. :"))
S = a*b 
P = 2*(a+b)
print(f"Ristküliku pindala on: {S} \n Ristküüliku ümbermõõt on: {P}")
#Ülesanne 8
kütus = int(input("Sisesta tangitud kütuse kogus liitris:"))
läbitud = int(input("Sisesta läbitud kilomeetrid:"))
kulu = läbitud/kütus
kulu100 = kulu*100
print(kulu100)
#Ülesanne 9
kiirus =float(29.9)
kaugus =int(input("Palju minutid sõidab:"))
k=kiirus/kaugus
print(k)
#Ülesanne 10
minutid_kasutajalt=int(input("aeg minutides:"))
tunnid=minutid_kasutajalt//60
minutid=minutid_kasutajalt%60
print(f"{tunnid}:{minutid}".center(20,"*"))
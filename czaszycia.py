"""
Autor: id3at
Program podaje czas zycia w sekundach minutach i dniach itd

"""

import datetime

IMIĘ = input("Podaje swoje imie: ")
while True:
    try:
        ROK = int(input("Podaj rok, swoich narodzin:"))
        MIESIAC = int(input("Podaj  miesiac, swoich narodzin:"))
        while True:
            if MIESIAC > 12:
                MIESIAC = int(input("Podaj  miesiac, swoich narodzin:"))
            else:
                break

        DZIEN = int(input("Podaj dzien, swoich narodzin:"))
        while True:
            if DZIEN > 31:
                DZIEN = int(input("Podaj dzien, swoich narodzin:"))
            else:
                break

        break

    except:
        print("Musisz wprowadzić odpowiedź za pomocą cyfr, zacznijmy od początku")

AKTUALNYCZAS = datetime.datetime.today()
DATANARODZIN = datetime.datetime(ROK, MIESIAC, DZIEN)
Wiek = AKTUALNYCZAS.year-DATANARODZIN.year

kiedysto = 100 + DATANARODZIN.year


Wiekdelta = AKTUALNYCZAS - DATANARODZIN
sek = Wiekdelta.total_seconds()
min = sek/60
godziny = min/60
c = (f"""\n Witaj {IMIĘ} !! \n  Masz już: {Wiek} lat. 
A to znaczy, że przeżyles już {Wiekdelta.days} dni, 
a to jest {int(sek)} sekund,
a to jest {int(min)} minut, 
a to jest {int(godziny)} godzin""")
print(c)
d = (f"\n 100 lat osiagniesz w roku:, {kiedysto}")
print(d)
with open("czaszycia.txt", "a") as t:
    t.write(c)
    t.write(d)

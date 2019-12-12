"""
Autor: Tomasz Głuc
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
wiekmies = (AKTUALNYCZAS.year - DATANARODZIN.year) * 12 + (AKTUALNYCZAS.month - DATANARODZIN.month)

kiedysto = 100 + DATANARODZIN.year


Wiekdelta = AKTUALNYCZAS - DATANARODZIN
sek = Wiekdelta.total_seconds()
min = sek/60
godziny = min/60
c = (f"""\n Witaj {IMIĘ} !! \n
Jest: {AKTUALNYCZAS: %A, %d, %B, %Y}.
Masz już: {Wiek} lat i {AKTUALNYCZAS.month - DATANARODZIN.month} miesiecy.
A to znaczy, że przeżyles już {wiekmies:,} miesiecy
a to jest {Wiekdelta.days:,} dni,
a to jest {int(godziny):,} godzin,
a to jest {int(min):,} minut,
a to jest {int(sek):,} sekund.
100 lat osiagniesz w roku:, {kiedysto}""")
print(c)
with open("czaszycia.txt", "a") as t:
    t.write(c)

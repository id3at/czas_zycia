"""
Autor id3at
Program. Twój cza zycia
"""

import datetime

while True:
    try:
        rok = int(input("Podaj rok, swoich narodzin:"))
        miesiac = int(input("Podaj  miesiac, swoich narodzin:"))
        while True:
            if miesiac > 12:
                miesiac = int(input("Podaj  miesiac, swoich narodzin:"))
            else:
                break
        dzien = int(input("Podaj dzien, swoich narodzin:"))
        while True:
            if dzien > 31:
                dzien = int(input("Podaj dzien, swoich narodzin:"))
            else:
                break
        break
    except:
        print("Musisz wprowadzić odpowiedź za pomocą cyfr, zacznijmy od początku")


def dat_uro(rok, miesiac, dzien):

    """
    Funkja zliczajaca czas zycia
    """
    akczas = datetime.datetime.today()
    urodz = datetime.datetime(rok, miesiac, dzien)
    wiekmies = (akczas.year - urodz.year) * 12 + (akczas.month - urodz.month)
    wiekdni = akczas - urodz
    sek = wiekdni.total_seconds()
    minuty = sek / 60
    godziny = minuty / 60

    return f'''Masz już: {akczas.year-urodz.year} lat i {akczas.month - urodz.month} miesiecy.
A to jest {wiekmies} miesiecy.
A to jest {wiekdni.days} dni.
A to jest {int(godziny)} godzin
A to jest {int(minuty)} minut.
A to jest {int(sek)} sekund'''

with open('czaszycia.txt', 'a')as t:
    t.write(dat_uro(rok, miesiac, dzien))
print(dat_uro(rok, miesiac, dzien))

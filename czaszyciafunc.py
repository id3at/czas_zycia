"""
Autor: Tomasz Głuc
Program podaje czas zycia w sekundach minutach i dniach itd
"""

import datetime

def czaszycia(IMIE="Tomasz", ROK=1983, MIESIAC=5, DZIEN=28):

    AKTUALNYCZAS = datetime.datetime.today()
    DATANARODZIN = datetime.datetime(ROK, MIESIAC, DZIEN)
    urojony = datetime.datetime((AKTUALNYCZAS.year + 1), MIESIAC, DZIEN)
    Wiek = AKTUALNYCZAS.year - DATANARODZIN.year
    mies = AKTUALNYCZAS.month - DATANARODZIN.month
    kiedysto = 100 + DATANARODZIN.year
    Wiekdelta = AKTUALNYCZAS - DATANARODZIN
    sek = Wiekdelta.total_seconds()
    min = sek / 60
    godziny = min / 60
    przyszleur = urojony - AKTUALNYCZAS

    if mies < 0:
        mies = 12 + int(mies)
        Wiek = int(AKTUALNYCZAS.year - DATANARODZIN.year) - 1

    wiekmies = (Wiek) * 12 + (mies)

    c = (f"""\n Witaj {IMIE} !! \n
    Jest: {AKTUALNYCZAS: %A, %d, %B, %Y}.
    Masz już: {Wiek} lat i {mies} miesiecy.
    A to znaczy, że przeżyles już {wiekmies:,} miesiecy
    a to jest {Wiekdelta.days // 7:,} tygodni,
    a to jest {Wiekdelta.days:,} dni,
    a to jest {int(godziny):,} godzin,
    a to jest {int(min):,} minut,
    a to jest {int(sek):,} sekund.
    100 lat osiagniesz w roku:, {kiedysto}
    Urodziny obchodzisz za {int(przyszleur.days)} dni""")
    return c
    # with open("czaszycia.txt", "a") as t:
    #     t.write(c)


IMIE = input("Podaje swoje imie: ")
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

    except ValueError:
        print("Musisz wprowadzić odpowiedź za pomocą cyfr, zacznijmy od początku")
print(czaszycia(IMIE, ROK, MIESIAC, DZIEN))

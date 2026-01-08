import random
from collections import Counter

def rzut_kosci():
    return [random.randint(1, 6) for _ in range(5)]

def sprawdz_uklad(kosci):
    kosci.sort()
    licznik = Counter(kosci)
    ilosci = sorted(licznik.values(), reverse=True)

    # STRITY
    if kosci == [1, 2, 3, 4, 5]:
        return ("Mały Strit", 5, 5)
    if kosci == [2, 3, 4, 5, 6]:
        return ("Duży Strit", 6, 6)

    # POKER
    if ilosci == [5]:
        v = kosci[0]
        return ("Poker", 8, v)

    # KARETA
    if ilosci == [4, 1]:
        v = licznik.most_common(1)[0][0]
        return ("Kareta", 7, v)

    # FULL
    if ilosci == [3, 2]:
        v = licznik.most_common(1)[0][0]
        return ("Full", 6, v)

    # TRÓJKA
    if ilosci == [3, 1, 1]:
        v = licznik.most_common(1)[0][0]
        return ("Trójka", 3, v)

    # DWIE PARY
    if ilosci == [2, 2, 1]:
        pary = [k for k, v in licznik.items() if v == 2]
        return ("Dwie Pary", 2, max(pary))

    # PARA
    if ilosci == [2, 1, 1, 1]:
        v = licznik.most_common(1)[0][0]
        return ("Para", 1, v)

    # NIC
    return ("Nic", 0, max(kosci))

# --- GRA ---
while True:
    print("\nTwój rzut:")
    gracz = rzut_kosci()
    print("Wynik rzutu:", gracz)
    n_g, s_g, w_g = sprawdz_uklad(gracz)
    print("Twój układ:", n_g)

    print("\nKomputer rzut:")
    komp = rzut_kosci()
    print("Wynik rzutu:", komp)
    n_k, s_k, w_k = sprawdz_uklad(komp)
    print("Układ komputera:", n_k)

    print("\nWynik gry:")
    if (s_g, w_g) > (s_k, w_k):
        print("Wygrałeś!")
    elif (s_g, w_g) < (s_k, w_k):
        print("Przegrałeś")
    else:
        print("Remis!")

    if input("\nGrasz dalej? (t/n): ").lower() != "t":
        print("Koniec gry")
        break

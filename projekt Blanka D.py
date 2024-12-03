import math
import matplotlib.pyplot as plt

def wymagana_predkosc_pozioma(l, H):
    g = 9.81
    if H <= 0 or l <= 0:
        raise ValueError("Odległość i wysokość muszą być dodatnie.")
    return math.sqrt(2 * g * H)

def wymagany_kat_wyrzutu(v0, l, H):
    g = 9.81
    if v0 <= 0 or l <= 0 or H < 0:
        raise ValueError("Dane wejściowe muszą być dodatnie.")
    delta = v0 ** 4 - g * (g * l ** 2 + 2 * H * v0 ** 2)
    if delta < 0:
        raise ValueError("Nie można obliczyć kąta dla podanych danych.")
    return math.degrees(math.atan((v0 ** 2 + math.sqrt(delta)) / (g * l)))

def wykres_dla_cial_niebieskich(v0, l, H):
    g_values = {
        "Merkury": 3.7,
        "Ziemia": 9.81,
        "Księżyc": 1.62,
        "Mars": 3.71,
        "Ganimedes": 1.428,
        "Ceres": 0.27
    }
    angles = {}
    for body, g in g_values.items():
        delta = v0 ** 4 - g * (g * l ** 2 + 2 * H * v0 ** 2)
        if delta < 0:
            angles[body] = 0
        else:
            angles[body] = math.degrees(math.atan((v0 ** 2 + math.sqrt(delta)) / (g * l)))

    plt.bar(angles.keys(), angles.values())
    plt.xlabel('Ciała niebieskie')
    plt.ylabel('Kąt wyrzutu (°)')
    plt.title('Kąt wyrzutu dla różnych ciał niebieskich')
    plt.show()

def main():
    try:
        choice = int(input("Wybierz opcję (1 - prędkość pozioma, 2 - kąt wyrzutu, 3 - wykres): "))
        if choice == 1:
            l = float(input("Podaj odległość od linii wyrzutu do środka koła (m): "))
            H = float(input("Podaj wysokość wyrzutu rzutu (m): "))
            print(f"Wymagana prędkość pozioma: {wymagana_predkosc_pozioma(l, H):.2f} m/s")
        elif choice == 2:
            v0 = float(input("Podaj prędkość początkową (m/s): "))
            l = float(input("Podaj odległość od linii wyrzutu do środka koła (m): "))
            H = float(input("Podaj wysokość wyrzutu rzutu (m): "))
            print(f"Kąt wyrzutu: {wymagany_kat_wyrzutu(v0, l, H):.2f}°")
        elif choice == 3:
            v0 = float(input("Podaj prędkość początkową (m/s): "))
            l = float(input("Podaj odległość od linii wyrzutu do środka koła (m): "))
            H = float(input("Podaj wysokość wyrzutu rzutu (m): "))
            wykres_dla_cial_niebieskich(v0, l, H)
        else:
            print("Nieprawidłowy wybór. Wybierz 1, 2 lub 3.")
    except ValueError:
        print("Błąd: Wprowadzono nieprawidłową wartość. Upewnij się, że podajesz liczby.")

if __name__ == "__main__":
    main()

# Opgave 1:
# Maak een tekstbestand met de naam, de geboortedatum en het telefoonnummer van je vrienden.

def create_friends_file():
    with open('Friends.txt', 'w') as f:
        f.write("Kees, 25-10-1995, 0612345678\n")
        f.write("Amber, 30-11-1990, 0612345678\n")
        f.write("Bart, 28-12-1992, 0612345678\n")
        f.write("Johan, 27-01-1993, 0612345678\n")
        f.write("Eva, 26-02-1994, 0612345678\n")

# Opgave 2: Maak een programma waarbij je de naam van een vriend invoert en het programma de gegevens van die vriend
# afdrukt met behulp van het tekstbestand dat je in opgave 1 hebt gemaakt.

def get_friend(name):
    with open('Friends.txt', 'r') as f:
        for line in f:
            if name in line:
                return line
    return None


# Opgave 3:
# Maak een programma waarbij je de naam van een vriend invoert en het programma de gegevens van die vriend


def insert(naam, geboortedatum, telefoonnummer):
    with open('Friends.txt', 'a') as f:
        f.write(f"{naam}, {geboortedatum}, {telefoonnummer}\n")


if __name__ == '__main__':
    running = True
    while running:
        create_friends_file()
        naam = input("Voer de naam van een vriend in: ")
        vriend = get_friend(naam)
        if vriend:
            print(vriend)
        else:
            print("Vriend niet gevonden.")
            geboortedatum = input("Voer de geboortedatum van de vriend in: ")
            telefoonnummer = input("Voer het telefoonnummer van de vriend in: ")
            insert(naam, geboortedatum, telefoonnummer)
            print("Vriend toegevoegd.")
        running = input("Wil je doorgaan? (y/n): ") == 'y'
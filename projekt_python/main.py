import random


class player:
    def __init__(self, name, role, weapon):
        self.name = name
        self.role = role
        self.weapon = weapon


class enemy:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon


thief = enemy
enemy.name = 'thief'

p1 = player
imie = input('Podaj imię: ')
imie = imie.capitalize()
imie = str(imie)
p1.name = imie
while True:
    character = input('wybierz klasę postaci (numer): \n1. wojownik \n2. mag \n3. strzelec ')
    if int(character) == 1:
        character = 'wojownik'
        p1.role = 'wojownik'
        break
    elif character == 2:
        character = 'mag'
        p1.role = 'mag'
        break
    elif character == 3:
        character = 'strzelec'
        p1.role = 'strzelec'
        break
    else:
        print('Wybierz prawidłową klasę')

print(f'Witaj {p1.role}u {p1.name}! ')

bron_wojownika_1 = {
    'nazwa': 'Excalibur',
    'sila': 3,
    'obrona': 6,
}

bron_maga_1 = {
    'nazwa': 'Wielka magiczna rozdzka',
    'sila': 6,
    'obrona': 2,
}

bron_strzelca_1 = {
    'nazwa': 'Pistolet czarnobrodego',
    'sila': 4,
    'obrona': 1,
}

bron_przeciwnika_1 = {
    'nazwa': 'scyzoryk',
    'sila': 2,
    'obrona': 1
}

if character == 'wojownik':
    p1.weapon = bron_wojownika_1
elif character == 'mag':
    p1.weapon = bron_maga_1
else:
    p1.weapon = bron_strzelca_1

thief.weapon = bron_przeciwnika_1

wyniki = open("wyniki.txt", 'w+')
menu = int(input('Czy chcesz zagrać w grę? \n 1. Tak \n 2. Wyjdź \n 3. Zobacz wyniki'))
points = 0

if menu == 1:
    print('Witaj w jaskiniach! Oby los się do Ciebie uśmiechnął!')


    def zwiedzanie_jaskin(points, gamer, enemy):
        zycie = 1
        tunel_z_przeciwnikiem = random.randint(1, 3)
        tunel = int(input('Który tunel wybierasz? 1-3 (numer)'))
        while zycie > 0:
            if tunel != tunel_z_przeciwnikiem:
                points += 1
            else:
                decyzja = int(input('Napotkałeś przeciwnika! Musisz walczyć (1) albo uciekać(2) !'))
                if decyzja == 2:
                    print(f"Postanowiłeś uciec z kopalni z wynikiem {points}!")
                    return points
                else:
                    decyzja_walka = int(input('Przeciwnik atakuje! Uderzasz (1) czy bronisz się (2)?'))
                    if decyzja_walka == 1:
                        if character == 1:
                            if bron_wojownika_1['sila'] > bron_przeciwnika_1['obrona']:
                                print('Gratulacje! Pokonałeś przeciwnika')
                                points += 1
                                continue
                            else:
                                print('Niestety nie udało się pokonać przeciwnika. Jesteś zmuszony opuścić jaskinię.')
                                return points
                        elif character == 2:
                            if bron_maga_1['sila'] > bron_przeciwnika_1['obrona']:
                                print('Gratulacje! Pokonałeś przeciwnika')
                                points += 1
                            else:
                                print('Niestety nie udało się pokonać przeciwnika. Jesteś zmuszony opuścić jaskinię.')
                                return points
                        else:
                            if bron_strzelca_1['sila'] > bron_przeciwnika_1['obrona']:
                                print('Gratulacje! Pokonałeś przeciwnika')
                                points += 1
                            else:
                                print('Niestety nie udało się pokonać przeciwnika. Jesteś zmuszony opuścić jaskinię.')
                                return points
                    else:
                        print('Udało ci się obronić przed ciosem przeciwnika!')

elif menu == 2:
    print('Do zobaczenia ponownie!')
    wyniki.close()

elif menu == 3:
    wyniki.read()
    wyniki.close()

zwiedzanie_jaskin(points, p1, thief)

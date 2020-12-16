prihlasovaci_udaje = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
         red, purple, yellow and gray beds of the Wasatch 
         Formation. Eroded portions of these horizontal 
         beds slope gradually upward from the valley floor 
         and steepen abruptly. Overlying them and extending 
         to the top of the butte are the much steeper 
         buff-to-white beds of the Green River Formation, 
         which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
         a portion of the largest deposit of freshwater fish 
         fossils in the world. The richest fossil fish deposits 
         are found in multiple limestone layers, which lie some 
         100 feet below the top of the butte. The fossils 
         represent several varieties of perch, as well as 
         other freshwater genera and herring similar to those 
         in modern oceans. Other fish such as paddlefish, 
         garpike and stingray are also present.'''
         ]

# přivitání uživatele, ad) 1
print('-' * 80)
print('Vítejte v naší aplikaci. Prosím, přihlašte se...')

# vyžádání přihlašovacích údajů od uživatele, ad) 2
uzivatelske_jmeno = str(input('Zadejte uživatelské jméno: '))
heslo = str(input('Zadejte heslo: '))

# zjištění, zda zadané údaje odpovídají někomu z registrovaných uživatelů, ad) 3
while prihlasovaci_udaje.get(uzivatelske_jmeno) != heslo:

    if prihlasovaci_udaje.get(uzivatelske_jmeno) != heslo:
        print('Zadané přihlašovací údaje jsou chybné. Zkuste to znovu...')

        uzivatelske_jmeno = str(input('Zadejte uživatelské jméno: '))
        heslo = str(input('Zadejte heslo: '))

    else:
        continue

print('-' * 80)

number_of_texts = len(TEXTS)
print(f'Máme celkem {number_of_texts} texty k analýze')

# program nechá uživatele vybrat mezi třemi texty, ad) 4
vyber_textu = int(input(f'Vyberte číslo textu 1-{number_of_texts}, který chcete podrobit analýze: '))

while vyber_textu > number_of_texts or vyber_textu <= 0:
    if vyber_textu > number_of_texts or vyber_textu <= 0:

        print(f'K dispozici máme pouze {number_of_texts} texty. Zkuste to znovu...')
        vyber_textu = int(input(f'Vyberte číslo textu 1-{number_of_texts}, který chcete podrobit analýze: '))

    else:
        continue

zvoleny_text = TEXTS[vyber_textu - 1]
print('')
print(f'Vybral jste následující text: \n\n{zvoleny_text}')
print('-' * 80)
print('Zde je jeho analýza...')
print('-' * 80)

# čistý list - slova očištěná od čárek, teček, mezer
cisty_list = []
for slovo in zvoleny_text.split():
    ciste_slovo = slovo.strip(',.')
    cisty_list.append(ciste_slovo)
print('')

# počet slov v textu
pocet_slov = len(cisty_list)

# vytvoření kopie čistého listu
cisty_list_kopie = cisty_list.copy()

# roztřídění "čistých" slov z "čistého listu" do kategorií
prvni_velke = []
vse_velkym = []
vse_malym = []
ciselny_string = []

while cisty_list:
    vybrane_slovo = cisty_list.pop()

    if vybrane_slovo.istitle():
        prvni_velke.append(vybrane_slovo)

    elif vybrane_slovo.isupper():
        vse_velkym.append(vybrane_slovo)

    elif vybrane_slovo.islower():
        vse_malym.append(vybrane_slovo)

    else:
        ciselny_string.append(vybrane_slovo)

# vypočteny statistiky vybraného textu, ad) 5
print(f'Celkový počet slov v textu je {pocet_slov}')
print(f'Počet slov s prvním velkým písmenem je: {len(prvni_velke)}')
print(f'Počet slov se všemi velkými písmeny je: {len(vse_velkym)}')
print(f'Počet slov se všemi malými písmeny je: {len(vse_malym)}')
print(f'Počet obsažených číselných strigů je: {len(ciselny_string)}')
print('-' * 80)

print()

# vytvoření slovníku, kde je délka jednotlivých slov jako klíč a četnost jako hodnota
cetnosti = {}

for prvky in cisty_list_kopie:
    if len(prvky) not in cetnosti:
        cetnosti[len(prvky)] = 1
    else:
        cetnosti[len(prvky)] += 1

print('Zde je zobrazení četnosti délek jednotlivých slov v textu')
print('-' * 80)

# vytvoření sloupcového grafu dle četnosti délek slov v textu, ad) 6
for k, v in cetnosti.items():
    print(k, '*' * v, v)

print('-' * 80)

# převod hodnot z listu na integer, součet všech cifer, ad) 7
ciselny_string_na_integer = [int(i) for i in ciselny_string]
print(f'Pokud sečteme všechny číselné hodnoty v textu, dostaneme číslo {sum(ciselny_string_na_integer)}')

import string
import random

## karakteret për të gjeneruar fjalëkalim
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    ## Gjatësia e fjalëkalimit nga përdoruesi
    length = int(input("Vendos gjatësinë e fjalëkalimit: "))

    ## number of character types
    alphabets_count = int(input("Vendos numerin e shkronjave ne fjalekalim: "))
    digits_count = int(input("Vendos numerin e shifrave në fjalëkalim: "))
    special_characters_count = int(input("Vendos numrin e karaktereve speciale në fjalëkalim: "))

    characters_count = alphabets_count + digits_count + special_characters_count

    ## kontrolloni gjatësinë totale me numërin e shumës së karaktereve
    ## printimi nuk është i vlefshëm nëse shuma është më e madhe se gjatësia
    if characters_count > length:
        print("Numri total i karaktereve është më i madh se gjatësia e fjalëkalimit")
        return

    ## inicializimi i fjalëkalimit
    password = []

    ## picking random alphabets
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    ## picking random digits
    for i in range(digits_count):
        password.append(random.choice(digits))

    ## picking random alphabets
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    ## nëse numri total i karaktereve është më i vogël se gjatësia e fjalëkalimit
    ## shton karaktere të rastësishme për ta bërë atë të barabartë me gjatësinë
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    random.shuffle(password)

    ## konvertimi i listës në string dhe printimi i listës
    print("".join(password))
    print("Rinor Lajçi 24/03/2022")

generate_random_password()

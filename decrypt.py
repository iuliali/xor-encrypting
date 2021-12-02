import sys


def decrypt(parola):
    l = len(parola)

    with open(nume_output, "rb") as file:
        continut = file.read().decode()
        lungime = len(continut)
        b = []
        with open(nume_input_recuperat, "a") as recuperat:
            for i in range(lungime):
                k = parola[i % l]
                recuperat.write(chr(ord(continut[i]) ^ ord(k)))


parola = sys.argv[1]
nume_output = sys.argv[2]
nume_input_recuperat = sys.argv[3]
parola_lista = [x for x in parola]
decrypt(parola_lista)

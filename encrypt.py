import sys


def encrypt(parola):
    l = len(parola)
    file = open(nume_input, "r")
    content = file.read()
    file.close()
    lungime = len(content)
    with open(nume_output, "ab") as output:
        for i in range(lungime):
            k = parola[i % l]
            output.write(bytes(chr(ord(content[i]) ^ ord(k)).encode()))


def verificare_parola(parola):
    if len(parola) < 10 or len(parola) > 15:
        print("Password must have more than 10 and less than 15 characters.")
        return 0
    if not parola.isalnum():
        print("Password must have at least one digit, one lowercase and one uppercase letter.")
        return 0
    else:
        if (True) in [x.isupper() for x in parola] and (True) in [x.islower() for x in parola] and (True) in [x.isdigit() for x in parola]:
            return 1
        else:
            print("Password must have at least one digit, one lowercase and one uppercase letter.")
            return 0


if len(sys.argv) != 4:
    print("The command must be \"python3 encrypt.py <password> input.txt output\" ")
    exit(0)
else:
    parola = sys.argv[1]
    nume_input = sys.argv[2]
    nume_output = sys.argv[3]
    parola_lista = [x for x in parola]
    if verificare_parola(parola):
        encrypt(parola_lista)
    else: exit(0)








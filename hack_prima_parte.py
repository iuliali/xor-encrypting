

def cauta():
    with open("input.txt", "rb") as input:
        contents = input.read()
        with open("output", "rb") as output:
            out = output.read()
        def xor(contents, passphrase):
            return bytes(content ^ passchr for content, passchr in zip(contents, passphrase)).decode()
        print(xor(contents,out)[0:15])

cauta()





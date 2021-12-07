f=open("output","rb")
g=open("parola.txt","w")
criptat=f.read()
f.close()
criptat=criptat[15:30]
min1=20
parolab=""
caractere="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def parolacreata_testata():
    global min1
    global parolab
    for c1 in caractere:
        for c2 in caractere:
            for c3 in caractere:
                for c4 in caractere:
                    for c5 in caractere:
                        for c6 in caractere:
                            for c7 in caractere:
                                for c8 in caractere:
                                    for c9 in caractere:
                                        for c10 in caractere:
                                            for c11 in caractere:
                                                for c12 in caractere:
                                                    for c13 in caractere:
                                                        for c14 in caractere:
                                                            for c15 in caractere:
                                                                parola=c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15
                                                                parola=parola.encode()
                                                                text=""
                                                                nrc=0
                                                                for j,k in zip(parola,criptat):
                                                                    text+=chr(j^k)
                                                                for l in text:
                                                                    if ord(l)>127:
                                                                        nrc+=1
                                                                if nrc<min1:
                                                                    min1=nrc
                                                                    parolab=parola.decode()
parolacreata_testata()
g.write(parolab)
g.close()
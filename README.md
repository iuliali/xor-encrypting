# **Numele echipei noastre: three haXORs**
<p>
  Echipa adversă: DreamTeam
  </p>
  <p>
  Parola echipei adverse: rT2w8eMZENRQWXh

</p>

<p align="center">
<b>  <img src="https://media4.giphy.com/media/l1J9RFoDzCDrkqtEc/giphy.webp?cid=ecf05e470gsglrax28ysr6clp7dg07b331q4dzo0yrdv14rs&rid=giphy.webp&ct=g" width="40" height="40" /> XOR ENCRYPTION <img src="https://media4.giphy.com/media/l1J9RFoDzCDrkqtEc/giphy.webp?cid=ecf05e470gsglrax28ysr6clp7dg07b331q4dzo0yrdv14rs&rid=giphy.webp&ct=g" width="40" height="40" />   </b>
</p>

# **CERINTA PROIECTULUI**
<i>

```

Scrieți scripturi python encrypt.py/decrypt.py care iau ca parametru în linia de comandă o cheie și un
fișier și realizează criptarea/decriptarea XOR folosind cheia dată. Programul va folosi cheia pentru a
cripta conținutul fișierului.
Exemplu:
• python encrypt parolamea2021 input.txt output
• python decrypt output parolamea2021 input_recuperat.txt
• Fișierul input.txt este mereu unul text. Fișierul output este unul binar, nu text (dar conține același
număr de caractere ca și input.txt).
Selectați o bucată de text de minim 100KB (literatură clasică de exemplu, în orice caz text lizibil în
limba română fără diacritice) și maxim 150KB în fișierul input.txt și generați fisierul output.
Nu scrieți niciunde parola folosită, aceasta trebuie să fie secretă. Nu spuneți parola și altor echipe.
Parola conține doar: litere mici, litere mari (ambele fără diacritice) și cifre. Dimensiunea parolei este
între 10 și 15 caractere.

```
</i>

# **MEMBRII ECHIPEI**


```
- Talpalariu Iulia-Georgiana  (Grupa 134)  Responsabila pentru cod si git
- Lem-Rau Dumitru-Alexandru  (Grupa 134)  Responsabil pentru testare si pagina de Readme
- Andreiana George-Leonardo  (Grupa 134)  Responsabil pentru documentatie si materiale
```


# **Materiale utilizate pentru documentare**


[WIKIPEDIA XOR_CHIPER](https://en.wikipedia.org/wiki/XOR_cipher) </br>
[TEXTUL UTILIZAT](https://ro.wikisource.org/wiki/Geniu_pustiu) </br>
[PRELUCRAREA TEXTULUI](https://www.curs-valutar-bnr.ro/inlocuire-diacritice-dintr-un-text) </br>

# **Instructiuni de utilizare**
```

Limbaj de programare utilizat -> Python


Versiunea limbajului -> 3.9.9
```

>Rularea Programului

Programul va fi rula din terminal folosind urmatoarele comenzi:
```
python3 encrypt.py <parola> input.txt output
```
```
python3 decrypt.py <parola> output input_recuperat.txt
```
<b> -> Input.txt si input_recuperat.txt sunt numele fisierelor folosite in acest program, input.txt fiind textul original, iar input_recuperat.txt fiind textul decodat. </b> </br>
<b> -> Aceste nume pot fi alese personal, dar fisierul de input trebuie creat in prealabil. </b>


# **Explicarea algoritmilor de decodare - partea a doua**

>Primul algoritm

Codul se afla in hack_prima_parte.py
Am folosit proprietatea operatiei de xor si am aflat parola facand xor intre input si output, utilizand functia pe care colegii din echipa adversa au realizat-o pentru criptare cu mici modificari. Cum stiam ca parola poate avea maxim 15 caractere, am luat doar primele 15 caractere din rezultat si le-am afisat. Daca parola avea mai putin de 15 caractere, la finalul parolei s-ar fi repetat primele caractere, iar astfel ne putem da seama de parola folosita. </b>


>Al doilea algoritm

Cel de-al doilea algoritm genereaza toate cheile posibile si le testeaza cu un sir de 15 caractere din fisierul output. </b>
Dupa aceea alege cele mai bune chei, care au cel mai mic numar de caractere decodate gresit, si le salveaza. </b>
Singurul lucru ramas este sa testam care dintre cheile alese este crea corecta, folosindu-le in algoritmul de decodare si comparand fisierul output cu fisierul input. </b>


# **Cuprins**

->Cerinta proiectului </br>
->Membrii echipei </br>
->Materialele utilizate </br>
->Instructiunile de utilizare </br>

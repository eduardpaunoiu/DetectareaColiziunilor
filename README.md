# DetectareaColiziunilor
Pentru rulare: se ruleaza fisierul main, iar fisierele de output sunt in folderul output.

Pentru inceput, am creat cateva fisiere in care se afla clasele cu care am lucrat: FiguraGeometrica, Cerc, Patrat,
Triunghi, Dreptunghi si Cadran. Initial, in clasa FiguraGeometrica aveam 3 metode abstracte pentru caclulul razei,
a coliziunilor si a semi-incluziunilor, insa ulterior mi-am dat seama ca ultimele 2 sunt la fel pentru fiecare figura
geometrica, asa ca le-am implementat direct acolo. Clasele care mostenesc FiguraGeometrica mostenesc, evident, si aceste
metode (in care pur si simplu am verificat conditiile din cerinta) si in plus, implementeaza metoda pentru calculul
razei cercului incadrator, in functie de tipul lor.
Clasa Cadran reprezinta mai degraba spatiul de lucru. Aici am inclus si o metoda pentru calculul cadranului in care se
afla un punct (va fi folosita pentru incadrarea centrului unei figuri).
Munca "mai grea" a inceput in scriptul main, unde ruleaza programul si unde am facut urmatoarele lucruri:
- folosind modulul os am initializat o lista cu numele fisierelor de intrare prin care am iterat (ca sa 
automatizez procesul de verificare a testelor);
- pentru fiecare test (fisier de intrare), citesc din fisier si initilizez obiecte in functie de tipul lor, prima linie
reprezentand intotdeauna coordonatele spatiului de lucru;
- dupa aceea, pentru fiecare din urmatoarele linii voi intializa cate o lista de date care va fi data (element cu
element) constuctorului;
- in functie de tipul primului element din acea lista, voi initializa o figura geometrica si ii voi calcula raza;
- creez fisierele de output in care voi scrie datele cerute: pentru fiecare figura cu centrul in interiorul unui
cadran calculez cu ce alte figuri intra in coliziune, ce alte figuri semi-include si in ce cadran se afla (am facut
acest lucru cu ajutorul a doua for-uri imbricate si a doua liste, in care am verificat cele doua proprietati);
- cu ajutorul unui index (care creste cu 1 la fiecare iteratie a for-ului mare) voi scrie in fisierul testindex
(index=0,9) datele mentionate anterior;
Legat de variabile si coding style, am incercat sa am toate variabilele in aceeasi limba (ca e destul de enervant sa 
le ai ba in engleza, ba in romana), si sa respect formatul PEP8 (asta a fost destul de usor, ca imi sugera PyCharm-ul
mereu spatii).

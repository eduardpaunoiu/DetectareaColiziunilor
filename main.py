from cadran import Cadran
from cerc import Cerc
from dreptunghi import Dreptunghi
from patrat import Patrat
from triunghi import Triunghi
import os

# Cu ajutorul modulului os, creez o lista cu numele fisierelor prin care voi itera.
lista_teste = os.listdir("./input")
# Retin si indexul fisierului (initial 0), care va creste cu 1 la fiecare iteratie a for-ului.
index = 0
for test in lista_teste:
    fisier_intrare = open("./input/" + test, "r")

    # Intr-o lista de intregi adaug coordonatele punctelor care delimiteaza spatiul de lucru (prima linie din fisier).
    date_cadran = [int(i) for i in fisier_intrare.readline().split()]

    # Initializez spatiul de lucru cu datele din lista
    spatiu_de_lucru = Cadran(date_cadran[0], date_cadran[1], date_cadran[2], date_cadran[3])

    # Citesc din fisier si initializez obiectele in functie de constructor. Detalii in README.
    lista_figuri = []
    for linie in fisier_intrare:
        lista = [i for i in linie.split()]
        if lista[0] == "cerc":
            c0 = Cerc(lista[1], int(lista[2]), int(lista[3]), int(lista[4]))
            lista_figuri.append(c0)
        elif lista[0] == "patrat":
            p0 = Patrat(lista[1], int(lista[2]), int(lista[3]), int(lista[4]))
            p0.calculeaza_raza()
            lista_figuri.append(p0)
        elif lista[0] == "dreptunghi":
            d0 = Dreptunghi(lista[1], int(lista[2]), int(lista[3]), int(lista[4]), int(lista[5]))
            d0.calculeaza_raza()
            lista_figuri.append(d0)
        elif lista[0] == "triunghi":
            t0 = Triunghi(lista[1], int(lista[2]), int(lista[3]), int(lista[4]), int(lista[5]), int(lista[6]))
            t0.calculeaza_raza()
            lista_figuri.append(t0)

    fisier_intrare.close()

    # Crearea fisierului de output intr-un director separat
    fisier_iesire = open("./output/test" + str(index), "w")

    # Scrierea datelor de output in fisier. Detalii in README.
    for figura_i in lista_figuri:
        coliziune = []
        semi_incluziune = []
        for figura_j in lista_figuri:
            # Sigur exista o complexitatea mai buna decat O(n^2), dar am zis sa nu ma complic.
            if figura_i.detectare_coliziune(figura_j) != "":
                coliziune.append(figura_j.id)
            if figura_i.detectare_semi_incluziune(figura_j) != "":
                semi_incluziune.append(figura_j.id)
        if spatiu_de_lucru.incadrare_figura(figura_i.coord_x, figura_i.coord_y) != "":
            fisier_iesire.write(figura_i.id + " | " + " ".join(map(str, coliziune)) + " | " + " ".join(
                map(str, semi_incluziune)) + " | " + spatiu_de_lucru.incadrare_figura(figura_i.coord_x,
                                                                                      figura_i.coord_y) + "\n")

    fisier_iesire.close()
    # Cresc index-ul cu un pentru ca voi trece la alt test.
    index += 1

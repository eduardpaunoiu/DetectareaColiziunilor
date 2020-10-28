import math


def calculeaza_distanta(x1, y1, x2, y2):
    """Calculeaza distanta dintre doua puncte A(x1,y1) si B(x2,y2)."""
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class Cadran(object):

    def __init__(self, x1, y1, x2, y2):
        """Constructorul clasei cadran, care este mai degraba spatiul de lucru."""
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def incadrare_figura(self, x, y):
        """In functie de parametrii x si y, calculez in ce cadran se afla un punct de coordonate x si y."""
        if (self.x1 + self.x2) / 2 < x < self.x2 and (self.y1 + self.y2) / 2 < y < self.y2:
            # Se afla in cadranul 1.
            return "1"
        elif self.x1 < x < (self.x1 + self.x2) / 2 and (self.y1 + self.y2) / 2 < y < self.y2:
            # Se afla in cadranul 2.
            return "2"
        elif self.x1 < x < (self.x1 + self.x2) / 2 and self.y1 < y < (self.y1 + self.y2) / 2:
            # Se afla in cadranul 3.
            return "3"
        elif (self.x1 + self.x2) / 2 < x < self.x2 and self.y1 < y < self.y2:
            # Se afla in cadranul 4.
            return "4"
        else:
            # Se afla in afara spatiului de lucru.
            return ""

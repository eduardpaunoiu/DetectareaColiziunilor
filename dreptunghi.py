from figura_geometrica import FiguraGeometrica


class Dreptunghi(FiguraGeometrica):
    name = "dreptunghi"
    raza = 0

    def __init__(self, index, x, y, l1, l2):
        """Constructorul clasei Dreptunghi"""
        self.id = index
        self.coord_x = x
        self.coord_y = y
        self.latime = l1
        self.lungime = l2

    def calculeaza_raza(self):
        """Implementez metoda pentru calculul razei cercului care inscrie dreptunghiul."""
        self.raza = max(self.latime, self.lungime) / 2

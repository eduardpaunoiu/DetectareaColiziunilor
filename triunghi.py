from figura_geometrica import FiguraGeometrica


class Triunghi(FiguraGeometrica):
    name = "triunghi"
    # Initializez raza cercului cu 0, pentru a putea fi calculata ulterior.
    raza = 0

    def __init__(self, index, x, y, l1, l2, l3):
        """Constructorul clasei triunghi."""
        self.id = index
        self.coord_x = x
        self.coord_y = y
        self.latura_1 = l1
        self.latura_2 = l2
        self.latura_3 = l3

    def calculeaza_raza(self):
        """Calculeaza raza cercului care inscrie triunghiul."""
        self.raza = max(self.latura_1, self.latura_2, self.latura_3) / 2

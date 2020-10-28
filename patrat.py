from figura_geometrica import FiguraGeometrica


class Patrat(FiguraGeometrica):
    name = "patrat"
    raza = 0

    def __init__(self, index, x, y, lat):
        """Constructorul clasei Patrat."""
        self.id = index
        self.coord_x = x
        self.coord_y = y
        self.latura = lat

    def calculeaza_raza(self):
        """Cacluleaza raza cercului care inscrie patratul."""
        self.raza = self.latura / 2

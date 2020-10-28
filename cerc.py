from figura_geometrica import FiguraGeometrica


class Cerc(FiguraGeometrica):
    name = "cerc"

    def __init__(self, index, x, y, r):
        """Constructorul clasei cerc."""
        self.id = index
        self.coord_x = x
        self.coord_y = y
        self.raza = r

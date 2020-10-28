from cadran import calculeaza_distanta


class FiguraGeometrica(object):
    def calculeaza_raza(self):
        """ Metoda (abstracta) pentru a calcula raza cercului care inscrie o figura. """
        pass

    # Metodele pentru detectarea coliziunilor si a semi-incluziunilor sunt la fel pentru fiecare forma geometrica.
    def detectare_coliziune(self, alta_figura):
        """ Metoda pentru a calcula daca exista coliziuni intre figurile geometrice. """

        # Am nevoie de aceasta conditie in main.
        if self == alta_figura:
            return ""

        if calculeaza_distanta(self.coord_x, self.coord_y,
                               alta_figura.coord_x, alta_figura.coord_y) <= self.raza + alta_figura.raza:
            # Dupa ce verific conditia de coliziune, returnez id-ul figurii.
            return alta_figura.id
        else:
            return ""

    def detectare_semi_incluziune(self, alta_figura):
        """ Metoda pentru a detecta daca o figura (self) semi-include alta figura."""
        if self.detectare_coliziune(alta_figura) and self.raza > alta_figura.raza:
            # Dupa ce verific conditia de semi-incluziune, voi returna id-ul figurii semi-incluse de self.
            return alta_figura.id
        else:
            # Altfel returnez stringul null.
            return ""

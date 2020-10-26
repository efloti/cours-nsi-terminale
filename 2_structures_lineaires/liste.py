class Cellule:
    """Fondation du type ListeSimple"""
    def __init__(self, valeur, suivante=None):
        self.valeur = valeur
        self._suivante = suivante  # éviter de jouer avec ce pointeur...

    @property
    def suivante(self):
        return self._suivante

    def __str__(self):
        if self._suivante is None:
            return f"{self.valeur}"
        return f"{self.valeur} → {self._suivante}"


class Liste:
    """Une liste chaînée simple - utilise Cellule"""
    def __init__(self):
        """Crée une liste chaînée vide"""
        self._tete = None
        self._queue = None
        self._taille = 0

    @property
    def tete(self):
        return self._tete

    @property
    def queue(self):
        return self._queue
    
    def __len__(self):
        return self._taille

    def __str__(self):
        if self._tete is None:
            return "None"
        else:
            return str(self._tete)

    def inserer_apres(self, valeur, cellule=None):
        """
        Insère valeur juste après cellule. Si cellule n'est pas précisée, l'insertion se fait en tête.
        """
        self._taille += 1
        cell = Cellule(valeur)

        # insertion en tête
        if cellule is None:
            cell._suivante = self._tete
            self._tete = cell
            # si la cellule est seule, elle est aussi la queue!
            if self._tete._suivante is None:
                self._queue = cell
            return

        # insertion queue
        if cellule._suivante is None:
            cellule._suivante = cell
            self._queue = cell
            return

        # insertion ailleurs
        cell._suivante = cellule._suivante
        cellule._suivante = cell

    def supprimer_apres(self, cellule=None):
        """
        Supprime et renvoie la valeur située dans la cellule qui suit celle fournie. Si aucune cellule n'est
        précisée, supprimer la cellule de tête.
        """
        # la liste est vide ou cellule n'a pas de suivante
        if self._tete is None or (cellule is not None and cellule._suivante is None):
            raise IndexError("Liste vide!")

        self._taille -= 1
        # supprimer en tête
        if cellule is None:
            v = self.tete.valeur
            if self._tete._suivante is None:
                self._queue = None
            self._tete = self.tete._suivante
            return v

        # ailleurs
        v = cellule._suivante.valeur
        # mais peut-être la queue
        if cellule._suivante is self._queue:
            self._queue = cellule
        cellule._suivante = cellule._suivante._suivante
        # penser à renvoyer la valeur effectivement supprimée
        return v


if __name__ == "__main__":
    test = Cellule(1, Cellule(2))
    assert str(test) == "1 → 2"
    l = Liste()
    assert str(l) == "None"
    l.inserer_apres(1)
    l.inserer_apres(2)
    assert str(l) == "2 → 1"
    assert len(l) == 2
    assert l.tete.valeur == 2
    assert l.tete.suivante.valeur == 1
    l.inserer_apres(3)
    l.supprimer_apres()
    assert l.tete.valeur == 2
    l.inserer_apres(3)
    l.supprimer_apres(l.tete)
    assert l.tete.valeur == 3 and l.tete.suivante.valeur == 1
    l.supprimer_apres(l.tete)
    assert l.queue is l.tete

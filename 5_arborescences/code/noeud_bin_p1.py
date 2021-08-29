class NoeudBin:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        # self.parent = None
        self.gauche = gauche
        self.droit = droit

    def est_double(self):
        """Renvoie True si le noeud a deux enfants exactement, False autrement."""
        return self.gauche and self.droit

    def est_feuille(self):
        """Renvoie True si le noeud n'a pas d'enfant, False autrement."""
        return not self.gauche and not self.droit

    def est_simple(self):
        """Renvoie True si le noeud n'a qu'un enfant, False autrement."""
        return self.gauche and not self.droit \
               or self.droit and not self.gauche

    def taille(self):
        """Renvoie le nombre de noeuds de l'arbre dont la racine est le noeud courant self"""
        if self.est_feuille():
            return 1
        return 1 + (self.gauche.taille() if self.gauche else 0) \
               + (self.droit.taille() if self.droit else 0)

    def hauteur(self):
        """Renvoie la hauteur de l'arbre dont la racine est le noeud courant self.
        La hauteur d'un arbre est le nombre de liens de sa plus grande branche.
        """
        if self.est_feuille():
            return 0
        return 1 + max(
            self.gauche.hauteur() if self.gauche else 0,
            self.droit.hauteur() if self.droit else 0
        )

    def est_ancetre(self, n):
        """Renvoie True si le noeud courant est un ancetre du noeud fourni en argument.
        Un noeud n1 est un ancetre d'un noeud n2 si n2 fait partie de l'arbre enraciné
        au noeud n1."""
        if self is n:
            return True
        return (self.gauche.est_ancetre(n) if self.gauche else False) or \
               (self.droit.est_ancetre(n) if self.droit else False)

    def est_descendant(self, n):
        """Renvoie True si le noeud courant est un descendant du noeud fourni en argument."""
        return n.est_ancetre(self)

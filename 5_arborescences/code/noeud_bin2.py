from noeud_bin_p2 import NoeudBin

class NoeudBin2(NoeudBin):
    def __init__(self, valeur, gauche=None, droit=None, parent=None):
        # appel du «constructeur» de NoeudBin
        super().__init__(valeur, gauche, droit)
        self.parent = parent
        # On fait pointer les enfants vers ce noeud
        if isinstance(self.gauche, NoeudBin2):
            self.gauche.parent = self
        if isinstance(self.droit, NoeudBin2):
            self.droit.parent = self
    
    def profondeur(self):
        """Renvoie la profondeur du noeud courant."""
        p = -1
        courant = self
        while courant:
            p += 1
            courant = courant.parent
        return p

    def est_ancetre(self, n):
        """Renvoie True si le noeud courant est un ancetre du noeud fourni en argument.
        Un noeud n1 est un ancêtre d'un noeud n2 si n2 fait partie de l'arbre enraciné
        au noeud n1.
        Est plus efficace que la version récursive de NoeudBin."""
        courant = n
        while courant:
            if courant is self:
                return True
            courant = courant.parent
        return False

    def occurrence(self):
        """Renvoie l'occurrence du noeud courant.
        L'occurrence de la racine est '', et si occ est l'occurrence d'un noeud,
        celle de son fils gauche est (occ + '0'), et celle de son fils droit (occ + '1')."""
        occ = ""
        courant = self
        while courant.parent:
            if courant.parent.gauche is courant:
                occ = "0" + occ
            else:
                occ = "1" + occ
            courant = courant.parent
        return occ
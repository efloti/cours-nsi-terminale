def ne_rien_faire(noeud):
    pass


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

    def est_localement_complet(self):
        """Test si l'arbre binaire enraciné au noeud courant self est localement complet.
        """
        if self.est_feuille():
            return True
        return (self.gauche.est_localement_complet() if self.gauche else False) and \
               (self.droit.est_localement_complet() if self.droit else False)

    def est_complet(self):
        """Test si l'arbre binaire enraciné au noeud courant self est complet.
        """
        h = self.hauteur()
        return self.taille() == 2 ** (h + 1) - 1

    def est_filiforme(self):
        if self.est_feuille():
            return True
        elif self.est_double():
            return False
        else:
            return self.gauche.est_filiforme() if self.gauche else self.droit.est_filiforme()

    def get_from_occ(self, occ):
        """Renvoie le noeud d'occurence donné par rapport au noeud courant self ou
        None si ce noeud n'existe pas."""
        n = self
        for c in occ:
            n = n.gauche if c == "0" else n.droit
            if not n:
                return None
        return n

    def occurrence(self, n):
        """Renvoie l'occurrence du noeud fourni en argument s'il est dans l'arbre enraciné
        au noeud courant, None autrement.
        L'occurrence de self est '', et si occ est l'occurrence d'un noeud, celle de son
        fils gauche est (occ + '0'), celle de son fils droit est (occ + '1')."""
        if self.est_feuille() and self is not n:
            return None
        elif n is self:
            return ""
        elif n is self.gauche:
            return "0"
        elif n is self.droit:
            return "1"
        
        ng = self.gauche.occurrence(n) if self.gauche else None
        nd = self.droit.occurrence(n) if self.droit else None
        if not ng and not nd:
            return None
        if ng:
            return "0" + ng
        if nd:
            return "1" + nd

    def parcours_main_gauche(self, t1=ne_rien_faire, t2=ne_rien_faire, t3=ne_rien_faire):
        # avant parcours du sous-arbre gauche
        t1(self)

        # parcours du sous-arbre gauche s'il existe.
        if self.gauche:
            self.gauche.parcours_main_gauche(t1, t2, t3)

        # deuxième rencontre:
        #   après avoir parcouru le sous-arbre gauche
        #   mais avant d'avoir parcouru le sous-arbre droit
        t2(self)

        # parcours du sous-arbre droit s'il existe.
        if self.droit:
            self.droit.parcours_main_gauche(t1, t2, t3)

        # troisième rencontre: après avoir parcouru le sous-arbre droit éventuel
        t3(self)

    def parcours_prefixe(self, t=lambda n: print(n.valeur)):
        """Parcours récursif à main gauche de l'arbre enraciné en self et applique le
        traitement t (une fonction qui prend en argument le noeud courant) **avant**
        de parcourir les sous-arbres."""
        self.parcours_main_gauche(t1=t)

    def parcours_infixe(self, t=lambda n: print(n.valeur)):
        """Parcours récursif à main gauche de l'arbre enraciné en self et applique le
        traitement t - une fonction qui prend en argument le noeud courant - **après**
        avoir parcouru le sous-arbre gauche (du noeud courant) mais **avant** d'avoir
        parcouru son sous-arbre droit."""
        self.parcours_main_gauche(t2=t)

    def parcours_postfixe(self, t=lambda n: print(n.valeur)):
        """Parcours récursif à main gauche de l'arbre enraciné en self et applique le
        traitement t (une fonction qui prend en argument le noeud courant) **après**
        avoir parcouru les sous-arbres."""
        self.parcours_main_gauche(t3=t)

    def parcours_niveau(self):
        """Parcours l'arbre en enraciné en self de façon que ses noeuds
        soit visités niveau après niveau et, pour un niveau donné, de la
        gauche vers la droite."""
        from collections import deque
        file = deque()
        file.appendleft(self)
        while len(file) > 0:
            noeud = file.pop()  # on défile
            if noeud.gauche:    # puis on enfile
                file.appendleft(noeud.gauche)
            if noeud.droit:
                file.appendleft(noeud.droit)
            print(noeud.valeur, end=" ")

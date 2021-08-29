class TasMin:
    """Un tas est un arbre binaire parfait: tous ses niveaux sont remplies sauf
    peut-être le dernier, mais même le dernier niveau est rempli par la gauche.
    Cette organisation particulière permet de représenter un tas avec un simple tableau:
    L'index d'une valeur correspond à la numérotation par niveau du noeud correspondant.
    La propriété de tas min est la suivante: tout noeud de l'arbre a une valeur inférieure
    ou au pire égale à celles de ses noeuds fils.
    Cette structure possède les méthodes d'une file de priorité min, à savoir: 
        - insérer une valeur
        - extraire la valeur la plus petite (qui est alors supprimé)
    Ces opérations ont un coût O(log n) où n est le nombre d'éléments du tas.
    Enfin, cette structure propose le tri d'un tableau sur place pour un coût O(nlog n),
    ce qui est optimal (du moins pour les tris par comparaison.)
    """
    PINF = float("+inf") # représente la valeur +infini.
    
    def __init__(self, tableau=None, clefn=None):
        """initialise le TasMin à partir du tableau fournie et sinon avec tas vide.
        clefn est une fonction qui, étant donné un objet du tas, renvoie sa clé.
        Par défaut, clefn considère que les éléments stocké dans le tas sont directement comparable.
        """
        self._t = []
        self.taille = 0
        self.__clefn = clefn if clefn else (lambda x: x)
        if tableau:
            self._construire(tableau)
    
    def _comp(self, i, j):
        """Renvoie True si l'objet d'index i a une clé strictement inférieure à celle de l'objet d'index j.
        sert principalement à «simplifier le code»."""
        if self._t[j] is self.PINF:
            return True
        return self.__clefn(self._t[i]) < self.__clefn(self._t[j])
        
    def __len__(self):
        "Renvoie le nombre d'éléments stocké dans le tas."
        return self.taille
    
    def _ip(self, i):
        "Renvoie l'index du parent du «noeud» d'index i."
        return (i + 1)// 2 - 1
    
    def _ig(self, i):
        "Renvoie l'index du fils gauche du noeud d'index i."
        return 2 * (i + 1) - 1
    
    def _id(self, i):
        "Renvoie l'index du fils droit du noeud d'index i."
        return 2 * (i + 1)
    
    def _entasser_min(self, i):
        """Routine utilitaire importante: si i est l'index d'un noeud qui
        ne respecte pas la propriété de tas min, ce noeud est échangé
        avec l'un de ses fils pour changer cet état de fait et cela est fait récursivement...
        de sorte qui si les noeuds sous celui-ci respectent la propriété de tas min, l'arbre
        enraciné en i retrouve globalement sa propriété de tas min."""
        mini = i
        g, d = self._ig(i), self._id(i)
        #if g < self.taille and self._t[g] < self._t[i]:
        if g < self.taille and self._comp(g, i):
            mini = g
        #if d < self.taille and self._t[d] < self._t[mini]:
        if d < self.taille and self._comp(d, mini):
            mini = d
        if mini != i:
            self._t[i], self._t[mini] = self._t[mini], self._t[i]
            self._entasser_min(mini)
    
    def _construire(self, tableau):
        """utilitaire: transforme un tableau arbitraire en tas min."""
        self._t = tableau
        self.taille = len(tableau)
        # i dernier noeud qui n'est pas une feuille
        i = self.taille // 2 - 1
        while i >= 0:
            self._entasser_min(i)
            i -= 1
    
    @staticmethod
    def trier(tableau):
        """Implémente le tri par tas: le tableau fourni est trié sur place dans l'ordre croissant."""
        t = TasMin(tableau)
        while t.taille > 1:
            t._t[0], t._t[t.taille-1] = t._t[t.taille-1], t._t[0]
            t.taille -= 1
            t._entasser_min(0)
     
    def min(self):
        """Renvoie l'objet dont la clé est minimal; ne supprimer pas l'objet du tas"""
        if self.taille == 0:
            raise IndexError("Le tas est vide!")
        return self._t[0]
   
    def extraire_min(self):
        """Renvoie et supprime l'objet du tas dont la clé est minimale."""
        if self.taille == 0:
            raise IndexError("Le tas est vide!")
        r = self._t[0]
        self._t[0] = self._t[self.taille-1]
        self.taille -= 1
        self._entasser_min(0)
        return r

    def diminuer(self, i, valeur):
        """Sert à diminuer la valeur portée par le noeud i. Le tas
        se «reconfigure» pour fichierconserver sa propriété de tas min."""
        if i >= self.taille:
            raise IndexError("indice non valide")
        if self._t[i] is not self.PINF and \
           self.__clefn(valeur) < self.__clefn(self._t[i]):
            raise Exception(f"{valeur} est plus petite que la valeur courante {self._t[i]}")
        self._t[i] = valeur
        ip = self._ip(i)
        #while i > 0 and self._t[ip] > self._t[i]:
        while i > 0 and self._comp(i, ip):
            self._t[ip], self._t[i] = self._t[i], self._t[ip]
            i = ip
            ip = self._ip(i)
    
    def inserer(self, valeur):
        "Insère une valeur dans le tas."
        self.taille += 1
        if len(self._t) < self.taille:
            self._t.append(self.PINF)
        else:
            self._t[self.taille - 1] = self.PINF
        self.diminuer(self.taille-1, valeur)
    
    def __str__(self):
        "Affiche le tableau sous-jacent du tas."
        return str(self._t[:self.taille])

class TasMax:
    """Similaire au tas min mais vérifie la propriété de tas max
    à savoir la valeur de tout noeud est supérieure (ou égale) à
    celles de ses enfants. Voir les commentaires pour TasMin ci-dessus."""
    
    MINF = float("-inf") # constante représentant l'infini
    
    def __init__(self, tableau=None):
        self._t = []
        self.taille = 0
        if tableau:
            self._construire(tableau)
    
    def __len__(self):
        return self.taille
    
    def _ip(self, i):
        return (i + 1)// 2 - 1
    
    def _ig(self, i):
        return 2 * (i + 1) - 1
    
    def _id(self, i):
        return 2 * (i + 1)
    
    def _entasser_max(self, i):
        maxi = i
        g, d = self._ig(i), self._id(i)
        if g < self.taille and self._t[g] > self._t[i]:
            maxi = g
        if d < self.taille and self._t[d] > self._t[maxi]:
            maxi = d
        if maxi != i:
            self._t[i], self._t[maxi] = self._t[maxi], self._t[i]
            self._entasser_max(maxi)
    
    def _construire(self, tableau):
        self._t = tableau
        self.taille = len(tableau)
        # i dernier noeud qui n'est pas une feuille
        i = self.taille // 2 - 1
        while i >= 0:
            self._entasser_max(i)
            i -= 1
    
    @staticmethod
    def trier(tableau):
        t = TasMax(tableau)
        while t.taille > 1:
            t._t[0], t._t[t.taille-1] = t._t[t.taille-1], t._t[0]
            t.taille -= 1
            t._entasser_max(0)
     
    def max(self):
        if self.taille == 0:
            raise IndexError("Le tas est vide!")
        return self._t[0]
   
    def extraire_max(self):
        if self.taille == 0:
            raise IndexError("Le tas est vide!")
        r = self._t[0]
        self._t[0] = self._t[self.taille-1]
        self.taille -= 1
        self._entasser_max(0)
        return r

    def augmenter(self, i, valeur):
        if i >= self.taille:
            raise IndexError("indice non valide")
        if valeur < self._t[i]:
            raise Exception(f"{valeur} est plus petite que la valeur courante {self._t[i]}")
        self._t[i] = valeur
        ip = self._ip(i)
        while i > 0 and self._t[ip] < self._t[i]:
            self._t[ip], self._t[i] = self._t[i], self._t[ip]
            i = ip
            ip = self._ip(i)
    
    def inserer(self, valeur):
        self.taille += 1
        if len(self._t) < self.taille:
            self._t.append(float("-inf"))
        else:
            self._t[self.taille - 1] = float("-inf")
        self.augmenter(self.taille-1, valeur)
    
    def __str__(self):
        return str(self._t[:self.taille])
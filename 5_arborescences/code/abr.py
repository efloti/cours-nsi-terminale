from noeud_bin2 import NoeudBin2

class ABR:
    """Modélise un arbre binaire de recherche en utilisant des noeuds de type NoeudBin2.
    Si l'on souhaite stocker des «objets» dans l'arbre, il doivent être de même nature
    et il faut alors préciser comment obtenir la clé de comparaison depuis ce genre d'objet.
    Pour cela, préciser l'argument «keyfn» du constructeur:
        il doit s'agir d'une fonction qui étant donné un objet renvoie sa clé.
        
        Ex: si les objets sont des dictionnaire de la forme {"nom":..., "prenom": ..., "age": ...} 
            et que la clé choisie est "age"
            alors keyfn(obj) renverrait obj["age"].
    
    Méthodes principales d'efficacité O(hauteur de l'arbre):
        - inserer(obj): insère obj dans l'ABR
        - supprimer(obj): supprime obj de l'ABR (s'il s'y trouve)
        - chercher(obj): renvoie True ou False selon que obj est dans l'ABR ou non
        - maximum(): renvoie l'objet contenant la clé la plus grande
    """
    
    def __init__(self, keyfn=lambda o: o):
        self.racine = None
        # calculer la taille d'un arbre est coûteux donc
        # mieux vaut tenir à jour cette information.
        self.taille = 0
        # de façon générale, un arbre binaire peut contenir n'importe quelle sorte d'objet
        # la fonction keyfn prend un tel objet et renvoie sa «clé»
        # l'attribut cle est une fonction qui, étant donné un noeud
        # renvoie la clé de l'objet stocké dans son attribut valeur.
        self.cle = lambda n: keyfn(n.valeur)
    
    def __len__(self):
        return self.taille
    
    def _maximum(self):
        """Renvoie le **noeud** contenant la plus grande clé ou None si l'arbre est vide."""
        n = self.racine
        while n.droit is not None:
            n = n.droit
        return n

    def maximum(self):
        """Utilise _maximum pour renvoyer l'objet contenant la plus grande clé
        ou None si l'arbre est vide."""
        n = self._maximum()
        return None if n is None else n.valeur
    
    def _chercher(self, o):
        """Renvoie le noeud contenant l'objet fourni en argument s'il est stocké
        dans l'arbre; sinon renvoie None."""
        n = self.racine
        while n is not None:
            co = self.cle(NoeudBin2(o))
            cn = self.cle(n)
            if co == cn:
                return n
            elif co < cn:
                n = n.gauche
            else:
                n = n.droit
        return None

    def chercher(self, o):
        """Renvoie True ou False selon si l'objet fourni est stocké dans l'arbre ou non."""
        n = self._chercher(o)
        return False if n is None else True

    def __contains__(self, o):
        """Permet la syntaxe naturelle «o in abr» où abr est de type ABR."""
        return self.chercher(o)
    
    def inserer(self, o):
        """Insère un noeud dont la valeur est l'objet fourni o dans l'ABR."""
        x = NoeudBin2(o)
        self.taille += 1

        # cas où l'arbre est vide
        if self.taille == 1:
            self.racine = x
            return

        # recherche du noeud où effectuer l'insertion
        gauche = True # de quel côté?
        n = self.racine
        while True:
            if self.cle(x) <= self.cle(n):
                if n.gauche:
                    n = n.gauche
                else:
                    break
            else:
                if n.droit:
                    n = n.droit
                else:
                    gauche = False
                    break

        x.parent = n
        if gauche:
            n.gauche = x
        else:
            n.droit = x
    
    def _succ(self, n):
        """Renvoie le noeud successeur du noeud n fourni en argument
        ou None s'il n'en a pas."""
        # 1er cas: si n a un fils droit
        if n.droit is not None:
            # trouver le minimum du sous-arbre enraciné en n.droit
            x = n.droit
            while x.gauche is not None:
                x = x.gauche
            return x

        # 2eme cas: n est le prédecesseur du noeud cherché qui est parmi ses ancêtre
        x = n
        # tant que x est un fils droit, remonter
        while x.parent and x.parent.droit == x:
            x = x.parent
        # De deux choses l'une: x n'a pas de parent ou c'est un fils gauche
        # dans le premier cas:
        if x.parent is None:
            # x est la racine donc pas de successeur pour n
            return None
        # dans le second cas:
        return x.parent
    
    def _supprimer(self, noeud):
        """Supprime le noeud fourni en argument (supposé dans l'ABR)"""

        if self.taille == 0:
            return

        self.taille -= 1
        n = noeud # n désigne le noeud à supprimer in fine
        if n.est_double():
            n = self._succ(noeud)
            # copions la valeur de succ(noeud) dans noeud
            noeud.valeur = n.valeur

        # à partir de là, on peut supposer que n n'est pas double

        # récupérons le fils éventuel de n à rattacher à son parent
        f = n.droit if n.gauche is None else n.gauche

        # si n est la racine, f devient la nouvelle racine
        if not n.parent:
            self.racine = f

        # soit p le parent de n
        p = n.parent


        # si le fils de n n'est pas None, il faut le faire pointer vers son nouveau parent
        if f is not None:
            f.parent = p

        # f doit-il être le fils gauche ou droit de p (si p n'est pas None)
        if p is not None:
            if p.gauche == n:
                p.gauche = f
            else:
                p.droit = f
        n.parent = None; n.gauche = None; n.droit = None # ménage!
        return n.valeur
    
    def supprimer(self, o):
        """Supprime l'objet fourni en argument s'il se trouve dans l'ABR.
        Autrement, n'a pas d'effet."""
        n = self._chercher(o)
        if n is not None:
            self._supprimer(n)
    
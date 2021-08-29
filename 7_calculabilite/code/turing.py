class TabBiDir:
    
    def __init__(self, g=None, d=None):
        self.g = [] if g is None else [g[len(g)-i-1] for i in range(len(g))] # ou g[::-1]...
        self.d = [] if d is None else d
    
    def imin(self):
        return -len(self.g)
    
    def imax(self):
        return len(self.d) - 1
    
    def append(self, v):
        self.d.append(v)

    def prepend(self, v):
        self.g.append(v)
    
    def __getitem__(self, i):
        if i >= 0:
            return self.d[i]
        else:
            return self.g[-i-1]

    def __setitem__(self, i, v):
        if i >= 0:
            self.d[i] = v
        else:
            self.g[-i-1] = v
    
    def __str__(self):
        if len(self.g) == 0 and len(self.d) == 0:
            return "[]"
        deb = str(list(reversed(self.g)))
        fin = str(self.d)
        if len(self.g) == 0:
            return fin
        elif len(self.d) == 0:
            return deb
        else:
            return deb[:-1] + ", " + fin[1:]

class TuringMachine:
    BLANC = '.' # le blanc de la machine
    def __init__(self, etat_initial, etat_final, regles):
        self.etat = etat_initial
        self.etat_final = etat_final
        self.regles = regles
        r = TabBiDir()
        r.prepend(self.BLANC)
        self.ruban = r
        self.i = 0 # position sur le ruban
    
    def est_arreter(self):
        return self.etat == self.etat_final
    
    def charger(self, entree, pos=0):
        """charge l'entrée fournie (chaîne de caractères) et la
        place sur le ruban à la position donnée."""
        N = len(entree)
        if pos == 0:
            for c in entree:
                self.ruban.append(c)
            self.ruban.append(self.BLANC)
        elif pos < 0:
            for _ in range(-pos):
                self.ruban.prepend(self.BLANC)
            if N + pos >= 0:
                for _ in range(N+pos):
                    self.ruban.append(self.BLANC)
            else:
                self.ruban.append(self.BLANC)
            for i in range(N):
                self.ruban[pos+i] = entree[i]
        else:
            for _ in range(pos+N+1):
                self.ruban.append(self.BLANC)
            for i in range(pos, pos+N):
                self.ruban[i] = entree[i-pos]

    def suivant(self):
        # lecture
        sym = self.ruban[self.i]
        # Récupérer le triplet correspondant
        sym, depl, etat = self.regles[self.etat][sym]
        # écriture
        self.ruban[self.i] = sym
        # si on est en bout de ruban, se donner de la marge
        if sym is not self.BLANC and self.i == self.ruban.imax():
            self.ruban.append(self.BLANC)
        if sym is not self.BLANC and self.i == self.ruban.imin():
            self.ruban.prepend(self.BLANC)
        # se déplacer et mettre à jour
        self.i += depl
        self.etat = etat
    
    def __str__(self):
        """Affiche la configuration courante de la machine."""
        # plaçons une marque sur le ruban
        sauv = self.ruban[self.i]
        self.ruban[self.i] = "secret"
        # un peu de ménage...
        ruban_str = str(self.ruban)[1:-1].replace("'", "").replace('"', "").replace(", ", " | ")
        # où est la marque?
        pos = ruban_str.find("secret")
        # créons une chaîne qui figure la position courante et l'état
        i_etat_str = " " * pos + "🠁\n" + " " * pos + self.etat
        # restaurer
        ruban_str = ruban_str.replace("secret", sauv) + "\n" + i_etat_str
        self.ruban[self.i] = sauv
        return ruban_str
    
    def executer_sur(self, entree, pos=0, verbeux=True):
        self.charger(entree, pos=pos)
        while not self.est_arreter():
            if verbeux:
                print(self)
            self.suivant()
        print("L'état du ruban est:")
        print(self)
        

B = TuringMachine.BLANC # alias
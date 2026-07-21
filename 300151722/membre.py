class Membre:
    def __init__(self, numero, nom, succursale, duree, prix, actif):
        self.__numero = numero
        self.__nom = nom
        self.__succursale = succursale
        self.__duree = duree
        self.__prix = prix
        self.__actif = actif

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def succursale(self):
        return self.__succursale

    @succursale.setter
    def succursale(self, succursale):
        self.__succursale = succursale

    @property
    def duree(self):
        return self.__duree

    @duree.setter
    def duree(self, duree):
        if duree > 0:
            self.__duree = duree

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, prix):
        if prix > 0:
            self.__prix = prix

    @property
    def actif(self):
        return self.__actif

    @actif.setter
    def actif(self, actif):
        if actif in ["Oui", "Non"]:
            self.__actif = actif

    def afficher(self):
        print(self.numero, self.nom, self.succursale, self.duree, self.prix, self.actif)


class MembreStandard(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, casier):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.casier = casier


class MembrePremium(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, coach):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.coach = coach


m1 = MembreStandard(1, "Julie Tremblay", "Centre-ville", 12, 45, "Oui", "C12")
m2 = MembrePremium(2, "Marc Bouchard", "Est", 6, 60, "Oui", "Alex")

m1.afficher()
m2.afficher()
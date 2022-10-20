class Personne:
    def __init__(self,nom,prenom,cin):
        self.nom=nom
        self.prenom=prenom
        self.cin=cin
    def ToString(self):
        print("Le nom est: ", self.nom,"\nPrenom est: ", self.prenom,"\nCin : ",  self.cin)
class Vaccine(Personne):
    def __init__(self,nom,prenom,cin,code,date):
        self.__code=code
        self.__date=date
    def get_code(self):
        return self.__code
    def get_date(self):
        return  self.__date
    def set_code(self,code1):
        self.code=code1
    def set_date(self,date1):
        self.date=date1
    def ToString(self):
        print( "Le patient du code de: ",self.__code,"a fait son vaccin a la date suivant:",self.__date)
class Vaccin:
    def __init__(self,code_vac,nom_vac,dure):
        self.code_vac=code_vac
        self.nom_vac=nom_vac
        self.dure=dure
    def recopie(self,c):
        self.code_vac=c.code_vac
        self.nom_vac=c.nom_vac
        self.dure=c.dure
    def ToString(self):
            print("Le code du vaccin est: ",self.code_vac,"\nLe nom du vaccin est: ",   self.nom_vac,"\nLa duré est",self.dure)
per=Personne("Bah","Idy","homme")
per.ToString()
vac=Vaccine("Bah","Idy","homme",2145,"10/21/2021")
vac.ToString()
vacin=Vaccin("2141","palue","24 secondes")
vc=Vaccin("1241","p","12 secondes")
vc.recopie(vacin)
vc.ToString()
vacin.ToString()

        

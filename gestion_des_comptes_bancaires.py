import random
class CompteBanquaire:
    def __init__(self, numero_compte, solde):
        self.__numero_compte = numero_compte
        self.__solde = solde
    
    def GetNum(self):
        return self.__numero_compte
    
    def SetNum(self, NewNum):
        self.__numero_compte = NewNum

    def GetSolde(self):
        return self.__numero_compte
    
    def SetSolde(self, NewSolde):
        self.__numero_compte = NewSolde

    def Deposer(self, Somme):
        return self.__solde == self.solde + Somme
    
    def Retirer(self, Somme):
        return self.__solde == self.solde - Somme
    
    
    
class AjouterUnCompte():
    __count = 0
    def __init__(self):
        AjouterUnCompte.__count += 1

    def GetCount(self):
        return self.__count
    
    def AfficherAjouterCompte(self):
        return random.randint(0, 100)



print("Menu : \n1.Ajouter un Compte\n2.Supprimer un Compte\n3.Les fonctionalités de mon compte")
Choice1 =input("Veuillez choisissez 1 ou 2 ou 3 : ")

Choice = AjouterUnCompte()
Compte = {}


# Client = {}
# Client['numero_compte'],Client['code_secret'] =Compte['numero_compte'],random.randint(1,99999999)
# for key,value in Client.items():
#      print(f"{key} : {value}")

# Client_compte = {}
# Client_compte[Compte['numero_compte']]
while True:
    
    if(Choice1 == "1"):
      x = input("Entrer le numero de client : ")
      NumCompte = print("Numero de compte = "+str(x)+str(Choice.AfficherAjouterCompte()))
      break
   
    elif(Choice1 == "2"):
        z = input("Veuillez entrer votre numero de compte : ")
        if(CompteBanquaire.GetNum == z):
            print("Votre compte a ete supprimer")
        else:
            print("Numéro de compte invalid")
        break

    elif(Choice1 == "3"):
        print("1. Modifier mon mot de passe\n2. Afficher mon solde\n3. Déposer une somme d’argent\n4. Retirer une somme d’argent")
        fonc = input("Veuillez choisissez 1 ou 2 ou 3 ou 4 : ")
        if(fonc == "1"):
            Modification_password = {}
            Modification_password['numero_compte'],Modification_password['password'] = input("Veuillez entrer votre numero de compte : "),input("Entrer votre mot de passe : ")
            newpass = input("Veuiller entrer votre nouveau mot de passe : ")
            Modification_password["password"] = newpass     
            for key,value in Modification_password.items():
                print(f"{key} : {value}")
            break
        elif(fonc == "2"):
            print("Votre solde de compte :",Compte["solde"],"DH")
            break
        elif(fonc == "3"):
            Compte['numero_compte'],Compte['solde'] = input("Entrer votre numéro de compte : "),input("Votre solde : ")
            somme = input("Veuillez entrer la somme d'argent que vous voulez la retirer : ")
            ST = float(Compte["solde"])+float(somme)
            print(ST,"DH")
            break
        elif(fonc == "4"):
            Compte['numero_compte'],Compte['solde'] = input("Entrer votre numéro de compte : "),input("Votre solde : ")
            somme = input("Veuillez entrer la somme d'argent que vous voulez la disposer : ")
            ST = float(Compte["solde"])-float(somme)
            print(ST,"DH")
            break
    else:
         break

    

# # # t1 = CompteBanquaire(123,6700)
# # # t1.Afficher()

# # # t2 = CompteBanquaire(646,789)
# # # t2.Afficher()

# # # t3 = CompteBanquaire(77567,789)
# # # t3.Afficher()




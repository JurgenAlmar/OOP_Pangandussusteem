# Parent Class
class User():
    def __init__(self, name, age, gender):#Kasutajal on nimi, vanus, sugu.
        self.name = name#nime atribuut mis on küljes endal
        self.age = age#vanuse atribuut mis on küljes endal
        self.gender = gender#soo atribuut mis on küljes endal

    def show_details(self):#See funktsioon näitab kasutaja detaile
        print("Personal Details")
        print("")
        print("Name ", self.name)#kui kasutaja sistestab enda nime siis väljastab ta selle
        print("Age  ", self.age)#kui kasutaja sisestab enda vanuse siis väljastab ta selle
        print("Gender ", self.gender)#kui kasutaja sisestab enda soo siis väljastab ta selle


# Child Class
class Bank(User):
    def __init__(self, name, age, gender):#Võtab eelmisest klassis või siis võib öelda vanemklassist omadused
        super().__init__(name, age, gender)
        self.balance = 0#konto alguses on jääk null sest nii see töötab

    def deposit(self, amount):#funtksioon et raha sisse panna
        self.amount = amount#konto sissemakse summa
        self.balance = self.balance + self.amount#lisab makse jäägile
        print("Account balance has been updated : ", self.balance)#näitab uut konto jääki

    def withdraw(self, amount):#funktsioon raha väljavõtta
        self.amount = amount#konto väljavõte summa
        if self.amount > self.balance:#kui kontol on vähem kui kasutaja välja võtab
            print("Insufficient Euro | Balance Available : ", self.balance)#väljastab kood et raha ei ole
        else:
            self.balance = self.balance - self.amount#kui kontol on raha lahutab selle ära
            print("Account balance has been updated : ", self.balance)#näitab uuendatud jääki

    def view_balance(self):#funktsioon kontojäägi nähemiseks
        self.show_details()#näitab kasutaja andmeid
        print("Account balance: ", self.balance)#näitab kontojääki
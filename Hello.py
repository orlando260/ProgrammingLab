
#x=input("dimmi una parola o una frase:")
#y=input("ora dimmi che lettera vuoi cercare:")
'''
def conta_lettere(x,y):
    z=0
    for i in x:
        if i==y:
            z=z+1
    print(f"{z}")
'''
#conta_lettere(x,y)

#x=input("type a number:")
#x=int(x)
#w=0
#for i in range(x-2):
#    if x%(i+2)==0:
#        w=1
#if w==1:
#    print(f"{x} non è un numero primo")
#else:
#    print(f"{x}  è un numero primo")
'''
x=[3,2,3,4,5,6,7,4,5,6,7,8]
def sommalista(x):
    z=0
    for i in range(len(x)):
        z=z+x[i]
    print(f"{z}")
sommalista(x)
'''
'''
x=str(input())
z=0
for i in range(len(x)):
    if x[i]!=x[-(i+1)]:
        z=1
if z==0:
    print("true")
else:
    print("false")
'''
'''
x="1"
y=[]
while x!="0":
    x=input()
    
    if x!="0":
        y.append(x)
print(f"{y}")

i=int(input())
j=int(input())
def fr_(y,i,j):
    h=y[i]
    f=y[j]
    y[j]=h
    y[i]=f

fr_(y,i,j)

print(f"{y}")
'''
'''
x="1"
y=[]
while x!="0":
    x=input()
    
    if x!="0":
        y.append(x)
print(f"{y}")

x="1"
z=[]
while x!="0":
    x=input()
    
    if x!="0":
        z.append(x)
print(f"{z}")

def elemento_comune(y,z):
    s=0
    for i in range(len(y)):
        for j in range(len(z)):
            if y[i]==z[j]:
                s=1
    return s
s=elemento_comune(y,z)
if s==1:
    print("c'è un elemento comune")
else:
    print("non c'è alcune elemento comune")
'''

'''
x="1"
y=[]
while x!="10":
    x=input("scrivi un numero da 0 a 9:")
    
    if x!="10":
        y.append(x)
print(f"{y}")

def trasforma(y):
    p=["zero","uno","due","tre","quattro","cinque","sei","sette","otto","nove"]
    
    s=[]
    for i in range(len(y)):
        for j in range(len(p)):
            if int(y[i])==j:
                s.append(p[j])
    return s
print(f"{trasforma(y)}")
'''
'''
x="1"
y=[]
while x!="0":
    x=input()
    
    if x!="0":
        y.append(x)
print(f"{y}")

def return_diz(y):
    z={}
    for i in range(len(y)):
        z[y[i]]=i+1
    return z
print(f"{return_diz(y)}")
'''
'''
with open("shampoo.csv", "r") as f:
    file = f.read()
#file=open('shampoo.csv', 'r')
print(file)
#file.close()

class prof:
    def __init__(self, name, surname):
        self.name=name
        self.surname=surname

    def __str__(self):
        return 'prof "{} {}""'.format(self.name,self.surname)
chili=prof('Giulio','Caravagna')
print(chili.name,chili.surname)
print(chili)

import random
class coin():
    def __init__(self,faccia):
        self.faccia=faccia
        
    def lancio(self):
        
        if random.randint(0,1)==1:
            self.faccia="testa"
        else:
            self.faccia="croce"
    def ritorno(self):
        return self.faccia
moneta=coin('testa')
moneta.lancio()
print(moneta.ritorno())

file=open('shampoo_sales.csv', 'r')
z=0
lista=[]
for i in file:
    date,valori=i.split(',')
    if valori!='Sales\n':
        z=z+float(valori)
print(z)
file.close

class Canguro():
    def __init__(self):
        self.contenuto_tasca=[]
    def intasca(self,x):
        self.contenuto_tasca.append(x)
    def __str__(self):
        return (f"{self.contenuto_tasca}")
Sium=Canguro()
x=1
while x!=0:
    x=int(input())
    if x!=0:
        Sium.intasca(x)
print(Sium)
'''
'''
class Veicolo():
    def __init__(self,x,p,a,m):
        self.modello=x
        self.marca=p
        self.anno=a
        self.speed=m
    def Accellerare(self):
        self.speed=self.speed+5
    def frenare(self):
        if self.speed>0:
            self.speed=self.speed-5
    def get_speed(self):
        print(self.speed)
    def __str__(self):
        return 'Veicolo: "{},{},{},{}"'. format(self.modello,self.marca,self.anno,self.speed)

class Auto(Veicolo):
    def __init__(self,x,p,a,m,d):
        super().__init__(x,p,a,m)
        self.Porte=d
    def __str__(self):
        return 'Veicolo: "{},{},{},{},{}"'. format(self.modello,self.marca,self.anno,self.speed,self.Porte)

class Moto(Veicolo):
    def __init__(self,x,p,a,m,c):
        super().__init__(x,p,a,m,c)
        self.tipo=c
    def __str__(self):
        return 'Veicolo: "{},{},{},{},{}"'. format(self.modello,self.marca,self.anno,self.speed,self.tipo)

s=input("inserisci modello veicolo: ")
t=input("inserisci marca veicolo: ")
c=int(input("anno di immatricolazione: "))
r=int(input())
if r==0:
    y=int(input("numero porte: "))
    Mio_veicolo=Auto(s,t,c,0,y)
elif r==1:
    y=input("tipo di moto: ")
    Mio_veicolo=Moto(s,t,c,0,y)
else:
    Mio_veicolo=Veicolo(s,t,c,0)

x=1
while x!=0:
    x=int(input())
    if x<0:
        Mio_veicolo.frenare()
    if x>0:
        Mio_veicolo.Accellerare()
    Mio_veicolo.get_speed()
print(Mio_veicolo.__str__())
'''
'''
class Persona():
    def __init__(self,ruolo,nome,cognome):
        self.ruolo=ruolo
        self.nome=nome
        self.cognome=cognome
    
    def saluta(self):
        print('Ciao sono',self.ruolo +",",self.nome,self.cognome)

class Studente(Persona):
    def __init__(self,nome,cognome,corso):
        super().__init__("Studente UNITS",nome,cognome)
        self.corso=corso
    
    def saluta(self):
        Persona.saluta(self)
        print(">Frequento il corso: ",self.corso)

class Docente(Persona):
    def __init__(self,nome,cognome,corso):
        super().__init__("Docente UNITS",nome,cognome)
        self.corso=corso
    def saluta(self):
        Persona.saluta(self)
        print(">Docente del corso: ",self.corso)
'''
'''
class Poligono():
    def __init__(self,lati):
        self.lati=lati
    
    def __str__(self):
        print(f"sono un poligono di {self.lati} lati")

class Quadrilatero(Poligono):
    def __init__(self):
        self.lati=4 
    def __str__(self):
        print("Sono un quadrilatero")

class Rettangolo(Quadrilatero):
    def __init__(self,base,altezza):
        super().__init__()
        self.base=base
        self.altezza=altezza
    def perimetro(self):
        return 2*self.base+2*self.altezza
    def area(self):
        return self.base*self.altezza
    def __str__(self):
        print("Sono un rettangolo")

class Triangolo(Poligono):
    def __init__(self,l1,l2,l3):
        self.lati=3
        self.lato1=l1
        self.lato2=l2
        self.lato3=l3
    def perimetro(self):
        return self.lato1+self.lato2+self.lato3
    def is_equilatero(self):
        if self.lato1==self.lato2==self.lato3:
            return True
        else:
            return False
    def __str__(self):
        print("Sono un triangolo")

'''
'''
class CSVfile():
    def __init__(self,CSV_file):
        self.name=CSV_file
    def get_data(self):
        with open(self.name,'r') as file:
            lista=[]
            for line in file:
                list=[]
                line=line.replace(","," ").replace("\n","")
                for i in line.split(" "):
                    list.append(i)
                
                lista.append(list)
        return (lista)
file=CSVfile("shampoo_sales.csv")
print(f"{file.get_data()}")
'''
'''
list=[1,2,3,4,5,6,7,8,9]
list1=[n for n in list if n%2!=0]
print(list1)

lista=[[1,2,3],[4,5],[6,7,8,1]]
list=[i for n in lista for i in n]
print(list)

lista1=[1,3,5,7]
lista2=[2,4,6]
lista=[x*i for i in lista1 for x in lista2 if x*i>10]
print(lista)

def Valverde(i,s,t):
    if i*i+s*s==t*t or s*s+t*t==i*i or t*t+i*i==s*s:
        return True
    else:
        return False
lista=[(i,s,t) for i in range(1,21) for s in range(i,21) for t in range(s,21) if Valverde(i,s,t)==True]
print(lista)

lista_a=[0,1,3,4]
lista_b=['a','b','c']


lista=[(i,el)for i in lista_a if i%2==0 for x,el in enumerate(lista_b) if x%2!=0]

print(lista)

frase=' Vai Mihailo, non mollare mai, un giorno arriverà un Doraimon croato con una tasca piena di abbonamenti ILLIMITATI'
frase=frase.split(', ')


dict={ parola: frase.count(parola) for parola in frase.split(' ') }

print(dict)
'''
'''
def New_dict(x):
    D={i: x.count(i) for i in x}
    return D
lista=["aereo","sinner","aldo","moro","tennis","zinna","sinner"]
print(New_dict(lista))
'''
'''
with open("shampoo_sales.csv") as File:
    sum=0
    for i in File:
        a,b,c=i.replace("\n",",").split(",")
        if b!="Sales":
            b=float(b)
            sum=sum+b
print(sum)
'''
'''
def conta(fil,parola):
    count=0
    with open(fil) as File:
        for line in File:
            line=line.replace("\n"," ").replace(","," ").replace("."," ")
            for i in line.split(" "):
                if i==parola:
                    count=count+1
    return count

print(conta("shampoo_sales.csv","Sales"))
'''
'''
class Persona:
    def __init__(self,ruolo,nome,cognome):
        self.ruolo=ruolo
        self.nome=nome
        self.cognome=cognome
    def saluta(self):
        print("ciao sono", self.nome, self.cognome, "e sono", self.ruolo)

class Studente(Persona):
    def __init__(self,ruolo,nome,cognome):
        super().__init__("Studente UNITS",nome,cognome)
        self.corso=[]
    def corsi(self):
        x=1
        while(x!=0):
            x=input()
            self.corso.append(x)
    def saluta(self):
        Persona.saluta(self)
        print(">frequento il corso di", self.corso)

class Docente(Persona):
    def __init__(self,ruolo,nome,cognome):
        super().__init__("Docente UNITS",nome,cognome)
        self.corso=[]
    def corsi(self):
        x=1
        while(x!=0):
            x=input()
            self.corso.append(x)
    def saluta(self):
        Persona.saluta(self)
        print(">Insegno nel corso di", self.corso)
'''
'''
class MovingAvarage():
    def __init__(self,x):
        self.finestra=x
    def compute(self,list):
        self.Lista=[]
        for i in range(0,len(list)-(self.finestra)+1):
            print("1",i)
            mean=0
            for j in range(0,self.finestra):
                mean=(list[j+i]+mean)
                print("2",j)
            self.Lista.append(mean/self.finestra)
        print(self.Lista)

moving_avarage=MovingAvarage(4)
result=moving_avarage.compute([6,5,1,3,4])
'''

class CSVTimeSeriesFile():
    def __init__(self,name):
        self.file=name
    def get_data(self):
        with open(self.file,'r') as file:
            lista=[]
            for line in file:
                line=line.replace("-",",").replace("\n","")
                a,b,c=line.split(",")
                lista.append(["{a}-{b}",c])

def compute_variation(time_series,inizio,fine):
    dict8={}
    for i in range(inizio,fine):
        for lista in time_series:
            somma=0
            j=0
            while(i in lista):
                j=j+1
                a,b=lista.split(",")
                b=int(b.replace("\n",""))
                somma=somma+b
            mean=somma/j
            
            

                


                
                







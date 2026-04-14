
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
'''
class CSVTimeSeriesFile():
    def __init__(self,name):
        self.file=name
    def get_data(self):
        lista=[]
        with open(self.file,'r') as file:
            
            for line in file:
                line=line.replace("\n","")
                a,c=line.split(",")
                lista.append([a,c])
        return lista

def compute_variation(time_series,inizio,fine):
    dict8={}
    for i in range(inizio,fine-1):
        k=i+1
        mean=0
        for lista in time_series:
            somma=0
            j=0
            while(i in lista):
                j=j+1
                a,b=lista.split(",")
                b=int(b.replace("\n",""))
                somma=somma+b
            mean=somma/j
        dict8['i']=mean
    dict88={}
    for i in range(inizio,fine):
            dict88['{i}-{k}']= dict8[i]-dict8[i+1]
    return dict88
'''
'''
class CSVfile():
    def __init__(self,CSV_file):
        if(type(CSV_file)==str):
            self.name=CSV_file
        else :
            print("sta roba non è una stringa")
            self.name=None
    def get_data(self):
        try:
            lista=[]
            with open(self.name,'r') as file:
                for line in file:
                    list=[]
                    line=line.replace(","," ").replace("\n","")
                    for i in line.split(" "):
                        list.append(i)
                    lista.append(list)
        except FileNotFoundError as e:
            print("sto file {} non esiste".format(self.name))
            print("e hai avuto sto errore:{}".format(e))
        return (lista)
    
class NumericalCSVfile(CSVfile):
    def __init__(self,CSV_file):
        super().__init__(CSV_file)
    def get_data(self):
        csv_file=super().get_data()
        for element in csv_file:
            try:
                element[1]= float(element[1])
            except:
                print("non posso convertire questo elemento ({}) in float".format(element[1]))
        return csv_file

    


file=NumericalCSVfile("shampoo_sales.csv")
print(f"{file.get_data()}")
'''
'''
import datetime
class Age():
    def __init__(self,day,month,year):
        self.year=year
        self.month=month
        self.day=day
        self.Oggi=datetime.datetime.now()
    def get_age(self):
        anni=self.Oggi-datetime.datetime(self.year,self.month,self.day)
        return int(anni.days/365)
    def prox_comple(self):
        diff=datetime.datetime((self.year+self.get_age()+1),self.month,self.day)-self.Oggi
        return diff

eta=Age(29,11,2006)
print(f"{eta.get_age()} anni")
print(eta.prox_comple())
'''
'''
a=0
while(a==0):
    a=input("inserire un numero: ")
    try:
        a=int(a)
    except Exception as e:
        print("{} non è un numero".format(a))
        print("ho avuto quindi questo errore {}".format(e))
        a=0
print(a*a)
'''
'''
while(True):
    print("seleziona\n1 per sommare due numeri\n" \
    "2 per fare una sottrazione tra due numeri\n" \
    "3 per uscire")
    var=input()
    try:
        var=int(var)
    except Exception as e:
        print("{} non è un numero".format(var))
        print("ho avuto quindi questo errore {}".format(e))
    if var==1:
        uno=input("primo numero: ")
        due=input("secondo numero: ")
        try:
            uno=int(uno)
        except Exception as e:
            print("{} non è un numero".format(uno))
            print("ho avuto quindi questo errore {}".format(e))
        try:
            due=int(due)
            uno=uno+due
            print(uno)
        except Exception as e:
            print("{} non è un numero".format(due))
            print("ho avuto quindi questo errore {}".format(e))
        
    if var==2:
        uno=input("primo numero: ")
        due=input("secondo numero: ")
        try:
            uno=int(uno)
        except Exception as e:
            print("{} non è un numero".format(uno))
            print("ho avuto quindi questo errore {}".format(e))
        try:
            due=int(due)
            uno=uno-due
            print(uno)
        except Exception as e:
            print("{} non è un numero".format(due))
            print("ho avuto quindi questo errore {}".format(e))
        
    if var==3:
        break
'''
'''
class ExamException(Exception):
    pass


class CSVTimeSeriesFile():
    def __init__(self,nome):
        self.nome=nome
        try:
            with open(self.nome, 'r') as file:
                next(file)
        except:
            raise ExamException("Errore: non legge il file")
    def get_data(self):
        lista=[]
        try:
            with open(self.nome, 'r') as file:
                next(file)
                for line in file:
                    List=[]
                    for i in line.split(","):
                        try:
                            List.append(float(i.replace("\n","")))
                        except:
                            List.append(i.replace("\n",""))
                    lista.append(List)
            return lista
        except Exception as e:
            print("il file {} non esiste".format(self.nome))
            print("di conseguenza c'è stato questo errore: {}".format(e))

def compute_variation(Data, first_year,last_year,N):
    Diz={}
    lista={}

    for i in range(first_year,last_year+1):
        somma=0
        media=0
        n=0
        
        for line in Data:
            
            if (any(str(i) in str(k) for k in line)):
                somma=somma+line[1]
                n=n+1

        lista[i]=somma/n
        for j in range(1,N+1):
            Somma=0
            m=0
            for line in Data:
                if line[0].startswith(str(i-j)):
                    Somma=Somma+line[1]
                    m=m+1
            if m!=0:
                media=media+Somma/m
        media=media/N
        if i-first_year>= N:
            Diz[i]=lista[i]-media
    return Diz
            
                
            





Nome= "../Downloads/GlobalTemperatures.csv"
Data=CSVTimeSeriesFile(Nome)
Data2=Data.get_data()
print(compute_variation(Data2,1900,1904,3))

'''
'''
class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self,nome):
        self.nome=nome
        try:
            with open(self.nome, 'r') as file:
                try:
                    next(file)
                except Exception as e:
                    raise ExamException("File non leggibile a causa del seguente errore:{}".format(e))
        except Exception as e:
            raise ExamException("File non apribile a causa del seguente errore:{}".format(e))
    def get_data(self,paese):
        lista=[]
        with open(self.nome) as file:
            for line in file:
                line=line.replace("\n","")
                try:
                    a,b,c=line.split(",")
                    if c==paese:
                        try:
                            lista.append([a,float(b)])
                        except:
                            continue
                except:
                    continue
        if lista==[]:
            return ("paese non presente nel file")
        return lista
    

def compute_variation(time_series1,time_series2,first_year,last_year):
    try:
        first_year=int(first_year)
    except:
        raise ExamException("numero non intero")
        
    diz={}
    Diz1={}
    Diz2={}
    Diz3={}
    Diz4={}
    for anno in range(first_year, last_year +1):
        media=0
        Media=0
        somma=0
        Somma=0
        Diz1[anno]=[elem[1] for elem in time_series1 if elem[0].startswith(str(anno))]
        Diz2[anno]=[elem[1] for elem in time_series2 if elem[0].startswith(str(anno))]
        for elem in Diz1[anno]:
            somma=somma+elem
            media=media+1
        Diz3[anno]=somma/media
        for elem in Diz2[anno]:
            Somma=Somma+elem
            Media=Media+1
        Diz4[anno]=Somma/Media
        diz[anno]=Diz4[anno]-Diz3[anno]
    if diz!={}:
        return diz
    else:
        raise ExamException("Errore: non è un intervallo con valori validi")
        
    



    
data=CSVTimeSeriesFile("../Downloads/GlobalLandTemperaturesByCountry.csv")
uno=data.get_data("Italy")
due=data.get_data("Japan")

print(compute_variation(uno,due,1945,1950))
'''

class ExamException(Exception):
    pass

class CSVTimeSeries():
    def __init__(self,nome):
        self.nome=nome
        try:
            with open(self.nome) as file:
                try:
                    next(file)
                except Exception as e:
                    raise ExamException("Errore: {}. File non leggibile".format(e))
        except Exception as e:
            raise ExamException("Errore: {}. File non esistente".format(e))
    
    def get_data(self, paese):
        lista=[]
        with open(self.nome) as file:
            for line in file:
                try:
                    a,b,c=line.replace("\n","").split(",")
                    if c==paese:
                        try:
                            lista.append([a,float(b)])
                        except:
                            continue
                except:
                    continue
        if lista==[]:
            raise ExamException("paese non presente nel file")
        return lista
    
data=CSVTimeSeries("../Downloads/aaa.csv")
time_series=data.get_data("Rome")
print(time_series)

def compute_slope(time_series, first_year, last_year):
    diz1={}
    if first_year>last_year:
        raise ExamException("intervallo non valido")
    for anno in range(first_year,last_year +1):
        lista=[]
        n=0
        for elem in time_series:
            if elem[0].startswith(str(anno)):
                lista.append(elem[1])
                n=n+1
        if n>=6:
            diz1[anno]=lista
    if diz1=={}:
        raise ExamException("intervallo non esistente")
    media_diz={}
    for anno in diz1:
        media=0
        n=0
        for elem in diz1[anno]:
            media=media+elem
            n=n+1
        media_diz[anno]=media/n
    print(media_diz)
    x=0
    y=0
    z=0
    for anno in diz1:
            x=x+anno
            z=z+1
            y=y+media_diz[anno]
    if z==0:
        raise ExamException("C'è qualche errore su n")
    xedia=x/z
    yenia=y/z
    m1=0
    m2=0
    for anno in diz1:
        m1=m1+(anno-xedia)*(media_diz[anno]-yenia)
        m2=m2+(anno-xedia)**2
    if m2==0:
        raise ExamException("C'è qualche errore con il denominatore")
    return m1/m2




print(compute_slope(time_series,1900,1902))








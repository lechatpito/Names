# Get a random first and last names according to their likeliness to appear in the US

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import re
import string
import datetime    
    
class Person:
    def __init__(self):  
        self.firstname=first_name()
        self.lastname=last_name()
        self.birth_date=birth_date()
        self.address=Address()
        self.email=email(self.firstname,self.lastname)
    
    def __str__(self):
        return "==Person==\nFirst name: "+self.firstname+"\nLast Name: "+self.lastname+"\nBirth date: "+str(self.birth_date)+"\nEmail: "+self.email+"\n-Address\n"+str(self.address)
                    
    
class Address:
    global streets
    global cities
    
    def __init__(self):
        __n=random.randrange(len(streets))
        self.street=streets[__n][1]
        self.street=self.street.rstrip()
        self.street=self.street.title()
    
        self.number=str(random.randrange(10000))  

        __n=random.randrange(len(cities))
        self.city=cities[__n][0]
        self.state=cities[__n][1]
        
        #borough=""
         #if street==streets[n][0]==1:
        #    borough='Algonquin'
        #if street==streets[n][0]==2:
        #   borough='Broker'
        #if street==streets[n][0]==3:
        #   borough='Dukes'
        #if street==streets[n][0]==4:
        #   borough='Bohan'
        #if street==streets[n][0]==5:
        #   borough='Parliament Island'
    
    def __str__(self):
        return "Street number: "+self.number+"\nStreet: "+self.street+"\nMunicipality: "+self.city+"\nState: "+self.state
        

#Names files processing
#Getting values from the files
# See files here: 
f=open('data/census-derived-all-first.txt')
flines=file.readlines(f)
fsplitlines=[]
for line in flines: fsplitlines.append(line.split())
fsplitlines.reverse()

g=open('data/dist.all.last')
glines=file.readlines(g)
gsplitlines=[]
for line in glines: gsplitlines.append(line.split())
gsplitlines.reverse()

u=open('data/emails-domains.txt')
domains=file.readlines(u)

s=open('data/street-names.txt')
lines=s.readlines()
streets=[]
p=re.compile('\w(\w)(.{32})\w{2}\w.{13}\s{1}.*')
for line in lines:
    m=p.match(line)
    if m:  streets.append(m.groups())

t=open('data/cities.txt')
lines=t.readlines()
cities=[]
p=re.compile('(.*);(.*);\d*')
for line in lines:
    m=p.match(line)
    if m:  cities.append(m.groups())

#Get a random name weighted by frequency
def get_name(pmin,pmax,lines):    
    n=list(lines)
    stop=0
    r=100
    while r>pmax: r=random.random()*100 #89.996 & 90.483
    #print '****************'
    #print r
    #print '****************'
    line=n[0]
    while (stop < 1 and r>pmin): #1.664 & 1.006
        line=n.pop()
        stop=float(line[2])>r
        if stop and len(n)>0:
            coin=random.choice([0,1])
            if coin: line=n.pop()    
    return line[0]

def first_name():
    return get_name(1.664,89.996,fsplitlines).title()

def last_name():
    return get_name(1.006,90.483,gsplitlines).title()

def full_name():
    name=get_name(1.664,89.996,fsplitlines),get_name(1.006,90.483,gsplitlines)
    return string.join(name).title()

def birth_date():
    now = datetime.datetime.now()
    return str(random.randrange(30)+1)+"-"+str(random.randrange(12))+"-"+str(now.year-random.randrange(18,101))

def email(fn,ln):
    global domains
    domain=domains[random.randrange(len(domains))]
    domain=domain.rstrip()
    x=random.randrange(5)
    if x==0:
        #firsnamelastname@domain
        return (fn+ln+'@'+domain)
    if x==1:
        #firsname.lastname@domain
        return (fn+"."+ln+'@'+domain)
    if x==2:
        #firsname.lastname@domain
        return (fn+"-"+ln+'@'+domain)
    if x==3:
        #flastname@domain
        return (fn[0]+ln+'@'+domain)
    if x==4:
        #firsnameRandomNr@domain
        number=random.randrange(10000)
        return (fn+str(number)+'@'+domain)        
    
def address():
    return Address()

    
if __name__ == "__main__":
    print str(Person())

    
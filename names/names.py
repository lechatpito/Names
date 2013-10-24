# Get a random first and last names according to their likeliness to appear in the US

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import re
import string
import datetime
import math

class Person:
    def __init__(self):  
        self.firstname=first_name()
        self.lastname=last_name()
        self.birth_date=birth_date()
        self.address=Address()
        self.email=email(self.firstname,self.lastname)
    
    def __str__(self):
        return self.firstname+" "+self.lastname+"\n"+str(self.age)+" years old"+"\n"+"email: "+self.email+"Address :\n"+str(self.address)
                    
    
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
        return self.number+" "+self.street+"\n"+self.city+", "+self.state

##Get a random name weighted by its frequency
# pmin and pmax are the min and max weights for names.
# lines is a list of names with weights
def get_name(pmin,pmax,lines):
    rand_val=random.random()*pmax
    lower=0
    upper=len(lines)-1
    return binary_search(lower,upper,rand_val,lines)

#finds the name corresponding to the value by performing a binary search in the lines tab
#returns the index of of the line tab corresponding to the value.
def binary_search(lower,upper,val,lines):
    med=int((lower+upper)/math.log(lower+upper))
    if val>=lines[med][2]:
        if val<float(lines[med+1][2]):
            name=lines[med][0]
        else:
            name=binary_search(med,upper,value,lines)
    else:
        if val>float(lines[med-1][2]):
            name=lines[med][0]
        else:
            if val<float(lines[1][2]):
                name=lines[0][0]
            else:
                name=binary_search(lower,med,val,lines)
    return name
    
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


#Names files processing
#Getting values from the files
# See files here: 
f=open('data/census-derived-all-first.txt')
flines=file.readlines(f)
fsplitlines=[]
for line in flines: fsplitlines.append(line.split())

g=open('data/dist.all.last')
glines=file.readlines(g)
gsplitlines=[]
for line in glines: gsplitlines.append(line.split())

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

  
    
    
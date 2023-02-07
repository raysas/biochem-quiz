#!/usr/bin/env python
# coding: utf-8

# # Chapter 2: Amino Acids- BioChemistry

# ## Import, Assign and Declare
# 
# *make sure you run this kernel before any other; not doing so will throw errors in the program*

# In[1]:


from random import *
from time import *

s=time();e=time()

aa={'A': 'Alanine',
 'R': 'Arginine',
 'N': 'Asparagine',
 'D': 'Aspartic acid',
 'C': 'Cysteine',
 'Q': 'Glutamine',
 'E': 'Glutamic acid',
 'G': 'Glycine',
 'H': 'Histidine',
 'I': 'Isoleucine',
 'L': 'Leucine',
 'K': 'Lysine',
 'M': 'Methionine',
 'F': 'Phenylalanine',
 'P': 'Proline',
 'S': 'Serine',
 'T': 'Threonine',
 'W': 'Tryptophan',
 'Y': 'Tyrosine',
 'V': 'Valine'
   }

#names of the aa when they're nternal residues (-yl)
residues={'A': 'Alanyl',
 'R': 'Argyl',
 'N': 'Asparagyl',
 'D': 'Aspartyl',
 'C': 'Cystyl',
 'Q': 'Glutaminyl',
 'E': 'Glutamyl',
 'G': 'Glycyl',
 'H': 'Histidyl',
 'I': 'Isoleucyl',
 'L': 'Leucyl',
 'K': 'Lysyl',
 'M': 'Methionyl',
 'F': 'Phenylalanyl',
 'P': 'Prolyl',
 'S': 'Seryl',
 'T': 'Threonyl',
 'W': 'Tryptophyl',
 'Y': 'Tyrosyl',
 'V': 'Valyl'
   }

#readily ionizable aa and approximation of their R group's pKa
ion={
    'R':13,
    'K':11,
    'H':6,
    'D':4,
    'E':4,
    'C':8,
    'Y':11
}
cation=['R','K','H']
anion=['D','E','C','Y']

symbols=aa.keys()

correct=0
count=0

def generate():
    '''generates a random amino acid symbol and returns it'''
    pick=choice(list(symbols))
    return pick

def name(a):
    '''takes an amino acid symbol and returns it full name'''
    return aa[a]

def ask(inp,ans):
    '''takes 2 strings: an input mquestion and its answer key and compares the prompted answer with key to return a boolean value'''
    guess=input(inp+":")
    if guess.lower()==ans.lower():
        print("yes.")
        return True
    print("nope. it's", ans)
    return False

def askCharge(inp,pH,ans):
    '''takes aas and pH and the correct charge, prompts the user for answer and compares; returns boolean value'''
    guess=input(inp+" for pH="+str(pH)+":")
    if guess.strip().lower()==ans.strip().lower():
        print("yes.")
        return True
    print("nope. it's", ans)
    return False

def createPeptide(chain_len):
    '''takes an integer and returns a random sequence of a peptide this length'''
    seq=''
    for i in range(chain_len):
        seq+=generate()
    return seq

def getCharge(a,pH):
    '''takes an amino acid at a specific pH and returns its charge'''
    if a not in ion.keys():
        #e.g. charge is considered neutral at pH of exactly 3 and exactly 9
        if pH<3:
            charge='+'
        elif pH>9:
            charge='-'
        else:
            charge='0'
    elif a in anion:
        if pH<3:
            charge='+'
        elif pH>ion[a]:
            charge='-'
        else:
            charge='0'
    else:
        if pH<9:
            charge='+'
        elif pH>ion[a]:
            charge='-'
        else:
            charge='0'
    return charge
        

def __process__():
    '''prints an animation for loading the answer
    yes i'm full of bullshit'''
    from time import sleep
    print('p',end='');sleep(1/5)
    print('r',end='');sleep(1/5)
    print('o',end='');sleep(1/5)
    print('c',end='');sleep(1/5)
    print('e',end='');sleep(1/5)
    print('s',end='');sleep(1/5)
    print('s',end='');sleep(1/5)
    print('i',end='');sleep(1/5)
    print('n',end='');sleep(1/5)
    print('g',end='');sleep(1/5)
    print('.',end='');sleep(1/2)
    print('.',end='');sleep(1/2)
    print('.',end='\n');sleep(1/2)

def evaluate(avg):
    '''evaluates the score given whether good or bad and returns the result'''
    __process__()
    if avg>.9:
        return ("astronomical ;D")
    elif avg>.8:
        return("shiny :D")
    elif avg>.6:
        return("time to revise a bit :)")
    elif avg>.4:
        return("study bro :(")
    else:
        return("bad bad bad bad... :/")
    

message='''
WELCOME TO BIOCHEM QUIZ VERSION 1.0!
------------------------------------
*this one deals with amino acids: naming, pH and charges
detail of each amino acid's properties will not be provided here
hopefully next versions will have them, not really dying to make one right now :p
*you can do whatever question at whatever order and with duplicates, chances same questions will be asked are pretty low
the answer of each question will be returned after one trial and all questions are equally worth
typos will be considered incorrect; answers are case-insesitive
make sure to run the last kernel to get how well you did
*re-running this kernel will automatically delete your prior score and restarts over
enjoy it, leave feedback below
last modified: 8:04PM 2/7/2023
'''
print(message)


# ### Problem I: Guess a.a.

# In[ ]:


count+=1
pick=generate()
sol=name(pick)

if ask(pick,sol):
    correct+=1

e=time()


# ### Problem II: Name the Di- and Tri-peptides

# In[ ]:


count+=1
chain_len=randint(2,3)

peptide='';seq=createPeptide(chain_len)

for j in range(chain_len-1):
    peptide+=residues[seq[j]]
    
peptide+=name(seq[chain_len-1])

if ask(seq,peptide):
    correct+=1
    
e=time()


# ### Problem III: Get pI

# In[ ]:


count+=1
a=generate()

print("make sure you put a floating point up to one decimal (e.g. 7.0)")

pka=[3,9]
pka.append(ion[a])
pka.sort()
if a not in ion.keys():
    pI=(3+9)/2
elif a in cation:
    pI=(pka[2]+pka[1])/2
elif a in anion:
    pI=(pka[0]+pka[1])/2

if ask(a,str(pI)):
    correct+=1
    
e=time()


# ### Problem IV: Get net Charge at specific pH

# In[ ]:


count+=1
a=generate()
pH=randrange(1,14)
charge=getCharge(a,pH)
        
print("valid answers are +, - or 0; \nnote whenever [zwitterion]=[ion @ pI edge] charge is counted null.")
    
if askCharge(a,pH,charge):
    correct+=1
    
e=time()


# ### Problem V: Get Charges of a peptide at a specific pH

# In[ ]:


count+=1
c=randint(3,8)
p=createPeptide(c)
pH=randrange(1,14)

print("note: answers for 0 positives and 1 negatives are in this format: 0 + 1 - ")

pos=1;neg=1 #total cations and anions taking into considerations the C and N termini
for a in p:
    if getCharge(a,pH)=='+':
        pos+=1
    elif getCharge(a,pH)=='-':
        neg+=1

total_charges=str(pos)+" + "+str(neg)+" -"
if askCharge(p,pH,total_charges):
    correct+=1
    
e=time()


# ## End quiz results

# In[ ]:


if count==0:
    print("how the hell you're gonna get stats if no answers are counted yet :/")
else:
    avg=correct/count
    print("\t\tSTATS:\n------------------------------------\n")
    print("score:\t\t\t%.2f/100"%(avg*100))
    print("total qestions:\t\t%d"%count)
    print("total correct:\t\t%d"%correct)
    print("time spent in seconds:\t%d"%(e-s))
    print(evaluate(avg))
    print("\np.s. no feedback will be taken lol\n3afekun 3iduwa teb2o :p\n------------------------------------\n")


# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 15:07:15 2021

@author: jjqoj
"""

import json
import requests
#from pprint import pprint

# Ejercicio 1 json

with open('D:/Users/JJQOJJ/Documents/JJQOJJ PESSOAL/0. AGE/5. MISION TIC 2022/PG CICLO 1/Ejercicios3.json',"r",encoding="utf-8") as f:
    data=json.load(f)


deporte="Tejo"
edad_min=30
edad_max=40


for nick,info in data.items():
    for i in info["deportes"]:
        if i==deporte:
            print(info["nombres"],info["apellidos"])

for nick,info in data.items():
    if info["edad"]>=edad_min and info["edad"]<=edad_max:
        print(info["nombres"],info["apellidos"])


user_deportes={}

for nick,info in data.items():
    for i in info["deportes"]:
        if i not in user_deportes:
            user_deportes[i]=[]

for deporte_i,vector_i in user_deportes.items():
    for nick,info in data.items():
        for i in info["deportes"]:
            if deporte_i==i:
                vector_i.append(nick)


with open('D:/Users/JJQOJJ/Documents/JJQOJJ PESSOAL/0. AGE/5. MISION TIC 2022/PG CICLO 1/Ejercicios3_deport.json',"w",encoding="utf-8") as g:    
   json.dump(user_deportes,g,indent=2)       

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 19:29:23 2021

@author: jjqoj
"""

# texto="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
# d={}

# for c in texto:
#     if c not in d:
#         d[c]=0
#     d[c]+=1
    
# print(d)


# Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.


dic_1={"Brasil":210461000,"México" : 125357000,"Colombia" : 49737000,"Argentina" : 44723000,
"Perú" : 32362000,
"Venezuela" : 32030000,
"Chile" : 18880000,
"Guatemala" : 17545000,
"Ecuador" : 17170000,
"Bolivia" : 11390000,
"Haití" : 11220000,
"Cuba" : 11212000,
"República Dominicana" : 10315000,
"Honduras" : 9087000,
"Paraguay" : 7104000,
"El Salvador" : 6675000,
"Nicaragua" : 6494000,
"Costa Rica" : 5032000,
"Panamá" : 4190000,
"Uruguay" : 3512000}


dic_2={"Brasil":210461000,"México" : 125357000}

dic_3={"Portugal":55555,"México" : 99999999,"Colombia" : 49737000,"España" : 7777777,
"Alemania" : 4444444}


D1={'nombre':'Carlos', 'Apellido':'Suares','nota1':3.8, 'nota2':4.1}
D2={'nombre':'Carlos','nota1':3.8}
D3={'nombre':'Carlos', 'nota2':4}
D4={'Apellido':'Suares','nota1':3.8, 'notaFinal':4.1}


def orden_values(dic):
    val=[]
    val=list(dic.values())
    val.sort()
    print(val)


#orden_values(dic_1)

# Desarrollar un algoritmo que verique si todas las clave:valor de un diccionario se encuentran en otro diccionario.
def clave_valor(dic_1,dic_2):
    for clave,valor in dic_2.items(): #x
        if clave not in dic_1: #X se revisa en el dic_2
            return False
        elif dic_1[clave]!=valor:
            return False
        else:
            print(" ",clave,valor)
    return True


#print(clave_valor(dic_1,dic_1))

#print(clave_valor(D1,D2))

def new_dicc(d1,d2):
    dic_novo={}
    dic_novo.update(d1)
    for clave_2 in d2:
        if clave_2 not in d1:
            dic_novo[clave_2]=d2[clave_2]
    return dic_novo


#print(new_dicc(dic_3,dic_2))



A={"nombres":"John Jairo","apellidos":"Quiroga Orozco","edad":32}
B={"nombres":"Fermat","apellidos":"Augusto","edad":58}
C={"nombres":"Banach","apellidos":"Oliveira","edad":32}
D={"nombres":"Galois","apellidos":"Franco","edad":62}
E={"nombres":"Hilbert","apellidos":"Espinoza","edad":48}
F={"nombres":"Newton","apellidos":"Gonzales","edad":78}
G={"nombres":"Cantor","apellidos":"Conjuntos","edad":85}

BASE_DATOS=[A,B,C,D,E,F,G]

#print(BASE_DATOS)

def imprimir(BASE_DATOS,edad_min,edad_max):
    contador=0
    for i in range(len(BASE_DATOS)):
        if BASE_DATOS[i]["edad"]>=edad_min and BASE_DATOS[i]["edad"]<=edad_max:
            print(BASE_DATOS[i]["nombres"],BASE_DATOS[i]["apellidos"])
            contador+=1
    if contador==0:
         print("No existen usuarios en los rangos entre",edad_min,"hasta",edad_max,"años")

imprimir(BASE_DATOS,40,50)





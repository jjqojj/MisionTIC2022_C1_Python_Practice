# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 14:36:46 2021

@author: jjqoj
"""


def material(X):
    try:
        material_piezas=[]
        for material in X:
            if material not in material_piezas:
                material_piezas.append(material)
        return material_piezas
    except:
       material_piezas=[]
       return material_piezas
       
       
def mefaltandelmaterial(X_codigos:list,Y_materiales:list,Z_material):
    dicc={}
    faltantes=[]
    for i in range(len(Y_materiales)):
        dicc[i]=Y_materiales[i]
    for j in X_codigos:
        for clave,material in dicc.items():
            if Z_material==material and j==clave:
                faltantes.append(j)
    return faltantes



# def mefaltandelmaterial(X_codigos:list,Y_materiales:list,Z_material):
#     dicc={}
#     faltantes=[]
#     for i in range(len(Y_materiales)):
#         dicc[i]=Y_materiales[i]
#     for clave,material in dicc.items():
#         for j in X_codigos:
#             if Z_material==material and j==clave:
#                 faltantes.append(clave)
#     return faltantes
#
#NOTAÇ código correcto, error en el "juez"de Moodle, no consideró la permutación de los elementos de la lista de salida

   

def notengo(X_otra,Y_yo):
    try:
        quiero=[]
        for pieza in X_otra:
            if pieza not in Y_yo:
                quiero.append(pieza)
        return quiero
    except:
        quiero=[]
        return quiero
    

def puedocambiar(X_otra,Y_yo):
    try:
        quiero_otra=[]
        for pieza in Y_yo:
                if pieza not in X_otra:
                    quiero_otra.append(pieza)
        quiero_yo=[]
        for pieza in X_otra:
                if pieza not in Y_yo:
                    quiero_yo.append(pieza)
        cantidad_otra=len(quiero_otra)
        cantidad_yo=len(quiero_yo)
        total_cambiar=min(cantidad_otra,cantidad_yo)
        return total_cambiar
    except:
        total_cambiar=0
        return total_cambiar
            

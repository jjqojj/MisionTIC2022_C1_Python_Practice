# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:31:43 2021

@author: jjqoj
"""

# def division(a,b):
#     try:
#         coc=a//b
#         res=a%b
#         return (coc,res)
#     except:
#         print("Error burro")
#         return ""

# def main():
#     try:
#         num=int(input("num: "))
#         den=int(input("den: "))
#         print(division(num,den))
#     except ValueError:
#         print("Digitó mal seu burro")

# main()


def div():
    try:
        num=int(input("Escriba: "))
        re=100/num
    except Exception as e:
        print(e,"\n",type(e))
    else:
        print("El resultado es",re)
    finally:
        print("Gané")

#div()

# Ejercicio 1 - excepción


def lista_error():
    try:
        lista=[1,2,3,4]
        lista[5]
    except:
        print("Mal burro jaja")


# Ejercicio 2

def operar(a,b):
    try:
        return a+b
    except:
        print("Solo puede sumar números reales")

def main():
    a=int(input())
    b="hola"
    operar(a,b)


#main()


def main_2():
    try:
        dict_1={"James":"Java", "Dennis":"C", "Das":"Python"}
        print(dict_1["Ada"])
    except:
        print("La clave ingresada no existe en el diccionrario")


#main_2()

############################################################################
##### LIBRERIAS

# import numpy as np

# # a=np.array(list(range(1,5)))
# # print(type(a))
# # print(a)
# # print(a.shape)


# # b=np.array([[1,2,3,4,5],[4,5,6,7,8]])
# # print(type(b))
# # print(b)
# # print(b.shape)


# # c=np.zeros((2,3,4))

# # print(c)


# # Crea un arreglo 2-dimensional con forma (3, 4)
# # a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# # print(a.shape)
# # print(a)
# # print("espacio")
# # b = a[:1, 2:4]
# # # El primer argumento indica las filas y el segundo las columnas
# # print(b)
# # print("------------------------")


# # x = np.array([[1,2,5], [3,4,6]], dtype=np.float64)
# # y = np.array([[5,6,-1], [7,8,-6]], dtype=np.float64)
# # print("Suma:")
# # print(x + y)
# # print("-----")
# # print(np.add(x, y))
# # print("raiz cuadrada:")
# # print(np.sqrt(y))


# import matplotlib.pyplot as plt



# # x = np.linspace(0, 2, 50)
# # #print(x)
# # # Aun con el OO-style, usamos ".pyplot.figure" para crear la figura.
# # fig, ax = plt.subplots() # Crea la figura y los ejes.
# # ax.plot(x, x, label="linear") # Dibuja algunos datos en los ejes.
# # ax.plot(x, x**2, label="quadratic") # Dibuja mas datos en los ejes.
# # ax.plot(x, x**3, label="cubic") # ... y algunos mas.
# # ax.set_xlabel("x label") # Agrega un x-label a los ejes.
# # ax.set_ylabel("y label") # Agrega un y-label a los ejes.
# # ax.set_title("Simple Plot") # Agrega ttulo a los ejes.
# # ax.legend() # Agrega una leyenda.


# # names = ["group_a", "group_b", "group_c"]
# # values = [3.4, 50.3, 23]
# # plt.figure(figsize=(9, 3))
# # plt.subplot(131)
# # plt.bar(names, values)
# # plt.subplot(132)
# # plt.scatter(names, values)
# # plt.subplot(133)
# # plt.plot(names, values)
# # plt.suptitle("Categorical Plotting")
# # plt.show()


# # dictc = {"country": ["Brazil", "Russia", "India",
# # "China", "South Africa", "Colombia"],
# # "capital": ["Brasilia", "Moscow", "New Dehli",
# # "Beijing", "Pretoria", "Bogota"],
# # "area": [8.516, 17.10, 3.286, 9.597, 1.221, 1.142],
# # "population": [200.4, 143.5, 1252, 1357, 52.98, 49.65] }
# import pandas as pd
# from collections import Counter
# # brics = pd.DataFrame(dictc)
# # print(brics)


# print(uploaded)


# cp = Counter(uploaded["Country"])
# print(cp.most_common(3))


# cp = Counter(uploaded["Price"])
# print(cp.most_common(3))





import pandas as pd
import datetime
import matplotlib.pyplot as plt

url="https://raw.githubusercontent.com/arleserp/MinTIC2022/master/files/SalesJan2009.csv"
ventasdf=pd.read_csv(url)


#Reporte por fecha
ventasdf["Transaction_date"]=pd.to_datetime(ventasdf["Transaction_date"])
A = (ventasdf["Transaction_date"]
    .dt.floor("d")
    .value_counts()
    .rename_axis("date")
    .reset_index(name="num ventas"))
G=A.plot(x="date",y="num ventas",color="green",title="Ventas por fecha")
plt.show()

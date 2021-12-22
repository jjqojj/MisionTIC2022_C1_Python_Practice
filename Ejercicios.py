# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:20:44 2021

@author: jjqoj
"""

from math import pi
from math import sqrt
import sys





def volumen_solido(r_1,r_2,h):
    if r_1<=0 or r_2<=0 or h<=0:
        return print("¡ERROR! Revise los valores ingresados, todos deben ser reales positivos")
    else:
        return print(((4/3)*pi*r_1*r_1**2)+((1/3)*pi*h*r_2**2))



def area_lateral_1(a,b,r):
    if a<=0 or b<=0 or r<=0:
        return print("¡ERROR! Revise los valores ingresados, todos deben ser reales positivos")
    else:
        return print(a*b+2*pi*r**2)



def area_lateral_2(a_2,b_2,a_1,b_1,r_1,r_2):
    if a_1<=0 or a_2<=0 or b_1<=0 or b_2<=0 or r_1<=0 or r_2<=0:
        return print("¡ERROR! Revise los valores ingresados, todos deben ser reales positivos")
    else:
        return print(a_2*b_2+a_1*b_1+pi*(r_1**2+r_2**2))


def carne(gallinas,gallos,pollitos):
    if gallinas<=0 or gallos<=0 or pollitos<=0:
        return print("¡ERROR! Revise los valores ingresados, todos deben ser reales positivos")
    else:
        return print(6*gallinas+7*gallos+pollitos)
    
    
def vueltas(B,P,M,H):
    costo=P*300+M*3300+H*350
    dif=B-costo
    if dif<0:
        return print("Debe en la compra",abs(dif))
    else:
        return print("Sobra de la compra",dif)
    
    
def prestamo(P,t):
    tiempo=str(t)
    deuda=int(P*(1+0.03)**t)
    return print("Para el mes "+tiempo+" debe cancelar",deuda)


def contagiados(C_inicial,D_dias):
    total=C_inicial*(2**(D_dias-1))
    return print("El total de contagiados en el día ",D_dias," es ",total)










#Problemas 08062021


def verificador_ASCII(num_int):
    if num_int>96 and num_int<123:
        aux=chr(num_int)
        return print("El entero",num_int, "corresponde a la letra minúscula en ASCII:",aux)
    else:
        return print ("El valor ingresado o no es un entero o no corresponde a una letra minúscula en ASCII")






def verificador_parimpar(var):
    aux=ord(var)
    if aux%2==0:
        return print("La cadena de longitu 1 <<",var, ">> su código ASCII es par.") 
    else:
        if aux%2!=0:
            return print("La cadena de longitu 1 <<",var, ">> su código ASCII es impar.") 


def ver_digito(var):
    aux=ord(var)
    if aux>47 and aux<58:
        return print("El caractér <<",var,">> es un dígito")
    else:
         return print("El caractér <<",var,">> no es un dígito")
     


def ver_tricotomia(num):
    if num>0:
        return print("El número",num,"es positivo")
    elif num<0:
        return print("El número",num,"es negativo")
    elif num==0:
        return print("El número",num,"es el neutro para la suma")
        
        
    
def ver_punto(cx,cy,px,py,r):
    cateto_x=abs(cx-px)
    cateto_y=abs(cy-py)
    pitagoras=sqrt(cateto_x**2+cateto_y**2)
    if pitagoras<r:
        return print("El punto (",px,",",py,") pertenece al círculo con centro (",cx,",",cy,") y radio r=",r)
    else:
        return print("El punto (",px,",",py,") no pertenece al círculo con centro (",cx,",",cy,") y radio r=",r)















def ver_triangulo(l_1,l_2,l_3):
    if l_1+l_2>l_3 and l_1+l_3>l_2 and l_2+l_3>l_1:
        return print("Si se puede construir un triángulo")
    else:
        maximo=max(l_1,l_2,l_3)
        if maximo==l_1:
            if l_2-l_3<=0:
                return print("No se puede construir un triángulo, se debe ajustar el segmento dos con valor mayor a",l_2)
            else:
                return print("No se puede construir un triángulo, se debe ajustar el segmento tres  con valor mayor a ",l_3)
        if maximo==l_2:
            if l_1-l_3<=0:
                return print("No se puede construir un triángulo, se debe ajustar el segmento uno con valor mayor a ",l_1)
            else:
                return print("No se puede construir un triángulo, se debe ajustar el segmento tres con valor mayor a ",l_3)
        if maximo==l_3:
            if l_1-l_2<=0:
                return print("No se puede construir un triángulo, se debe ajustar el segmento uno con valor mayor a ",l_1)
            else:
                return print("No se puede construir un triángulo, se debe ajustar el segmento dos con valor mayor a ",l_2)
                


##################################### Ejercicios 09/06/2021

def min_maquina():
    Xo=1
    Xi=Xo/2.0
    while Xi>0.0:
        Xo=Xi
        Xi=Xo/2.0
    return Xo

# Problema 1 - ciclos

# i=1
# while i>2:
#     print(i)
#     i+=1
# print("No ingresó al ciclo")


def problema_3(num_int):
    while num_int>64 and num_int<91:
        num_int=int(input("El valor ingresado corresponde a una letra mayúscula abc del ingles en código ASCII, registre un nuevo número entero: "))
    return print("El valor ingresado NO corresponde a una letra mayúscula abc del ingles en código ASCII")

# suma=0
# while True:
#     dato=int(input("ok "))
#     if dato==0:
#         break
#     suma+=dato
# print("La suma es: " + str(suma))



# Parte 2


def problem_1():
    num=1
    while num<=100:
        cuadrado=num**2
        print("El cuadrado de "+str(num)+" es "+str(cuadrado))
        num+=1



def problem_2():
    num=1
    while num%2!=0 and num<=999:
        print("Número impar:",num,end=" ")
        num+=2
    num=2
    while num%2==0 and num<=1000:
        print("Número par:",num,end=" ")
        num+=2

def problem_3(num):
    while num% 2==0 and num>=2:
        print(num)
        num-=2
    print("El número ingresado no es un número par")

def problem_4():
    paisA=25000000
    paisB=18900000
    x=0
    while paisA>paisB:
        tasa_crecimientoA=((paisA*2)/100)
        tasa_crecimientoB=((paisB*3)/100)
        paisA+=tasa_crecimientoA
        paisB+=tasa_crecimientoB
        x+=1
    ano=2020+x
    print("El país B superará en población al país A en el año",ano)


def problem_5():
    n=0.0
    e_1=2**n
    e_2=2**(n-1.0)
    valor_1=e_1+1.0
    valor_2=e_2+1.0
    while valor_1-valor_2!=0:
        n-=1.0
        e_1=2**n
        e_2=2**(n-1.0)
        valor_1=e_1+1.0
        valor_2=e_2+1.0
    print(1,"+", e_2)


# Ciclos para

def suma(entero):
    suma_partial=0
    for i in range(entero+1):
        suma_partial+=i
    return suma_partial

def main():
    n=int(input("n?= "))
    print("La suma de los primeros n números es:", end=" ")
    print(suma(n))


def problem_1_for():
    for i in range(100):
        print("El cuadrado de ",i+1," es ",(i+1)**2)

def problem_2_for():
    for i in range(1000):
        if (i+1)%2!=0:
            print("Número impar",i+1,end=" ")
    print("")
    for i in range(1000):
        if (i+1)%2==0:
            print("Número par",i+1,end="     ")

def problem_3_for(num_par):
    for i in range(num_par,0,-2):
        if i%2==0:
            print(i)
    
def problem_4_for(num_int):
    
    for i in range(1,num_int+1):
        factorial=1
        for j in range (1,i+1):
            factorial=factorial*j
        print(i, " su factorial es ",factorial)
            

def problem_5_for(n):
    valor=[2]
    resultado=1
    for i in valor*(n):
        resultado=resultado*i
    print(resultado)
        
def problem_6_for(n,x):
    lista=[x]
    resul=1
    for j in lista*n:
        resul=resul*j
    print(resul)
    
def problem_7_for():
    for i in range(1,11):
        print("Tabla de multiplicar del",i)
        print("")
        for j in range (1,11):
            print(i,"x",j,"=",i*j)
        print("")
        print("")


def x_elevado(x,n):
    lista=[x]
    resul=1
    for j in lista*n:
        resul=resul*j
    return resul

def factorial(num_int):
    
    for i in range(1,num_int+1):
        factorial=1
        for j in range (1,i+1):
            factorial=factorial*j
    return factorial





def exp(x,n):
    suma=1
    for i in range(1,n):
        calculo=float(x_elevado(x,i))/float(factorial(i))
        suma=suma+calculo
    print(suma)

def sen(x,n): #recuerde que x son valoresen radianes
    suma=x
    for i in range (1,n):
        calculo=(x_elevado(-1,i)*x_elevado(x,2*i+1))/(factorial(2*i+1))
        suma=suma+calculo
    print(suma)


# Tuplas, listas y matrices


# Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

def promedio(A):
    m=len(A)
    sum_A=0
    for i in range(m):
        sum_A+=A[i]
    average=sum_A/m
    return average


# Producto punto
def producto_punto(A,B):
    n_A=len(A)
    n_B=len(B)
    if n_A==n_B:
        producto=0
        for i in range(n_A):
            producto+=A[i]*B[i]
    print(producto)
    
# Producto directo

def producto_directo(A,B):
    n_A=len(A)
    n_B=len(B)
    if n_A==n_B:
        producto=[]
        for i in range(n_A):
            producto.append(A[i]*B[i])
    print(producto)
    
# Mediana

def mediana(A):
    n_A=len(A)
    B=sorted(A)
    if n_A%2!=0:
        print(B[(n_A//2)])
    else:
        print(promedio([B[(n_A//2)-1],B[(n_A//2)]]))
        
# Problema 5 - dejar ceros al final del vector




def ceros_final(A):
    C=[]
    n_A=len(A)
    contar=0
    for i in range(n_A):
        if A[i]!=0:
            C.append(A[i])
        else:
            contar+=1
    n_A=len(A)
    while contar>0:
        C.append(0)
        contar-=1
    print(C)
            

    
# ceros_final([0,0,0,1,0,6,3,0,8,9,7,0,0,8,5,0])


def suma_matrices(A,B):
# Revisando si las matrices están bien definidas para la operación
    verificar_A=[]
    verificar_B=[]
    C=[]
    if len(A)==len(B):
        for i in range(len(A)):
            verificar_A.append(len(A[i]))
        if max(verificar_A)!=min(verificar_A):
            print("Error")
            sys.exit()
        else:
            columna_A=len(A[0])
        for j in range(len(B)):
            verificar_B.append(len(B[i]))
        if max(verificar_B)!=min(verificar_B):
            print("Error")
            sys.exit()
        else:
             columna_B=len(A[0])
        if columna_A==columna_B:
            for i in range(len(A)):
                fila=[]
                for j in range(len(A[0])):
                    fila.append(A[i][j]+B[i][j])
                C.append(fila)
    else:
        print("Error")
        sys.exit()
    print(C)
        


A=[[1,2,3],[4,5,6]]
B=[[7,8,9],[10,11,12]]


suma_matrices(A,B)
            
        
def producto_matrices(A,B):
# Revisando si las matrices están bien definidas para la operación
    verificar_A=[]
    filas_A=len(A)
    verificar_B=[]
    filas_B=len(B)
    for i in range(len(A)):
        verificar_A.append(len(A[i]))
    if max(verificar_A)!=min(verificar_A):
        print("Error")
        sys.exit()
    else:
        columnas_A=len(A[0])
    for j in range(len(B)):
        verificar_B.append(len(B[i]))
    if max(verificar_B)!=min(verificar_B):
        print("Error")
        sys.exit()
    else:
        columnas_B=len(B[0])
# Fin de las verificaciones, matrices consistentes
    if columnas_A==filas_B: #Criterio para poder hacer el producto
# Creando una matriz C de ceros con el tamaño generado por el futuro producto
        C=[]
        fila_cero=[]
        contador_1=columnas_B
        contador_2=filas_A
        while contador_1>0:
            fila_cero.append(0)
            contador_1-=1
        while contador_2>0:
            C.append(fila_cero.copy())
            contador_2-=1
# Fin de la matriz de ceros
# Inicio def producto matricial
        for i in range(filas_A):
            suma=0
            #fila_C=[]
            for j in range(columnas_B):
                suma=0
                for w in range(filas_B):
                    suma+=A[i][w]*B[w][j]
                    C[i][j]=suma
        print(C)
    else:
        print("Error")
        sys.exit()



#A=[[3,4,5,3],[2,5,1,2],[1,7,2,6]]
#B=[[9,1],[7,2],[6,3],[2,4]]

#producto_matrices(A,B)



def cuadrado_magico(A):
# Revisando si las matrices están bien definidas para la operación
    verificar_A=[]
    filas_A=len(A)
    for i in range(len(A)):
        verificar_A.append(len(A[i]))
    if max(verificar_A)!=min(verificar_A):
        print("Error, matriz mal definida")
        sys.exit()
    else:
        columnas_A=len(A[0])
# Control de matrices cuadradas
    if filas_A==columnas_A:
        resultado_filas=[]
        resultado_columnas=[]
        suma_diagonal_1=0
        suma_diagonal_2=0
        for i in range(filas_A):
            suma_filas=0
            for j in range(columnas_A):
                suma_filas+=A[i][j]
            resultado_filas.append(suma_filas)
# Criterio de filas - inicio
        if max(resultado_filas)!=min(resultado_filas):
            print("No es un cuadrado mágico")
            sys.exit()
# Criterio de filas - fin
        for i in range(filas_A):
            suma_columnas=0
            for j in range(columnas_A):
                suma_columnas+=A[j][i]
            resultado_columnas.append(suma_columnas)
# Criterio de columnas - inicio
        if max(resultado_columnas)!=min(resultado_columnas):
            print("No es un cuadrado mágico")
            sys.exit()
# Criterio de columnas - fin
        for w in range(filas_A):
            suma_diagonal_1+=A[w][w]
        contador=0
        for s in range(filas_A-1,-1,-1):
            suma_diagonal_2+=A[s][contador]
            contador+=1
    if suma_filas==suma_columnas and suma_diagonal_1==suma_diagonal_2 and suma_filas==suma_diagonal_1:
        print("Es un cuadrado mágico")
    else:
        print("No es un cuadrado mágico")
            
            
            
#A=[[8,1,6],[3,5,7],[4,9,2]]
#B=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]    

#D=[[10,1,6],[3,5,7],[4,9,2]]   
#E=[[8,1,6,7],[3,5,7],[4,9,2]]  

#cuadrado_magico(E)
            

            
  
        
        
        
        

















    
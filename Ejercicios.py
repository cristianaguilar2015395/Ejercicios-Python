from math import sqrt
from operator import itemgetter
#EJERCICIO 1 "Dado un entero, determinar si es par."

def ejercicio_1(valor):
    if valor%2==0:
        return True
    else:
        return False
           
#EJERCICIO 2 "Dado un número real representando una temperatura
             #en grados Farenheit, encontrar su equivalente en grados Celcios"

def ejercicio_2(valor):
    valorFh = ((valor)-32)*5/9
    return valorFh

#EJERCICIO 3 "Dados dos enteros (base y potencia, en este orden), determinar manualmente
             #el valor que se obtiene al evaluar base^potencia"5 

def ejercicio_3(valor1, valor2):
    return valor1**valor2


#EJERCICIO 4 "Dada una hilera de caracteres y una longitud de párrafo (en este orden),
             #devolver una hilera de caracteres que centre la palabra en un párrafo de
             #ancho como el dado, utilizando de relleno asteriscos"

def ejercicio_4(x,y):
    a = 0
    for i in x:
        if(i.isalpha() or i == 0,9):
            a += 1
    b = y - a
    c = b/2
    z = '*' * int(c)
    print(z,x,z)

#EJERCICIO 5 "Dadas dos listas, representando dos vectores, encuentre el vector
             #resultante del producto cruz entre ambos vectores dados."

def ejercicio_5(lista1, lista2):
    resultado = [lista1[1]*lista2[2] - lista1[2]*lista2[1],
                 lista1[2]*lista2[0] - lista1[0]*lista2[2],
                 lista1[0]*lista2[1] - lista1[1]*lista2[0]]
    return resultado

#EJERCICIO 6 "Dada una lista ordenable, devuelva otra lista con los mismos
             #elementos, pero en orden descendente. Implemente el algoritmo de
             #Bubble Sort."

def ejercicio_6(lista):
    valores = lista
    v = len(valores)
    for i in range(v):
        for j in range(0, v-i-1):
            if valores[j]<valores[j+1]:
                valores[j],valores[j+1] = valores[j+1],valores[j]
    return valores

#EJERCICIO 7 "Encuentre una lista con todos los múltiplos de 4 o 7, menores
             #a 1000, presente la lista ordenada de menor a mayor."

def ejercicio_7():
    lista1 = [x for x in range (1000) if x %4==0 or x %7==0]
    return lista1

#EJERCICIO 8 "Dado un entero mayor que cero, imprima un triángulo de dicha
             #altura, usando asteriscos."

def ejercicio_8(x):
    for i in range(1,x):
      print(' '*(x-i),'* '*(i))

#EJERCICIO 9 "Dados tres números (en ningún orden en particular), determinar
             #si estos podrían representar los lados de un triángulo rectángulo
             #(estos grupos de tres números se conocen como Tripletas Pitagóricas)"
      
def ejercicio_9(num1,num2,num3):
    if num1>num2 and num1>num3 or num2>num1 and num2>num3 or num3>num2 and num3>num1 or num1>num2 and num1>num3 or num2>num1 and num2>num3 or num3>num2 and num3>num1:
        if num2 ** 2 + num3 ** 2 == num1 ** 2 or num1 ** 2 + num2 ** 2 == num3 ** 2 or num3 ** 2 + num1 ** 2 == num2 ** 2:
          return True
        else:
          return False

#EJERCICIO 10 "Dadas tres tuplas (en ningún orden en particular) representando
              #tres puntos en un espacio bidimensional, determine el tipo de
              #triángulo que representan. No asuma inmediatamente que los puntos
              #representan un triángulo.'

def ejercicio_10(x1,x2,x3):
    if x1>180 or x2>180 or x3>180:
        return False
    if x1==0 or x2==0 or x3==0:
        return False
    
    if x1==x2 and x2==x3:
        return("Equilatero")
    
    if x1==x2 or x1==x3 or x2==x3:
        return("Isosceles")
    
    if x1 != x2 and x2 != x3:
        return("Escaleno")
    
    if x1>90 or x1<180 and x1<90 and x2>90 or x2<180 and x2<90 and x3>90 or x3<180 and x2<90:
        return("Obtuso")
    
    if x1==90 or x2==90 or x3==90:
        return("Rectangulo")
    

#EJERCICIO 11 "Dada una hilera de caracteres, determine si es un Palíndromo."

def ejercicio_11(x):
    palabra = ''
    cont = len(x)
    indice = -1
    while cont > 0:
        palabra += x[indice]
        indice -= 1
        cont -= 1
    if palabra == x:
        return True
    else:
        return False

#EJERCICIO 12 "Dado un número entero positivo menor o igual que 1000, encuentre
              #su representación en palabras"

NUM_MAX = 1000

UNIDADES = (
    'cero', 'uno', 'dos', 'tres','cuatro', 'cinco', 'seis', 'siete', 'ocho','nueve'
)
                                                                                                                    
DESP_DIEZ = (
    'diez', 'once', 'doce', 'trece', 'catorce', 'quince','dieciseis','diecisiete','dieciocho','diecinueve'
)

DECENAS = (
    'cero','diez','veinte','treinta','cuarenta','cincuenta','sesenta','setenta','ochenta','noventa'
)

CIENTOS = (
    '_','ciento','doscientos', 'trescientos','cuatroscientos','quinientos','seiscientos','setecientos','ochocientos','novecientos'
)

def ejercicio_12(numero):
    numero_entero = int(numero)
    if numero_entero > NUM_MAX:
        raise OverflowError('ERROR, Elija un numero menor o igual a 1000')
    if numero_entero < 0:
        return 'menos %s' % representacion_letras(abs(numero))
    letras_decimal = ''
    parte_decimal = int(round((abs(numero) - abs(numero_entero)) * 100))
    if parte_decimal > 9:
        letras_decimal = 'punto %s' % representacion_letras(parte_decimal)
    elif parte_decimal > 0:
        letras_decimal = 'punto cero %s' % representacion_letras(parte_decimal)
    if (numero_entero <= 99):
        resultado = decenas(numero_entero)
    elif (numero_entero <= 999):
        resultado = centenas(numero_entero)
    else:
        return ("MIL (Numero maximo permitido)")
    if parte_decimal > 0:
        resultado = '%s %s' % (resultado, letras_decimal)
    return resultado

def decenas(numero):
    if numero < 10:
        return UNIDADES[numero]
    decena, unidad = divmod(numero, 10)
    if numero <= 19:
        resultado = DESP_DIEZ[unidad]
    elif numero <= 29:
        resultado = 'veinti%s' % UNIDADES[unidad]
    else:
        resultado = DECENAS[decena]
        if unidad > 0:
            resultado = '%s y %s' % (resultado, UNIDADES[unidad])
    return resultado

def centenas(numero):
    centena, decena = divmod(numero, 100)
    if numero == 0:
        resultado = 'cien'
    else:
        resultado = CIENTOS[centena]
        if decena > 0:
            resultado = '%s %s' % (resultado, decenas(decena))
    return resultado


#EJERCICIO 13 "Dado un entero positivo, determinar la suma de sus divisores propios."

def ejercicio_13(x):
    valorx = 0
    for i in range(1,x+1):
        if x % i == 0:
            valorx += i
    return valorx
    

#EJERCICIO 14 "Dado un entero positivo, determinar si es un Número primo."

def ejercicio_14(numero):
    if numero < 2:
        return False
    for i in range(2,numero):
        if numero%i == 0:
            return False
        return True
        

#EJERCICIO 15 "Dado un entero positivo, determinar si es un Número perfecto.'

def ejercicio_15(numero):
    suma = 0
    for i in range(1,numero):
        if(numero % i == 0):
            suma = suma + i
    if numero == suma:
        return True
    else:
        return False

#EJERCICIO 16 "Dados dos enteros positivos, determinar si son Números amigos."

def ejercicio_16(x,y):
    valorx = 0
    valory = 0
    for i in range(1,x):
        if x%i==0:
            valorx+=i

    for k in range(1,y):
        if y%k==0:
            valory+=k
    return valorx==y and valory==x
       
    
#EJERCICIO 17 "Dados dos enteros positivos, determinar si son Primos relativos."

def ejercicio_17(valor1,valor2):
    array = []
    for i in range(2,valor1):
        if valor1 % i == 0:
            array.append(i)
    for i in range(2, valor2):
        if valor2 % i == 0 and i in array:
            return False
        return True

#EJERCICIO 18 "Dado un entero positivo, determinar si pertenece a la Serie
              #de Fibonacci."

def ejercicio_18(valor1):
    x = 0
    y = 1
    while x < valor1:
        print(x, end = ', ')
        x,y = y,x+y 
    return valor1 

#EJERCICIO 19 "Dado un entero positivo, determinar el primer número de la
              #Serie de Fibonacci que cumple con tener al menos ese número
              #de dígitos."

def ejercicio_19(valor1):
    x=0
    def Fibonacci(num):
        if num==1 or num==0:
            return num
        else:
            return Fibonacci(num-2) + Fibonacci(num-1)
    for x in range (0,valor1):
        print(Fibonacci(x))

#EJERCICIO 20 "Encuentre todas las Tripletas Pitagóricas que cumplen"

def ejercicio_20():
    ar=[]
    for a in range (1,1000):
        for b in range(a+1,1000):
            x =  b**2 - a**2
            y = 2*a*b
            z = a**2+b**2
            if((x**2 + y**2) == z**2) and (x+y+z) == 1000:
                ar.append([x,y,z])
    return ar
            
    

#EJERCICIO 21 "Dado un entero positivo, encontrar todos los números primos
              #menores o iguales a dicho entero."

def ejercicio_21(numero):
    lista = []
    for i in range(2, numero+1):
        if Ejercicio14(i):
            lista.append(i)
    return lista

#EJERCICIO 22 "Dadas cuatro tuplas (en ningún orden en particular) representando
              #cuatro puntos en un espacio bidimensional, determine si en
              #conjunto representan un cuadrado."

def ejercicio_22(px1,py1,px2,py2,px3,py3,px4,py4):
    t1 = int(sqrt((px1-px2)**2 + (py1-py2)**2))
    t2 = int(sqrt((px2-px3)**2 + (py2-py3)**2))
    t3 = int(sqrt((px3-px4)**2 + (py3-py4)**2))
    t4 = int(sqrt((px4-px1)**2 + (py4-py1)**2))

    t5 = int(sqrt((px3-px1)**2 + (py3-py1)**2))
    t6 = int(sqrt((px4-px2)**2 + (py4-py2)**2))
    if t1 == t2 and t2 == t3 and t3 == t4 and t5 == t6:
        return True
    else:
        return False
    #usar los puntos(0,1,3,5,7,2,4,-2)
    


#EJERCICIO 23 "Escriba un programa que lea los contenidos de triangle.txt,
              #y calcule el camino de adyacentes que suma el total más largo."

def ejercicio_23():
    contenedor = []

    archivo = open ("triangle.txt","r")
    for i in archivo:
        i = i.split()
        i = list(map(int, i))
        contenedor.append(i)

    for subindex in range(len(contenedor), 1, -1):
        next_line = contenedor[subindex - 1]
        prev_line = contenedor[subindex - 2]

        for column in range(len(prev_line)):
            prev_line[column] = prev_line[column] + max(next_line[column], next_line[column + 1])

    print(contenedor[0][0])


#EJERCICIO 24 "Dada una lista, encuentre una lista con todas las posibles
              #listas representando las permutaciones de la lista original."

def ejercicio_24(lista):
    suma = 0
    x = len(lista)
    
    for i in range(x):
        for a in range(0, x-i-1):
            if lista[a] > lista[a+1]:
                lista[a], lista[a+1] = lista[a+1], lista[a]
        print(lista)

    for i in range(x):
        for a in range(0, x-i-1):
            if lista[a] < lista[a+1]:
                lista[a], lista[a+1] = lista[a+1], lista[a]
        print(lista)




    


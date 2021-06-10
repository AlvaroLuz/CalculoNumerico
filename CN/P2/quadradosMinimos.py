import math
import numpy as np

xTable = [0, 1, 2, 3, 4, 5]
yTable = [27, 42, 60, 87, 127, 185]
n = 6

def generalLinearApplication(x, y, nonLinear=False):
    sumX = sum(x)
    sumY = sum(y)
    sumXY = 0
    sumXSqr = 0
    
    for aux1, aux2 in zip(x,y):
        sumXY += round(aux1*aux2,7)
    for aux in x:
        sumXSqr+= round(aux**2,7)
    
    #formula:
    #      (n*sumXY - sumX*sumY)         (sumX * sumXY -sumY * sum(x^2))
    # a = -----------------------   b = ---------------------------------
    #      (n*sum(x^2) - sumX^2)             (sumX^2 - n* sum(x^2))
    
    a = round((round(n * sumXY,7) - round(sumX*sumY,7) )/(round(n*sumXSqr,7) - round(sumX**2,7)),7)
    b = round((round(sumX *sumXY,7) - round(sumY*sumXSqr,7))/(round(sumX**2,7) - round(n*sumXSqr,7)),7)
    

    if nonLinear == 'log':
        print(f'a:{a}')
        print(f'b:{b}')
        f_string = f'{a}*log(x)+{b}'
        def f(x):
            y = a*np.log(x)+b
            return y
    elif nonLinear == 'expEuler':
        print(f'a:{a}')
        b = round(math.e**b,7)
        print(f'b:{b}')
        f_string = f'{b}*e^({a}x)'

        def f(x):
            y = b*(math.e**(a*x))
            return y
    elif nonLinear == 'exp':
        a = round(math.e**a,7)
        print(f'a:{a}')
        b = round(math.e**b,7)
        print(f'b:{b}')
        f_string = f'{b}*{a}^x'

        def f(x):
            y = b*(a**x)
            return y
    elif nonLinear == 'pot':
        print(f'a:{a}')
        b = round(math.e**b,7)
        print(f'b:{b}')

        f_string = f'{b}*(x^{a})'
        def f(x):
            y = (b)*(x**a)
            return y
    else:
        print(f'a:{a}')
        print(f'b:{b}')
        f_string = f'{a}*x+{b}'
        def f(x):
            y = a*x+b
            return y

    return f, f_string

def logaritmica(x, y, constNum = False):
    if constNum:
        for i in range (0,len(y)):
            y[i] = y[i] + constNum
    
    newX = x
    for i in range(0,len(x)):
        newX[i] = round(np.log(x[i]),7)
    print(newX)

    f,f_string = generalLinearApplication(newX, y, 'log')

    if constNum:
        f_string = f'{-constNum}+' + f_string

    return f, f_string

def exponencialEuler(x, y, constNum=False):
    if constNum:
        for i in range (0,len(y)):
            y[i] = y[i] + constNum

    newY = y
    for i in range (0,len(y)):
        newY[i] = round(np.log(y[i]),7)
    print(newY)

    f, f_string = generalLinearApplication(x,newY, 'expEuler')
    
    if constNum:
        f_string = f'{-constNum}+' + f_string

    return f, f_string

def exponencial(x, y, constNum=False):
    if constNum:
        for i in range (0,len(y)):
            y[i] = y[i] + constNum

    newY = y
    for i in range (0,len(y)):
        newY[i] = round(1/(y[i]*round(math.cos(x[i]), 7)),7)
    print(newY)

    f, f_string = generalLinearApplication(x,newY, 'exp')
    
    if constNum:
        f_string = f'{-constNum}+' + f_string

    return f, f_string

def potencia(x, y, constNum = False):
    if constNum:
        for i in range (0,len(y)):
            y[i] = y[i] + constNum
    
    newX = x
    for i in range(0,len(x)):
        newX[i] = round(np.log(x[i]),7)
    print(newX)
    newY = y
    for i in range (0,len(y)):
        newY[i] = round(np.log(y[i]),7)
    print(newY)
    
    f, f_string = generalLinearApplication(newX,newY, 'pot')
    
    if constNum:
        f_string = f'{-constNum}+' + f_string
    
    return f, f_string

f, f_string = exponencial(xTable,yTable)
print(f_string)
print(f(3))
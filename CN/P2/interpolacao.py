import numpy as np
x = [-2, -1, 1, 2, 3]
y = [0, 6, 24, 60, 64]

nm = 5      #tamanho da tabela xy
n = 3       #numero de pontos utilizados
ns = 2      #posicao na tabela do primeiro ponto utilizado
ne = ns+n   #posicao na tabela do ultimo ponto utilizado
xi = 1.5    #aproximacao inicial

def div_diff_function(known_points):
    f_cache = {(xi,):yi for xi,yi in sorted(known_points)}
    
    def f(xs):
        xi_tuple = tuple(sorted(xs))
        if xi_tuple not in f_cache:
            f_cache[xi_tuple] = (f(xi_tuple[1:]) - f(xi_tuple[:-1])) /  \
                             float(xi_tuple[-1]  -   xi_tuple[0])
        return round(f_cache[xi_tuple],7)
    
    return f

def _str_newton_poly(coeffs, x_knots):
    basis, poly_string = '', str(coeffs[0])
    for ci,xi in zip(coeffs[1:], x_knots[:-1]):
        # basis (x - x0)(x - x1)...(x - xi)
        if xi < 0:
            basis += '(x + ' + str(-xi) + ')'
        elif xi == 0:
            basis += 'x'
        else:
            basis += '(x - ' + str(xi) + ')'
        
        # append the ith's term, e.g. ci(x-x0)(x-x1)...(x-xi)
        add = ' + ' if ci >= 0 else ' - '
        if ci == 0:
            next
        elif abs(ci) == 1: 
            poly_string += add + basis
        else:
            poly_string += add + str(abs(ci)) + basis
    return 'p(x) = ' + poly_string

def newtInt(x,y,n,xi):
    matrizPrint = [ [ 0 for i in range(nm) ] for j in range(nm) ]
    matriz = np.zeros(shape=(nm,nm))
    yint = np.zeros(shape=n)
    
    x_knots = sorted(point[0] for point in zip(x[ns:ne],y[ns:ne]))
    div_diffs=div_diff_function(zip(x[ns:ne],y[ns:ne]))
    coeffs = [div_diffs(x_knots[:i+1]) for i in range(len(x_knots))]

    for i in range (0,nm):
        matriz[i][0] = y[i]
        matrizPrint[i][0]= y[i]
    for j in range(1, nm):
        for i in range (0, nm-j):
            matriz[i][j] = round((matriz[i+1][j-1]-matriz[i][j-1])/(x[i+j]-x[i]),7)
            matrizPrint[i][j] = round(matriz[i][j],7) 
    
    for i in range(0,nm):
        print(matrizPrint[i])
    print(_str_newton_poly(coeffs, x_knots))
    
    xterm=1
    yint[0] = matriz[ns][0]

    for order in range(1,n):
        xterm = xterm * (xi-x[order+ns-1])
        yint2 = yint[order-1] + matriz[ns][order] * xterm
        yint[order] = yint2
    
    print(f'x = {round(yint2,7)}')
    aux = []
    for i in matriz:
        aux.append(i[ne-2 ])
    maxVal = (max(aux , key = abs))

    string_erro = 'calculo do erro:'
    erro = 1
    for aux in x[ns:ne]:
        string_erro += f'|x-{aux}|*'
        erro *= abs((xi -aux)) 
    
    string_erro+=f'|{maxVal}|'
    
    erro*= abs(maxVal)
    print (string_erro)
    print(f'erro = {round(erro,7)}')


newtInt(x,y,n,xi)
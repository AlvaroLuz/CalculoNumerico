import numpy as np

matrizx =[[-5, 2, 2],
          [-2, 4, 1],
          [1, -2, 6]]
matrizx = np.asarray(matrizx)
vetory= [2,
        -1,
         1]
vetory = np.asarray(vetory)
x = [-1,
      0,
    -0.5]
x = np.asarray(x)

n=3

epsilon = 0.1

def criterioParada(x, xant):
    absMaxX = abs(max(np.asarray(x), key=abs))
    erroAtual = round(max(np.subtract(np.asarray(x),np.asarray(xant)),key =abs),7)/round(absMaxX,7)
    erroAtual = round(erroAtual,7)
    print(f'x(k) - x(k-1):{np.subtract(np.asarray(x),np.asarray(xant))}')
    print(f'calculo do erro :{round(max(np.subtract(np.asarray(x),np.asarray(xant))),7)}/{round(absMaxX,7)} = {abs(erroAtual)}')
    print(f'{abs(erroAtual)}<{epsilon} = {abs(erroAtual)<epsilon}')
    print()
    if abs(erroAtual)<epsilon:
        return True
    return False
conta_printada =False
iteracao = 0
while True:
    iteracao +=1
    print(f'ITERACAO:{iteracao}')
    print()
    xant=x
    x = []
    conta= []
    resposta= []
    for i in range(0,n):
        string_conta = f"    x{i+1} = 1/(A{i+1}{i+1})*"
        string_resultado = f"    x{i+1} = {round((1/matrizx[i][i]),7)}*"
        string_conta += f"(b{i+1}" 
        string_resultado += f"({vetory[i]}"

        sigma = 0
        for j in range(0, n):
            if j != i:
                string_conta+= f'+(A({i+1},{j+1})*X({j+1}))'
                string_resultado+=f'+(({matrizx[i][j]})*({xant[j]}))'
                sigma = sigma + matrizx[i][j]*xant[j]
        
        conta.append(string_conta)
        resposta.append(string_resultado)

        x.append(round((round((1/matrizx[i][i]),7))*(vetory[i]-sigma),7))
    
    
    if(not conta_printada):
        print('formula:')
        for i in conta:
            print(i)
        conta_printada = True
        print()
    for i in resposta:
        print(i)
    print()
    print(f'vetor resultado:{x}')      
    print()      
    if criterioParada(x, xant):
        break

def convergeLinha(matriz):
    for i in range(0, n):
        soma = 0
        for j in range (0, n):
            if j != i:
                soma += matriz[i][j]
        if matriz[i][i]<soma:
            return False
    return True
def convergeColuna(matriz):
    for i in range(0, n):
        soma = 0
        for j in range (0, n):
            if j != i:
                soma += matriz[j][i]
        if matriz[i][i]<soma:
            return False
    return True
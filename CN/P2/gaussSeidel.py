import numpy as np

matrizx = [[6, -1, 3],
           [1, 5, -3],
           [-1, -3,  8]]

vetory= [-3,
         2,
         5]
x = [-1,
     2,
     0.5]

n=3

epsilon = 0.01

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

iteracao = 0
conta_printada = False

while True:
    iteracao +=1
    print(f'ITERACAO:{iteracao}')
    print()
    xant = x
    x = []
    conta    = []
    resposta = []
    for i in range(0, n):
        sigma = 0
        string_conta    = f"    x{i+1} = (b{i+1}-("
        string_resposta = f"    x{i+1} = ({vetory[i]}-("
        
        for j in range (0, i):
            string_conta   += f'(A{i+1}{j+1}*x(k){j+1})+'
            string_resposta+= f'(({matrizx[i][j]})*({x[j]}))+'
            sigma = sigma + matrizx[i][j]*x[j]
        for j in range (i+1,n):
            string_conta   += f'(A{i+1}{j+1}*x(k-1){j+1})+'
            string_resposta+= f'(({matrizx[i][j]})*({xant[j]}))+'
            sigma = sigma + matrizx[i][j]*xant[j]

        string_resposta = string_resposta[:len(string_resposta)-2]
        string_conta = string_conta[:len(string_conta)-2]
        string_conta   +="))"
        string_resposta+="))"
        conta.append(string_conta)
        resposta.append(string_resposta)
        
        x.append(round((vetory[i]-sigma)/matrizx[i][i],7))
    
    if(not conta_printada):
        print('formula:')
        for i in conta:
            print(i)
        print()
        conta_printada = True
    for i in resposta:
        print(i)
    print()
    print(f'vetor resultado: {x}')
    print()
    if(criterioParada(x, xant)):
        break

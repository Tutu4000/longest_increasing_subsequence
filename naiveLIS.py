from random import randint
import time
def naive(entrada, n):
    solucao = 1
    for i in range(n, -1, -1):
        if entrada[i] < entrada[n]:
            solucao = max(solucao, 1 + naive(entrada, i))
    return solucao

def naive_lis(entrada):
    maximo = 1
    n = len(entrada)
    for i in range(n):
        maximo = max(maximo, naive(entrada, i))
    return maximo

def gerar_entrada(n):
    return [randint(0, 10000) for _ in range(n)]

entrada = gerar_entrada(1000)
with open('entrada.txt', 'w') as f:
    f.write("entrada: ")
    f.write(', '.join(map(str, entrada)))
    f.write('\n')
    f.write("solucao: ")
    #medir tempo em miliseconds
    inicio = time.time()
    f.write(', '.join(map(str, str(naive_lis(entrada)))))
    fim = time.time()
    f.write('\n')
    f.write("tempo: ")
    f.write(str((fim - inicio) * 1000))

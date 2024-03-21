from random import randint
import time
def subseq(entrada):
    n = len(entrada)
    sol = [1] * n
    for i in range(1, n):
        for j in range(i):
            if entrada[i] > entrada[j] and sol[i] < sol[j] + 1:
                sol[i] = sol[j] + 1
    return sol


def construir_sol(entrada, sol):
    n = len(entrada)
    maximo = max(sol)
    solucao = [0] * maximo
    for i in range(n - 1, -1, -1):
        if sol[i] == maximo:
            solucao[maximo - 1] = entrada[i]
            maximo -= 1
    return solucao

def maior_subsequencia(entrada):
    sol = subseq(entrada)
    return construir_sol(entrada, sol)

def gerar_entrada(n):
    return [randint(0, 10000) for _ in range(n)]

entrada = gerar_entrada(100000)
with open('entrada.txt', 'w') as f:
    f.write("entrada: ")
    f.write(', '.join(map(str, entrada)))
    f.write('\n')
    f.write("solucao: ")
    #medir tempo em miliseconds
    inicio = time.time()
    f.write(', '.join(map(str, maior_subsequencia(entrada))))
    fim = time.time()
    f.write('\n')
    f.write("tempo: ")
    f.write(str((fim - inicio) * 1000))


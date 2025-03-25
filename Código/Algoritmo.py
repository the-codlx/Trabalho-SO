import os
import time
import math
from multiprocessing import Process, Pool

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result




if __name__ == "__main__":

    #estrutura que vai guardar os dados do arquivo
    dados = []

    try:

        diretorio = ["C:/Users/Lucas/Documents/estudos/Trabalho-SO/listas_grandes", "C:/Users/Lucas/Documents/estudos/Trabalho-SO/listas_pequenas"]

        print("ESCOLHA O DIRETORIO:\n[0] LISTA GRANDE \n[1] LISTA PEQUENA")

        escolha = int(input())

        if(escolha != 0 and escolha != 1):
            raise Exception("Opção inválida")        


        nome_arquivo = input("\nDIGITE O NOME DO ARQUIVO: ")
        nome_arquivo = diretorio[escolha] + "/" + nome_arquivo + ".txt"


        with open(nome_arquivo, 'r') as file:
            for linha in file:
                linha = linha.strip()
                dados.append(int(linha))


    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


    tempo_sequencial_10_vezes = []

    for i in range(10):
        inicio_sequencial = time.perf_counter() * 1000
        mergeSort(dados)
        mergeSort(dados)
        fim_sequencial = time.perf_counter() * 1000

        tempo_sequencial_10_vezes.append(fim_sequencial - inicio_sequencial)
    

    tempo_sequencial = sum(tempo_sequencial_10_vezes) / len(tempo_sequencial_10_vezes)


    # Execução paralela

    tempo_paralelo_10_vezes = []

    for i in range(10):
        inicio_paralelo = time.perf_counter() * 1000

        p1 = Process(target=mergeSort, args=(dados,))
        p2 = Process(target=mergeSort, args=(dados,))

        p1.start()
        p2.start()

        p1.join()   
        p2.join()

        fim_paralelo = time.perf_counter() * 1000

        tempo_paralelo_10_vezes.append(fim_paralelo - inicio_paralelo)


    tempo_paralelo = sum(tempo_paralelo_10_vezes) / len(tempo_paralelo_10_vezes)

    #Resultados

    diferenca = tempo_sequencial - tempo_paralelo


    if tempo_sequencial < 1:
        print(f"Tempo sequencial: {tempo_sequencial:.3f} milissegundos")
    else:
        print(f"Tempo sequencial: {int(tempo_sequencial)} milissegundos")


    if tempo_paralelo < 1:
        print(f"Tempo paralelo: {tempo_paralelo:.3f} milissegundos")
    else:
        print(f"Tempo paralelo: {int(tempo_paralelo)} milissegundos")

    
    if(diferenca < 1):
        print(f"Diferença: {diferenca:.3f} milissegundos a favor do paralelismo")
    else:
        print(f"Diferença: {int(diferenca)} milissegundos a favor do paralelismo")


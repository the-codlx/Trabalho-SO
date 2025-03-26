import multiprocessing
import os
import time
import math
from multiprocessing import Process, Pool

# merge sequencial
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

    # fusão (merge) de duas listas ordenadas.
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

<<<<<<< Updated upstream

# Divide um array em N partes aproximadamente iguais, de acordo com o número de CPUs disponíveis
=======
# divide um array em N partes aproximadamente iguais
>>>>>>> Stashed changes
def dividir_array(arr, num_partes):

    tamanho = len(arr)
    chunk_size = tamanho // num_partes
    partes = [arr[i * chunk_size: (i + 1) * chunk_size] for i in range(num_partes)]
    
    if tamanho % num_partes != 0:
        partes[-1].extend(arr[num_partes * chunk_size:])
    return partes


# Função auxiliar para realizar o merge de um par de listas.
def merge_pair(pair):
<<<<<<< Updated upstream
=======
    
    # função auxiliar para realizar o merge de um par de listas.
    # se a segunda lista estiver vazia (caso de número ímpar), retorna a primeira.
>>>>>>> Stashed changes

    left, right = pair
    if not right:
        return left
    return merge(left, right)

<<<<<<< Updated upstream

# Realiza a fusão (merge) paralela de uma lista de listas ordenadas.
def merge_paralelo(listas):
=======
def merge_paralelo(listas, pool):
    
    #realiza a fusão (merge) paralela de uma lista de listas ordenadas.
    #reutiliza o Pool passado como parâmetro.
    
    while len(listas) > 1:
        pares = []
        # agrupa as listas em pares; se o número for ímpar, o último par terá a segunda lista vazia
        for i in range(0, len(listas), 2):
            if i + 1 < len(listas):
                pares.append((listas[i], listas[i+1]))
            else:
                pares.append((listas[i], []))

        # usa o mesmo pool para fazer merge dos pares
        listas = pool.map(merge_pair, pares)
>>>>>>> Stashed changes

    num_cpus = multiprocessing.cpu_count()
    with Pool(processes=num_cpus) as pool:
        while len(listas) > 1:
            pares = []
            # Agrupa as listas em pares; se o número for ímpar, o último par terá a segunda lista vazia
            for i in range(0, len(listas), 2):
                if i + 1 < len(listas):
                    pares.append((listas[i], listas[i+1]))
                else:
                    pares.append((listas[i], []))
            listas = pool.map(merge_pair, pares)
    return listas[0]

<<<<<<< Updated upstream
def merge_sort_paralelo(arr):
    """
    Merge Sort paralelizado:
      1. Divide os dados em partes iguais, de acordo com o número total de CPUs.
      2. Ordena cada parte em paralelo.
      3. Utiliza a função merge_paralelo para combinar as partes ordenadas de forma paralela.
    """
    num_cpus = multiprocessing.cpu_count()  # Obtém o número total de CPUs disponíveis
    partes = dividir_array(arr, num_cpus)     # Divide os dados em partes iguais

    # Ordena cada pedaço em paralelo utilizando o Pool
    with Pool(processes=num_cpus) as pool:
        partes_ordenadas = pool.map(mergeSort, partes)

    # Utiliza a função merge_paralelo para juntar as partes ordenadas
    lista_ordenada = merge_paralelo(partes_ordenadas)
=======
def merge_sort_paralelo(arr, pool):
    
    # merge Sort paralelizado:
    #  1. divide os dados em partes iguais, de acordo com o número total de CPUs.
    #  2. ordena cada parte em paralelo (usando o Pool recebido como parâmetro).
    #  3. utiliza a função merge_paralelo (também usando o mesmo Pool) para combinar as partes ordenadas.
    
    num_cpus = multiprocessing.cpu_count()
    partes = dividir_array(arr, num_cpus)

    # ordena cada pedaço em paralelo utilizando o Pool
    partes_ordenadas = pool.map(mergeSort, partes)

    
    # fusão paralela, usando o mesmo pool
    lista_ordenada = merge_paralelo(partes_ordenadas, pool) 
>>>>>>> Stashed changes
    return lista_ordenada




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


    

    # execução sequencial
    inicio_sequencial = time.perf_counter() * 1000
<<<<<<< Updated upstream
    mergeSort(dados)
=======

    mergeSort(dados.copy())

>>>>>>> Stashed changes
    fim_sequencial = time.perf_counter() * 1000
    

    tempo_sequencial = fim_sequencial - inicio_sequencial


    # execução paralela

    inicio_paralelo = time.perf_counter() * 1000

<<<<<<< Updated upstream
    p1 = Process(target=merge_sort_paralelo, args=(dados,))

    p1.start()

    p1.join()   
=======
    # cria um Pool de processadores
    with multiprocessing.Pool(processes= multiprocessing.cpu_count()) as pool:
        # executa o merge sort paralelo usando o pool
        merge_sort_paralelo(dados.copy(), pool)    

>>>>>>> Stashed changes

    fim_paralelo = time.perf_counter() * 1000


    tempo_paralelo = fim_paralelo - inicio_paralelo


    #resultados

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

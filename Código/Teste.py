
import os
import time
import math
from multiprocessing import Process, Pool

def calcular_operacao_intensiva(n):
    for _ in range(100):
        resultado = math.factorial(30000)

    print(f"Processo {n} completou operações intensivas")


def square(n):
    return(os.getpid(), n, n * n)


def base_exponte(base, exponente):
    return base ** exponente    


if __name__ == "__main__":

    # É executado de forma paralela, ou seja, são criado dois processos diferentes    

    inicio_paralelo = time.perf_counter()
    
    p1 = Process(target=calcular_operacao_intensiva, args=(1,))
    p2 = Process(target=calcular_operacao_intensiva, args=(2,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    fim_paralelo = time.perf_counter()

    print("---------------------------")
    print(os.getpid(), os.getppid(), p1.pid, p2.pid)
    print("---------------------------")
    
    # Versão sequencial (é executado pelo processo principal, ou seja, o processo pai)
    inicio_sequencial = time.perf_counter()

    calcular_operacao_intensiva(3)
    calcular_operacao_intensiva(4)
    fim_sequencial = time.perf_counter()

    time.sleep(2)

    
    print("---------------------------")
    print(os.getpid())
    print("---------------------------")

    # Resultados
    print(f"Tempo paralelo: {fim_paralelo - inicio_paralelo:.2f} segundos")
    print(f"Tempo sequencial: {fim_sequencial - inicio_sequencial:.2f} segundos")
    diferenca = (fim_sequencial - inicio_sequencial) - (fim_paralelo - inicio_paralelo)
    print(f"Diferença: {diferenca:.2f} segundos a favor do paralelismo")

    # Pool

    numbers = [1, 2, 3, 4, 5]


    #Pool

    with Pool(2) as pool:
        results = pool.map(square, numbers)
        print(results)
        for pid, n, sq in results:
            print(f"Processo {pid} calculou {n} ao quadrado = {sq}")

    # Pool com argumentos

    inicio_paralelo2 = time.perf_counter()

    with Pool(5) as pool:
        results = pool.starmap(base_exponte, [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])
        for valor in results:
            print(valor)


    fim_paralelo2 = time.perf_counter()

    print(f"Tempo paralelo: {fim_paralelo2 - inicio_paralelo2:.2f} segundos")
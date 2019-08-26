'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF969 -- Algoritmos e Estruturas de Dados


FORKED FROM: Antônio Paulino de Lima Neto (apln2@cin.ufpe.br) (2018-03-01)

Autor:  Anderson Sobrinho Lima Laurentino
Email:         asll@cin.ufpe.br
Data:            2019-08-26
'''
import sys
import numpy as np
import matplotlib.pyplot as plt
from Cronometro import Cronometro

MAX = 999999

def gera_seq_aleatoria(size):
   return np.random.randint(-MAX,MAX, size=size)

def conta_somas(vetor):
    total = 0
    size = len(vetor)

    for i in range(size - 1):
        unknows = set()
        for j in range(i + 1, size):
            # Sum two number of the triple and discover the target value 
            x = - (vetor[i] + vetor[j])

            # Check if the target is in unknows's numbers set
            if x in unknows: total += 1
            
            # case not add in unknows's numbers set
            else: unknows.add(vetor[j])

    return total

def main():
    ##########################
    #         CONFIG
    ##########################
    seeds = [11,7,13,19,5189,600,1000,1500,1500,1500, 1000]
    size = [50,100,250,500,1000,1500,2000,2500,3000,3500,7000]
    epcohs = []
    ##########################
    ##########################


    ##########################
    #   RUN THE EXPERIMENTS
    ##########################
    # Throw the experiments
    for exp in range(5):
        print(f">>>> EXPERIMENTO: {exp + 1} <<<<")
        results = []
        for i,seed in enumerate(seeds):
            np.random.seed(seed)
            vetor = gera_seq_aleatoria(size[i])

            cron = Cronometro()
            
            cron.Iniciar()
            conta_somas(vetor)
            cron.Parar()

            results.append(cron.Exibir())

            print(f"Tempo gasto com {size[i]} elementos foi {cron} segundos")
            del vetor
            del cron
        
        epcohs.append(results)
        print()
    ##########################
    ##########################


    ##########################
    #    PLOT THE RESULTS
    ##########################

    # Generate the scatter X and Y
    scatter_x = size * len(epcohs)
    scatter_y = np.concatenate(epcohs)

    # Create a polinomial function of 1 dimension
    fit_fn = np.poly1d(np.polyfit(scatter_x,scatter_y,1))
    
    plt.title("Resultados")
    
    # PLOT: Linear Regression
    line, = plt.plot(scatter_x, fit_fn(scatter_x), '--', c="#0c29d0")
    line.set_dashes([10,5,10,5])

    # PLOT: Poly Regression
    plt.plot(size, np.mean(epcohs, axis=0), c="#ff5900", label="Regressão Poly")

    # PLOT: STM
    plt.fill_between(size, np.min(epcohs, axis=0), np.max(epcohs, axis=0), alpha=.3, facecolor="#ff5900", label="Desvio")
    
    # PLOT: Scatter
    plt.scatter(scatter_x, scatter_y, c="#0c29d0", label="Tempos")
    
    plt.legend(['Tendência', 'Regressão Polinomial', 'Desvio', 'Tempos'])
    
    plt.show()
    ##########################
    ##########################




if __name__ == '__main__':
    main()
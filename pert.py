#BREVE CONTEXTUALIZAÇÃO. O ARQUIVO TXT TEM O CARACTERE '-' PARA TAREFAS QUE NAO POSSUEM PRECEDENTES
#AS ARESTAS FANTASMAS FORAM RESOLVIDAS REPETINDO O VERTICE QUE POSSUI MAIS DE UMA DEPENDENCIA E -1 PARA VALOR
#DA TAREFA REPETIDA. EXEMPLO: A TAREFA G TEM AS TAREFAS A E B COMO PRECEDENTES E DURACAO 5
#   G A,B 5 ---> G A 5
#                G B -1
#UTILILIZEI O GRAFO DA TAREFA DISPONÍVEL EM https://www.ime.usp.br/~rvicente/PERT_CPM.pdf

##### MONTANDO O GRAFO #####
entrada = open("pert.txt")

linhas = entrada.readlines()
grafo = {}
duracao = {}

for x in linhas:
    vertice, precedente, tempo = x.split()
    if int(tempo) > 0:
        duracao[vertice] = tempo

    if precedente != '-':
            if vertice not in grafo:
                grafo[vertice] = [precedente]
            else:
                grafo[vertice].append(precedente)
    else:
        grafo[vertice] = precedente

##### ENCONTRANDO O TEMPO TOTAL, MAIS CEDO, MAIS TARDE, FOLGAS E CAMINHO CRITICO #####
tempo_maximo = 0
visitados = {}
tempo_mais_Cedo = {}
tempo_mais_Tarde = {}
caminho_Critico = []
V = []
folgas = {}

for x in grafo:
    temp = 0

    for y in grafo[x]:
        if len(grafo[x]) <= 1:
            if(y == '-'):
                visitados[x] = duracao[x]
                tempo_mais_Cedo[x] = duracao[x]
            elif y in visitados:
                visitados[x] = (int(duracao[x]) + int(visitados[y]))
                tempo_mais_Cedo[x] = visitados[x]
        else:
            if temp == 0:
                visitados[x] = (int(duracao[x]) + int(visitados[y]))
                tempo_mais_Cedo[x] = visitados[x]
                temp = visitados[x]
            else:
                if (int(duracao[x]) + int(visitados[y])) > temp:
                    visitados[x] = (int(duracao[x]) + int(visitados[y]))
                    tempo_mais_Cedo[x] = visitados[x]
                    temp = visitados[x]

for x in visitados:
    if tempo_maximo < int(visitados[x]):
        tempo_maximo = int(visitados[x])

for x in reversed(grafo):
    t = True
    for y in grafo:
        for z in grafo[y]:
            if (x == z):
                if x not in V:
                    tempo_mais_Tarde[x] = (int(tempo_mais_Tarde[y]) - int(duracao[y]))
                    t = False
                    V.append(x)
                else:
                    tempo_mais_Tarde[x] = min((int(tempo_mais_Tarde[y]) - int(duracao[y])), tempo_mais_Tarde[x])
    
    if(t == True):
        tempo_mais_Tarde[x] = tempo_maximo

for x in grafo:
    if(int(tempo_mais_Cedo[x]) == int(tempo_mais_Tarde[x])):
        caminho_Critico.append(x)
    else:
        folgas[x] = int(tempo_mais_Tarde[x]) - int(tempo_mais_Cedo[x])

print("------------------------------------------")
print(f'Tempo total do projeto: {tempo_maximo}')

for x in grafo:
    print(f'Tempos mais cedo e mais tarde de {x}: ({tempo_mais_Cedo[x]}, {tempo_mais_Tarde[x]})')

print(f'Caminho critico: {caminho_Critico}')
print(f'Folgas: {folgas}')
print("------------------------------------------")

#------------------------------------------
#Tempo total do projeto: 43
#Tempos mais cedo e mais tarde de A: (7, 7)
#Tempos mais cedo e mais tarde de B: (5, 12)
#Tempos mais cedo e mais tarde de C: (16, 16)
#Tempos mais cedo e mais tarde de D: (27, 27)
#Tempos mais cedo e mais tarde de E: (11, 18)
#Tempos mais cedo e mais tarde de F: (20, 22)
#Tempos mais cedo e mais tarde de G: (30, 30)
#Tempos mais cedo e mais tarde de H: (28, 30)
#Tempos mais cedo e mais tarde de I: (36, 36)
#Tempos mais cedo e mais tarde de J: (34, 36)
#Tempos mais cedo e mais tarde de K: (43, 43)
#Caminho critico: ['A', 'C', 'D', 'G', 'I', 'K']
#Folgas: {'B': 7, 'E': 7, 'F': 2, 'H': 2, 'J': 2}
#------------------------------------------
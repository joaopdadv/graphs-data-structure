graph = [
    [0,0,0,1,1,0],
    [0,0,1,1,1,1],
    [0,1,0,0,0,1],
    [1,1,0,0,1,1],
    [1,1,0,1,0,1],
    [0,1,1,1,1,0],
]

def euler(graph):
    for i in range(len(graph)):
        count = 0
        for j in graph[i]:
            if j == 1:
                count += 1
        if count % 2 != 0:
            return
    
    # A partir daqui sabemos que o grafo possui um ciclo.
    sequencia = [0]
    nextIndex = 1
    node = graph[0]

    explore = False

    while(not explore):
        i = 0
        while i < len(node):
            if node[i] == 1:
                # print(graph)
                # Marca a aresta como já nagevada no grafo
                graph[sequencia[nextIndex - 1]][i] = 0
                graph[i][sequencia[nextIndex - 1]] = 0       

                # Adiciona vértice na sequência
                sequencia.insert(nextIndex, i)

                # Atualiza node que para ser explorado
                node = graph[i]

                # Reinicia contador para que o node seja explorado desde o início
                i = 0
                nextIndex += 1
            else:
                i += 1

        # Detectou o fim de um ciclo

        h = 0
        sequence_length = len(sequencia)
        keepExploring = False

        # Buscando nodes com arestas não exploradas
        while h < sequence_length:
            for f in range(len(graph[sequencia[h]])):
                if graph[sequencia[h]][f] == 1:
                    # Achei um node com partes não exploradas

                    # Atualizando o node a ser explorado
                    node = graph[sequencia[h]]
                    nextIndex = h + 1

                    h = sequence_length  # Exit the while loop
                    keepExploring = True
                    break
            h += 1

        # Significa que a matriz está zerada
        explore = not keepExploring    

    return sequencia



print(euler(graph))
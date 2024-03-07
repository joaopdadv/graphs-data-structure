graph = [
    [0,1,1,1,1],
    [1,0,1,1,1],
    [1,1,0,1,1],
    [1,1,1,0,1],
    [1,1,1,1,0],
]

def euler(graph):
    for i in range(len(graph)):
        count = 0
        for j in graph[i]:
            if(j == 1):
                count += 1
        if(count%2 != 0):
            return False
    
    return True




print(euler(graph))

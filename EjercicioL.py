def desencolar(cola, primero, ultimo, tam):
    if primero == 0:
        print("Cola vacía")
        return None, primero, ultimo
    else:
        D = cola[primero]
        if primero == ultimo:
            primero = 0
            ultimo = 0
        else:
            primero = primero + 1
        return D, primero, ultimo

def encolar(cola, primero, ultimo, tam, D):
    if (primero == 1 and ultimo == tam) or (ultimo + 1 == primero):
        print("Cola llena")
    else:
        if ultimo == tam:
            ultimo = 1
        else:
            ultimo = ultimo + 1
        cola[ultimo] = D
        if primero == 0:
            primero = 1
    return primero, ultimo

def mostrar_matriz_adyacencia(matriz_adyacencia):
    print("Matriz de adyacencia:")
    for fila in matriz_adyacencia:
        print(fila)

def mostrar_vector_visitado(visitado):
    print("Vector visitados:", visitado)

def BFS(matriz_adyacencia, inicio, tam):
    vertices = len(matriz_adyacencia)
    visitado = [0] * vertices  #Se inicializa el vector con 0
    cola = [None] * (tam + 1)  
    primero = 0
    ultimo = 0

    mostrar_matriz_adyacencia(matriz_adyacencia)  # Matriz de adyacencia
    mostrar_vector_visitado(visitado)  # Vector visitado antes del recorrido

    visitado[inicio] = 1 #Marca el nodo de inicio como visitado y lo encola
    primero, ultimo = encolar(cola, primero, ultimo, tam, inicio)

    #Mientras la cola no esté vacía
    while primero != 0:
        v, primero, ultimo = desencolar(cola, primero, ultimo, tam) #Desencola el nodo y obtiene el indice
        print("Visitando el nodo:", v + 1)  # Mostrar el nodo actual que se está visitando

        # Recorrer todos los nodos adyacentes al nodo v
        for w in range(vertices):
            if matriz_adyacencia[v][w] == 1 and visitado[w] == 0: #Si no ha sido visitado
                visitado[w] = 1 #Marcar como visitado
                primero, ultimo = encolar(cola, primero, ultimo, tam, w) #Encolar el nodo W

    print("\nVector después del recorrido:")
    mostrar_vector_visitado(visitado)

grafo = {
    1: [2, 3],
    2: [1, 4, 5, 9],
    3: [1, 6, 7],
    4: [2, 8],
    5: [2, 8],
    6: [3, 8],
    7: [3, 8],
    8: [4, 5, 6, 7],
    9: [2]
}

# Construir matriz de adyacencia a partir del grafo
nodos = len(grafo)
matriz_adyacencia = [[0] * nodos for _ in range(nodos)]

for nodo, adyacentes in grafo.items():
    for adyacente in adyacentes:
        matriz_adyacencia[nodo - 1][adyacente - 1] = 1

inicio = int(input("Ingrese el nodo inicial (1 a 9): ")) - 1

print("\nInicio del recorrido desde el nodo: ", inicio + 1)
BFS(matriz_adyacencia, inicio, nodos)




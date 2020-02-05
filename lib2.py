import lib

def productoMatriz(A,B):
    """
    Esta función recibe como parametros dos matrices representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna el producto matricial
    como una lista de listas, si las dimensiones son correctas, de lo contrario retornar un mensaje
    de alerta.
    """
    M = []
    if len(A[0]) == len(B):
        for i in range(len(A)):
            M.append([])        
            for j in range(len(B[0])):
                M[i].append((0,0))
                for k in range(len(B)):
                    M[i][j] = lib.suma(M[i][j], lib.producto(A[i][k], B[k][j]))
                    
        return M
    else:
        return 'Dimensiones incorrectas'


def sumaMatriz(A,B):
    """
    Esta función recibe como parametros dos matrices representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la suma matricial
    como una lista de listas, si las dimensiones son correctas, de lo contrario retornar un mensaje
    de alerta.
    """
    M = []
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            M.append([])        
            for j in range(len(A[0])):
                M[i].append(lib.suma(A[i][j], B[i][j]))
        return M

    else:
        return 'Dimensiones incorrectas'


def escalarMatriz(A,k):
    """
    Esta función recibe como parametros una matriz representada con una lista de listas y un 
    esclar que es un números complejos en forma de tupla. Retorna el producto escalar
    como una lista de listas.
    """
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = lib.producto(k,A[i][j])
    return A
            
def inversoAditivoMatriz(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna el inverso aditivo
    de la matriz como una lista de listas.
    """
    A = escalarMatriz(A,(-1,0))
    return A

def transpuestaMatriz(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la transpuesta
    de la matriz como una lista de listas.
    """
    M = []
    for i in range(len(A[0])):
        M.append([])
        for j in range(len(A)):
            M[i].append(A[j][i])
    return M

def conjugadaMatriz(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la conjudaga
    de la matriz como una lista de listas.
    """
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = lib.conjugado(A[i][j])
    return A

def dagaMatriz(A):
    """
    Esta función recibe como parametro una matriz representada con una lista de listas,
    donde sus entradas son números complejos en forma de tupla. Retorna la adjunta o daga
    de la matriz como una lista de listas.
    """
    return transpuestaMatriz(conjugadaMatriz(A))

def main():
    
    A = [[(1,0),(1,0),(1,0)],
         [(1,0),(1,0),(1,0)]]
        
    B = [[(1,0),(1,0),(1,0)],
         [(1,0),(1,0),(1,0)],
         [(1,0),(1,0),(1,0)]]
    
    C = conjugadaMatriz(A)
    
    for i in range(len(C)):
        print(C[i])
    
main()

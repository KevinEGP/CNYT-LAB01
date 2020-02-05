import lib

def productoMatriz(A,B):
    M = []
    for i in range(len(A)):
        M.append([])
        for j in range(len(B[0])):
            M[i].append((0,0))
            for k in range(len(B)):
                M[i][j] = lib.suma(M[i][j],lib.producto(A[i][k], B[k][j]))
    return(M)

def sumaMatriz(A,B):
    M = []
    for i in range(len(A)):
        M.append([])
        for j in range(len(A[0])):
            M[i].append(lib.suma(A[i][j], B[i][j]))

def escalarMatriz(A,k):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = lib.producto(k,A[i][j])
    return A
            
def transpuestaMatriz(A):
    M = []
    for i in range(len(A[0])):
        M.append([])
        for j in range(len(A)):
            M[i].append(A[j][i])
    return M

def conjugadaMatriz(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = lib.conjugado(A[i][j])
    return A

def dagaMatriz(A):
    return transpuestaMatriz(conjugadaMatriz(A))
    
def main():
    A = [[(3,4),(-1,0),(1,1)],
         [(1,0),(0,2),(2,2)]
        ]

    B = [[(1,-1),(0,0)],
         [(3,4),(-1,0)]
        ]
    print(productoMatriz(A,dagaMatriz(B)))


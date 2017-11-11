import numpy as np

n = int(input('Enter number of variables: '))

#Getting matrix A

A = []
print('enter elements of A')
for i in range(0,n):
    
    A.append([])
    for j in range(0,n):
        p = float(input())
        A[i].append(p)

#Initializing matrix U with all zeroes
U = []
for i in range(0,n):
    U.append([])
    for j in range(0,n):
        U[i].append(0)

#Initializing matrix L with all zeroes
L = []
for i in range(0,n):
    L.append([])
    for j in range(0,n):
        L[i].append(0)
        
#Initializing Identity matrix Identity matrix
I = []
for i in range(0,n):
    I.append([])
    for j in range(0,n):
        if(i == j):
            I[i].append(1)
        else:
            I[i].append(0)

#Calculating elements of L and U
for i in range(0,n):
    #getting lower triangular matrix L.
    for j in range(0,n):
        if(j < i):
            L[j][i] = 0
        else:
            L[j][i] = A[j][i]
            for k in range(0,i):
                L[j][i] = L[j][i] - L[j][k]*U[k][i]
    #getting upper triangular matrix U.
    for j in range(0,n):
        if(j < i):
            U[i][j] = 0
        elif(j == i):
            U[i][j] = 1
        else:
            U[i][j] = A[i][j]/L[i][i]
            for k in range(0,i):
                U[i][j] = U[i][j] - ((L[i][k]*U[k][j])/L[i][i])
                
            
X = [None for i in range(n)]

Y = [None for i in range(n)]

print('After decompodition matrix L is')
for i in range(0,n):
    for j in range(0,n):
        print(L[i][j], end = "\t")
    print("")
print('')

print('After decompodition matrix U is')
for i in range(0,n):
    for j in range(0,n):
        print(U[i][j], end = "\t")
    print("")
print('')

#Inverse of matrix L calculation
LInverse = np.linalg.inv(L)
print('Inverse of matrix L is:')
for i in range(0,n):
    for j in range(0,n):
        print(LInverse[i][j], end = "\t")
    print("")
print('')

#Inverse of matrix U calculation
print('Inverse of matrix U is:')
UInverse = np.linalg.inv(U)
for i in range(0,n):
    for j in range(0,n):
        print(UInverse[i][j], end = "\t")
    print("")
print('')

#Finding Inverse of A
print('Inverse of matrix A is:')
AInverse = np.matmul(UInverse,LInverse)
for i in range(0,n):
    for j in range(0,n):
        print(AInverse[i][j], end = "\t")
    print("")
print('')


#######################for testing pupose only#########################
print('')
print('Test if the results are matched with actual A and A inverse')
print('A')
print(np.matmul(L,U))
print('A inverse')
print(np.linalg.inv(A))

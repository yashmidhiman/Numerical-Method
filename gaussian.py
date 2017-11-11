
##Number of variables in the system of equation
n = int(input('Enter number of variables: '))

matrix = []
#if the variable is not present in the equation, enter 0 for it's coefficient.
for i in range(0,n):
    print('enter the coeffients of equation')
    matrix.append([])
    for j in range(0,n+1):
        p = float(input())
        matrix[i].append(p)


flag = 0
#upper triangular matrix generation
for j in range(0,n):
    for i in range(0,n):
        if(i>j):
            if(matrix[j][j] == 0):
                flag = 1
            else:
                c = (matrix[i][j]/matrix[j][j])
                for k in range(0,n+1):
                    matrix[i][k] = (matrix[i][k] - (c*matrix[j][k]))
x = [None for i in range(n+1)]

if(matrix[n-1][n-1] == 0):
    flag = 1
else:
    x[n-1] = matrix[n-1][n]/matrix[n-1][n-1]


#backward substitution
if(flag == 0):
    for i in range(n-2,-1,-1):
        sum = 0
        if(matrix[i][i] == 0):
            flag = 1
        else:
            for j in range(i+1,n):
                sum = sum+matrix[i][j]*x[j]
            
            x[i] = (matrix[i][n]-sum)/matrix[i][i]
            if(x[i] == -0.0):
                x[i] = 0.0

    print('solution is: ')
    for i in range(0,n):
        print(x[i])
else:
    print('These system of equations have no solution')

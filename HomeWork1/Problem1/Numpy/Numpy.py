#Arrays
import numpy

def arrays(arr):
    res = numpy.array(arr,float)
    result = numpy.flip((res))
    return result


arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#Shape and Reshape

import numpy

arr = input().strip().split(' ')

result  =  numpy.array(arr, dtype = int)

print (numpy.reshape(result,(3,3)))

#Transpose and Flatten
import numpy as np

N, M = map(int, input().split())

matrix = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

print(np.transpose(matrix))
print(matrix.flatten())


#Eye and Identity
import numpy

numpy.set_printoptions(legacy='1.13')

N, M = map(int, input().split())

print(numpy.eye(N, M))

#Array Mathematics
import numpy as np

N, M = map(int, input().split())

A = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

B = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)

#Sum and Prod
import numpy as np

N, M = map(int, input().split())

A = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

sums = np.sum(A, axis=0)

result = np.prod(sums)

print(result)

#Min and Max

import numpy as np

N, M = map(int, input().split())

A = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

minimums = np.min(A, axis=1)

result = np.max(minimums)

print(result)

#Mean, Var, and Std
import numpy as np

N, M = map(int, input().split())

A = np.array([
    list(map(int, input().split()))
    for _ in range(N)
])

print(np.mean(A, axis=1))
print(np.var(A, axis=0))
print(round(np.std(A), 11))

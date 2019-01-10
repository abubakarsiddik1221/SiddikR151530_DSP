import numpy as np

m1=input("No. of rows in matrix : ")
n1=input("No. of columns in matrix : ")

print("Enter matrix A ")
A=numpy.empty((m1,n1))
for i in range(m1):
	for j in range(n1):
		A[i,j]=input("")

print("Matrix A is ")
for i in range(m1):
	for j in range(n1):
		print(A[i,j]), '\t',
	print
print('\n')

print("The Eigen values of matrix A is ")
print np.linalg.eigvals(A)
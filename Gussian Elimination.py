import numpy as np

pivot=[1,1]
turn=1
row=1
col=1
coeffmat=np.array([[2,-1,1],[4,2,1],[6,-4,2],[-1,4,-2]])






#print("This is the current System being solved: ")
#print(coeffmat,rightside)


#for i in range(3):                                   #Prints all elements in current array
 #   for j in range (3):
  #      print(coeffmat[i,j])
        
        
        
#for (turn) to (n-1):
#    
#    for (row=turn+1) to n:
#        m=(-coeffmat[i,j]/coeffmat[i,j])
#        coeffmat[1,turn]=0
#        for (col=coeffmat[turn]+1) to (n+1):
#            coeffmat[i,j]=coeffmat[i,j] + m(coeffmat[i,j])
#            
    
    


def GaussElim(A):
    
    n=len(A)

    for i in range(0,n):   #search for maximum in this column
        maxE1=abs(A[i][i])
        maxRow=i
        for k in range(i+1,n):
            if abs(A[k][i])>maxE1:
                maxE1=abs(A[k][i])
                maxRow=k
                # swap maximum row with current row (column by column)
        for k in range(i,n):
            tmp=A[maxRow][k]
            A[maxRow][k]=A[i][k]
            A[i][k]=tmp

        for k in range(i+1,n):
            c=-A[k][i]/A[i][i]
            for j in range(i,n-1):
                if i==j:
                    A[k][j]=0
                else:
                    A[k][j]+=c*A[i][j]
                    #solve equation Ax+b for an upper triangular matrix A
    x=[0 for i in range(n)]
    for i in range(n-1,-1,-1):
        x[i]=A[i][n]/A[i][i]
        for k in range(i-1,-1,-1):
            A[k][n]-=A[k][i]*x[i]
    return x




GaussElim(coeffmat)
 
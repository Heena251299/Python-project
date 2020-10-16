
def add(K, N, lo, hi, val): 

	K[lo] += val 
	if (hi != N - 1): 
		K[hi + 1] -= val 


def updateArray(K, N): 


	for i in range(1, N): 
		K[i] += K[i - 1] 

# sort array funciton
def SortArr(K, N, Z): 
	updateArray(K, N)
	
	K.sort()
	Z.sort()
	if(K==Z):
	    print("YES")
	else:
	    print("NO")
	
# main program execution starts from here..
for i in range(int(input())):
    N = int(input())
    C = list(map(int,input().split()))
    Z = list(map(int,input().split()))
    K = [0]*N 
    for j in range(N):
        first = j-C[j]
        end = j+C[j]
        if(first<0):first=0
        if(end>=N):end=N-1
        add(K, N, first, end, 1)
   
    SortArr(K, N, Z)
	   

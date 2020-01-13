N = int(input("Enter N\n"))
c = 0
for i in range(1,N+1):
    if N % i == 0:
        c+=1
print("Input: "+str(N)+" Output: "+str(c))

# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5

n=int(input('enter no.'))
for i in range(n,0,-1):
    for j in range(1,i+1,1):
        print(n-(i-1),end=" ")
    print()
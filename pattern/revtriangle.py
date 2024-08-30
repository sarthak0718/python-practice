        #    10987
        #    456
        #    32
        #    1

n=int(input('enter a no.'))
for i in range(1,n,1):
    for j in range(1,(n+1)-i):
        print('*',end='')
    print()

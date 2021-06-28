n=str(input("enter :"))
n=list(map(str,n))
for i in range(10):
    n[-1]=i
    for j in n:
        a=j,end=""
    print(a)
    break 

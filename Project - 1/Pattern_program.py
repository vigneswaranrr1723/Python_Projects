n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()
print()
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print("*",end=" ")
    print()
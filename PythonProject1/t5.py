
for i  in range(0,10):
    for j in range(1,10-i-1):
        print("  ",end="")
    for k in range(1,i):
        print("*     ",end="")
    print()


j=1
for i in range(0,6):
    for j in range(1,i+1):
        print(j,end=" ")
        j=j+1
    print()


n=1
for i in range(0,6):
    for j in range(1,i):
        print(n,end=" ")
        n=n+1
    print()


n=0
for i in range(0,6):
    for j in range(0,i):
        print(n,end=" ")
        n=n+1

    print()



n=0
for i  in range(0,6):
    for j in range(0,6-i):
        print(n,end=" ")
        n=n+1
    print()

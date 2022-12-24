n,m = input().split()
n = int(n)
m = int(m)

b = []
for i in range(n):
  c = list(map(int,input().split()))
  b.append(c)

  
b1 = []
for i in range(n):
  c1 = list(map(int,input().split()))
  b1.append(c1)

for i in range(n):
 for a in range(m):
    print(b[i][a]+b1[i][a], end=" ")
 print("")

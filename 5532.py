l = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
c = 0
d = 0

if A%C != 0:
  c = A//C+1
else:
  c=A//C
if B%D != 0:
  d = B//D+1
else:
  d=B//D

if c>d:
  print(l-c)
else:
  print(l-d)

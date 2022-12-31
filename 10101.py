n = []
for i in range(1,4):
  t = int(input())
  n.append(t)

if n[0]+n[1]+n[2] == 180:
  if n[0] == n[1] or n[1] == n[2] or n[0] == n[2]:
    if n[0] and n[1] and n[2] == 60:
          print("Equilateral")
    else:
      print("Isosceles")
  else:
    print("Scalene")
else:
  print("Error")

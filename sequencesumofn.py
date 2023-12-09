def subsets(a,k):
  n = len(a)
  b = [[0 for h in range(n)] for h in range(n)]
  d = 0
  for i in range(n):
    for j in range(i, n):
      if i == j:
        b[i][j] = a[i]
      else:
        b[i][j] = b[i][j-1] + a[j]
      if b[i][j] == k:
        d += 1
  return d
f = open('input.inp','r')
g = open('output.out','w')
n,h = [*map(int,f.readline().split())]
b = [*map(int,f.read().split())]
print(subsets(b,h))

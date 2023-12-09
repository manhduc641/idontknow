import time
def tim(n,st,b,a):
  if n == 0:
    a.append(b[:])
    return
  if n < 0:
    return
  for i in range(st,n+1):
    if i >= 5:
      b.append(i)
      tim(n-i,i,b,a)
      b.pop()
def xuat(n):
  a = []
  tim(n,5,[],a)
  print(len(a))
st = time.time()
xuat(100)
print(time.time()-st)

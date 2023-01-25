def fib():
  x = int(input('enter for i th term : '))
  l=[1,1]
  for i in range(1,x-1):
    sum = 0;                             #fib series
    sum= l[i]+l[i-1]
    l.append(sum)
  print(l)
fib()

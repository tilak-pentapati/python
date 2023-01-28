y = input('enter a number to get list of prime numbers less than given number: ')
l=[]
def check(x):  
    if x.isdigit():
      def pr(x):
        program = False
        if int(x)==1:
         print('should be greater 1')
        elif int(x)>1:                               # prime_or_not program
           for i in range(2,int(x)):
             if int(x)%i==0:
              program =  True
              break
             else:
               continue

        if program:
            pass
        else:
            l.append(x)
      pr(x)
    else :
      print('value must be interger')                        # large no takes more time, Use it in local machine
for i in range(2,int(y)+1):
  a = check(str(i))
num = int(input('enter a number get its prime factors: '))
pr_f= []
for k in range(0,len(l)):
  if (num//int(l[k]) != 0 and num%int(l[k]) == 0):
    pr_f.append(l[k])
  else:
    pass
print(pr_f)

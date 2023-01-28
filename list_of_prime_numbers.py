y = input('enter a number to get list of prime numbers less than given number: ')
l=[]
def check(x):
    if x.isdigit():
      def pr(x):
        program = False
        if int(x)==1:
         print('should be greater 1')
        elif int(x)>1:                                    # prime_or_not program
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
                                                             # gives list of prime numbers
print(l)
print('No of Prime numbers from 0 to '+ str(y) +' are '+ str(len(l))) 

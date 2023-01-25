def main():
  program = True
  while  program:
      x = input('Enter a integer to check even or odd: ')
   
      if x.isdigit():
       if int(x)%2 == 0:
         print('Even Number')
         program = False                            # even_odd program
       else:
         print('Odd Number')
         program = False

      else :
         print('value must be interger')
         program = False

main()

f = open("ti.txt", "r")
i = 0
li = []

for x in f:
    i += 1
    li.append(x)
y_l = []

for x in range(1, i+1):
    a = li[x - 1]
    n = []
    for y in a:
        if y.isdigit():
            n.append(y)
    separator = ''
    y_l.append(separator.join(n))

o_nu = []
for z in y_l:
    if z.isdigit():
        o_nu.append(z)


class Num:
  twenty_less = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
  all_tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
  thousands = ["", "Thousand", "Million", "Billion", "Trillion"]

  def num_to_word(self, num):
        if num == 0:
         return "Zero"
        i = 0
        word = ""
        while num > 0:
         if (num % 1000) != 0:
            word = self.root(num % 1000) + Num.thousands[i] + " " + word
         i = i + 1
         num = num // 1000
        return word.strip()
  def root(self,i):
         if i == 0 :
          return ""
         elif i < 20:
          return Num.twenty_less[i] + " "
         elif i < 100:

          return Num.all_tens[i//10]+ " " + self.root(i%10)
         else:
          return Num.twenty_less[i//100] + " Hundred " + self.root(i%100)



nu = Num()


wor = []
for qw in o_nu:
  wor.append(nu.num_to_word(int(qw)))


f.close()

low =[]
for q in range(0,len(o_nu)):
    low.append(o_nu[q] + " " + wor[q] + " ")

print(low)
f = open("ti.txt","a")
f.write("        ")
f.close()

f = open("ti.txt","a")
f.writelines(low)
f.close()

# Hello World program in Python
tab = ["HAPPY","NEW","YEAR","_^^_"]

for i in range(20):
  j = i*"*"+"2021"+"*"*i
  tab.append(j)
  
tab.append("2021") 

print(15*" "+tab[0]+" "+tab[1]+" "+tab[2]+"\n")
print(21*" "+tab[3])

for j in range(4,len(tab)-1):
  z=len(tab)-j
  print(z*" "+tab[j])
  
for i in range(0,2):
  print((j-2)*" "+tab[len(tab)-1])
  
print(47*"^")

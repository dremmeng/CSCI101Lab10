#Drew Remmenga
#Section F
# Forty Five  Minutes

filename=input("Enter the name of the file containing math problems : ")

with open(filename) as f:
  read=f.readlines()
  final=[]
  for i in read:
    result=round(eval(i.replace(",","")))
    final.append(result)

output=input("Enter the name of the file in which to store the results :")

with open(output, 'w') as f:
    for item in final:
        f.write("%i," % item)
f.close()

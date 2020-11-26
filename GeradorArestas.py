import sys
import random

ANumb = int(sys.argv[1], 10)
string = ""

for i in range(ANumb):
  for j in range(ANumb):
    if j > i:
      if random.randint(0, 10) < 2:
        string += str(i)+","+str(j)+"\n"


file = open("Arestas.txt", "w") 
file.write(string) 
file.close()
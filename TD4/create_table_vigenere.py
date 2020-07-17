import sys
import re
import json

base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("\\begin{tabular}{", "c|"*len(base), "}")

print(" &", "&".join(base), "\\\\")
print("\\hline")

for lettre in base:
  index = base.index(lettre)
  serie = lettre+base[index:]+base[:index]
  print(" &", "&".join(serie), "\\\\")

print("\\end{tabular}")

#l = []
#for i in base:
#  l.append(i)
#dic = {}
#for ligne in open(sys.argv[1]).readlines():
#  ligne=ligne.upper()
#  lettre, elem = re.split("=", ligne)
#  elem = re.sub('"|\n',"",elem)
#  dic.setdefault(lettre, {})
#  for i in range(0, len(base)):
#    dic[lettre][base[i]] = elem[i]
#
#w = open("vigenere.json", "w")
#w.write(json.dumps(dic, indent= 2))
#w.close()

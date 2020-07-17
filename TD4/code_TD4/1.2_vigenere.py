import json
f = open("Epistemo-TD4-vigenere.json")
dico_vigenere = json.load(f)
f.close()
message_base = "TOTOTITI"#seulement des majuscules
cle = "TOKEN"#la clé n'a pas de signification
while len(cle)<len(message_base):
  cle+=cle
print("Message à coder : ",message_base)
print("Clé : ", cle)
message_code = ""
cpt = 0#va encoder la position où l'on est dans le message à coder
for caractere in message_base:
  caractere_cle = cle[cpt]
  caractere_code = dico_vigenere[caractere][caractere_cle]
  message_code+=caractere_code
  cpt+=1
print("Message codé : ", message_code)


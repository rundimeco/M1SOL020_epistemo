
def coder(message, cle):
  alphabet =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
 'W', 'X', 'Y', 'Z']
  message_code = ""
  for caractere in message:
    position = alphabet.index(caractere)
    caractere_code = alphabet[position+cle]
    message_code+=caractere_code
  return message_code

message_a_coder = "BONJOUR"
cle = 5
message_bien_code = coder(message_a_coder, cle)

print("message :", message_a_coder)
print("clé :", cle)
print("message codé :", message_bien_code) 

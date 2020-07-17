#coding:utf-8
## !!! Attention le fichier "Epistemo-TD4-vigenere.json" doit être placé dans le même répertoire (voir l'ouverture de fichier dans la fonction get_dic_vigenere)

def lire_ouvrir_fichier(chemin):
  f = open(chemin, "r")
  chaine= f.read()
  f.close()
  return chaine

def preparer_msg_cle(message, cle):
  message=message.upper()#on met le message en casse majuscule
  cle=cle.upper()#idem pour la clé
  while len(cle)<len(message):#on duplique la clé pour qu'elle soit de la même taille que le message à coder
    cle = cle+cle
  return message, cle

def get_dic_vigenere():
  chaine = lire_ouvrir_fichier("Epistemo-TD4-vigenere.json")
  dic_vigenere = eval(chaine)
  return dic_vigenere

def code_vigenere(message, cle):
  dic_vigenere = get_dic_vigenere()
  message, cle = preparer_msg_cle(message, cle)
  msg_code =""
  for i in range(0, len(message)):#on a ici une "liste" d'entiers permetatnt de parcourir chaque caractère du message et d'avoir son index (i)
    caractere_courant = message[i]
    caractere_cle = cle[i]
    caractere_code = dic_vigenere[caractere_courant][caractere_cle]  #NB: on a deux séries de crochets correspondant aux deux dimensions du dictionnaire python
    msg_code +=caractere_code#on ajouter à notre variable de sortie
  return msg_code

msg = input("Quel message souhaitez vous encoder?\n")

cle = input("avec Quelle clé (chaîne de caractères)?\n")
msg_code = code_vigenere(msg, cle)

print("En encodant le message:\n", msg)
print("Avec la clé:\n", cle)
print("On obtient le message codé:\n", msg_code)

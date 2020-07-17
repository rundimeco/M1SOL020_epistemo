def coder_decoder(msg, cle):
  table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  l = []
  for t in table:l.append(t)
  print l
  msg_decode =""
  for lettre in msg:
    if lettre not in table:
      msg_decode+=lettre
    for i in range(0, len(table)):
      if lettre == table[i]:
        break
    if i+cle>26:
      i=i-26
    msg_decode+= table[i+cle]
  return msg_decode

print coder_decoder("TOTO", 3)
    

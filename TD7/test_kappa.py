
from nltk import agreement

annotateur1 = ["DET", "NOM", "ADJ", "ADV", ]
annotateur2 = ["DET", "NOM", "NOM", "ADV"]
annotateurs = [annotateur1, annotateur2]
donnees = []

for i in range(len(annotateurs)):
  for j in range(len(annotateur1)):
    donnees.append([str(i), str(j), annotateurs[i][j]])

ratingtask = agreement.AnnotationTask(data=donnees)

print("kappa " +str(ratingtask.kappa()))
print("fleiss " + str(ratingtask.multi_kappa()))
print("alpha " +str(ratingtask.alpha()))
print("scotts " + str(ratingtask.pi()))

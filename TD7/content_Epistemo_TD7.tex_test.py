
from nltk import agreement
annotateur1 = ["DET", "NOM", "ADJ", "ADJ", "ADV", "DET","ADJ", "ADV"]
annotateur2 = ["DET", "NOM", "ADJ", "NOM", "ADV", "NOM","ADV", "ADV"]
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
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
cm = confusion_matrix(annotateur1, annotateur2)
classes = list(set(annotateur1+annotateur2))

fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(cm, annot=True, xticklabels=classes, yticklabels=classes,cmap=plt.cm.Reds )
plt.ylim([len(classes), 0])

plt.show()

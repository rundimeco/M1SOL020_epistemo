import matplotlib.pyplot as plt
import seaborn as sns

def mc2dic(data2, etiquettes):
  for i, etiq in enumerate(etiquettes):
    dic.setdefault(etiq, {"VP":0, "FP":0, "FN":0})
    dic[etiq]["VP"] = data2[i][i]
    for j in range(len(etiquettes)):
      if i!=j:
        dic[etiq]["FP"] += data1[i][j]#le reste de la ligne : FP
        dic[etiq]["FN"] += data1[j][i]#le reste de la colonne : FN
  return dic

def get_stats(dic, classes):
  Bonnes_predictions = 0
  Total_instances = 0
  for etiq, stats in dic.items():
    VP = stats["VP"]
    FP = stats["FP"]
    FN = stats["FN"]
    Bonnes_predictions+=VP
    Total_instances+= FP+FN
    #...
  print("Exactitude (accuracy): %f"%(Bonnes_predictions/Total_instances))

etiquettes = ["A", "B", "C", "D", "E"]

data1 = [
     [1, 0, 2, 0, 0], 
     [1, 9, 4, 80, 0], 
     [20, 1, 28, 5, 0], 
     [0, 18, 0, 1, 0], 
     [1, 0, 0, 0, 59]
     ]

dic = {}
for i, etiq in enumerate(etiquettes):
  dic.setdefault(etiq, {"VP":0, "FP":0, "FN":0})
  dic[etiq]["VP"] = data1[i][i]
  for j in range(len(etiquettes)):
    if i!=j:
      dic[etiq]["FP"] += data1[i][j]#le reste de la ligne : FP
      dic[etiq]["FN"] += data1[j][i]#le reste de la colonne : FN

get_stats(dic, etiquettes)

fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(data1, annot=True, xticklabels=etiquettes, yticklabels=etiquettes,cmap=plt.cm.Reds )
plt.ylim([len(etiquettes), 0])

#plt.show()
plt.savefig("matrice1.png")

data2 = [ 
	[5, 0, 0, 584, 1],
	[0, 4, 0, 84, 0],
	[1, 0, 8, 12, 2],
	[0, 0, 0, 42, 0],
	[0, 0, 0, 168, 8]
      ]

dic = mc2dic(data2, etiquettes)
get_stats(dic, etiquettes)

fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(data2, annot=True, xticklabels=etiquettes, yticklabels=etiquettes,cmap=plt.cm.Reds )
plt.ylim([len(etiquettes), 0])

#plt.show()
plt.savefig("matrice2.png")

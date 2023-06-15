import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import confusion_matrix
import graphviz

# Zadanie 3

df = pd.read_csv("C:/Users/Marcelina/Desktop/InfP/IO/lab05/iris.csv")
# print(df.isnull().any())
# print(df.describe())

sns.pairplot(df, hue='species')
# plt.show()

all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
all_classes = df['species'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=278877)
print("Train inputs:\n", train_inputs)
print("\n``````````````````````````````````")
print("Test inputs:\n", test_inputs, "\n")

dtc = DecisionTreeClassifier()
dtc.fit(train_inputs, train_classes)

dot_data = export_graphviz(dtc, out_file=None, 
                           feature_names=df.columns[:-1],  
                           class_names=df['species'].unique(),  
                           filled=True, rounded=True,  
                           special_characters=True)  
graph = graphviz.Source(dot_data)

graph.format = 'jpg'
graph.render('decision_tree')
dd_accuracy = dtc.score(test_inputs, test_classes)

print("Accuracy: ", dd_accuracy*100, "%\n")

setosa, versicolor, virginica = 0, 0, 0

for i in test_classes:
    if i == 'setosa':
        setosa += 1
    elif i == 'versicolor':
        versicolor += 1
    else:
        virginica += 1
print("Test classes:")
print("Setosa: ", setosa)
print("Versicolor: ", versicolor)
print("Virginica: ", virginica)



y_pred = dtc.predict(test_inputs)
cm = confusion_matrix(test_classes, y_pred)
print("\nConfusion matrix:\n", cm, "\n")

# Drzewko decyzyjne jest wytrenowane lepiej o ok. 2.3% niż w zadaniu 2.



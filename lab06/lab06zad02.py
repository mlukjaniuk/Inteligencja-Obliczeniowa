print("\nZadanie 2:\n")
import pandas as pd
df = pd.read_csv("C:/Users/Marcelina/Desktop/InfP/IO/lab05/iris.csv")
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import metrics



df_norm = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
target = df[['species']].replace(['setosa','versicolor','virginica'],[0,1,2])

# setosa - 0, versicolor - 1, virginica - 2

df = pd.concat([df_norm, target], axis=1)
train, test = train_test_split(df, test_size = 0.3)
trainX = train[['sepal.length','sepal.width','petal.length','petal.width']]
trainY=train.species
testX = test[['sepal.length','sepal.width','petal.length','petal.width']]
testY = test.species

clf2 = MLPClassifier(hidden_layer_sizes=(2,), max_iter = 3000, random_state=13)
clf2.fit(trainX, trainY)
prediction2 = clf2.predict(testX)
print(f"Test values: {testY.values}\n")
print(f"Prediction with 2 hidden neurons: {prediction2}")
print(f"Accuracy with 2 hidden neurons: {metrics.accuracy_score(prediction2,testY)} ({int(metrics.accuracy_score(prediction2,testY)*100)}%)\n")
clf3 = MLPClassifier(hidden_layer_sizes=(3,), max_iter = 3000, random_state=13)
clf3.fit(trainX, trainY)
prediction3 = clf3.predict(testX)
print(f"Prediction with 3 hidden neurons: {prediction3}")
print(f"Accuracy with 3 hidden neurons: {metrics.accuracy_score(prediction3,testY)} ({int(metrics.accuracy_score(prediction3,testY)*100)}%)\n")
clf33 = MLPClassifier(hidden_layer_sizes=(3,3), max_iter = 8000, random_state=13)
clf33.fit(trainX, trainY)
prediction33 = clf33.predict(testX)
print(f"Prediction with 2 layers of 3 hidden neurons: {prediction33}")
print(f"Accuracy with 2 layers of 3 hidden neurons: {metrics.accuracy_score(prediction33,testY)} ({int(metrics.accuracy_score(prediction33,testY)*100)}%)\n")


# Accuracy for default max_iter (3 trials):
# Accuracy with 2 hidden neurons:  0.6, 0.6666666666666666, 0.5555555555555556
# Accuracy with 3 hidden neurons:  0.35555555555555557, 0.2, 0.4222222222222222
# Accuracy with 2 layers of 3 hidden neurons:  0.35555555555555557, 0.2, 0.4222222222222222
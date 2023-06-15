print("\nZadanie 3:\n")
import pandas as pd
df = pd.read_csv("C:/Users/Marcelina/Desktop/InfP/IO/lab06/diabetes.csv")
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix

df_norm = df[['pregnant-times', 'glucose-concentr', 'blood-pressure', 'skin-thickness', 'insulin', 'mass-index', 'pedigree-func', 'age']
    ].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
target = df[['class']].replace(['tested_negative','tested_positive'],[0,1])

# tested_negative - 0, tested_positive - 1

df = pd.concat([df_norm, target], axis=1)
train, test = train_test_split(df, test_size = 0.3)
trainX = train[['pregnant-times','glucose-concentr','blood-pressure','skin-thickness','insulin','mass-index','pedigree-func','age']]
trainY = train['class']
testX = test[['pregnant-times','glucose-concentr','blood-pressure','skin-thickness','insulin','mass-index','pedigree-func','age']]
testY = test['class']

clf = MLPClassifier(activation='relu', hidden_layer_sizes=(6,3), max_iter = 500, random_state=13)
clf.fit(trainX, trainY)
prediction = clf.predict(testX)
print(f"Test values: {testY.values}")
print(f"Prediction: {prediction}")
print(f"Accuracy: {metrics.accuracy_score(prediction,testY)} ({int(metrics.accuracy_score(prediction,testY)*100)}%)")
print(f"Confusion matrix:\n{confusion_matrix(testY, prediction)}")


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

# Zadanie 4

dd_accuracy = 95.55555555555556
print("DD Accuracy: ", dd_accuracy, "%\n")

df = pd.read_csv("C:/Users/Marcelina/Desktop/InfP/IO/lab05/iris.csv")
y = df['species']
X = df.drop('species', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=278877)
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

classifier3 = KNeighborsClassifier(n_neighbors=3)
classifier3.fit(X_train, y_train)
y_pred3 = classifier3.predict(X_test)
acc3 = classifier3.score(X_test, y_test)
print("3NN Accuracy: ", acc3*100, "%\n")
cm3 = confusion_matrix(y_test, y_pred3)
print("Confusion matrix 3NN:\n", cm3, "\n")

classifier5 = KNeighborsClassifier(n_neighbors=5)
classifier5.fit(X_train, y_train)
y_pred5 = classifier5.predict(X_test)
acc5 = classifier5.score(X_test, y_test)
print("5NN Accuracy: ", acc5*100, "%\n")
cm5 = confusion_matrix(y_test, y_pred5)
print("Confusion matrix 5NN:\n", cm5, "\n")

classifier11 = KNeighborsClassifier(n_neighbors=11)
classifier11.fit(X_train, y_train)
y_pred11 = classifier11.predict(X_test)
acc11 = classifier11.score(X_test, y_test)
print("11NN Accuracy: ", acc11*100, "%\n")
cm11 = confusion_matrix(y_test, y_pred11)
print("Confusion matrix 11NN:\n", cm11, "\n")

gnb = GaussianNB()
y_predNB = gnb.fit(X_train, y_train).predict(X_test)
accNB = gnb.score(X_test, y_test)
print("Gaussian NB Accuracy: ", accNB*100, "%\n")
cmNB = confusion_matrix(y_test, y_predNB)
print("Confusion matrix Gaussian NB:\n", cmNB, "\n")

#Najlepszy jest klasyfikator 5NN i 11NN z niemal identyczną dokładnością równą około 97.78%.





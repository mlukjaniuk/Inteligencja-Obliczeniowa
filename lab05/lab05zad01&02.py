import pandas as pd
df = pd.read_csv("C:/Users/Marcelina/Desktop/InfP/IO/lab05/iris.csv")
from sklearn.model_selection import train_test_split
import tabulate

# Zadanie 1

# print(df)

# print(df.values)

#wszystkie wiersze, kolumna nr 0
# print(df.values[:, 0])
#wiersze od 5 do 10, wszystkie kolumny
# print(df.values[5:11, :])
#dane w komórce [1,4]
# print(df.values[1, 4])

#podzial na zbior testowy (30%) i treningowy (70%), ziarno losowosci = 13
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=13)

print(test_set)
print(test_set.shape[0])

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

# Zadanie 2

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=278877)

test_set_df = pd.DataFrame(test_set, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'iris_class'])

def classify_iris_old(sl, sw, pl, pw):
    if sl > 4:
        return("setosa")
    elif pl <= 5:
        return("virginica")
    else:
        return("versicolor")

good_predictions_old = 0
len = test_set.shape[0]
for i in range(len):
    if classify_iris_old(test_set[i,0], test_set[i,1], test_set[i,2], test_set[i,3]) == test_set[i,4]:
        good_predictions_old = good_predictions_old + 1
        
print(good_predictions_old)
print(good_predictions_old/len*100, "%")

#posortuj wg gatunku
# train_set = train_set[train_set[:,4].argsort()]
# print(train_set)

#setosa | sl min 4.3 max 5.7 | sw min 3.0 max 4.4 | pl min 1.2 max 1.9 | pw < 1 
#versicolor | sl min 5.0 max 6.9 | sw min 2.0 max 3.8 | pl min 4.8 max 6.9 | pw min 1.0 max 1.7
#virginica | sl min 5.6 max 7.7 | sw min 2.2 max 3.8 | pl min 4.8 max 6.9 | pw min 1.4 max 2.5

setosa_train_set = train_set[train_set[:,4] == "setosa"]
versicolor_train_set = train_set[train_set[:,4] == "versicolor"]
virginica_train_set = train_set[train_set[:,4] == "virginica"]
setosa_min_sl = setosa_train_set[:,0].min()
setosa_max_sl = setosa_train_set[:,0].max()
setosa_min_sw = setosa_train_set[:,1].min()
setosa_max_sw = setosa_train_set[:,1].max()
setosa_min_pl = setosa_train_set[:,2].min() 
setosa_max_pl = setosa_train_set[:,2].max()
setosa_min_pw = setosa_train_set[:,3].min()
setosa_max_pw = setosa_train_set[:,3].max()
versicolor_min_sl = versicolor_train_set[:,0].min()
versicolor_max_sl = versicolor_train_set[:,0].max()
versicolor_min_sw = versicolor_train_set[:,1].min()
versicolor_max_sw = versicolor_train_set[:,1].max()
versicolor_min_pl = versicolor_train_set[:,2].min()
versicolor_max_pl = versicolor_train_set[:,2].max()
versicolor_min_pw = versicolor_train_set[:,3].min()
versicolor_max_pw = versicolor_train_set[:,3].max()
virginica_min_sl = virginica_train_set[:,0].min()
virginica_max_sl = virginica_train_set[:,0].max()
virginica_min_sw = virginica_train_set[:,1].min()
virginica_max_sw = virginica_train_set[:,1].max()
virginica_min_pl = virginica_train_set[:,2].min()
virginica_max_pl = virginica_train_set[:,2].max()
virginica_min_pw = virginica_train_set[:,3].min()
virginica_max_pw = virginica_train_set[:,3].max()


print(tabulate.tabulate([["setosa", setosa_min_sl, setosa_max_sl, setosa_min_sw, setosa_max_sw, setosa_min_pl, setosa_max_pl, setosa_min_pw, setosa_max_pw],
                            ["versicolor", versicolor_min_sl, versicolor_max_sl, versicolor_min_sw, versicolor_max_sw, versicolor_min_pl, versicolor_max_pl, versicolor_min_pw, versicolor_max_pw],
                            ["virginica", virginica_min_sl, virginica_max_sl, virginica_min_sw, virginica_max_sw, virginica_min_pl, virginica_max_pl, virginica_min_pw, virginica_max_pw]],
                            headers=["iris_class", "sepal_length_min", "sepal_length_max", "sepal_width_min", "sepal_width_max", "petal_length_min", "petal_length_max", "petal_width_min", "petal_width_max"]))

def classify_iris(sl, sw, pl, pw):
    if pw < 1:
        return("setosa")
    elif sl > 6.9 or sw > 3.4 or pl > 5.1 or pw > 1.7:
        return("virginica")
    else:
        return("versicolor")
    
good_predictions = 0
len = test_set.shape[0]
for i in range(len):
    if classify_iris(test_set[i,0], test_set[i,1], test_set[i,2], test_set[i,3]) == test_set[i,4]:
        good_predictions = good_predictions + 1

print("Liczba wszystkich próbek: ", len)
print("Liczba poprawnie sklasyfikowanych próbek: ", good_predictions)
print("Procent poprawnie sklasyfikowanych próbek: ", good_predictions/len*100, "%")

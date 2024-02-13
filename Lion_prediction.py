import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("Lion_alpha.csv")
print(df.dtypes)
print(df["mane_color"].unique())
df["mane_color"] = df["mane_color"].replace({"Blonde" : 1, "Dark Brown" : 2,
                                             "Reddish-Brown": 3, "Black": 4, "Blonde with Dark Tips" : 5 , "Sandy": 6})
print(df["health"].unique())
df["health"] = df["health"].replace({"Poor" : 1, "Good" : 2, "Great" : 3, "Excelent" : 4})
X = df[["age", "weight", "mane_color", "health"]]
y = df["alpha"]
scaler = StandardScaler()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=8, test_size=0.3)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = RandomForestClassifier(max_depth=7, class_weight="balanced")
model.fit(X_train, y_train)
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f'Test set accuracy:\t{accuracy}')
print(f'Test set precision:\t{precision}')
print(f'Test set recall:\t{recall}')
print(f'Test set f1-score:\t{f1}')


test_conf_matrix = pd.DataFrame(
    confusion_matrix(y_test, y_pred),
    index=['actual no', 'actual yes'],
    columns=['predicted no', 'predicted yes']
)
print(test_conf_matrix)

accuracy_train = []
accuracy_test = []
depths = range(1, 26)
for i in depths:
    rf = RandomForestClassifier(max_depth=i, class_weight="balanced")
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    accuracy_test.append(accuracy_score(y_test, rf.predict(X_test)))
    accuracy_train.append(accuracy_score(y_train, rf.predict(X_train)))

# Find the best accuracy and at what depth that occurs
best_acc = np.max(accuracy_test)
best_depth = depths[np.argmax(accuracy_test)]
print(f'The highest accuracy on the test is achieved when depth: {best_depth}')
print(f'The highest accuracy on the test set is: {round(best_acc * 100, 3)}%')

# Plot the accuracy scores for the test and train set over the range of depth values
plt.plot(depths, accuracy_test, 'bo--', depths, accuracy_train, 'r*:')
plt.legend(['test accuracy', 'train accuracy'])
plt.xlabel('max depth')
plt.ylabel('accuracy')
plt.show()

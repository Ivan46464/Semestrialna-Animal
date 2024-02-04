import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))
coefficients = model.coef_
intercept = model.intercept_

print('coefficeints: ', coefficients)
print('intercept: ', intercept)


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
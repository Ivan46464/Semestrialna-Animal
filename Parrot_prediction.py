import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from LinearRegression import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv("Parrot.csv")
df['parrot_name'] = df['parrot_name'].replace({'Budgerigar': 1, 'Eclectus': 2, 'Rose-ringed parakeet': 3})
# correlation_matrix = df.corr()
# plt.show()
# df_corr = df.corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(df_corr, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.show()
multi_lin = LinearRegression()
X = df[["age", "parrot_name"]]
y = df["number_of_words"]
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.8,random_state=6)
multi_lin.fit(X_train,y_train)
score = multi_lin.score(X_train,y_train)
print(f'Train score {score}')
score_test = multi_lin.score(X_test,y_test)
print(f'Test score {score_test}')
parrot = [[12, 1]]
parrot_pred = multi_lin.predict(parrot)
print(round(parrot_pred[0]))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from LinearRegression import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
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
poly = PolynomialFeatures(degree=43)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_poly)
X_test_scaled = scaler.transform(X_test_poly)
# Create and fit the polynomial regression model
poly_reg = LinearRegression()
poly_reg.fit(X_train_scaled, y_train)
# Evaluate the model
score_train = poly_reg.score(X_train_scaled, y_train)
score_test = poly_reg.score(X_test_scaled, y_test)
pred_y_test = poly_reg.predict(X_test_scaled)
MSE_test = mean_squared_error(y_test, pred_y_test)
r2 = r2_score(y_test, pred_y_test)
sig = [12, 1]
print(f'Train score: {score_train}')
print(f'Test score: {score_test}')
print(f'Testing Error (MSE): {MSE_test}')
print(f'R2 Score: {r2}')
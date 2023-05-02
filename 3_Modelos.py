import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import  LogisticRegression

url ="https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
df = pd.read_csv(url, names=names)


x_train, x_test, y_train, y_test = train_test_split(df[df.columns[0:4]], df[df.columns[-1]], test_size=0.2)

#print(train.shape)
#print(test.shape)





modelos = []

modelo = LogisticRegression(random_state=0).fit(x_train, y_train)

print(modelo.score(x_test, y_test))

print(modelo.predict(x_test))
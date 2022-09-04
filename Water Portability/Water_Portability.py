import  matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
data = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/INTEL_Project/water_potability.csv")
data
data.head()
data.info()
data.isnull().sum()
data.fillna(data.mean(),inplace=True)
data.describe()
data.columns
sns.heatmap(data.corr())
sns.heatmap(data.corr(),annot=True)
data.boxplot(figsize=(15,6))
x = data.drop('Potability', axis=1)
y = data['Potability']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, shuffle=True, random_state=101)
x_train
y_train
x_test
y_test
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score
dt = DecisionTreeClassifier(criterion='gini', min_samples_split=10, splitter='best')
dt.fit(x_train, y_train)
prediction = dt.predict(x_test)
accuracy_dt = accuracy_score(y_test, prediction)*100
accuracy_dt
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold

dt = DecisionTreeClassifier()

criterion = ["gini", "entropy"]
splitter = ['best', 'random']
min_samples_split = range(1, 10)

parameters = dict(criterion=criterion, splitter=splitter, min_samples_split=min_samples_split)
cv = RepeatedStratifiedKFold(n_splits = 5, random_state = 101)
grid_search_dt = GridSearchCV(estimator=dt, param_grid=parameters, n_jobs=-1, cv=cv, scoring='accuracy', error_score=0)
grid_search_dt.fit(x_train, y_train)
print("Training Score: ", grid_search_dt.score(x_train, y_train)*100)
print("Testing Score: ", grid_search_dt.score(x_test, y_test)*100)
grid_search_dt.predict(x_test)
print(grid_search_dt.best_params_)
confusion_matrix(y_test, grid_search_dt.predict(x_test))

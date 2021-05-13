import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression
dataset=pd.read_csv('C:\\Users\\pavas\\Desktop\\c++\\weather.csv')
print(dataset.shape)
print(dataset.describe())
dataset.plot(x='MinTemp',y='MaxTemp',style='o')
plt.title('MIN VS MAX')
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')
plt.show()

plt.figure(figsize=(30,10))
plt.tight_layout()
sea.displot(dataset['MaxTemp'])
plt.show()

x=dataset['MinTemp'].values.reshape(-1,1)
y=dataset['MaxTemp'].values.reshape(-1,1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=0)
r=LinearRegression()
r.fit(x_train,y_train)

print('intercept',r.intercept_)

print('cofficent',r.coef_)

y_pred= r.predict(x_test)
plt.scatter(x_test,y_test,color='red')
plt.plot(x_test,y_test,color='blue',linewidth='2')
plt.show()

print('mean absolute error:',metrics.mean_absolute_error(y_test,y_pred))
print('mean squared error:',metrics.mean_squared_error(y_test,y_pred))
print('root mean squared error:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))


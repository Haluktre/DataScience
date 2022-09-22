# Data Science Library

A data science library for simple linear regression and multiple linear regression calculations that I developed for my own work.

# Simple Linear Regression and Multiple Linear Regression 

Linear regression analysis is used to estimate the value of one variable relative to the value of another variable. The variable you want to predict is called the dependent variable. The variable you use to predict the value of the other variable is called the independent variable.

Below is the simple linear regression formula ⬇

![555-1024x505](https://user-images.githubusercontent.com/44750494/187763548-9dbdbb0a-9cac-4499-a2ce-bcff816e08b7.png)

# Test Code

```python
import dataScience as ds
import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [12,16,18,20,24]

model = ds.SimpleLinearRegression()

model.fit(x, y)

print("score:",model.R_square,"b0:",model.b0,"b1:",model.b1)

y_predicts = []

for i in x:
    y_predicts.append(model.predict(i))
    
plt.plot(x, y, "ro", x, y_predicts, "-b")
plt.show()
```
## Output
```python
Finished fit!
score: 0.9799999999999999 b0: 9.600000000000001 b1: 1.4
```
![Figure 2022-08-31 235603](https://user-images.githubusercontent.com/44750494/187781116-92e6d163-6064-4c83-99df-9a5821de974d.png)


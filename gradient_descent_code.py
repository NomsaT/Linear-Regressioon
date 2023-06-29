#the libraries below are used for scientific computing and data visualization
import numpy as np
import matplotlib.pyplot as plt
# the array function generates all values of x(from 0->to->9<10)
X=np.arange(10) 
Y=(X-5)**2 +3 
print(X,Y)

#generate dummy data
plt.style.use("seaborn")
plt.xlabel("X")
plt.ylabel("Y")

#Gradient Descent
#initialize X with any random value
#Constant learning rate
x=9
lr=0.1  

#execiting 50 steps in the algorithm   (dy/dx=(x-5)**2+ 3==2(x-5)+0)      (dy/dx of a constant=0)
plt.plot(X,Y)
for i in range(100):
    grad=2*(x-5) 
    x=x-lr*grad
    y=(x-5)**2 +3
    plt.scatter(x,y)
    print(x)

plt.show()


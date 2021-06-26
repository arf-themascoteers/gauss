import numpy as np
import matplotlib.pyplot as plt
import toss

numbers = np.array(toss.toss_in_a_year())
std = np.std(numbers)
mean = np.mean(numbers)
std_distance = (numbers - mean)/std
# plt.plot(std_distance)


#plt.plot(x,y)
data = plt.hist(numbers, bins=100)
x = data[1][0:100]
y = data[0]
for i in range(len(x)):
    if y[i] == 0 and i!= 0:
        y[i] = y[i-1]
min_y = np.min(y[y > 0])
y[y==0] = min_y
plt.plot(x, y)
plt.show()


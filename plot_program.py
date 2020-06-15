import numpy as np
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
data = np.genfromtxt('Temp_Reading.txt',delimiter = ',')
i =1;
moving_averages = []
Data1 = []
while i < len(data):
    moving_averages = data[i]
    Data=moving_averages[0]
    Data1.append(Data)
    i+=1
i = 1
die_averages = []
die_value = []
while i < len(data):
    die_averages = data[i]
    Data=die_averages[1]
    die_value.append(Data)
    i+=1
size = 10
i = 0
averages = []
while i < len(data) - size + 1:
    value = Data1[i : i + size]
    average = sum(value) / size
    averages.append(average)
    i += 1
name=["Object Temp","Die Temp"]
plt1.xlabel("range")
plt1.ylabel("Temperture");
plt1.title("Temperture plot")
plt1.ylim(20,50)
plt1.plot(averages)
plt2.plot(die_value)
plt1.legend(name)
plt1.show()
plt2.show()

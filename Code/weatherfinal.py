import serial   # for Serial communication
import time     # for delay functions
import numpy as np
import pandas as pd
from sklearn.svm import SVC

arduino = serial.Serial('com4', 9600)   # Create Serial port object

time.sleep(2)                           # wait for 2 seconds for the communication to get established


x = pd.read_csv('delhidata.csv')

# print(list(x))

a = np.array(x)

y = a[:, 3]

x = np.column_stack((x.hum, x.tempm))


clf = SVC(kernel='rbf', gamma=10)

clf.fit(x, y)

print(clf.predict([[25, 43]]))


while 1:  # Do this in loop

    temp = int(arduino.readline(2))
    bin1 = arduino.readline()
    hum = int(arduino.readline(2))
    bin2 = arduino.readline()

    print("temperature :", temp)
    print("humidity:", hum)

    z = [[temp, hum]]
    print(clf.predict(z))







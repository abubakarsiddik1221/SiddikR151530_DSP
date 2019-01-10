import matplotlib.pyplot as plt
import numpy as m
F1=5
F2=20
t=m.arange(0,1,0.01)
A=m.sin(2*m.pi*F1*t)
plt.subplot(311)
plt.plot(t,A)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
B=m.sin(2*m.pi*F2*t)
plt.subplot(312)
plt.plot(t,B)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
C=A+B
plt.subplot(313)
plt.plot(t,C)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
plt.show()

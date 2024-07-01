import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,100)

y_sin= np.sin(x)
y_cos= np.cos(x)

plt.plot(x,y_sin,label="seno")
plt.plot(x,y_cos,label="coseno")

plt.xlabel("x")
plt.xlabel("y")
plt.title("Funciones Seno y Coseno")

plt.legend()

plt.show()





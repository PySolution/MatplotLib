
import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4]

x=np.arange(0, 10, 0.1)
fig1, f1_axes = plt.subplots(ncols=2, nrows=2, figsize = (10, 7))
fig1.suptitle('Figura com 4 gráficos')

#Configurações no gráfico 1 [0,0]
f1_axes[0,0].set_title('Seno de x e -x')
f1_axes[0,0].plot(np.sin(x), label = "sen(x)", color = "#db4242")
f1_axes[0,0].plot(np.sin(-x), label = "sen(-x)", color = "#80ed5f")
f1_axes[0,0].legend()

#Configurações no gráfico 2 [0,1]
f1_axes[0,1].plot(np.tan(x), label = "tan(x)", color = "#db4242")
f1_axes[0,1].plot(np.tan(-x), label = "tan(-x)", color = "#80ed5f")
f1_axes[0,1].set_title('Tangente de x e -x')
f1_axes[0,1].legend()

#Configurações no gráfico 3 [1,0]
f1_axes[1,0].set_title('Seno e Coseno de x')
f1_axes[1,0].plot(np.sin(x), label = "sen(x)", color = "#db4242")
f1_axes[1,0].plot(np.cos(x), label = "cos(x)", color = "#80ed5f")
f1_axes[1,0].legend()

#Configurações no gráfico 4 [1,1]
f1_axes[1,1].set_title('Radiano de x e -x')
f1_axes[1,1].plot(np.radians(x), label = "radians(x)", color = "#db4242")
f1_axes[1,1].plot(np.radians(-x), label = "radians(-x)", color = "#80ed5f")
f1_axes[1,1].legend()

plt.show()




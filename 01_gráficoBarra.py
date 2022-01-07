
import matplotlib.pyplot as plt

x=[0,2,3,4,8]
y=[0,4,3,1,7]

plt.bar(x, y, label = 'Dados')
plt.ylabel("Eixo Y")
plt.xlabel("Eixo x")
plt.title("Título do Gráfico")
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
plt.legend()
plt.show()



import matplotlib.pyplot as plt


#Propriedades gerais e legendas
plt.ylabel('Eixo Y')
plt.xlabel('Eixo x')
plt.title('Gráfico de linhas')
plt.axis(ymin=0, ymax=15)
plt.xticks([2,5,8,11,14,17])

#Propriedades do primeiro gráfico
x=[1,4,7,10,13,16]
y=[4,3,8,5,12,7]
plt.plot(x, y, label = 'Dados1', color = '#f52a2a')

#Propriedades do segundo gráfico
x=[2,5,8,11,14,17]
y=[1,2,4,6,8,10]
plt.plot(x, y, label = 'Dados2', color = '#24e02d')

#Propriedades do terceiro gráfico
x=[3,6,9,12,15,18]
y=[3,5,1,11,4,3]
plt.plot(x, y, label = 'Dados3', color = '#244de0')

plt.legend()
plt.show()


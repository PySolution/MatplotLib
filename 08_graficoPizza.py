
import matplotlib.pyplot as plt

#Definindo as labels e valores de cada item
labels = 'Luz', 'Água', 'Gás', 'Internet', 'Netflix'
sizes = [200.00, 125.00, 80.00, 145.00, 40.00]

#Definindo a parte do gráfico para explosão
explode = (0,0,0.1,0,0)

fig1, ax1 = plt.subplots(figsize = (5,5))

#Definindo as cores de cada parte do gráfico em padrão hexadecimal
c = ['#4fff4f', '#34b334', '#288a28', '#196119', '#0f400f']

#Inserindo os atributos de exposão e cores
ax1.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%',
        shadow = True, startangle = 90, colors = c)

ax1.axis('equal')

plt.show()



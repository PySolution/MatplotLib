
import matplotlib.pyplot as plt

import numpy as np

#Definindo a descrição dos dados do gráfico
labels = ['Luz', 'Água', 'Gás', 'Internet', 'Netflix']

#Definindo o valor de cada dado
sizes = [200.00, 125.00, 80.00, 145.00, 40.00]

#Criamos a área para plotar o gráfico e definimos seu tamanho
fig1, ax1 = plt.subplots(figsize=(7, 5), subplot_kw=dict(aspect="equal"))

#Função para calculo de porcentagem e tipo de valor
def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return"{:.1f}%\n(R$ {:d})".format(pct, absolute)

#Criamos o gráfico e inserimos a função da legenda interna
wedges, texts, autotexts = ax1.pie(sizes, autopct = lambda pct: func(pct, sizes),
                                   textprops=dict(color="w"))

#Definindo a caixa da legenda externa (título, localização e ancoragem)
ax1.legend(wedges, labels, title = 'Ítens', loc = 'center left',
           bbox_to_anchor=(1, 0, 0.5, 1))

#Definimos o título do gráfico
ax1.set_title('Gastos mensais')

#Mostrando o gráfico
plt.show()



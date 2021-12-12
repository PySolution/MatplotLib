
import matplotlib.pyplot as plt

labels = 'Luz', 'Água', 'Gás', 'Internet', 'Netflix'
sizes = [200.00, 125.00, 80.00, 145.00, 40.00]

fig1, ax1 = plt.subplots()

ax1.set_title('Gastos mensais')
ax1.pie(sizes, labels = labels, shadow=True,
        autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

plt.show()


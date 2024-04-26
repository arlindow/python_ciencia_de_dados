import matplotlib.pyplot as plt
import numpy as np

# Dados para o gráfico
labels = ['janeiro: R$232.88', 'fevereiro: R$0.00', 'março: R$0.00', 'abril: R$0.00', 'maio: R$0.00', 'junho: R$0.00']
valores = [232.88, 200.00, 200.00, 200.00, 200.00, 200.00]
cores = ['red', 'yellow', 'orange', 'green', 'blue', 'black']


# Criando o gráfico de donuts
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(valores, labels=labels, colors=cores, autopct='', startangle=90)


# Adicionando um círculo branco no meio para criar o donut
centro_circulo = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centro_circulo)


# Ajustando os aspectos do gráfico
ax.axis('equal')  # Desenhar como um círculo
plt.title('Comissão Mensal - 2024 ')


# Exibe o gráfico
plt.show()



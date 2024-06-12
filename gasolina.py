import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura dos dados
df = pd.read_csv('gasolina.csv')

# Criação do gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda', marker='o')

# Configurações do gráfico
plt.title('Preço da Gasolina em São Paulo nos 10 primeiros dias de Julho de 2021')
plt.xlabel('Dia')
plt.ylabel('Preço de Venda (R$)')
plt.grid(True)

# Salvando o gráfico
plt.savefig('gasolina.png')

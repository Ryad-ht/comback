import pandas as pd
import matplotlib.pyplot as plt

# Lire le fichier CSV dans un DataFrame
df = pd.read_csv('Data Set- Inc5000 Company List_2014.csv')

# Calculer la moyenne de la croissance pour chaque valeur de 'yrs_on_list'
avg_growth_by_yrs = df.groupby('yrs_on_list')['growth'].mean()

# Créer un graphique pour visualiser la relation
plt.figure(figsize=(10, 6))
avg_growth_by_yrs.plot(kind='bar', rot=0)
plt.title('Impact de l\'ancienneté sur la croissance moyenne')
plt.xlabel('Nombre d\'années dans la liste')
plt.ylabel('Croissance moyenne')
plt.show()
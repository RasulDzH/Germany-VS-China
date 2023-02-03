import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('countries of the world.csv')
df.info()
print(df.head())
print(df['Country'].value_counts())
print('Где уровень жизни лучше в Германии или Китае?')

ger_lit = df[df['Country']=='Germany']['Birthrate']
ch_lit = df[df['Country']=='China']['Birthrate']
ger_clim = df[df['Country']=='Germany']['Deathrate']
ch_clim = df[df['Country']=='China']['Deathrate']
ger_ind = df[df['Country']=='Germany']['Population']
ch_ind = df[df['Country']=='China']['Population']

print('Культура', 'Германия:', round(ger_lit, 2), 'Китай:', round(ch_lit, 2))
print('Климат:', 'Германия:', round(ger_clim, 2), 'Китай:', round(ch_clim, 2))
print('Промышленность:', 'Германия:', round(ger_ind, 2), 'Китай:', round(ch_ind, 2))

s = pd.Series(data = [ger_lit, ch_lit, ger_clim, ch_clim, ger_ind, ch_ind],
index = ['Культура Германии', 'Культура Китая', 'Климат Германии', 'Климат Китая', 'Промышленность Германии', 'Промышленность Китая'])
s.plot(kind = 'barh')
plt.show()
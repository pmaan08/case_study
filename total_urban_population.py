import matplotlib.pyplot as plt
import pandas as pd

urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

df_urb_pop = next(urb_pop_reader)

df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])

#zip of pops to list of tuples           
pops_list = list(pops)

#to create new column total urban population 
#list comprehension
df_pop_ceb['Total Urban Population']=[int(el[0] * el[1] * 0.01) for el in pops_list]

#plotting urban population data

df_pop_ceb.plot(kind='scatter',x='Year',y='Total Urban Population')
plt.show()

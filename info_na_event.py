import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

deelnemers = pd.read_csv('data_interviews.csv')


# x-as waardes
x_values = ['ja', 'nee']



jong = deelnemers[deelnemers['Leeftijd'] <= 26]
gezinnen = deelnemers[(deelnemers['Leeftijd'] > 26) & (deelnemers['Leeftijd'] <= 50)]
oud = deelnemers[deelnemers['Leeftijd'] > 50]


# optellen Bewust zijn
jong_counts = jong['Zou_Info_willen_na_event'].value_counts()
gezinnen_counts = gezinnen['Zou_Info_willen_na_event'].value_counts()
oud_counts = oud['Zou_Info_willen_na_event'].value_counts()


def categoriseer(wilt):
    if 'ja'.lower() in str(wilt).lower():
        return 'ja'
    elif 'nee'.lower() in str(wilt).lower():
        return 'nee'
    else:
        return 'n.v.t.'

# Apply the categorization function to the DataFrame
jong['Zou_Info_willen_na_event'] = jong['Zou_Info_willen_na_event'].apply(categoriseer)
gezinnen['Zou_Info_willen_na_event'] = gezinnen['Zou_Info_willen_na_event'].apply(categoriseer)
oud['Zou_Info_willen_na_event'] = oud['Zou_Info_willen_na_event'].apply(categoriseer)

# figuur en staafbreedte toevoegen
fig, ax = plt.subplots()
bar_width = 0.2

x_pos = np.arange(len(x_values))

# groepeer
jong_counts = jong.groupby('Zou_Info_willen_na_event').size().reindex(x_values, fill_value=0)
gezinnen_counts = gezinnen.groupby('Zou_Info_willen_na_event').size().reindex(x_values, fill_value=0)
oud_counts = oud.groupby('Zou_Info_willen_na_event').size().reindex(x_values, fill_value=0)




# staafdiagrammen voor elk doelgroep
ax.bar(x_pos - bar_width, jong_counts, bar_width, label='Jongeren', color='#5A5A5A')
ax.bar(x_pos, gezinnen_counts, bar_width, label='Gezinnen', color='#FFA500')
ax.bar(x_pos + bar_width, oud_counts, bar_width, label='Ouderen', color='#40e0d0')
# x-as labelen en titel
ax.set_xticks(x_pos)
ax.set_xticklabels(x_values)
ax.set_xlabel('wilt meer info')
ax.set_ylabel('Aantal mensen')
ax.set_title('Wilt meer info')

# legenda toevoegen
ax.legend()
# de staafdiagram 
plt.show()
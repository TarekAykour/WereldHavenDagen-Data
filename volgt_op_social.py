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
jong_counts = jong['Volgt_Op_Socials'].value_counts()
gezinnen_counts = gezinnen['Volgt_Op_Socials'].value_counts()
oud_counts = oud['Volgt_Op_Socials'].value_counts()


def categoriseer(wilt):
    if 'ja'.lower() in str(wilt).lower():
        return 'ja'
    elif 'nee'.lower() in str(wilt).lower():
        return 'nee'
    else:
        return 'n.v.t.'

# Apply the categorization function to the DataFrame
jong['Volgt_Op_Socials'] = jong['Volgt_Op_Socials'].apply(categoriseer)
gezinnen['Volgt_Op_Socials'] = gezinnen['Volgt_Op_Socials'].apply(categoriseer)
oud['Volgt_Op_Socials'] = oud['Volgt_Op_Socials'].apply(categoriseer)

# figuur en staafbreedte toevoegen
fig, ax = plt.subplots()
bar_width = 0.2

x_pos = np.arange(len(x_values))

# groepeer
jong_counts = jong.groupby('Volgt_Op_Socials').size().reindex(x_values, fill_value=0)
gezinnen_counts = gezinnen.groupby('Volgt_Op_Socials').size().reindex(x_values, fill_value=0)
oud_counts = oud.groupby('Volgt_Op_Socials').size().reindex(x_values, fill_value=0)




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
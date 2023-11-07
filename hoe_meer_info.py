import pandas as pd
import matplotlib.pyplot as plt


# CSV lezen
deelnemers = pd.read_csv('data_interviews.csv')



# leeftijden
jong = deelnemers[deelnemers['Leeftijd'] <= 26]
gezinnen = deelnemers[(deelnemers['Leeftijd'] > 26) & (deelnemers['Leeftijd'] <= 50)]
oud = deelnemers[deelnemers['Leeftijd'] > 50]

# optellen Bewust zijn
jong_counts = jong['Hoe_info_ontvangen'].value_counts()
Gezinnen_counts = gezinnen['Hoe_info_ontvangen'].value_counts()
oud_counts = oud['Hoe_info_ontvangen'].value_counts()

print(jong_counts)


x_values = ['sociale media', 'TV/radio en krant', 'nieuwsbrief' ]

# 'Aantal_keer_geweest' categorizeren
def categoriseer(manier):
    if 'social' in str(manier):
        return 'sociale media'
    elif 'flyers' in str(manier) or 'nieuws' in str(manier) or 'website' in str(manier):
        return 'nieuwsbrief'
    elif 'TV' in str(manier) or  'radio' in str(manier) or 'krant' in str(manier):
        return 'TV/radio en krant'
    else:
        return 'nothing'


# categorizeer aantal_keer_geweest
jong['Hoe_info_ontvangen'] = jong['Hoe_info_ontvangen'].apply(categoriseer)
gezinnen['Hoe_info_ontvangen'] = gezinnen['Hoe_info_ontvangen'].apply(categoriseer)
oud['Hoe_info_ontvangen'] = oud['Hoe_info_ontvangen'].apply(categoriseer)



# staafdiagram maken
fig, ax = plt.subplots()
bar_width = 0.2
x_pos = range(len(x_values))

# aantal keren optellen en groeperen
jong_counts = jong.groupby('Hoe_info_ontvangen').size().reindex(x_values, fill_value=0)
gezinnen_counts = gezinnen.groupby('Hoe_info_ontvangen').size().reindex(x_values, fill_value=0)
oud_counts = oud.groupby('Hoe_info_ontvangen').size().reindex(x_values, fill_value=0)

ax.bar([x - bar_width for x in x_pos], jong_counts, bar_width, label='Jongeren', color='#5A5A5A')
ax.bar(x_pos, gezinnen_counts, bar_width, label='Gezinnen', color='#FFA500')
ax.bar([x + bar_width for x in x_pos], oud_counts, bar_width, label='Ouderen', color='#40e0d0')

# labels
ax.set_xticks(x_pos)
ax.set_xticklabels(x_values)
ax.set_xlabel('Soorten Media')
ax.set_ylabel('Aantal mensen')
ax.set_title('Bewustwording WHD')

# legenda
ax.legend()

# diagram 
plt.show()
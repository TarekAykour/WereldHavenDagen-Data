import pandas as pd
import matplotlib.pyplot as plt


# CSV lezen
deelnemers = pd.read_csv('data_interviews.csv')



# leeftijden
jong = deelnemers[deelnemers['Leeftijd'] <= 26]
gezinnen = deelnemers[(deelnemers['Leeftijd'] > 26) & (deelnemers['Leeftijd'] <= 50)]
oud = deelnemers[deelnemers['Leeftijd'] > 50]

# optellen Bewust zijn
jong_counts = jong['Hoe_zou_info_willen'].value_counts()
Gezinnen_counts = gezinnen['Hoe_zou_info_willen'].value_counts()
oud_counts = oud['Hoe_zou_info_willen'].value_counts()

print(jong_counts)


x_values = ['aftermovie/foto\'s', 'sociale media', 'nieuwsbrief' ]

# 'Aantal_keer_geweest' categorizeren
def categoriseer(reden):
    reden = str(reden).lower()  # Convert to lowercase for case-insensitive comparison
    if 'movie' in reden or 'foto' in reden:
        return 'aftermovie/foto\'s'
    elif 'social' in reden:
        return 'sociale media'
    elif 'nieuws' in reden:
        return 'nieuwsbrief'

# categorizeer aantal_keer_geweest
jong['Hoe_zou_info_willen'] = jong['Hoe_zou_info_willen'].apply(categoriseer)
gezinnen['Hoe_zou_info_willen'] = gezinnen['Hoe_zou_info_willen'].apply(categoriseer)
oud['Hoe_zou_info_willen'] = oud['Hoe_zou_info_willen'].apply(categoriseer)



# staafdiagram maken
fig, ax = plt.subplots()
bar_width = 0.2
x_pos = range(len(x_values))

# aantal keren optellen en groeperen
jong_counts = jong.groupby('Hoe_zou_info_willen').size().reindex(x_values, fill_value=0)
gezinnen_counts = gezinnen.groupby('Hoe_zou_info_willen').size().reindex(x_values, fill_value=0)
oud_counts = oud.groupby('Hoe_zou_info_willen').size().reindex(x_values, fill_value=0)

ax.bar([x - bar_width for x in x_pos], jong_counts, bar_width, label='Jongeren', color='#5A5A5A')
ax.bar(x_pos, gezinnen_counts, bar_width, label='Gezinnen', color='#FFA500')
ax.bar([x + bar_width for x in x_pos], oud_counts, bar_width, label='Ouderen', color='#40e0d0')

# labels
ax.set_xticks(x_pos)
ax.set_xticklabels(x_values)
ax.set_xlabel('Reden')
ax.set_ylabel('Aantal mensen1')
ax.set_title('Motivatie van gaan')

# legenda
ax.legend()

# diagram 
plt.show()
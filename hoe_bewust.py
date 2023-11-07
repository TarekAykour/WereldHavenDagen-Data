import pandas as pd
import matplotlib.pyplot as plt


# CSV lezen
deelnemers = pd.read_csv('data_interviews.csv')



# leeftijden
jong = deelnemers[deelnemers['Leeftijd'] <= 26]
gezinnen = deelnemers[(deelnemers['Leeftijd'] > 26) & (deelnemers['Leeftijd'] <= 50)]
oud = deelnemers[deelnemers['Leeftijd'] > 50]

# optellen Bewust zijn
jong_counts = jong['Hoe_Bewust'].value_counts()
Gezinnen_counts = gezinnen['Hoe_Bewust'].value_counts()
oud_counts = oud['Hoe_Bewust'].value_counts()

print(jong_counts)


x_values = ['School', 'Woont er naast', 'nieuws', 'mond-tot-mond', 'TV en radio/krant', 'stad', 'overig']

# 'Aantal_keer_geweest' categorizeren
def manier_gezien(media):
    if str(media) == 'School'or str(media) == 'school':
        return 'School'
    elif str(media) == 'Woont er naast' or 'huis' in str(media):
        return 'Woont er naast'
    elif 'mond' in str(media):
        return 'mond-tot-mond' 
    elif str(media) == 'stad' or 'advertenties' in str(media):
        return 'stad'
    elif 'nieuws' in str(media):
        return 'nieuws'
    elif 'TV' in str(media) or 'radio' in str(media) or 'krant' in str(media) or 'flyers' in str(media):
        return 'TV en radio/krant'
    else:
        return 'overig'


# categorizeer aantal_keer_geweest
jong['Hoe_Bewust'] = jong['Hoe_Bewust'].apply(manier_gezien)
gezinnen['Hoe_Bewust'] = gezinnen['Hoe_Bewust'].apply(manier_gezien)
oud['Hoe_Bewust'] = oud['Hoe_Bewust'].apply(manier_gezien)



# staafdiagram maken
fig, ax = plt.subplots()
bar_width = 0.2
x_pos = range(len(x_values))

# aantal keren optellen en groeperen
jong_counts = jong.groupby('Hoe_Bewust').size().reindex(x_values, fill_value=0)
gezinnen_counts = gezinnen.groupby('Hoe_Bewust').size().reindex(x_values, fill_value=0)
oud_counts = oud.groupby('Hoe_Bewust').size().reindex(x_values, fill_value=0)

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
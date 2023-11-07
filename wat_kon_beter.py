import pandas as pd
import matplotlib.pyplot as plt


# CSV lezen
deelnemers = pd.read_csv('data_interviews.csv')



# leeftijden
jong = deelnemers[deelnemers['Leeftijd'] <= 26]
gezinnen = deelnemers[(deelnemers['Leeftijd'] > 26) & (deelnemers['Leeftijd'] <= 50)]
oud = deelnemers[deelnemers['Leeftijd'] > 50]

# optellen Bewust zijn
jong_counts = jong['Wat_Kon_Beter'].value_counts()
Gezinnen_counts = gezinnen['Wat_Kon_Beter'].value_counts()
oud_counts = oud['Wat_Kon_Beter'].value_counts()

print(jong_counts)


x_values = ['drukte', 'promotie', 'niks']

# 'Aantal_keer_geweest' categorizeren
def categoriseer(reden):
    reden = str(reden).lower()  # Convert to lowercase for case-insensitive comparison
    if 'drukte' in reden:
        return 'drukte'
    elif 'promotie' in reden:
        return 'promotie'
    elif 'niks' in reden:
        return 'niks'


# categorizeer aantal_keer_geweest
jong['Wat_Kon_Beter'] = jong['Wat_Kon_Beter'].apply(categoriseer)
gezinnen['Wat_Kon_Beter'] = gezinnen['Wat_Kon_Beter'].apply(categoriseer)
oud['Wat_Kon_Beter'] = oud['Wat_Kon_Beter'].apply(categoriseer)



# staafdiagram maken
fig, ax = plt.subplots()
bar_width = 0.2
x_pos = range(len(x_values))

# aantal keren optellen en groeperen
jong_counts = jong.groupby('Wat_Kon_Beter').size().reindex(x_values, fill_value=0)
gezinnen_counts = gezinnen.groupby('Wat_Kon_Beter').size().reindex(x_values, fill_value=0)
oud_counts = oud.groupby('Wat_Kon_Beter').size().reindex(x_values, fill_value=0)

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
import pandas as pd
import matplotlib.pyplot as plt

# CSV lezen
deelnemers = pd.read_csv('data_interviews.csv')

# leeftijden
jong = deelnemers[deelnemers['Leeftijd'] <= 26]
gezinnen = deelnemers[(deelnemers['Leeftijd'] > 26) & (deelnemers['Leeftijd'] <= 50)]
oud = deelnemers[deelnemers['Leeftijd'] > 50]

# x-as 
x_values = ['0', '1-2', '3-5', '5+']

# 'Aantal_keer_geweest' categorizeren
def categorize_attendance(attendance):
    if attendance == 0:
        return '0'
    elif 1 <= attendance <= 2:
        return '1-2'
    elif 3<= attendance <= 5:
        return '3-5'
    else:
        return '5+'

# categorizeer aantal_keer_geweest
jong['Aantal_keer_geweest'] = jong['Aantal_keer_geweest'].apply(categorize_attendance)
gezinnen['Aantal_keer_geweest'] = gezinnen['Aantal_keer_geweest'].apply(categorize_attendance)
oud['Aantal_keer_geweest'] = oud['Aantal_keer_geweest'].apply(categorize_attendance)


# staafdiagram maken
fig, ax = plt.subplots()
bar_width = 0.2
x_pos = range(len(x_values))

# aantal keren optellen en groeperen
jong_counts = jong.groupby('Aantal_keer_geweest').size().reindex(x_values, fill_value=0)
gezinnen_counts = gezinnen.groupby('Aantal_keer_geweest').size().reindex(x_values, fill_value=0)
oud_counts = oud.groupby('Aantal_keer_geweest').size().reindex(x_values, fill_value=0)

ax.bar([x - bar_width for x in x_pos], jong_counts, bar_width, label='Jongeren', color='#5A5A5A')
ax.bar(x_pos, gezinnen_counts, bar_width, label='Gezinnen', color='#FFA500')
ax.bar([x + bar_width for x in x_pos], oud_counts, bar_width, label='Ouderen', color='#40e0d0')

# labels
ax.set_xticks(x_pos)
ax.set_xticklabels(x_values)
ax.set_xlabel('Aantal keer geweest')
ax.set_ylabel('Aantal mensen')
ax.set_title('Geweest naar het evenement')

# legenda
ax.legend()

# diagram 
plt.show()

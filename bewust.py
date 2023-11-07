import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt



def bewust():
    deelnemers = pd.read_csv('data_interviews.csv')



    # categorizeren van de deelnemers op basis van leeftijd
    jong = deelnemers[deelnemers['Leeftijd'] <= 26]
    Gezinnen = deelnemers[(deelnemers['Leeftijd'] > 26) & (deelnemers['Leeftijd'] <= 50)]
    oud = deelnemers[deelnemers['Leeftijd'] > 50]



    # Bewust van evenement


    # optellen Bewust zijn
    jong_counts = jong['Bewust_Van_Evenement'].value_counts()
    Gezinnen_counts = Gezinnen['Bewust_Van_Evenement'].value_counts()
    oud_counts = oud['Bewust_Van_Evenement'].value_counts()

    # x-as waardes
    x_values = ['Ja', 'Nee']

    # figuur en staafbreedte toevoegen
    fig, ax = plt.subplots()
    bar_width = 0.2

    # x positie definieren
    x_pos = np.arange(len(x_values))

    # staafdiagrammen voor elk doelgroep
    ax.bar(x_pos - bar_width, jong_counts, bar_width, label='Jongeren', color='#5A5A5A')
    ax.bar(x_pos, Gezinnen_counts, bar_width, label='Gezinnen', color='#FFA500')
    ax.bar(x_pos + bar_width, oud_counts, bar_width, label='Ouderen', color='#40e0d0')

    # x-as labelen en titel
    ax.set_xticks(x_pos)
    ax.set_xticklabels(x_values)
    ax.set_xlabel('Bewust van het Evenement')
    ax.set_ylabel('Aantal mensen')
    ax.set_title('Bewust van WHD')

    # legenda toevoegen
    ax.legend()

    # de staafdiagram 
    plt.show()








# deelnemers['Bewust_Van_Evenement'].plot(kind='bar', vert=False, figsize=(14,6))
# plt.show()

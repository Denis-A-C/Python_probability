# Todo add your code her# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as sts
from collections import Counter
import scipy.stats as stats
def modify_column(x):
    if x == '-':
        x = 0
    return x
def modify_interest(x):
    if x == 'dezacord total':
        x = 0
    elif x == 'dezacord':
        x = 1
    elif x == 'acord':
        x = 2
    elif x == 'acord total':
        x = 3
    return x
def modify_timp(x):
    if x == 'sub 10':
        x = 0
    elif x == 'intre 10 si 20':
        x = 1
    elif x == 'peste 20':
        x = 2
    return x
def modify_gender(x):
    if x == 'B':
        x = 1
    elif x == 'F':
        x = 0
    return x
def modify_loc(x):
    if x == 'rural':
        x = 1
    elif x == 'urban':
        x = 0
    return x
data = pd.read_excel('Rezultate.xlsx')
data = data.drop(labels = [57, 137, 66, 141])
data = data.reset_index(drop = True)
data['Examen Partial (4p)'] = data['Examen Partial (4p)'].apply(modify_column)
data['Examen Final (6p)'] = data['Examen Final (6p)'].apply(modify_column)
data['Total (10p)'] = data['Total (10p)'].apply(modify_column)
data['Materia este interesanta'] = data['Materia este interesanta'].apply(modify_interest)
data['Ore dedicate invatarii'] = data['Ore dedicate invatarii'].apply(modify_timp)
data['Domiciliul'] = data['Domiciliul'].apply(modify_loc)
data['Genul'] = data['Genul'].apply(modify_gender)
medie_partial = sum(data['Examen Partial (4p)']) / (len(data['Examen Partial (4p)']))
medie_examen = sum(data['Examen Final (6p)']) / (len(data['Examen Final (6p)']))
medie_total = sum(data['Total (10p)']) / (len(data['Total (10p)']))
corelatie = np.corrcoef(data['Examen Partial (4p)'], data['Examen Final (6p)'])
mediana_partial = sts.median(data['Examen Partial (4p)'])
mediana_examen = sts.median(data['Examen Final (6p)'])
mediana_total = sts.median(data['Total (10p)'])
deviatie_partial = sts.stdev(data['Examen Partial (4p)'])
deviatie_final = sts.stdev(data['Examen Final (6p)'])
Ox_gen = ['Fete', 'Baieti']
fete = Counter(data['Genul'])[0] / len(data['Genul']) * 100;
baieti = Counter(data['Genul'])[1] / len(data['Genul']) * 100;
dispersie_gen = [fete, baieti]
Ox_domiciliu = ['Rural', 'Urban']
dispersie_domiciliu = [(len(data['Domiciliul']) - sum(data['Domiciliul'])) / len(data['Domiciliul']) * 100, sum(data['Domiciliul']) / len(data['Domiciliul']) * 100]

dezacord_t = Counter(data['Materia este interesanta'])[0] / len(data['Materia este interesanta']) * 100
dezacord = Counter(data['Materia este interesanta'])[1] / len(data['Materia este interesanta']) * 100
acord = Counter(data['Materia este interesanta'])[2] / len(data['Materia este interesanta']) * 100
acord_t = Counter(data['Materia este interesanta'])[3] / len(data['Materia este interesanta']) * 100
Ox_acord = ['Dezacord total', 'Dezacord', 'Acord', 'Acord total']
interes = [dezacord_t, dezacord, acord, acord_t]
sub10 = Counter(data['Ore dedicate invatarii'])[0] / len(data['Ore dedicate invatarii']) * 100;
peste10 = Counter(data['Ore dedicate invatarii'])[1] / len(data['Ore dedicate invatarii']) * 100;
peste20 = Counter(data['Ore dedicate invatarii'])[2] / len(data['Ore dedicate invatarii']) * 100;
Ox_invatare = ['Sub 10 ore', 'Intre 10 si 20 de ore', 'Peste 20 de ore']
invatare = [sub10, peste10, peste20]
# plt.figure()
# plt.bar(Ox_gen, dispersie_gen)
# plt.suptitle('Dispersie gen')
# plt.figure()
# plt.bar(Ox_domiciliu, dispersie_domiciliu)
# plt.suptitle('Dispersie domiciliu')
# plt.figure()
# plt.bar(Ox_acord, interes)
# plt.suptitle('Dispersia in functie de cat de interesanta e materia')
# plt.figure()
# plt.bar(Ox_invatare, invatare)
# plt.suptitle('Dispersia in functie de timpul alocat invatarii')
baieti_total = []
for i in range (len(data)):
    if data.loc[i].at['Genul'] == 1:
        baieti_total.append(data.loc[i].at['Total (10p)'])
fete_total = []
for i in range (len(data)):
    if data.loc[i].at['Genul'] == 0:
        fete_total.append(data.loc[i].at['Total (10p)'])
t_test_gen = stats.ttest_ind(a=baieti_total, b=fete_total, equal_var=True)

oras_total = []
for i in range (len(data)):
    if data.loc[i].at['Domiciliul'] == 0:
        oras_total.append(data.loc[i].at['Total (10p)'])
rural_total = []
for i in range (len(data)):
    if data.loc[i].at['Domiciliul'] == 1:
        rural_total.append(data.loc[i].at['Total (10p)'])
t_test_domiciliu = stats.ttest_ind(a=oras_total, b=rural_total, equal_var=True)

partial_scalat = []
for i in range (len(data)):
    partial_scalat.append(data.loc[i].at['Examen Partial (4p)'] * 10 / 4)


examen_scalat = []
for i in range (len(data)):
    examen_scalat.append(data.loc[i].at['Examen Final (6p)'] * 10 / 6)
t_test_scalat = stats.ttest_ind(partial_scalat, examen_scalat)

opinie = []
for i in range (len(data)):
    if data.loc[i].at['Materia este interesanta'] == 0 or data.loc[i].at['Materia este interesanta'] == 1:
        opinie.append(0)
    elif data.loc[i].at['Materia este interesanta'] == 2 or data.loc[i].at['Materia este interesanta'] == 3:
        opinie.append(1)
        
promovare = []
for i in range (len(data)):
    if data.loc[i].at['Total (10p)'] >= 5:
        promovare.append(1)
    else:
        promovare.append(0)
tabel = pd.crosstab(opinie, promovare)
statistica_chi2, p_val, _, _ = stats.chi2_contingency(tabel)
#Author: Nitzan Saar
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)
def read_data():
    data = pd.read_csv("breast-cancer.data")
    data.columns = ['class', 'age', 'menopause', 'column4', 'column5', 'column6', 'column7', 'breast',
                    'specific_loc', 'column10']
    return data

def most_common_classif(classsif):
    d = read_data()
    mc = d[classsif].value_counts()
    print('most common classification')
    print(mc[ :1])

def most_common_val_for_age_menopause_w_recurrences():
    d = read_data()
    recurrences = d[d['class'] == 'recurrence-events']
    print('most common age amongst patients with recurrence')
    mc_age = recurrences['age'].value_counts()
    print(mc_age[:1])
    print('most common menopause amongst patients with recurrence')
    mc_menopause = recurrences['menopause'].value_counts()
    print(mc_menopause[:1])

def plot_recurrences():
    d = read_data()
    recurrences = d[d['class'] == 'recurrence-events']
    ages = recurrences['age'].value_counts()
    ages.plot(kind='bar')
    plt.title('Number of recurrences per age group')
    plt.show()



most_common_classif('class')
most_common_val_for_age_menopause_w_recurrences()
plot_recurrences()




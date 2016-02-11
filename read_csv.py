from pandas import read_csv
import scipy.stats
from numpy import loadtxt

data = read_csv('resources/raop.csv')
#data = read_csv('resources/raop.csv', header=None)

#print(data) # pandas data-frame
#print(data.values) # numpy-array containing values



for column in data.columns[:-1]: # all columns except last
    x = data[column]
    y = data['requester_received_pizza(class)']
    print('{} {} {}'.format(column,
    'Spearman',
    scipy.stats.spearmanr(x, y)))
    print('{} {} {}'.format(column,
    'Pearson',
    scipy.stats.pearsonr(x, y)))

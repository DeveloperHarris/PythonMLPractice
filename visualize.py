import pandas as pd 
import numpy as np 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt 

#Step 1 - download the data
dataframe_all = pd.read_csv('https://d396qusza40orc.cloudfront.net/predmachlearn/pml-training.csv')
num_rows = dataframe_all.shape[0]

#Step 2 - clean the data
#count the number of missing elements (NaN) in each column
counter_nan = dataframe_all.isnull().sum()
counter_without_nan = counter_nan[counter_nan==0]
#remove the columns with missing elements
dataframe_all = dataframe_all[counter_without_nan.keys()]
#remove the first 7 columns which contain no discriminative information
dataframe_all = dataframe_all.ix[:,7:]

#Step 3 - create feature vectors
x = dataframe_all.ix[:,:-1].values
standard_scaler = StandardScaler()
x_std = standard_scaler.fit_transform(x)

# t distributed stochastic neighbor embedding (t-SNE) visualization
tsne = TSNE(n_components=2, random_state=0)
x_test_2d = tsne.fit_transform(x_std)

#scatter plot the sample points among 5 classes
markers =('s', 'd', 'o', '^', 'v')
color_map = {0: 'red', 1:'blue', 2:'lightgreen', 3:'purple', 4:'cyan'}
plt.figure()
for idx, cl in enumerate(np.unique(x_test_2d)):
	plt.scatter(x=x_test_2d[cl, 0], y=x_test_2d[cl,1], c=color_map[idx], marker=markers[idx], label=cl)
plt.show()
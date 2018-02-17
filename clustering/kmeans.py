import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import collections

def kmeans_clustering():

    df = pd.read_csv('matrixdata.csv',
                        index_col = 0)

    # Make a copy of the data frame
    df_tr = df

    # Standardize data with Z-score
    clmns = ['action', 'strategy','rpg', 'indie', 'adventure', 'sports', 'simulation', 'mmo', 'free', 'casual']
    df_tr_std = stats.zscore(df_tr[clmns])

    # Cluster the data
    kmeans = KMeans(n_clusters=7, random_state=0).fit(df_tr_std)
    labels = kmeans.labels_

    # Insert respective clusters to the original data
    df_tr['clusters'] = labels

    # Add the cluster column
    clmns.extend(['clusters'])

    # Cluster analysis
    print (df_tr[clmns].groupby(['clusters']).mean())

    # Write dataframe to file
    df_tr.to_csv('out.csv')
    
def plotting(df_tr):
    sns.lmplot('action', 'strategy', 
           data=df_tr, 
           fit_reg=False, 
           hue="clusters",  
           scatter_kws={"marker": "D", 
                        "s": 100})
    plt.title('Clusters Action vs Strategy')
    plt.xlabel('Action')
    plt.ylabel('Strategy')

    plt.show()
    
def showhistogram(df_tr):
    

    arr = df_tr.as_matrix(columns = df_tr.columns[10:])
    arr = arr.ravel()

    counter = collections.Counter(arr)

    print(counter)

    plt.hist(arr, bins=7, align='left')
    plt.show()

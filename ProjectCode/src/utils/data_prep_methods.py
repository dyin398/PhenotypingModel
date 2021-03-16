from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Function takes in data excluding target values and uses sklearn function
# to standardise the values
def standardiseData(data):
    data = StandardScaler().fit_transform(data)
    return data

# Performs the PCA algorithm on a dataset and returns the output values as a 
# 2D array
def PCAalgorithm(data, components):
    pca = PCA(n_components=components)
    principleComponents = pca.fit_transform(data)
    return principleComponents
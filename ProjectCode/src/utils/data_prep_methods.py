from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import SelectKBest
from scipy import stats

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

# Takes in two arrays of data and returns their tau value (how well they are correlated)
# and p_value
def kendallTau(data, outcomes):
    tau, p_value = stats.kendalltau(data, outcomes)
    return tau, p_value

# takes in array of features, target and number of features. Uses ANOVA algorithm
# to find the kBest features and returns them
def ANOVA(data, target, kBest):
    selector = SelectKBest(f_classif, k=kBest)
    output_features = selector.fit_transform(data, target)
    return output_features

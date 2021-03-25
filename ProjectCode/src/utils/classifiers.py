from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler

####################################
#     Preprocessing Functions      #
####################################
def minMaxScaler(data):
    scaler = MinMaxScaler();
    return scaler.fit_transform(data)

def standardScaler(data):
    scaler = StandardScaler()
    return scaler.fit_transform(data)

####################################
#       Classifier Functions       #
####################################
def logisticRegression(data, outcome):
    X = data
    y = outcome
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return y_test, X_test, model

def decisionTree(data, outcome):
    X = data
    y = outcome
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    return y_test, X_test, model

def neuralNetwork(data, outcome):
    X = data
    y = outcome
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=1)
    model = MLPClassifier(hidden_layer_sizes=(13, 13, 13), activation='relu', solver='adam', max_iter=500)
    model.fit(X_train, y_train)
    return y_test, X_test, model

def predict(model, data):
    predictions = model.predict(data)
    return predictions
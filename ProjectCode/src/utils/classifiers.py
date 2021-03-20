from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
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
    predictions = model.predict(X_test)
    return y_test, predictions

def decisionTree(data, outcome):
    X = data
    y = outcome
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return y_test, predictions

def neuralNetwork(data, outcome):
    X = data
    y = outcome
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=1)
    model = MLPClassifier(hidden_layer_sizes=(13, 13, 13), activation='relu', solver='adam', max_iter=500)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return y_test, predictions

####################################
#        Analysis Functions        #
####################################
def getClassificationReport(y_test, predictions):
    return classification_report(y_test, predictions)

def getConfusionMatrix(y_test, predictions):
    return confusion_matrix(y_test, predictions)

def getAccuracyScore(y_test, predictions):
    return accuracy_score(y_test, predictions)

def printAnalysis(y_test, predictions):
    print(getClassificationReport(y_test, predictions))
    print(getConfusionMatrix(y_test, predictions))
    print(getAccuracyScore(y_test, predictions))
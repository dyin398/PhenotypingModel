from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

####################################
#       Classifier Functions       #
####################################
def logisticRegression(data, outcome):
    X = data#.drop(['PATIENT', 'Outcome'], axis=1)
    y = outcome#data['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.70, random_state=1)
    model = LogisticRegression()
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
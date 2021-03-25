from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

####################################
#        Analysis Functions        #
####################################
def getClassificationReport(y_test, predictions):
    return classification_report(y_test, predictions)

def getConfusionMatrix(y_test, predictions):
    return confusion_matrix(y_test, predictions)

def getAccuracyScore(y_test, predictions):
    return accuracy_score(y_test, predictions)
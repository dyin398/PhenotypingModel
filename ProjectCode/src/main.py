from dataPrep.data_preparation import DataWrangler
from utils.classifiers import logisticRegression, decisionTree, printAnalysis, minMaxScaler, standardScaler

def main():
    wrangler = DataWrangler()
    patient_features, patient_outcomes = wrangler.wrangleData()
    # print(patient_features)
    performLogisticRegression(patient_features, patient_outcomes)
    # performDecisionTree(patient_features, patient_outcomes)

def performLogisticRegression(features, outcomes):
    features = minMaxScaler(features)
    y_test, predictions = logisticRegression(features, outcomes)
    printAnalysis(y_test, predictions)

def performDecisionTree(features, outcomes):
    features = minMaxScaler(features)
    y_test, predictions = decisionTree(features, outcomes)
    printAnalysis(y_test, predictions)

if __name__ == "__main__":
    main()
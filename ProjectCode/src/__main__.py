from dataPrep.data_preparation import DataWrangler
from utils.classifiers import logisticRegression, decisionTree, neuralNetwork, printAnalysis, minMaxScaler, standardScaler
from utils.data_prep_methods import ANOVA
import pandas as pd

def main():
    wrangler = DataWrangler()
    [patient_features, patient_outcomes], feature_names = wrangler.wrangleData()
    # features = pd.DataFrame(patient_features, columns=feature_names)

    # performLogisticRegression(patient_features, patient_outcomes)
    # performDecisionTree(patient_features, patient_outcomes)
    performNeuralNetwork(patient_features, patient_outcomes)


def performLogisticRegression(features, outcomes):
    features = minMaxScaler(features)
    y_test, predictions = logisticRegression(features, outcomes)
    printAnalysis(y_test, predictions)


def performDecisionTree(features, outcomes):
    features = minMaxScaler(features)
    y_test, predictions = decisionTree(features, outcomes)
    printAnalysis(y_test, predictions)

def performNeuralNetwork(features, outcomes):
    features = standardScaler(features)
    y_test, predictions = neuralNetwork(features, outcomes)
    printAnalysis(y_test, predictions)


if __name__ == "__main__":
    main()

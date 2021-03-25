from classifiers.logistic_regression import LogisticRegression
from classifiers.decision_tree import DecisionTree
from classifiers.neural_network import NeuralNetwork
from classifiers.loaded_classifier import LoadedClassifier

def createClassifier(name):
    classifier = None
    if name == "Logistic Regression":
        classifier = LogisticRegression()
    elif name == "Neural Network":
        classifier = NeuralNetwork()
    elif name == "Decision Tree":
        classifier = DecisionTree()
    elif name.endswith(".sav"):
        classifier = LoadedClassifier(name)
    return classifier
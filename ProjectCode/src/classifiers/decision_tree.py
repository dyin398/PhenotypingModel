from classifiers.classifier import Classifier
from utils.classifiers import minMaxScaler, decisionTree, predict

# Decision Tree classifier class
class DecisionTree(Classifier):

    def scaleData(self):
        self.data = minMaxScaler(self.data)

    def createClassifier(self):
        self.scaleData()
        y_test, X_test, model = decisionTree(self.data, self.outcomes)
        super().serialiseClassifier(model)
        predictions = predict(model, X_test)
        return [y_test, predictions]
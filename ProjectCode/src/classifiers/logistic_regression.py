from classifiers.classifier import Classifier
from utils.classifiers import minMaxScaler, logisticRegression, predict
import pickle

class LogisticRegression(Classifier):

    def scaleData(self):
        self.data = minMaxScaler(self.data)

    def createClassifier(self):
        self.scaleData()
        y_test, X_test, model = logisticRegression(self.data, self.outcomes)
        super().serialiseClassifier(model)
        predictions = predict(model, self.data)
        return [self.outcomes, predictions]
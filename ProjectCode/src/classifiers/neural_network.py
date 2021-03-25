from classifiers.classifier import Classifier
from utils.classifiers import minMaxScaler, neuralNetwork, predict

class NeuralNetwork(Classifier):

    def scaleData(self):
        self.data = minMaxScaler(self.data)

    def createClassifier(self):
        self.scaleData()
        y_test, X_test, model = neuralNetwork(self.data, self.outcomes)
        super().serialiseClassifier(model)
        predictions = predict(model, X_test)
        return [y_test, predictions]
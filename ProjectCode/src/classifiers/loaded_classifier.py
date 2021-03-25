from classifiers.classifier import Classifier
from utils.classifiers import predict, minMaxScaler
import pickle

class LoadedClassifier(Classifier):
    def __init__(self, classifier_path):
        super(LoadedClassifier, self).__init__()
        self.classifier_path = classifier_path

    def scaleData(self):
        self.data = minMaxScaler(self.data)

    def createClassifier(self):
        self.scaleData()
        model = pickle.load(open(self.classifier_path, 'rb'))
        predictions = predict(model, self.data)
        return [self.outcomes, predictions]

from abc import ABC, abstractmethod
import os
import pickle

class Classifier(ABC):
    def __init__(self):
        self.data = None
        self.outcomes = None
        self.classifier = None
        self.results = None
        self.output_path = "resources/outputData/trainedClassifier.sav"

    @abstractmethod
    def scaleData(self):
        pass

    @abstractmethod
    def createClassifier(self):
        pass

    def serialiseClassifier(self, model):
        self.removeOutputFile()
        pickle.dump(model, open(self.output_path, 'wb'))

    def getResults(self):
        self.getResults()

    def setData(self, data, outcomes):
        self.data = data
        self.outcomes = outcomes

    def removeOutputFile(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)
from abc import ABC, abstractmethod
import os
import pickle

# Abstract classifier class. Scales data so that it can be classifed then creates a classifier. Will train the
# classifier on the data and test on the remaining data. Newly made classifiers will be serialised and stored in
# the trainedClassifier.sav file
class Classifier(ABC):
    def __init__(self):
        self.data = None
        self.outcomes = None
        self.classifier = None
        self.results = None
        self.output_path = "resources/outputData/trainedClassifier.sav"

    # Abstract method to scale data
    @abstractmethod
    def scaleData(self):
        pass

    # Abstract method to create a specific classifier
    @abstractmethod
    def createClassifier(self):
        pass

    # Method to serialise a classifier if necessary
    def serialiseClassifier(self, model):
        self.removeOutputFile()
        pickle.dump(model, open(self.output_path, 'wb'))

    def getResults(self):
        self.getResults()

    def setData(self, data, outcomes):
        self.data = data
        self.outcomes = outcomes

    # Remove trained classifier if exists so it can be replaced
    def removeOutputFile(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)
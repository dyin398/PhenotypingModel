import abc
from abc import ABC, abstractmethod

class Extractor(ABC):

    # Initialise class with data and outcomes
    def __init__(self, data, outcomes):
        pass

    # Abstract method to extract data with relevance to outcomes
    def extractFeatures(self):
        pass

    # Abstract method to manually assess the importance of each feature 
    # and remove the unecessary features
    def manuallyRemoveFeatures(self):
        pass
    
    # Abstract method to use different preparation methods to 
    # optimise remaining data values.
    def featureSelection(self):
        pass
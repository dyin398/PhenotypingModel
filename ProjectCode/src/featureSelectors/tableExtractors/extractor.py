from abc import ABC, abstractmethod

# Abstract class containing potential methods for data preparation. Includes
# a super method which takes a dataframe and outputs it in suitable form
class Extractor(ABC):

    # Initialise class with data and outcomes
    def __init__(self, data, outcomes):
        pass

    # Abstract method to extract data with relevance to outcomes
    @abstractmethod
    def extractFeatures(self):
        pass

    # Abstract method to manually assess the importance of each feature 
    # and remove the unecessary features
    @abstractmethod
    def manuallyRemoveFeatures(self):
        pass
    
    # Suggested method to clean data selected for parsing
    def cleanData(self):
        pass

    # Abstract method to transform data into something that can be computed
    @abstractmethod
    def transformData(self):
        pass

    # Suggested method to use different preparation methods to
    # optimise remaining data values.
    def featureSelection(self):
        pass

    # Suggested method which returns data for main to impute if values are missing
    def returnImputeData(self):
        pass

    # Method turning dataframe into a dictionary of patient to array of features
    # and a list of feature names
    def dataFrameToDict(self, data):
        patients = data['PATIENT']
        features = data.drop(['PATIENT'], axis=1)
        patientsList = patients.values.tolist()
        featuresList = features.values.tolist()
        featuresDict = {}
        featureNames = list(data.columns.values) 

        for i in range(len(patientsList)):
            patient = patientsList[i]
            feature = featuresList[i]
            featuresDict[patient] = feature
        
        return featuresDict, featureNames
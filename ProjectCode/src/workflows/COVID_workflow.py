from workflows.classification_workflow import ClassificationWorkflow
from featureSelectors.feature_selector import FeatureSelector
from classifiers.classifier_factory import createClassifier
from analysers.analyser_factory import createAnalyser

class COVID_Workflow(ClassificationWorkflow):

    def createFeatureSelector(self):
        self.featureSelector = FeatureSelector(["supplies.csv", "procedures.csv", "conditions.csv", "patients.csv", "observations.csv"])

    def createMLClassifier(self):
        self.mlClassifier = createClassifier("resources/outputData/trainedClassifier.sav")

    def createAnalyser(self):
        self.analyser = createAnalyser("COVID")
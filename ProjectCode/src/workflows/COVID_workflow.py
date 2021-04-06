from workflows.classification_workflow import ClassificationWorkflow
from featureSelectors.feature_selector import FeatureSelector
from classifiers.classifier_factory import createClassifier
from analysers.analyser_factory import createAnalyser

class COVID_Workflow(ClassificationWorkflow):

    # specifies tables that need to be extracted
    def createFeatureSelector(self):
        self.featureSelector = FeatureSelector(["supplies.csv", "procedures.csv", "conditions.csv", "patients.csv", "observations.csv"])

    # specifies which classifier it requires. Either a pretrained one or a new one
    def createMLClassifier(self):
        self.mlClassifier = createClassifier("resources/outputData/trainedClassifier.sav")

    # specifies a class of required analysis methods
    def createAnalyser(self):
        self.analyser = createAnalyser("COVID")
from workflows.classification_workflow import ClassificationWorkflow
from featureSelectors.feature_selector import FeatureSelector
from classifiers.classifier_factory import createClassifier
from analysers.analyser_factory import createAnalyser

class COVID_Workflow(ClassificationWorkflow):

    def createFeatureSelector(self):
        self.featureSelector = FeatureSelector(self.tables)

    def createMLClassifier(self):
        self.mlClassifier = createClassifier(self.classifier)

    def createAnalyser(self):
        self.analyser = createAnalyser(self.analyser_name)
from abc import ABC, abstractmethod

class ClassificationWorkflow(ABC):
    def __init__(self, tables, classifier, analyser):
        # Create fields for class including inputs and empty workflow objects
        self.tables = tables
        self.classifier = classifier
        self.analyser_name = analyser
        self.featureSelector = None
        self.mlClassifier = None
        self.analyser = None

        # Create workflow objects
        self.createWorkflowObjects()

        # Execute workflow
        self.executeWorkflow()

    def createWorkflowObjects(self):
        self.createFeatureSelector()
        self.createMLClassifier()
        self.createAnalyser()

    def executeWorkflow(self):
        [data, outcomes], features = self.featureSelector.wrangleData()
        self.mlClassifier.setData(data, outcomes)
        results = self.mlClassifier.createClassifier()
        self.analyser.analyse(results)

    @abstractmethod
    def createFeatureSelector(self):
        pass

    @abstractmethod
    def createMLClassifier(self):
        pass

    @abstractmethod
    def createAnalyser(self):
        pass
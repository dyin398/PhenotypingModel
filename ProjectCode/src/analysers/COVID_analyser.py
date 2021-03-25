from analysers.analyser import Analyser
from utils.analyser_methods import getClassificationReport, getConfusionMatrix, getAccuracyScore

class COVID_Analyser(Analyser):
    def analyse(self, results):
        y_test = results[0]
        predictions = results[1]
        results = []
        results.append(getClassificationReport(y_test, predictions))
        results.append(getConfusionMatrix(y_test, predictions))
        results.append(getAccuracyScore(y_test, predictions))
        super().printToOutput(results)
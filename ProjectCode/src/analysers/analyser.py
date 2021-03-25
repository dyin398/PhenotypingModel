from abc import ABC, abstractmethod
import os

class Analyser(ABC):
    def __init__(self):
        self.output_path = "resources/outputData/analysis.txt"

    @abstractmethod
    def analyse(self, results):
        pass

    def printToOutput(self, output):
        self.removeOutputFile()
        with open(self.output_path, 'w') as file_handler:
            for item in output:
                file_handler.write("{}\n".format(item))

    def removeOutputFile(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)
from abc import ABC, abstractmethod
import os

# Abstract analyser class. An analyser includes methods analyse a given set of data and print the
# analysis to an output folder
class Analyser(ABC):
    def __init__(self):
        self.output_path = "resources/outputData/analysis.txt"

    # Abstract analyse method. Takes in results and calls printToOutput
    @abstractmethod
    def analyse(self, results):
        pass

    # Prints outputs to an output file
    def printToOutput(self, output):
        self.removeOutputFile()
        with open(self.output_path, 'w') as file_handler:
            for item in output:
                file_handler.write("{}\n".format(item))

    # Removes file if already exists
    def removeOutputFile(self):
        if os.path.exists(self.output_path):
            os.remove(self.output_path)
from analysers.COVID_analyser import COVID_Analyser

def createAnalyser(analyser_name):
    analyser = None
    if analyser_name == "COVID":
        analyser = COVID_Analyser()
    return analyser
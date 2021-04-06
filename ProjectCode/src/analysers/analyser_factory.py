from analysers.COVID_analyser import COVID_Analyser

# Factory for analyser classes. Returns an analyser
def createAnalyser(analyser_name):
    analyser = None
    if analyser_name == "COVID":
        analyser = COVID_Analyser()
    return analyser
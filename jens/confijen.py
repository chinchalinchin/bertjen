class configuration:
    
    SERIES_ACC = 100
    TRIG_ACC = 170
    NPI_ACC = 100
    LPI_ACC = 1000
    SQ_ACC = 500
    ROOT_ACC = 150
    LN_ACC = 1000
    NORM_ACC = 10000
    VERBOSE = True
    EXTRA_VERBOSE = False
    LAG = 2

    INTEGRATION_CHOICE = 3
    TECHNIQUES = {
        0:"ENDPOINT",
        1:"MIDPOINT",
        2:"TRAPEZOID",
        3: "SIMPSON"
    }

    def switchTechnique(self, arg):
        return self.TECHNIQUES.get(arg, "nothing")

    def getIntegrationTechnique(self):
        return self.switchTechnique(self.INTEGRATION_CHOICE)

    def setIntegrationTechnique(self, arg):
        if(arg != self.INTEGRATION_CHOICE):
            self.INTEGRATION_CHOICE = arg
            return True
        else: 
            return False

    def getVerbose(self):
        return self.VERBOSE

    def setVerbose(self, v):
        if(v != self.VERBOSE):
            self.VERBOSE = v
            return True
        else: 
            return False

    def getExtraVerbose(self):
        return self.EXTRA_VERBOSE

    def setExtraVerbose(self, ev):
        if(ev != self.EXTRA_VERBOSE):
            self.EXTRA_VERBOSE = ev
            return True
        else:
            return False
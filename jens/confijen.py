import sys
import json
import helpjen
import datetime

class configuration:

    def __init__(self):
        self.TRIG_LIMIT = 4000
        self.LN_LIMIT = 1000
        self.LN_BREAK = 0.000000001
        self.TECHNIQUES = {
            0:"ENDPOINT",
            1:"MIDPOINT",
            2:"TRAPEZOID",
            3: "SIMPSON"
        }
        self.ANGLE_UNITS = {
            0: "RADIANS",
            1: "DEGREES"
        }
        self.SYMBOLS = {
            "cap_sigma": '\u03A3',
            "sigma" :  '\u03C3',
            "pi": '\u03C0',
            "mu" :'\u03BC',
            "delta":'\u03B4',
            "theta": '\u03F4',
            "sq": '\u221A'
        }
        self.configure()

    def configure(self):
        with open('./jens/gollys/config.json') as json_file:
            data = json.load(json_file)
            self.SERIES_ACC = data['SERIES_ACC']
            self.TRIG_ACC = data['TRIG_ACC']
            self.NPI_ACC = data['NPI_ACC']
            self.LPI_ACC = data['LPI_ACC']
            self.SQ_ACC = data['SQ_ACC']
            self.ROOT_ACC = data['ROOT_ACC']
            self.LN_ACC = data['LN_ACC']
            self.NORM_ACC =data['NORM_ACC']
            self.VERBOSE = data['VERBOSE']
            self.EXTRA_VERBOSE = data['EXTRA_VERBOSE']
            self.LAG = data['LAG']
            self.INTEGRATION_CHOICE= data['INTEGRATION_CHOICE']
            self.ANGLE_CHOICE = data['ANGLE_UNITS']

    def retrieveConstantStore(self):
        with open('./jens/gollys/store.json') as json_file:
            data = json.load(json_file)
        return data

    def retrieveActualStore(self):
        with open('./jens/gollys/actual.json') as json_file:
            data = json.load(json_file)
        return data

    def saveConfiguration(self, myMath):
        data = {}
        # data['config'] = []
        data["SERIES_ACC"] = self.SERIES_ACC
        data["TRIG_ACC"] = self.TRIG_ACC
        data["NPI_ACC"] = self.NPI_ACC
        data["LPI_ACC"] = self.LPI_ACC
        data["SQ_ACC"] = self.SQ_ACC
        data["ROOT_ACC"] = self.ROOT_ACC
        data["LN_ACC"] = self.LN_ACC
        data["NORM_ACC"] = self.NORM_ACC
        data["VERBOSE"] = self.VERBOSE
        data["EXTRA_VERBOSE"] =self.EXTRA_VERBOSE
        data["LAG"] = self.LAG
        data["INTEGRATION_CHOICE"]= self.INTEGRATION_CHOICE
        data["ANGLE_UNITS"] = self.ANGLE_CHOICE
        with open('./jens/gollys/config.json', 'w') as outfile:
            json.dump(data, outfile)
        data = {}
        data["e_store"] = myMath.e_store
        data["newtpi_store"] = myMath.newtpi_store
        data["liebpi_store"] = myMath.liebpi_store
        data["newtroot_2_store"] = myMath.newtroot_2_store
        data["newtroot_3_store"] = myMath.newtroot_3_store
        data["binroot_2_store"] = myMath.binroot_2_store
        with open('./jens/gollys/store.json', 'w') as outfile:
            json.dump(data, outfile)

    def switchUnits(self, arg):
        return self.ANGLE_UNITS.get(arg, "nothing")

    def switchTechnique(self, arg):
        return self.TECHNIQUES.get(arg, "nothing")

    def getIntegrationTechnique(self):
        return self.switchTechnique(self.INTEGRATION_CHOICE)

    def getAngleUnits(self):
        return self.switchUnits(self.ANGLE_CHOICE)

    def getSymbol(self, sym):
        return self.SYMBOLS.get(sym, "not found")

    def setIntegrationTechnique(self, arg):
        if(self.switchTechnique(arg) == "nothing"):
            return False
        else:
            if(arg != self.INTEGRATION_CHOICE):
                self.INTEGRATION_CHOICE = arg
                return True
            else: 
                return False

    def setAngleUnits(self, arg):
        if(self.switchUnits(arg) == "nothing"):
            return False
        else:
            if(arg != self.ANGLE_CHOICE):
                self.ANGLE_CHOICE = arg
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
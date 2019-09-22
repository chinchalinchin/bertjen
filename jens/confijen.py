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
            1: "DEGREES",
            2: "GRADIANS"
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
        with open('config.json') as json_file:
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

    def saveConfiguration(self):
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
        data["ANGLE_UNITS"] = self.ANGLE_UNITS
        with open('config.json', 'w') as outfile:
            json.dump(data, outfile)
        return None

    def calibrate(self, math, printer):
        flag1 = self.calibrateTrig(math, printer)
        flag2 = self.calibrateLn(math, printer)
        flag3 = self.calibrateRoot(math, printer)
        return flag1 or flag2 or flag3
        # return flag1 or flag2 or ... 

    def calibrateLn(self, math, printer):
        current = math.nearestPerfectLn(self.LN_BREAK)
        startTime = datetime.datetime.now()
        for index in range(1, self.LN_LIMIT):
            current = current + 2 * (self.LN_BREAK- math.exp(current))/(self.LN_BREAK+math.exp(current))
            if helpjen.isNan(current):
                old = self.LN_ACC
                self.LN_ACC = index - 1
                if(old == self.LN_ACC):
                    return False
                else:
                    return True
            now = datetime.datetime.now()
            if self.VERBOSE and (now - startTime > datetime.timedelta(seconds=self.LAG)):
                printer.warn("Calibrating Natural Log", "confijen.calibrateLn")
                printer.warn(f'Current Natural Log Iteration Threshold: {index}', "confijen.calibrateLn")  
                startTime = datetime.datetime.now()    

    def calibrateTrig(self, math, printer):
        startTime = datetime.datetime.now()
        for index in range(1, self.TRIG_LIMIT):
            try:
                float(math.power(4, index)*math.power(math.factorial(index), 2)*(2*index+1))
            except Exception as e:
                old = self.TRIG_ACC
                self.TRIG_ACC = index - 1
                if self.TRIG_ACC%2==1:
                    self.TRIG_ACC = self.TRIG_ACC - 1
                if(old == self.TRIG_ACC):
                    return False
                else:
                    return True
            now = datetime.datetime.now()
            if self.VERBOSE and (now - startTime > datetime.timedelta(seconds=self.LAG)):
                printer.warn("Calibrating Trig Series Approximation", "confijen.calibrateTrig")
                printer.warn(f'Current Trig Iteration Threshold: {index}', "confijen.calibrateTrig")
                startTime = datetime.datetime.now()

    def calibrateRoot(self, math, printer):
        return False

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
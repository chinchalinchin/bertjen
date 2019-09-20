import sys
import json

class configuration:
    
    self.TRIG_LIMIT = 4000
    self.LN_LIMIT = 1000000000

    def __init__(self):
        TECHNIQUES = {
            0:"ENDPOINT",
            1:"MIDPOINT",
            2:"TRAPEZOID",
            3: "SIMPSON"
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
            self.LN_ACC = data['LN_ACC']
            self.NORM_ACC =data['NORM_ACC']
            self.VERBOSE = data['VERBOSE']
            self.EXTRA_VERBOSE = data['EXTRA_VERBOSE']
            self.LAG = data['LAG']
            self.INTEGRATION_CHOICE= data['INTEGRATION_CHOICE']

    def saveConfiguration(self):
        data = {}
        # data['config'] = []
        data["SERIES_ACC"] = self.SERIES_ACC
        data["TRIG_ACC"] = self.TRIG_ACC
        data["NPI_ACC"] = self.NPI_ACC
        data["LPI_ACC"] = self.LPI_ACC
        data["SQ_ACC"] = self.SQ_ACC
        data["LN_ACC"] = self.LN_ACC
        data["NORM_ACC"] = self.NORM_ACC
        data["VERBOSE"] = self.VERBOSE
        data["EXTRA_VERBOSE"] =self.EXTRA_VERBOSE
        data["LAG"] = self.LAG
        data["INTEGRATION_CHOICE"]= self.INTEGRATION_CHOICE
        with open('config.json', 'w') as outfile:
            json.dump(data, outfile)
        return None

    def calibrate(self, math):
        flag1 = self.calibrateTrig(math)
        return flag1
        # return flag1 or flag2 or ... 

    def calibrateLn(self, math):
        return None

    def calibrateTrig(self, math):
        float_max = sys.float_info.max
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
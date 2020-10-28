import helpjen
import datetime

class ratchet:

    def __init__(self, myConfig, myPrinter, myMath):
        self.conf = myConfig
        self.printer = myPrinter
        self.math = myMath

    def calibrate(self):
        flag1 = self.calibrateTrig()
        flag2 = self.calibrateLn()
        flag3 = self.calibrateRoot()
        return flag1 or flag2 or flag3
        # return flag1 or flag2 or ... 

    def calibrateLn(self):
        current = self.math.nearestPerfectLn(self.conf.LN_BREAK)
        startTime = datetime.datetime.now()
        for index in range(1, self.conf.LN_LIMIT):
            current = current + 2 * (self.conf.LN_BREAK- self.math.exp(current))/(self.conf.LN_BREAK+self.math.exp(current))
            if helpjen.isNan(current):
                old = self.conf.LN_ACC
                self.conf.LN_ACC = index - 1
                if(old == self.conf.LN_ACC):
                    return False
                else:
                    return True
            now = datetime.datetime.now()
            if self.conf.VERBOSE and (now - startTime > datetime.timedelta(seconds=self.conf.LAG)):
                self.printer.warn("Calibrating Natural Log", "mathbert.calibrateLn")
                self.printer.warn(f'Current Natural Log Iteration Threshold: {index}', "mathbert.calibrateLn")  
                startTime = datetime.datetime.now()    

    def calibrateTrig(self):
        startTime = datetime.datetime.now()
        for index in range(1, self.conf.TRIG_LIMIT):
            try:
                float(self.math.power(4, index)*self.math.power(self.math.factorial(index), 2)*(2*index+1))
            except Exception as e:
                old = self.conf.TRIG_ACC
                self.conf.TRIG_ACC = index - 1
                if self.conf.TRIG_ACC%2==1:
                    self.conf.TRIG_ACC = self.conf.TRIG_ACC - 1
                if(old == self.conf.TRIG_ACC):
                    return False
                else:
                    return True
            now = datetime.datetime.now()
            if self.conf.VERBOSE and (now - startTime > datetime.timedelta(seconds=self.conf.LAG)):
                self.printer.warn("Calibrating Trig Series Approximation", "confijen.calibrateTrig")
                self.printer.warn(f'Current Trig Iteration Threshold: {index}', "confijen.calibrateTrig")
                startTime = datetime.datetime.now()

    def calibrateRoot(self):
        return False
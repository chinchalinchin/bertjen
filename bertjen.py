import sys, os
sys.path.append(os.path.join(sys.path[0], "jens"))
sys.path.append(os.path.join(sys.path[0], "berts"))

from mathbert import mathbert
from finbert import finbert
from statbert import statbert

from menujen import menujen
from printjen import printjen
from confijen import configuration
import helpjen

class bertjen:

    # todo: degree/radian setting
    def __init__(self):
        self.printer = printjen()
        self.conf = configuration()
        self.menu = menujen(self.conf, self.printer)
        self.math = mathbert(self.conf, self.printer)
        self.stat = statbert(self.conf, self.printer, self.math)
        self.fin = finbert(self.conf, self.printer, self.math, self.stat)
        self.alive = True

    def doProgram(self):
        self.printer.printMenu()
        self.printer.line("Make A Selection")
        while self.alive:
            rawIn = self.menu.getMenuInput()
            if(len(rawIn) == 0):
                self.printer.warn("No Input Provided", "doProgram")
            if(len(rawIn) == 1):
                if self.conf.EXTRA_VERBOSE:
                    self.printer.warn("No Argument Provided, Proceeding Through Function Manually", "doProgram")
                switchIn = self.menu.switch(rawIn[0])
                self.doManual(switchIn)
            else: 
                if self.conf.EXTRA_VERBOSE:
                    self.printer.warn("Argument Provided In Line", "doProgram")
                rawIn[0] = self.menu.switch(rawIn[0])
                self.callFunction(rawIn)

    def callFunction(self, args):
        result = "error"
        noOutput = self.menu.isNoOutput(args[0])
        if(not noOutput):
            now = self.menu.time(True, None)
        # 1 : COMPUTATION
        #################
        if self.conf.EXTRA_VERBOSE:
            self.printer.warn(f'Step 1: Computation Of {self.menu.unswitch(args[0])}')
        try:
            # COUNT
            if(args[0] == 0):
                result = self.math.countFormula(int(args[1]))
            # EXP
            elif(args[0] == 2):
                result = self.math.exp(float(args[1]))
            # FACTORIAL
            elif(args[0] == 3):
                result = self.math.factorial(int(args[1]))
            # LIEBPI
            elif(args[0] == 4):
                result = self.math.liebPi()
            # NORMCDF
            elif(args[0] == 6):
                result = self.stat.normalDistribution(float(args[1]), float(args[2]), float(args[3]))
            # NORMPDF
            elif(args[0] == 7):
                result = self.stat.normalDensity(float(args[1]), float(args[2]), float(args[3]))
            # NEWTPI
            elif(args[0 ]== 8):
                result = self.math.newtPi()
            # POWER
            elif(args[0] == 9):
                result = self.math.power(float(args[1]), int(args[2]))
            # NEWTROOT
            elif(args[0] == 11):
                result = self.math.newtRoot(float(args[1]))
            # BLACKSCHOLES
            elif(args[0] ==12):
                result = self.fin.BSF(float(args[1]), float(args[2]), float(args[3]),
                                        float(args[4]), float(args[5]), float(args[6]),
                                        helpjen.switchToBool("Call", "Put", args[7]))
            # LN
            elif(args[0] == 13):
                result = self.math.naturalLog(float(args[1]))
            # BINROOT
            elif(args[0] == 15):
                result = self.math.binRoot(float(args[1]), float(args[2]))
            # COS
            elif(args[0] == 16):
                result = self.math.cos(float(args[1])) 
            # SIN
            elif(args[0] == 17):
                result = self.math.sin(float(args[1]))
            # ARCSIN
            elif(args[0] == 18):
                result = self.math.asin(float(args[1]))
            # TAN
            elif(args[0] == 19):
                result = self.math.tan(float(args[1]))
            # ARCCOS
            elif(args[0] == 20):
                result = self.math.acos(float(args[1]))
            # ARCTAN
            elif(args[0] == 21):
                result = self.math.atan(float(args[1]))
            # BINPMF
            elif(args[0] == 24):
                result = self.stat.binomialMass(int(args[1]), float(args[2]), int(args[3]))
            # BINCDF
            elif(args[0] == 25):
                result = self.stat.binomialDistribution(int(args[1]), float(args[2]), int(args[3]))
            # LOG
            elif(args[0] == 27):
                result = self.math.log(float(args[1]), float(args[2]))
            # INTEGRAL SET
            elif(args[0] == 22):
                integralFlag = self.conf.setIntegrationTechnique(int(args[1]))
            # VERB SET
            elif(args[0] == 23):
                verbChangedFlag = self.conf.setVerbose(helpjen.switchYesOrNo(args[1]))
                extraChangedFlag = self.conf.setExtraVerbose(helpjen.switchYesOrNo(args[2]))
            # BERTJEN CALIBRATE
            elif(args[0] == 26):
                bertFlag = self.conf.calibrate(self.math, self.printer)
        # 1A : EXCEPTIONS
        ################
        except Exception as e:
            if self.conf.EXTRA_VERBOSE:
                self.printer.warn(f'Step 1A : Exception Handling For {self.menu.unswitch(args[0])}')
            # COUNT
            if(args[0] == 0):
                self.printer.warn(str(e), "mathbert.countFormula")
            # EXP
            elif(args[0] == 2):
                self.printer.warn(str(e), "mathbert.exp")
            # FACTORIAL
            elif(args[0] == 3):
                self.printer.warn(str(e), "mathbert.factorial")
            # LIEBPI
            elif(args[0] == 4):
                self.printer.warn(str(e), "mathbert.liebPi")
            # NORMCDF
            elif(args[0] == 6):
                self.printer.warn(str(e), "statbert.normalDistribution")
            # NORMPDF
            elif(args[0] == 7):
                self.printer.warn(str(e), "statbert.normalDensity")
            # NEWTPI
            elif(args[0 ]== 8):
                self.printer.warn(str(e), "mathbert.newtPi")
            # POWER
            elif(args[0] == 9):
                self.printer.warn(str(e), "mathbert.power")
            # NEWTROOT
            elif(args[0] == 11):
                self.printer.warn(str(e), "mathbert.newtRoot")
            # BLACKSCHOLES
            elif(args[0] ==12):
                self.printer.warn(str(e), "finbert.BSF")
            # LN
            elif(args[0] == 13):
               self.printer.warn(str(e), "mathbert.naturalLog")
            # BINROOT
            elif(args[0] == 15):
                self.printer.warn(str(e), "mathbert.binRoot")
            # COS
            elif(args[0] == 16):
                self.printer.warn(str(e), "mathbert.cos")
            # SIN
            elif(args[0] == 17):
                self.printer.warn(str(e), "mathbert.sin")
            # ARCSIN
            elif(args[0] == 18):
                self.printer.warn(str(e), "mathbert.asin")
            # TAN
            elif(args[0] == 19):
                self.printer.warn(str(e), "mathbert.tan")
            # ARCCOS
            elif(args[0] == 20):
                self.printer.warn(str(e), "mathbert.acos")
            # ARCTAN
            elif(args[0] == 21):
                self.printer.warn(str(e), "mathbert.atan")
            # BINPMF
            elif(args[0] == 24):
                self.printer.warn(str(e), "mathbert.binomialMass")
            # BINCDF
            elif(args[0] == 25):
                self.printer.warn(str(e), "mathbert.binomialDistribution")
            # LOG
            elif(args[0] == 27):
                self.printer.warn(str(e), "mathbert.log")
            # INTEGRAL SET
            elif(args[0] == 22):
                self.printer.warn(str(e), "confijen.setIntegrationTechnique")
            # VERB SET
            elif(args[0] == 23):
                self.printer.warn(str(e), "confijen.setVerbose")
            # BERTJEN CALIBRATE
            elif(args[0] == 26):
                self.printer.warn(str(e), "confijen.calibrate")
        
        if(not noOutput):
            self.menu.time(False, now)

        # 2 : FORMAT RESULTS
        ####################
        outString = "error"
        capSigma = self.conf.getSymbol("cap_sigma")
        sigma = self.conf.getSymbol("sigma")
        pi = self.conf.getSymbol("pi")
        mu = self.conf.getSymbol("mu")
        sq = self.conf.getSymbol("sq")
        # COUNT
        if(args[0] == 0):
            outString = f'{capSigma} {str(args[1])} = {str(result)}'
        elif(args[0] == 2):
             outString = f'e^({str(args[1])}) = {str(result)}' 
        # FACTORIAL
        elif(args[0] == 3):
            outString = f'{str(args[1])}! = {str(result)}'
        # LIEBPI
        elif(args[0] == 4):
            outString = f'{pi} = {str(result)}'
        # NORMCDF
        elif(args[0] == 6):
            Zscore = self.stat.standardize(float(args[1]), float(args[2]), float(args[3]))
            outString = f'Normal(x={str(args[1])},{mu}={str(args[2])}, {sigma}={str(args[3])}) = P(Z<{str(Zscore)}) = {str(result)}'
        # NORMPDF
        elif(args[0] == 7):
            Zscore = self.stat.standardize(float(args[1]), float(args[2]), float(args[3]))
            outString = f'Normal\'(x={str(args[1])}, {mu}={str(args[2])}, {sigma}={str(args[3])}) = P(Z={str(Zscore)}) = {str(result)}'
        # NEWTPI
        elif(args[0 ]== 8):
            outString = f'{pi} = {str(result)}'
        # POWER
        elif(args[0] == 9):
            outString = f'{str(args[1])}^{str(args[2])} = {str(result)}'
        # NEWTROOT
        elif(args[0] == 11):
            outString = f'{sq}{str(args[1])} = {str(result)}'
        # BLACKSCHOLES
        elif(args[0] ==12):
            option = "Call" if args[7] else "Put"
            argument = f'S={str(args[1])}, K={str(args[2])}, r={str(args[3])}, d={str(args[4])}'
            argument = argument + f', {sigma}={str(args[5])}, t={str(args[6])}'
            outString = f'{option}({argument}) = {str(result)}'
        # LN
        elif(args[0] == 13):
            outString = f'ln({str(args[1])}) = {str(result)}'
        # BINROOT
        elif(args[0] == 15):
            outString = f'({str(args[1])})^({str({args[2]})}) = {str(result)}'
        # COS
        elif(args[0] == 16):
            outString = f'cos({str(args[1])}) = {str(result)}'
        # SIN
        elif(args[0] == 17):
            outString = f'sin({str(args[1])}) = {str(result)}'
        # ARCSIN
        elif(args[0] == 18):
            outString = f'arcsin({str(args[1])}) = {str(result)}'
        # TAN
        elif(args[0] == 19):
            outString = f'tan({str(args[1])}) = {str(result)}'
        # ARCCOS
        elif(args[0] == 20):
            outString = f'arccos({str(args[1])}) = {str(result)}'
        # ARCTAN
        elif(args[0] == 21):
            outString = f'arctan({str(args[1])}) = {str(result)}'
        # BINPMF
        elif(args[0] == 24):
            outString = f'Binomial\'(n={str(args[1])},p={str(args[2])},x={str(args[3])}) = {str(result)}'
        # BINCDF
        elif(args[0] == 25):
            outString = f'Binomial(n={str(args[1])},p={str(args[2])},x={str(args[3])}) = {str(result)}'
        # LOG
        elif(args[0] == 27):
            outString = f'Log(base={str(args[2])}, x={str(args[1])}) = {str(result)}'
        # INTEGRAL SET
        elif(args[0] == 22):
            if integralFlag:
                self.printer.warn(f'Integration Technique Changed: {self.conf.getIntegrationTechnique()}',
                                 "confijen.integrationTechnique")
            else:
                self.printer.warn(f'Integration Technique Unchanged: {self.conf.getIntegrationTechnique()}', 
                                "confijen.integrationTechnique")
        # VERB SET
        elif(args[0] == 23):
            if verbChangedFlag:
                self.printer.warn(f'Verbose Setting Changed: {"Yes" if self.conf.getVerbose() else "No"}', 
                                "confijen.verbose")
            else:
                self.printer.warn(f'Verbose Setting Unchanged: {"Yes" if self.conf.getVerbose() else "No"}', 
                                "confijen.verbose")
            if extraChangedFlag:
                self.printer.warn(f'Extra Verbose Setting Changed: {"Yes" if self.conf.getExtraVerbose() else "No"}', 
                                "confijen.extraVerbose")
            else:
                self.printer.warn(f'Extra Verbose Setting Unchanged: {"Yes" if self.conf.getExtraVerbose() else "No"}', 
                                "confijen.extraVerbose")
        # BERTJEN CALIBRATE
        elif(args[0] == 26):
            if bertFlag:
                self.printer.warn("Bertjen Info Changed!", "confijen.calibrate")
                self.menu.printBertjenDetails()
            else:
                self.printer.warn("Bertjen Info Unchanged!", "confijen.calibrate")                
        # HELP
        elif(args[0] == 29):
            self.menu.printFunctionDetails(self.menu.switch(args[1]))
        
        if(not noOutput):
            self.printer.output(outString)

    def doManual(self, switchIn):
        args = []
        args.append(switchIn)
        self.menu.printFunctionTitle(switchIn)
        # COUNT 
        if switchIn == 0:
            n = self.menu.getInt("Please Enter Number of Terms")
            args.append(n)
        # EXP
        elif switchIn == 2:
            ex = self.menu.getFloat("Please Enter Exponent")
            args.append(ex)
        # FACT
        elif switchIn == 3:
            n = self.menu.getInt("Please Enter A Number")
            args.append(n)
        # PRINT MENU
        elif switchIn == 5:
            self.menu.printMenu()
        # NORMCDF
        elif switchIn == 6:
            mu = self.menu.getFloat("Please Enter Mean")
            sigma = self.menu.getFloat("Please Enter Sigma")
            x = self.menu.getFloat("Please Enter X")
            args.append(x)
            args.append(mu)
            args.append(sigma)
        # NORMPDF
        elif switchIn == 7:
            mu = self.menu.getFloat("Please Enter Mean")
            sigma = self.menu.getFloat("Please Enter Sigma")
            x = self.menu.getFloat("Please Enter X")
            args.append(x)
            args.append(mu)
            args.append(sigma)
        # POWER
        elif switchIn == 9:
            b = self.menu.getFloat("Please Enter Base b: ")
            a = self.menu.getFloat("Please Enter Exponent a: ")
            args.append(b)
            args.append(a)
        # NEWTROOT
        elif switchIn == 11:
            n = self.menu.getFloat("Please Enter Number")
            args.append(n)
        # BLACKSCHOLES
        elif switchIn == 12:
            opt = self.menu.getBinaryDecision("Call", "Put")
            s = self.menu.getFloat("Spot Price")
            k = self.menu.getFloat("Strike Price")
            r = self.menu.getFloat("Continuous Risk Free Rate")
            d = self.menu.getFloat("Continuous Dividend Rate")
            o = self.menu.getFloat("Observed Volatility")
            t = self.menu.getFloat("Time To Expiration")
            args.append(s)
            args.append(k)
            args.append(r)
            args.append(d)
            args.append(o)
            args.append(t)
            args.append(opt)
        # LN
        elif switchIn == 13:
            n = self.menu.getFloat("Please Enter Number")
            args.append(n)
        # BINROOT
        elif switchIn == 15:
            n = self.menu.getFloat("Please Enter Number")
            r = self.menu.getFloat("Please Enter Root")
            args.append(n)
            args.append(r)
        # COS
        elif switchIn == 16:
            n = self.menu.getFloat("Please Enter Number (In Radians)")
            args.append(n)
        # SIN
        elif switchIn == 17:
            n = self.menu.getFloat("Please Enter Number (In Radians)")
            args.append(n)
        # ASIN
        elif switchIn == 18:
            n = self.menu.getFloat("Please Enter Number")
            args.append(n)
        # TAN
        elif switchIn == 19:
            n = self.menu.getFloat("Please Enter Number (In Radians)")
            args.append(n)
        # ACOS
        elif switchIn == 20:
            n = self.menu.getFloat("Please Enter Number")
            args.append(n)
        # ATAN
        elif switchIn == 21:
            n = self.menu.getFloat("Please Enter Number")
            args.append(n)
        # BINPMF
        elif switchIn == 24:
            n = self.menu.getInt("Please Enter Number Of Trials")
            p = self.menu.getFloat("Please Enter Probability Of Success")
            x = self.menu.getInt("Please Enter Desired Probability Mass")
            args.append(n)
            args.append(p)
            args.append(x)
        # BINCDF
        elif switchIn == 25:
            n = self.menu.getInt("Please Enter Number Of Trials")
            p = self.menu.getFloat("Please Enter Probability Of Success")
            x = self.menu.getInt("Please Enter Desired Probability Mass")
            args.append(n)
            args.append(p)
            args.append(x)
        # LOG
        elif switchIn == 27:
            a = self.menu.getFloat("Please Enter Base")
            x = self.menu.getFloat("Please Enter Number")
            args.append(x)
            args.append(a)
        # INTEGRAl SET
        elif switchIn == 22:
            self.menu.printIntegrationDetails(self.conf)
            n = self.menu.getTechnique(self.conf)
            changedFlag = self.conf.setIntegrationTechnique(n)
            if changedFlag:
                self.printer.warn(f'Integration Technique Changed: {self.conf.getIntegrationTechnique()}',
                                 "confijen.integrationTechnique")
            else:
                self.printer.warn(f'Integration Technique Unchanged: {self.conf.getIntegrationTechnique()}', 
                                "confijen.integrationTechnique")
        # VERBOSE SET
        elif switchIn == 23:
            self.menu.printVerboseDetails(self.conf)
            self.printer.bullet("Verbose?")
            verboseFlag = self.menu.getBinaryDecision("Yes", "No")
            changedFlag = self.conf.setVerbose(verboseFlag)
            if changedFlag:
                self.printer.warn(f'Verbose Setting Changed: {"Yes" if verboseFlag else "No"}', 
                                "confijen.verbose")
            else:
                self.printer.warn(f'Verbose Setting Unchanged: {"Yes" if verboseFlag else "No"}', 
                                "confijen.verbose")
            self.menu.printExtraVerboseDetails(self.conf)
            self.printer.bullet("Extra Verbose?")
            extraVerboseFlag = self.menu.getBinaryDecision("Yes", "No")
            changedFlag = self.conf.setExtraVerbose(extraVerboseFlag)
            if changedFlag:
                self.printer.warn(f'Extra Verbose Setting Changed: {"Yes" if extraVerboseFlag else "No"}', 
                                "confijen.extraVerbose")
            else:
                self.printer.warn(f'Extra Verbose Setting Unchanged: {"Yes" if extraVerboseFlag else "No"}', 
                                "confijen.extraVerbose")
        # BERTJEN CALIBRATE
        elif switchIn == 26:
            self.menu.printBertjenDetails(self.conf)
            self.printer.bullet("Calibrate Bertjen To System?")
            calibrateFlag = self.menu.getBinaryDecision("Yes", "No")
            if calibrateFlag:
                changedFlag = False
                try:
                    changedFlag = self.conf.calibrate(self.math, self.printer)
                except Exception as e:
                    self.printer.warn(str(e), "confijen.calibrate")
                if changedFlag:
                    self.printer.warn("Bertjen Info Changed!", "confijen.calibrate")
                    self.menu.printBertjenDetails()
                else:
                    self.printer.warn("Bertjen Info Unchanged!", "confijen.calibrate")
        # SAVE
        elif switchIn == 28:
            self.printer.bullet("Save Or Forget?")
            saveFlag = self.menu.getBinaryDecision("Save", "Forget")
            if saveFlag:
                self.conf.saveConfiguration()
                self.printer.warn("Configuration Saved To File", "config.json")
            else:
                self.printer.warn("Configuration Not Saved", "config.json")
        # HELP
        elif switchIn == 29:
            func = self.menu.getFunctionIndex()
            self.menu.printFunctionDetails(func)
        # QUIT
        elif switchIn == 99:
            self.alive = False
        # NOT FOUND
        elif switchIn != 4 and switchIn != 8:
            self.printer.warn("Error. Make Another Selection", "doProgram")
        # IF NOT CONFIGURE FUNCTION, CALL FUNCTION
        if(switchIn != 99 and switchIn != 28 and (not self.menu.isNoOutput(switchIn))):
            self.callFunction(args)
        self.printer.divider()

########################################################################
#                              MAIN                                    #
########################################################################
if __name__ == '__main__':
    bertjen = bertjen()
    bertjen.doProgram()

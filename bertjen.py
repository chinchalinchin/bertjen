import sys, os
sys.path.append(os.path.join(sys.path[0], "jens"))
sys.path.append(os.path.join(sys.path[0], "berts"))
sys.path.append(os.path.join(sys.path[0], "jens","gollys"))
sys.path.append(os.path.join(sys.path[0], "berts","chets"))

from mathbert import mathbert
from finbert import finbert
from statbert import statbert

from menujen import menujen
from printjen import printjen
from confijen import configuration
from identijen import identijen
import helpjen

class bertjen:

    # ADDING NEW FUNCTIONS:
    # 1: add function title to printjen.printMenu
    # 2: add function name to identijen.switcher and identijen.unswitcher 
    #   dictionaries
    # 3: add title to menujen.getFunctionTitle
    # 4: add description to menujen.getFunctionDetails
    # 5: add function to menujen input groupings based on input type,
    #   class type and output type
    #   -primary groupings: singleArg, doubleArg, tripleArg, specialArg
    #   -secondary groupings: intArg, floatArg, boolArg, stringArg,
    #                         compoundArg
    #   -non-hierarchical groupings: trigFunc, normalFunc, binomialFunc,
    #                                noOutputFunc
    #       A: If special input, ensure menujen.getMenuInput 
    #           properly filters input
    # 6: Add to manual call in bertjen.doManual
    # 7: Add to function call list in bertjen.callFunction
    #       A: Add to Computation
    #       B: Add to Exception Handling (if applicable)
    #       C: Add to Output Formatting
    #       D: Add to Output or Prevent Output
    #
    # TODO: function recursion, i.e. cos(newtPi()) or 'cos npi' from line
    # TODO: Config preferredPi, preferredRoot2, preferredRoot3
    #        with confijen and config.json.
    # TODO: Allow preferences to be set with new admin function

    def __init__(self):
        self.printer = printjen()
        self.conf = configuration()
        self.ident = identijen()
        self.menu = menujen(self.conf, self.printer, self.ident)
        self.math = mathbert(self.conf, self.printer)
        self.stat = statbert(self.conf, self.printer, self.math)
        self.fin = finbert(self.conf, self.printer, self.math, self.stat)
        self.alive = True

    # Import mathbert from bertjen so it may be configured properly
    def getMathbert(self):
        myPrinter = printjen()
        myConf = configuration()
        # todo turn off verbose settings in configruation
        myMath = mathbert(myConf, myPrinter)
        return myMath
    
    # Import statbert from bertjen so it may be configured properly
    def getStatbert(self):
        myPrinter = printjen()
        myConf = configuration()
        # todo turn off verbose settings in configruation
        myMath = mathbert(myConf, myPrinter)
        myStat = statbert(myConf, myPrinter, myMath)
        return myStat

    # Import finbert from bertjen so it may be configured properly
    def getFinbert(self):
        myPrinter = printjen()
        myConf = configuration()
        # todo turn off verbose settings in configruation
        myMath = mathbert(myConf, myPrinter)
        myStat = statbert(myConf, myPrinter, myMath)
        myFin = finbert(myConf, myPrinter, myMath, myStat)
        return self.fin

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
                switchIn = self.ident.switch(rawIn[0])
                self.doManual(switchIn)
            else: 
                if self.conf.EXTRA_VERBOSE:
                    self.printer.warn("Argument Provided In Line", "doProgram")
                rawIn[0] = self.ident.switch(rawIn[0])
                self.callFunction(rawIn)

    def callFunction(self, args):
        result = "error"
        noOutput = self.ident.isNoOutput(args[0])
        if(not noOutput):
            now = self.menu.time(True, None)
        # 1 : COMPUTATION
        #################
        if self.conf.EXTRA_VERBOSE:
            self.printer.warn(f'Step 1: Computation Of {self.ident.unswitch(args[0])}', "callFunction")
        try:
            if(args[0] == self.ident.switch("CF")):
                result = self.math.countFormula(int(args[1]))
            elif(args[0] == self.ident.switch("E")):
                result = self.math.exp(float(args[1]))
            elif(args[0] == self.ident.switch("F")):
                result = self.math.factorial(int(args[1]))
            elif(args[0] == self.ident.switch("LPI")):
                result = self.math.liebPi()
            elif(args[0] == self.ident.switch("NORMCDF")):
                result = self.stat.normalDistribution(float(args[1]), float(args[2]), float(args[3]))
            elif(args[0] == self.ident.switch("NORMPDF")):
                result = self.stat.normalDensity(float(args[1]), float(args[2]), float(args[3]))
            elif(args[0 ]== self.ident.switch("NPI")):
                result = self.math.newtPi()
            elif(args[0] == self.ident.switch("P")):
                result = self.math.power(float(args[1]), int(args[2]))
            elif(args[0] == self.ident.switch("SQ")):
                result = self.math.newtRoot(float(args[1]))
            elif(args[0] == self.ident.switch("BS")):
                result = self.fin.BSF(float(args[1]), float(args[2]), float(args[3]),
                                        float(args[4]), float(args[5]), float(args[6]),
                                        helpjen.switchToBool("Call", "Put", args[7]))
            elif(args[0] == self.ident.switch("LN")):
                result = self.math.naturalLog(float(args[1]))
            elif(args[0] == self.ident.switch("ROOT")):
                result = self.math.binRoot(float(args[1]), float(args[2]))
            elif(args[0] == self.ident.switch("COS")):
                result = self.math.cos(float(args[1])) 
            elif(args[0] == self.ident.switch("SIN")):
                result = self.math.sin(float(args[1]))
            elif(args[0] == self.ident.switch("ASIN")):
                result = self.math.arcsin(float(args[1]))
            elif(args[0] == self.ident.switch("TAN")):
                result = self.math.tan(float(args[1]))
            elif(args[0] == self.ident.switch("ACOS")):
                result = self.math.arccos(float(args[1]))
            elif(args[0] == self.ident.switch("ATAN")):
                result = self.math.arctan(float(args[1]))
            elif(args[0] == self.ident.switch("SEC")):
                result = self.math.sec(float(args[1]))
            elif(args[0] == self.ident.switch("CSC")):
                result = self.math.csc(float(args[1]))
            elif(args[0] == self.ident.switch("COT")):
                result = self.math.cot(float(args[1]))
            elif(args[0] == self.ident.switch("BINPMF")):
                result = self.stat.binomialMass(int(args[1]), float(args[2]), int(args[3]))
            elif(args[0] == self.ident.switch("BINCDF")):
                result = self.stat.binomialDistribution(int(args[1]), float(args[2]), int(args[3]))
            elif(args[0] == self.ident.switch("LOG")):
                result = self.math.log(float(args[1]), float(args[2]))
            elif(args[0] == self.ident.switch("I")):
                integralFlag = self.conf.setIntegrationTechnique(int(args[1]))
            elif(args[0] == self.ident.switch("V")):
                verbChangedFlag = self.conf.setVerbose(helpjen.switchYesOrNo(args[1]))
                extraChangedFlag = self.conf.setExtraVerbose(helpjen.switchYesOrNo(args[2]))
            elif(args[0] == self.ident.switch("B")):
                if(helpjen.switchYesOrNo(args[1])):
                    bertFlag = self.math.calibrate()
                else:
                    bertFlag = False
            elif(args[0] == self.ident.switch("N")):
                angleFlag = self.conf.setAngleUnits(int(args[1]))
            elif(args[0] == self.ident.switch("MPI")):
                result = self.math.machinPi()
        # 1A : EXCEPTIONS
        ################
        except Exception as e:
            if self.conf.EXTRA_VERBOSE:
                self.printer.warn(f'Step 1A : Exception Handling For {self.ident.unswitch(args[0])}', "callFunction")
            if(args[0] == self.ident.switch("CF")):
                self.printer.warn(str(e), "mathbert.countFormula")
            elif(args[0] == self.ident.switch("E")):
                self.printer.warn(str(e), "mathbert.exp")
            elif(args[0] == self.ident.switch("F")):
                self.printer.warn(str(e), "mathbert.factorial")
            elif(args[0] == self.ident.switch("LPI")):
                self.printer.warn(str(e), "mathbert.liebPi")
            elif(args[0] == self.ident.switch("NORMCDF")):
                self.printer.warn(str(e), "statbert.normalDistribution")
            elif(args[0] == self.ident.switch("NORMPDF")):
                self.printer.warn(str(e), "statbert.normalDensity")
            elif(args[0]== self.ident.switch("NPI")):
                self.printer.warn(str(e), "mathbert.newtPi")
            elif(args[0] == self.ident.switch("P")):
                self.printer.warn(str(e), "mathbert.power")
            elif(args[0] == self.ident.switch("SQ")):
                self.printer.warn(str(e), "mathbert.newtRoot")
            elif(args[0] == self.ident.switch("BS")):
                self.printer.warn(str(e), "finbert.BSF")
            elif(args[0] == self.ident.switch("LN")):
               self.printer.warn(str(e), "mathbert.naturalLog")
            elif(args[0] == self.ident.switch("ROOT")):
                self.printer.warn(str(e), "mathbert.binRoot")
            elif(args[0] == self.ident.switch("COS")):
                self.printer.warn(str(e), "mathbert.cos")
            elif(args[0] == self.ident.switch("SIN")):
                self.printer.warn(str(e), "mathbert.sin")
            elif(args[0] == self.ident.switch("ASIN")):
                self.printer.warn(str(e), "mathbert.asin")
            elif(args[0] == self.ident.switch("TAN")):
                self.printer.warn(str(e), "mathbert.tan")
            elif(args[0] == self.ident.switch("ACOS")):
                self.printer.warn(str(e), "mathbert.acos")
            elif(args[0] == self.ident.switch("ATAN")):
                self.printer.warn(str(e), "mathbert.atan")
            elif(args[0] == self.ident.switch("SEC")):
                self.printer.warn(str(e), "mathbert.sec")
            elif(args[0] == self.ident.switch("CSC")):
                self.printer.warn(str(e), "mathbert.csc")
            elif(args[0] == self.ident.switch("COT")):
                self.printer.warn(str(e), "mathbert.cot")
            elif(args[0] == self.ident.switch("BINPMF")):
                self.printer.warn(str(e), "mathbert.binomialMass")
            elif(args[0] == self.ident.switch("BINCDF")):
                self.printer.warn(str(e), "mathbert.binomialDistribution")
            elif(args[0] == self.ident.switch("LOG")):
                self.printer.warn(str(e), "mathbert.log")
            elif(args[0] == self.ident.switch("I")):
                self.printer.warn(str(e), "confijen.setIntegrationTechnique")
            elif(args[0] == self.ident.switch("V")):
                self.printer.warn(str(e), "confijen.setVerbose")
            elif(args[0] == self.ident.switch("B")):
                self.printer.warn(str(e), "confijen.calibrate")
            elif(args[0] == self.ident.switch("MPI")):
                self.printer.warn(str(e), "mathbert.machinPi")

        # 2 : FORMAT RESULTS
        ####################
        if(not noOutput):
            self.menu.time(False, now)
        outString = "error"
        capSigma = self.conf.getSymbol("cap_sigma")
        sigma = self.conf.getSymbol("sigma")
        pi = self.conf.getSymbol("pi")
        mu = self.conf.getSymbol("mu")
        sq = self.conf.getSymbol("sq")
        delta = self.conf.getSymbol("delta")
        if(args[0] == self.ident.switch("CF")):
            outString = f'{capSigma} {str(args[1])} = {str(result)}'
        elif(args[0] == self.ident.switch("E")):
             outString = f'e^({str(args[1])}) = {str(result)}' 
        elif(args[0] == self.ident.switch("F")):
            outString = f'{str(args[1])}! = {str(result)}'
        elif(args[0] == self.ident.switch("LPI")):
            outString = f'{pi} = {str(result)}'
        elif(args[0] == self.ident.switch("MPI")):
            outString = f'{pi} = {str(result)}'
        elif(args[0] == self.ident.switch("NORMCDF")):
            Zscore = self.stat.standardize(float(args[1]), float(args[2]), float(args[3]))
            outString = f'Normal(x={str(args[1])}, {mu}={str(args[2])}, {sigma}={str(args[3])}) = P(Z<{str(Zscore)}) = {str(result)}'
        elif(args[0] == self.ident.switch("NORMPDF")):
            Zscore = self.stat.standardize(float(args[1]), float(args[2]), float(args[3]))
            outString = f'Normal\'(x={str(args[1])}, {mu}={str(args[2])}, {sigma}={str(args[3])}) = P(Z={str(Zscore)}) = {str(result)}'
        elif(args[0 ]== self.ident.switch("NPI")):
            outString = f'{pi} = {str(result)}'
        elif(args[0] == self.ident.switch("P")):
            outString = f'{str(args[1])}^{str(args[2])} = {str(result)}'
        elif(args[0] == self.ident.switch("SQ")):
            outString = f'{sq}{str(args[1])} = {str(result)}'
        elif(args[0] == self.ident.switch("BS")):
            option = "Call" if args[7] else "Put"
            argument = f'S={str(args[1])}, K={str(args[2])}, r={str(args[3])}, {delta}={str(args[4])}'
            argument = argument + f', {sigma}={str(args[5])}, t={str(args[6])}'
            outString = f'{option}({argument}) = {str(result)}'
        elif(args[0] == self.ident.switch("LN")):
            outString = f'ln({str(args[1])}) = {str(result)}'
        elif(args[0] == self.ident.switch("ROOT")):
            outString = f'({str(args[1])})^({str(args[2])}) = {str(result)}'
        elif(args[0] == self.ident.switch("COS")):
            outString = f'cos({str(args[1])}) = {str(result)}'
        elif(args[0] == self.ident.switch("SIN")):
            outString = f'sin({str(args[1])}) = {str(result)}'
        elif(args[0] == self.ident.switch("ASIN")):
            outString = f'arcsin({str(args[1])}) = {str(result)}'
        elif(args[0] == self.ident.switch("TAN")):
            outString = f'tan({str(args[1])}) = {str(result)}'
        elif(args[0] == self.ident.switch("ACOS")):
            outString = f'arccos({str(args[1])}) = {str(result)}'
        elif(args[0] == self.ident.switch("ATAN")):
            outString = f'arctan({str(args[1])}) = {str(result)}'
        elif(args[0] == self.ident.switch("SEC")):
            outString = f'sec({str(args[1])}) = {str(result)}'
        elif(args[0] == self.ident.switch("CSC")):
            outString = f'csc({str(args[1])}) = {str(result)}'
        elif(args[0] == self.ident.switch("COT")):
            outString = f'cot({str(args[1])}) = {str(result)}'
        elif(args[0] == self.ident.switch("BINPMF")):
            outString = f'Binomial\'(n={str(args[1])},p={str(args[2])},x={str(args[3])}) = {str(result)}'
        elif(args[0] == self.ident.switch("BINCDF")):
            outString = f'Binomial(n={str(args[1])},p={str(args[2])},x={str(args[3])}) = {str(result)}'
        elif(args[0] == self.ident.switch("LOG")):
            outString = f'Log(base={str(args[2])}, x={str(args[1])}) = {str(result)}'
        elif(args[0] == self.ident.switch("I")):
            if integralFlag:
                self.printer.warn(f'Integration Technique Changed: {self.conf.getIntegrationTechnique()}',
                                 "confijen.integrationTechnique")
            else:
                self.printer.warn(f'Integration Technique Unchanged: {self.conf.getIntegrationTechnique()}', 
                                "confijen.integrationTechnique")
        elif(args[0] == self.ident.switch("V")):
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
        elif(args[0] == self.ident.switch("B")):
            if bertFlag:
                self.printer.warn("Bertjen Info Changed!", "confijen.calibrate")
            else:
                self.printer.warn("Bertjen Info Unchanged!", "confijen.calibrate")
        elif(args[0] == self.ident.switch("N")):
            if angleFlag:
                self.printer.warn(f'Angle Unit Setting Changed: {self.conf.getAngleUnits()}', "confijen.ANGLE_UNITS")
            else:
                self.printer.warn(f'Angle Unit Setting Unchanged: {self.conf.getAngleUnits()}', "confijen.ANGLE_UNITS")                
        elif(args[0] == self.ident.switch("H")):
            self.menu.printFunctionDetails(self.ident.switch(args[1]))
        
        if(not noOutput):
            self.printer.output(outString)

    def doManual(self, switchIn):
        args = []
        args.append(switchIn)
        self.menu.printFunctionTitle(switchIn)
        # COUNT, FACT
        if switchIn == self.ident.switch("CF") or switchIn == self.ident.switch("F"):
            n = self.menu.getInt("Please Enter A Number")
            args.append(n)
        # EXP, NEWTROOT, LN, COS, SIN, TAN, ACOS, ASIN, ATAN, SEC, CSC, COT
        elif (switchIn == self.ident.switch("E") or switchIn == self.ident.switch("SQ") 
                or switchIn == self.ident.switch("LN") or self.ident.isTrigFunction(switchIn)):
            x = self.menu.getFloat("Please Enter A Number")
            args.append(x)
        # BINROOT, LOG
        elif switchIn == self.ident.switch("ROOT") or switchIn == self.ident.switch("LOG"):
            x1 = self.menu.getFloat("Please Enter A Number")
            x2 = self.menu.getFloat("Please Enter A Number")
            args.append(x1)
            args.append(x2)
        # POWER
        elif switchIn == self.ident.switch("P"):
            b = self.menu.getFloat("Please Enter Base b: ")
            a = self.menu.getFloat("Please Enter Exponent a: ")
            args.append(b)
            args.append(a)
        # NORMCDF, NORMPDF
        elif self.ident.isNormalFunction(switchIn):
            mu = self.menu.getFloat(f'Please Enter {self.conf.getSymbol("mu")}')
            sigma = self.menu.getFloat(f'Please Enter {self.conf.getSymbol("sigma")}')
            x = self.menu.getFloat("Please Enter X")
            args.append(x)
            args.append(mu)
            args.append(sigma)
        # BINPMF, BINCDF
        elif self.ident.isBinomialFunction(switchIn):
            n = self.menu.getInt("Please Enter Number Of Trials")
            p = self.menu.getFloat("Please Enter Probability Of Success")
            x = self.menu.getInt("Please Enter Desired Probability Mass")
            args.append(n)
            args.append(p)
            args.append(x)
        # BLACKSCHOLES
        elif switchIn == 12:
            opt = self.menu.getBinaryDecision("Call", "Put")
            s = self.menu.getFloat("Spot Price, S")
            k = self.menu.getFloat("Strike Price, K")
            r = self.menu.getFloat("Continuous Risk Free Rate, r")
            d = self.menu.getFloat(f'Continuous Dividend Rate, {self.conf.getSymbol("delta")}')
            o = self.menu.getFloat(f'Observed Volatility, {self.conf.getSymbol("sigma")}')
            t = self.menu.getFloat("Time To Expiration, t")
            args.append(s)
            args.append(k)
            args.append(r)
            args.append(d)
            args.append(o)
            args.append(t)
            args.append(opt)
        ## ADMIN COMMANDS
        # PRINT MENU
        elif switchIn == self.ident.switch("M"):
            self.printer.printMenu()
        # HELP
        elif switchIn == self.ident.switch("H"):
            func = self.menu.getFunctionIndex()
            self.menu.printFunctionDetails(func)
        # INTEGRAl SET
        elif switchIn == self.ident.switch("I"):
            self.menu.printIntegrationDetails()
            n = self.menu.getTechnique()
            changedFlag = self.conf.setIntegrationTechnique(n)
            if changedFlag:
                self.printer.warn(f'Integration Technique Changed: {self.conf.getIntegrationTechnique()}',
                                 "confijen.INTEGRATION_CHOICE")
            else:
                self.printer.warn(f'Integration Technique Unchanged: {self.conf.getIntegrationTechnique()}', 
                                "confijen.INTEGRATION_CHOICE")
        # VERBOSE SET
        elif switchIn == self.ident.switch("V"):
            self.menu.printVerboseDetails()
            self.printer.bullet("Verbose?")
            verboseFlag = self.menu.getBinaryDecision("Yes", "No")
            changedFlag = self.conf.setVerbose(verboseFlag)
            if changedFlag:
                self.printer.warn(f'Verbose Setting Changed: {"Yes" if verboseFlag else "No"}', 
                                "confijen.VERBOSE")
            else:
                self.printer.warn(f'Verbose Setting Unchanged: {"Yes" if verboseFlag else "No"}', 
                                "confijen.VERBOSE")
            self.printer.bullet("Extra Verbose?")
            extraVerboseFlag = self.menu.getBinaryDecision("Yes", "No")
            changedFlag = self.conf.setExtraVerbose(extraVerboseFlag)
            if changedFlag:
                self.printer.warn(f'Extra Verbose Setting Changed: {"Yes" if extraVerboseFlag else "No"}', 
                                "confijen.EXTRA_VERBOSE")
            else:
                self.printer.warn(f'Extra Verbose Setting Unchanged: {"Yes" if extraVerboseFlag else "No"}', 
                                "confijen.EXTRA_VERBOSE")
        # BERTJEN CALIBRATE
        elif switchIn == self.ident.switch("B"):
            self.menu.printBertjenDetails()
            self.printer.bullet("Calibrate Bertjen To System?")
            calibrateFlag = self.menu.getBinaryDecision("Yes", "No")
            if calibrateFlag:
                changedFlag = False
                try:
                    changedFlag = self.math.calibrate()
                except Exception as e:
                    self.printer.warn(str(e), "confijen.calibrate")
                if changedFlag:
                    self.printer.warn("Bertjen Info Changed!", "confijen.calibrate")
                    self.menu.printBertjenDetails()
                else:
                    self.printer.warn("Bertjen Info Unchanged!", "confijen.calibrate")
        # SAVE
        elif switchIn == self.ident.switch("S"):
            self.printer.line("Save configuration to gollys/store.json?")
            saveFlag = self.menu.getBinaryDecision("Yes", "No")
            if saveFlag:
                self.conf.saveConfiguration(self.math)
                self.printer.warn("Configuration Saved To File", "config.json")
                self.printer.warn("Constant Store Saved To File", "store.json")
            else:
                self.printer.warn("Configuration Not Saved", "config.json")
                self.printer.warn("Constant Store Not Saved To File", "store.json")
        # ANGLE
        elif switchIn == self.ident.switch("N"):
            self.menu.printAngleDetails()
            n = self.menu.getAngleUnit()
            changedFlag = self.conf.setAngleUnits(n)
            if changedFlag:
                self.printer.warn(f'Angle Setting Changed: {self.conf.getAngleUnits()}',
                                 "confijen.ANGLE_UNITS")
            else:
                self.printer.warn(f'Integration Technique Unchanged: {self.conf.getAngleUnits()}', 
                                "confijen.ANGLE_UNITS")
        # QUIT
        elif switchIn == self.ident.switch("Q"):
            self.alive = False
        # NOT FOUND
        elif (switchIn != self.ident.switch("NPI") and switchIn != self.ident.switch("LPI")
                and switchIn != self.ident.switch("MPI")):
            self.printer.warn("Error. Make Another Selection", "doProgram")
        # IF NOT CONFIGURE FUNCTION, CALL FUNCTION
        if(switchIn != self.ident.switch("Q") and switchIn != self.ident.switch("S") 
            and (not self.ident.isNoOutput(switchIn))):
            self.callFunction(args)

########################################################################
#                              MAIN                                    #
########################################################################
if __name__ == '__main__':
    bertjen = bertjen()
    bertjen.doProgram()

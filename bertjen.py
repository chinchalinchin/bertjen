import sys, os
sys.path.append(os.path.join(sys.path[0], "jens"))
sys.path.append(os.path.join(sys.path[0], "berts"))

from mathbert import mathbert
from finbert import finbert
from statbert import statbert

from menujen import menujen
from confijen import configuration
import helpjen

class bertjen:

    def __init__(self):
        self.conf = configuration()
        self.menu = menujen()
        self.math = mathbert(self.conf, self.menu)
        self.stat = statbert(self.conf, self.menu, self.math)
        self.fin = finbert(self.conf, self.menu, self.math, self.stat)
        self.alive = True

    def doProgram(self):
        self.menu.printMenu()
        while self.alive:
            rawIn = self.menu.getMenuInput()
            switchIn = self.menu.switch(rawIn)
            self.doStep(switchIn)

    def doStep(self, input):
        #########
        # COUNT #
        #########
        if input == 0:
            self.menu.subtitle("First N Sum Formula")
            # INPUT
            n = self.menu.getInt("Please Enter Number of Terms")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.countFormula(n)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.countFormula")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Sum of first {str(n)} natural numbers = {str(result)}')
        ###############
        # EXPONENTIAL #
        ###############
        elif input == 2:
            self.menu.subtitle("Exponential Infinite Sum Approximation")
            # INPUT
            ex = self.menu.getFloat("Please Enter Exponent")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.exp(ex)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.exp")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'e ^{str(ex)} = {str(result)}')
        #############
        # FACTORIAL #
        #############
        elif input == 3:
            self.menu.subtitle("Factorial Function")
            # INPUT
            n = self.menu.getInt("Please Enter A Number")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.factorial(n)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.factorial")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'{str(n)}! = {str(result)}')
        ############################
        # LIEBNIZ PI APPROXIMATION #
        ############################
        elif input == 4:
            self.menu.subtitle("Liebniz Series Pi Approximation")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.liebPi()
            except Exception as e:
                self.menu.warn(str(e), "mathbert.liebPi")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Pi = {str(result)}')
        ##############
        # PRINT MENU #
        ##############
        elif input == 5:
            # OUTPUT
            self.menu.printMenu()
        ##############
        # NORMAL CDF #
        ##############
        elif input == 6:
            self.menu.subtitle("Normal CDF Function")
            # INPUT
            mu = self.menu.getFloat("Please Enter Mean")
            sigma = self.menu.getFloat("Please Enter Sigma")
            x = self.menu.getFloat("Please Enter X")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.stat.normalDistribution(x, mu, sigma)
            except Exception as e:
                self.menu.warn(str(e), "statbert.normalIntegral")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output("Norm CDF = " + str(result))
        ##############
        # NORMAL PDF #
        ##############
        elif input == 7:
            self.menu.subtitle("Normal PDF Function")
            # INPUT
            mu = self.menu.getFloat("Please Enter Mean")
            sigma = self.menu.getFloat("Please Enter Sigma")
            x = self.menu.getFloat("Please Enter X")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.stat.normalDensity(x, mu, sigma)
            except Exception as e:
                self.menu.warn(str(e), "statbert.normalDensity")
            self.menu.time(False, now)
            # OUPUT
            self.menu.output(f'Norm PDF = {str(result)}')
        ###########################
        # NEWTON PI APPROXIMATION #
        ###########################
        elif input == 8:
            self.menu.subtitle("Newton Series Pi Approximation")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.newtPi()
            except Exception as e:
                self.menu.warn(str(e), "mathbert.newtPi")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Pi = {str(result)}')
        #########
        # POWER #
        #########
        elif input == 9:
            self.menu.subtitle("Base Exponentiator Function")
            # INPUT
            b = self.menu.getFloat("Please Enter Base b: ")
            a = self.menu.getFloat("Please Enter Exponent a: ")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.power(b,a)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.power")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'{str(b)}^{str(a)} = {str(result)}')
        ####################################
        # NEWTON SQUARE ROOT APPROXIMATION #
        ####################################
        elif input == 11:
            self.menu.subtitle("Newton's Method Square Root Approximation")
            # INPUT
            n = self.menu.getFloat("Please Enter Number")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.newtRoot(n)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.newtRoot")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Newton\'s Approximation of Sqrt({str(n)}) = {str(result)}')
        #########################
        # BLACK SCHOLES FORMULA #
        #########################
        elif input == 12:
            self.menu.subtitle("Black-Scholes Formula Function")
            # INPUT
            opt = self.menu.getBinaryDecision("Call", "Put")
            s = self.menu.getFloat("Spot Price")
            k = self.menu.getFloat("Strike Price")
            r = self.menu.getFloat("Continuous Risk Free Rate")
            d = self.menu.getFloat("Continuous Dividend Rate")
            o = self.menu.getFloat("Observed Volatility")
            t = self.menu.getFloat("Time To Expiration")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True,None)
            try:
                result = self.fin.BSF(s,k,r,d,o,t,opt)
            except Exception as e:
                self.menu.warn(str(e), "finbert.BSF")
            self.menu.time(False, now)
            # OUTPUT
            if(opt):
                option = "Call"
            else:
                option = "Put"
            self.menu.output(f'Black-Scholes {option} Value =  {str(result)}')
        ##############################
        # NATURAL LOG APPROXIMATION  #
        ##############################
        elif input == 13:
            self.menu.subtitle("Halley's Method Natural Log Approximation")
            # INPUT
            n = self.menu.getFloat("Please Enter Number")
            # COMPUTATION
            reuslt = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.naturalLog(n)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.naturalLog")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'LN({str(n)}) =  {str(result)}')
        #################################
        # Nth ROOT SERIES APPROXIMATION #
        #################################
        elif input == 15:
            self.menu.subtitle("Binomial Series Root Approximation")
            self.menu.warn("Interval of Convergence [0,2]", "mathbert.binRoot")
            # INPUT
            n = self.menu.getFloat("Please Enter Number")
            r = self.menu.getFloat("Please Enter Root")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.binRoot(n,r)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.binRoot")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Binomial Approximation of {str(n)}^{str(r)} = {str(result)}')
        ###############################
        # COSINE SERIES APPROXIMATION #
        ###############################
        elif input == 16:
            self.menu.subtitle("Cosine Series Approximation")
            self.menu.warn("Angle Measured In Radians", "mathbert.cos")
            # INPUT
            n = self.menu.getFloat("Please Enter Number (In Radians)")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.cos(n)
            except Exception as e:
                self.menu.warn(str(e),"mathbert.cos")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Series Approximation of cos({str(n)}) =  {str(result)}')
        #############################
        # SINE SERIES APPROXIMATION #
        #############################
        elif input == 17:
            self.menu.subtitle("Sine Series Approximation")
            self.menu.warn("Angle Measured In Radians", "mathbert.sin")
            # INPUT
            n = self.menu.getFloat("Please Enter Number (In Radians)")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.sin(n)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.sin")
            self.menu.time(False,now)
            # OUTPUT
            self.menu.output(f'Series Approximation of sin({str(n)}) =  {str(result)}')
        #################################
        # ARC SINE SERIES APPROXIMATION #
        #################################
        elif input == 18:
            self.menu.subtitle("Arc Sine Series Approximation")
            self.menu.warn("Arc Sine Domain: [-1,1]", "mathbert.arcsin")
            # INPUT
            n = self.menu.getFloat("Please Enter Number")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.arcsin(n)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.arcsin")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Series Approximation of arcsin({str(n)}) =  {str(result)}')
        ################################
        # TANGENT SERIES APPROXIMATION #
        ################################
        elif input == 19:
            self.menu.subtitle("Tangent Series Approximation")
            self.menu.warn("Angle Measured In Radians", "mathbert.tan")
            # INPUT
            n = self.menu.getFloat("Please Enter Number (In Radians)")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.tan(n)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.tan")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Series Approximation of tan({str(n)}) =  {str(result)}')
        ##################################
        # ARCCOSINE SERIES APPROXIMATION #
        ##################################
        elif input == 20:
            self.menu.subtitle("Arc Cosine Series Approximation")
            self.menu.warn("Arc Cosine Domain: [-1, 1]", "mathbert.arccos")
            # INPUT
            n = self.menu.getFloat("Please Enter Number")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.arccos(n)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.arccos")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Series Approximation of arccos({str(n)}) =  {str(result)}')
        ###################################
        # ARCTANGENT SERIES APPROXIMATION #
        ###################################
        elif input == 21:
            self.menu.subtitle("Arctangent Series Approximation")
            # INPUT
            n = self.menu.getFloat("Please Enter Number")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.arctan(n)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.arctan")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Series Approximation of arctan({str(n)}) = {str(result)}') 
        ######################################
        # BINOMIAL PROBABILITY MASS FUNCTION #
        ######################################
        elif input == 24:
            self.menu.subtitle("Binomial Probability Mass Function")
            self.menu.bullet("P(X=x)")
            # INPUT
            n = self.menu.getInt("Please Enter Number Of Trials")
            p = self.menu.getFloat("Please Enter Probability Of Success")
            x = self.menu.getInt("Please Enter Desired Probability Mass")
            # COMPUTATION
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.stat.binomialMass(n, p, x)
            except Exception as e:
                self.menu.warn(str(e), "statbert.binomialMass")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Binomial Probability Mass({str(x)}) = {str(result)}')
        #############################################
        # BINOMIAL CUMULATIVE DISTRIBUTION FUNCTION #
        #############################################
        elif input == 25:
            self.menu.subtitle("Binomial Cumulative Distribution Function")
            self.menu.bullet("P(X<=x)")
            # INPUT
            n = self.menu.getInt("Please Enter Number Of Trials")
            p = self.menu.getFloat("Please Enter Probability Of Success")
            x = self.menu.getInt("Please Enter Desired Probability Mass")
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.stat.binomialDistribution(n, p, x)
            except Exception as e:
                self.menu.warn(str(e), "statbert.binomialDistribution")
            self.menu.time(False, now)
            # OUTPUT
            self.menu.output(f'Binomial Cumulative Distribution({str(x)}) = {str(result)}')
        ######################
        # LOGARITHM FUNCTION #
        ######################
        elif input == 27:
            self.menu.subtitle("Logarithm Function")
            # INPUT
            a = self.menu.getFloat("Please Enter Logarithm Base")
            x = self.menu.getFloat("Please Enter Number")
            result = "error"
            now = self.menu.time(True, None)
            try:
                result = self.math.log(x, a)
            except Exception as e:
                self.menu.warn(str(e), "mathbert.log")
            self.menu.time(False, now)
            self.menu.output(f'Base {a} Logarithm of {x} = {result}')
        ########################
        # INTEGRATION SETTINGS #
        ########################
        elif input == 22:
            self.menu.subtitle("Configure Integration Settings")
            self.menu.bullet("Available Techniques")
            self.menu.bullet("Option : Technique")
            for key, value in self.conf.TECHNIQUES.items():
                self.menu.command(f'Option {key}', f'{value}')
            self.menu.divider()
            self.menu.command("Current Integration Technique", str(self.conf.getIntegrationTechnique()))
            self.menu.divider()
            n = self.menu.getTechnique(self.conf)
            changedFlag = self.conf.setIntegrationTechnique(n)
            if changedFlag:
                self.menu.warn(f'Integration Technique Changed: {self.conf.getIntegrationTechnique()}',
                                 "confijen.integrationTechnique")
            else:
                self.menu.warn(f'Integration Technique Unchanged: {self.conf.getIntegrationTechnique()}', 
                                "confijen.integrationTechnique")
        ####################
        # VERBOSE SETTINGS #
        ####################
        elif input == 23:
            self.menu.subtitle("Configure Verbose Settings")
            self.menu.bullet("Simple Verbose Setting")
            self.menu.command("Current Simple Verbose Setting", 
                                "Yes" if self.conf.getVerbose() else "No")
            self.menu.bullet("Verbose?")
            verboseFlag = self.menu.getBinaryDecision("Yes", "No")
            changedFlag = self.conf.setVerbose(verboseFlag)
            if changedFlag:
                self.menu.warn(f'Verbose Setting Changed: {"Yes" if verboseFlag else "No"}', 
                                "confijen.verbose")
            else:
                self.menu.warn(f'Verbose Setting Unchanged: {"Yes" if verboseFlag else "No"}', 
                                "confijen.verbose")
            self.menu.bullet("Extra Verbose Setting")
            self.menu.command("Current Extra Verbose Setting", 
                                "Yes" if self.conf.getExtraVerbose() else "No")
            self.menu.bullet("Extra Verbose?")
            extraVerboseFlag = self.menu.getBinaryDecision("Yes", "No")
            changedFlag = self.conf.setExtraVerbose(extraVerboseFlag)
            if changedFlag:
                self.menu.warn(f'Extra Verbose Setting Changed: {"Yes" if extraVerboseFlag else "No"}', 
                                "confijen.extraVerbose")
            else:
                self.menu.warn(f'Extra Verbose Setting Unchanged: {"Yes" if extraVerboseFlag else "No"}', 
                                "confijen.extraVerbose")
        #####################
        # CALIBRATE BERTJEN #
        #####################
        elif input == 26:
            self.menu.subtitle("Calibrate System Settings")
            self.menu.bullet("Bertjen Info")
            self.menu.command("Trig Series Max Loop Iterations", self.conf.TRIG_ACC)
            self.menu.command("Ln Series Max Loop Iterations", self.conf.LN_ACC)
            self.menu.bullet("System Info")
            self.menu.command("Float Max", sys.float_info.max)
            self.menu.command("Float Min", sys.float_info.min)
            self.menu.bullet("Calibrate Bertjen To System?")
            calibrateFlag = self.menu.getBinaryDecision("Yes", "No")
            if calibrateFlag:
                changedFlag = False
                try:
                    changedFlag = self.conf.calibrate(self.math, self.menu)
                except Exception as e:
                    self.menu.warn(str(e), "confijen.calibrate")
                if changedFlag:
                    self.menu.warn("Bertjen Info Changed!", "confijen.calibrate")
                    self.menu.bullet("New Bertjen Info")
                    self.menu.command("Trig Series Max Loop Iterations", self.conf.TRIG_ACC)
                    self.menu.command("Ln Series Max Loop Ierations", self.conf.LN_ACC)
                else:
                    self.menu.warn("Bertjen Info Unchanged!", "confijen.calibrate")
        #
        #
        #
        elif input == 28:
            self.menu.subtitle("Save Bertjen Configuration")
            saveFlag = self.menu.getBinaryDecision("Save", "Forget")
            if saveFlag:
                self.conf.saveConfiguration()
                self.menu.warn("Configuration Saved To File", "config.json")
            else:
                self.menu.warn("Configuration Not Saved", "config.json")
        ########
        # QUIT #
        ########
        elif input == 99:
            self.alive = False
        #############
        # NOT FOUND #
        #############
        else:
            self.menu.warn("Error. Make Another Selection", "doProgram")
        self.menu.divider()
            
########################################################################
########################################################################
#                              MAIN                                    #
########################################################################
########################################################################
if __name__ == '__main__':
    bertjen = bertjen()
    bertjen.doProgram()

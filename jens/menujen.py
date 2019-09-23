import datetime
import helpjen
import sys

class menujen:

    def __init__(self, myConf, myPrinter, myIdent):
        self.conf = myConf
        self.printer = myPrinter
        self.ident = myIdent

    def printFunctionTitle(self, which):
        if(which == self.ident.switch("CF")):
            self.printer.subtitle("Sum Of First N Integers Function")
        elif(which == self.ident.switch("E")):
            self.printer.subtitle("Taylor Series Exponential Approximation")
        elif(which == self.ident.switch("F")):
            self.printer.subtitle("Factorial Function")
        elif(which == self.ident.switch("LPI")):
            self.printer.subtitle("Liebniz's Infinite Series Pi Approximation")
        elif(which == self.ident.switch("NORMCDF")):
            self.printer.subtitle("Normal Cumulative Probability Distribution Function")
        elif(which == self.ident.switch("NORMPDF")):
            self.printer.subtitle("Normal Probability Density Function")
        elif(which == self.ident.switch("NPI")):
            self.printer.subtitle("Newton's Infinite Series Pi Approximation")
        elif(which == self.ident.switch("P")):
            self.printer.subtitle("Power Function")
        elif(which == self.ident.switch("SQ")):
            self.printer.subtitle("Newton's Method Square Root Approximation")
        elif(which == self.ident.switch("BS")):
            self.printer.subtitle("Black Scholes Option Value Functoin")
        elif(which == self.ident.switch("LN")):
            self.printer.subtitle("Halley's Method Natural Log Approximation")
        elif(which == self.ident.switch("ROOT")):
            self.printer.subtitle("Binomial Series Root Approximation")
        elif(which == self.ident.switch("COS")):
            self.printer.subtitle("Taylor Series Cosine Approximation")
        elif(which == self.ident.switch("SIN")):
            self.printer.subtitle("Taylor Series Sine Approximation")
        elif(which == self.ident.switch("ASIN")):
            self.printer.subtitle("Taylor Series Arc Sine Approximation")
        elif(which == self.ident.switch("TAN")):
            self.printer.subtitle("Taylor Series Tangent Approximation")
        elif(which == self.ident.switch("ACOS")):
            self.printer.subtitle("Taylor Series Arc Cosine Approximation")
        elif(which == self.ident.switch("ATAN")):
            self.printer.subtitle("Taylor Series Arc Tangent Approximation")
        elif(which == self.ident.switch("I")):
            self.printer.subtitle("Integral Approximation Technique")
        elif(which == self.ident.switch("V")):
            self.printer.subtitle("Verbose Settings")
        elif(which == self.ident.switch("BINPMF")):
            self.printer.subtitle("Binomial Probability Mass Function")
        elif(which == self.ident.switch("BINCDF")):
            self.printer.subtitle("Binomial Cumulative Probability Distribution Function")
        elif(which == self.ident.switch("B")):
            self.printer.subtitle("Bertjen Settings Calibration")
        elif(which == self.ident.switch("LOG")):
            self.printer.subtitle("Logarithm Function")
        elif(which == self.ident.switch("S")):
            self.printer.subtitle("Save Bertjen Configuration")
        elif(which == self.ident.switch("H")):
            self.printer.subtitle("Help Function")
        elif(which == self.ident.switch("SEC")):
            self.printer.subtitle("Taylor Series Secant Approximation")
        elif(which == self.ident.switch("CSC")):
            self.printer.subtitle("Taylor Series Cosecant Approximation")
        elif(which == self.ident.switch("COT")):
            self.printer.subtitle("Taylor Series Cotangent Approximation")
        elif(which == self.ident.switch("N")):
            self.printer.subtitle("Angle Unit Settings")

    def printFunctionDetails(self, which):
        self.printFunctionTitle(which)
        self.printer.divider()
        self.printer.subtitle("Description")
        if(which == self.ident.switch("CF")):
            self.printer.line("Sums up the first --n integers")
            self.printer.subtitle("Arguments")
            self.printer.argument("n", "Number of integers to be summed", "int")
        elif(which == self.ident.switch("E")):
            self.printer.line("Raises e to the specific power --x")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "power e is raised to", "float")
            self.printer.warn("Check Bertjen Configuration with 'B' to see loop iteration settings", "confijen")
        elif(which == self.ident.switch("F")):
            self.printer.line("Computes the factorial of the specified integer --n")
            self.printer.subtitle("Arguments")
            self.printer.argument("n", "Number of factorial", "int")
        elif(which == self.ident.switch("LPI")):
            self.printer.line("Approximates pi with Liebniz's infinite series approximation")
            self.printer.subtitle("Arguments")
            self.printer.argument("none", "n/a", "null")
            self.printer.subtitle("Notes")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
        elif(which == self.ident.switch("NORMCDF")):
            self.printer.line(f'Computes a normal probability --x P(X<x) for a given mean')
            self.printer.line(f'--{self.conf.getSymbol("mu")} and standard deviation --{self.conf.getSymbol("sigma")}')
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Desired probability", "float")
            self.printer.argument(f'{self.conf.getSymbol("mu")}', "Mean", "float")
            self.printer.argument(f'{self.conf.getSymbol("sigma")}', "Standard deviation", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
        elif(which == self.ident.switch("NORMPDF")):
            self.printer.line(f'Computes a normal density --x P(X=x) for a given mean')
            self.printer.line(f'--{self.conf.getSymbol("mu")} and standard deviation --{self.conf.getSymbol("sigma")}')
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Desired density", "float")
            self.printer.argument(f'{self.conf.getSymbol("mu")}', "Mean", "float")
            self.printer.argument(f'{self.conf.getSymbol("sigma")}', "Standard deviation", "float")
        elif(which == self.ident.switch("NPI")):
            self.printer.line("Approximates pi with Newton's infinte series approximation")
            self.printer.subtitle("Arguments")
            self.printer.argument("none", "n/a", "null")
            self.printer.subtitle("Notes")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
        elif(which == self.ident.switch("P")):
            self.printer.line("Raises a specified base --b to a specified power --a")
            self.printer.subtitle("Arguments")
            self.printer.argument("b", "Base", "float")
            self.printer.argument("a", "Exponent", "int")
        elif(which == self.ident.switch("SQ")):
            self.printer.line("Approximates the square root of input --x using Newton's Method")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Root to be taken", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
        elif(which == self.ident.switch("BS")):
            self.printer.line("Uses the Black-Scholes formula to calculate the theoretical")
            self.printer.line("value of an option given observed market data")
            self.printer.subtitle("Arguments")
            self.printer.argument("S", "Spot price", "float")
            self.printer.argument("K", "Strike price", "float")
            self.printer.argument("r", "Interest rate, annual continuous", "float")
            self.printer.argument(f'{self.conf.getSymbol("delta")}', "Dividend rate, annual continuous", "float")
            self.printer.argument(f'{self.conf.getSymbol("sigma")}', "Implied volatility, annual", "float")
            self.printer.argument("t", "Time to expiration, years", "float")
            self.printer.argument("opt", "Type of option", "string: 'Call'/'Put'")
        elif(which == self.ident.switch("LN")):
            self.printer.line("Approximates natural log of input --x using Halley's method")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Natural log to be taken", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
        elif(which == self.ident.switch("ROOT")):
            self.printer.line("Approximates the nth root --r of input --n using a binomial series")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Number whose root is to be found", "float")
            self.printer.argument("r" , "Root to be taken", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Interval of Convergence [0, 2]", "mathbert.binRoot")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
        elif(which == self.ident.switch("COS")):
            self.printer.line("Approximates the cosine of input --x using a Taylor series")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Angle whose cosine is to be found", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
            self.printer.warn("Defaults to radians", "mathbert.cos")
        elif(which == self.ident.switch("SIN")):
            self.printer.line("Approximates the sine of input --x using a Taylor series")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Angle whose sine is to be found" , "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
            self.printer.warn("Defaults to radians", "mathbert.sin")
        elif(which == self.ident.switch("ASIN")):
            self.printer.line("Approximates the arc sine of input --x using a Taylor series")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Scalar whose arc sine is to be found", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
            self.printer.warn("Defaults to radians", "mathbert.asin")
        elif(which == self.ident.switch("TAN")):
            self.printer.line("Approximates the tangent of input --x using a Taylor series")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Angle whose tangent is to be found", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
            self.printer.warn("Defaults to radians", "mathbert.tan")
        elif(which == self.ident.switch("ACOS")):
            self.printer.line("Approximates the arc cosine of input --x using a Taylor series")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Scalar whose arc cosine is to be found", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
            self.printer.warn("Defaults to radians", "mathbert.acos")
        elif(which == self.ident.switch("ATAN")):
            self.printer.line("Approximates the arc tangent of input --x using a Taylor series")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Scalar whose arc tangent is to be found", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Check config with 'B' to see iteration settings", "confijen")
            self.printer.warn("Defaults to radians", "mathbert.tan")
        elif(which == self.ident.switch("BINPMF")):
            self.printer.line("Computes the binomial probability mass --x P(X=x) for a")
            self.printer.line("given binomial distribution with probability of success")
            self.printer.line("--p and number of trials --n")
            self.printer.subtitle("Arguments")
            self.printer.argument("n", "Number of trials", "int")
            self.printer.argument("p", "Probability of success", "float")
            self.printer.argument("x", "Desired probability mass", "int")
        elif(which == self.ident.switch("BINCDF")):
            self.printer.line("Computes the binomial cumulative probability--x P(X<=x)")
            self.printer.line("for a given binomial distribution with probability of")
            self.printer.line("success --p and number of trials --n")
            self.printer.subtitle("Arguments")
            self.printer.argument("n", "Number of trials", "int")
            self.printer.argument("p", "Probability of success", "float")
            self.printer.argument("x", "Desired cumulative probability", "int")
        elif(which == self.ident.switch("LOG")):
            self.printer.line("Computes the logarithm of --x for a given base --b")
            self.printer.line("using the change of base formula and the Halley's method")
            self.printer.line("approximation for natural logs")
        elif(which == self.ident.switch("I")):
            self.printer.line("Configures the integration technique used to approximate integrals")
            self.printer.subtitle("Arguments")
            self.printer.argument("t", "Technique to be used", "int")
            self.printer.subtitle("Notes")
            self.printer.warn("Check Integration with 'I' to see integration techniques", "confijen")
        elif(which == self.ident.switch("V")):
            self.printer.line("Configures the verbose settings for Bertjen")
            self.printer.subtitle("Arguments")
            self.printer.argument("v", "Verbose setting", "YES/NO")
            self.printer.argument("x", "Extra verbose setting", "YES/NO")
            self.printer.subtitle("Notes")
            self.printer.warn("Check Verbose Settings with 'V'", "confijen")
        elif(which == self.ident.switch("B")):
            self.printer.line("Calibrates Bertjen to System settings")
            self.printer.line("c", "Configure Bertjen", "YES/NO")
        elif(which == self.ident.switch("S")):
            self.printer.line("Saves the current Bertjen configuration")
        elif(which == self.ident.switch("H")):
            self.printer.line("Provides an explanation for a given function --f")
            self.printer.subtitle("Arguments")
            self.printer.argument("f", "Function whose description is required", "string")
        elif(which == self.ident.switch("SEC")):
            self.printer.line("Approximates the secant of an angle --x using a Taylor")
            self.printer.line("series.")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Angle whose secant is required", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Secant calls cosine approximation", "mathbert.sec")
            self.printer.warn("Defaults to radians", "mathbert.sec")
        elif(which == self.ident.switch("CSC")):
            self.printer.line("Approximates the cosecant of an angle --x using a Taylor")
            self.printer.line("series.")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Angle whose cosecant is required", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Cosecant calls sine approximation", "mathbert.csc")
            self.printer.warn("Defaults to radians", "mathbert.csc")
        elif(which == self.ident.switch("COT")):
            self.printer.line("Approximates the cotangent of an angle --x using a Taylor")
            self.printer.line("series.")
            self.printer.subtitle("Arguments")
            self.printer.argument("x", "Angle whose cotangent is required", "float")
            self.printer.subtitle("Notes")
            self.printer.warn("Cotangent calls tangent approximation", "mathbert.cot")
            self.printer.warn("Defaults to radians", "mathbert.cot")
        elif(which == self.ident.switch("N")):
            self.printer.line("Configures Bertjen Angle Unit Measures")
            self.printer.subtitle("Arguments")
            self.printer.argument(f'{self.conf.getSymbol("theta")}', "Angle unit measure", "int" )
            self.printer.subtitle("Notes")
            self.printer.warn("Check Angle Settings with 'Ang' to see units", "confijen")
        self.printer.divider()

    def printBertjenDetails(self):
        self.printer.bullet("Bertjen Info")
        self.printer.command("Trig Series Max Loop Iterations", self.conf.TRIG_ACC)
        self.printer.command("Ln Series Max Loop Iterations", self.conf.LN_ACC)
        self.printer.bullet("System Info")
        self.printer.command("Float Max", sys.float_info.max)
        self.printer.command("Float Min", sys.float_info.min)

    def printVerboseDetails(self):
        self.printer.bullet("Verbose Settings")
        self.printer.command("Current Simple Verbose Setting", 
                                "Yes" if self.conf.getVerbose() else "No")
        self.printer.command("Current Extra Verbose Setting", 
                                "Yes" if self.conf.getExtraVerbose() else "No")

    def printIntegrationDetails(self):
        self.printer.bullet("Available Techniques")
        self.printer.bullet("Option : Technique")
        for key, value in self.conf.TECHNIQUES.items():
            self.printer.command(f'{key}', f'{value}')
        self.printer.divider()
        self.printer.command("Current Integration Technique", str(self.conf.getIntegrationTechnique()))
        self.printer.divider()

    def printAngleDetails(self):
        self.printer.bullet("Available Units")
        self.printer.bullet("Option : Unit")
        for key, value in self.conf.ANGLE_UNITS.items():
            self.printer.command(f'{key}', f'{value}')
        self.printer.divider()
        self.printer.command("Current Angle Unit", str(self.conf.getAngleUnits()))
        self.printer.divider()

    def printStoreDetails(self, stores, actuals):
        self.printer.subtitle("Pi Store")
        act_pi = actuals['actual_pi']
        n_pi = stores['newtpi_store']
        l_pi = stores['liebpi_store']
        self.printer.subtitle("Actual Value (As Calculated By Microsoft Calculator)")
        self.printer.command("actual_pi", f'{act_pi}')
        self.printer.subtitle("Approximations")
        self.printer.command("newtpi_store", f'{str(n_pi)}')
        self.printer.command("liebpi_store", f'{str(l_pi)}')
        self.printer.subtitle("Errors")
        if(n_pi>act_pi):
            absErr = n_pi - act_pi
        else:
            absErr = act_pi - n_pi
        self.printer.command("newtpi_store absolute error", f'{str(absErr)}')
        self.printer.command("newtpi_store percentage error", f'{str(absErr*100/act_pi)}%')
        if(l_pi>act_pi):
            absErr = l_pi - act_pi
        else:
            absErr = act_pi - l_pi
        self.printer.command("liebpi_store absolute error", f'{str(absErr)}')
        self.printer.command("liebpi_store percentage error", f'{str(absErr*100/act_pi)}%')

        self.printer.subtitle(f'{self.conf.getSymbol("sq")}2 Store')
        act_sq_2 = actuals['actual_root_2']
        n_sq_2 = stores['newtroot_2_store']
        bin_sq_2 = stores['binroot_2_store']
        self.printer.subtitle("Actual Value (As Calculated By Microsoft Calculator)")
        self.printer.command("actual_root_2", f'{str(act_sq_2)}')
        self.printer.subtitle("Approximations")
        self.printer.command("newtroot_2_store", f'{str(n_sq_2)}')
        self.printer.command("binroot_2_store", f'{str(bin_sq_2)}')
        self.printer.subtitle("Errors")
        if(n_sq_2>act_sq_2):
            absErr = n_sq_2 - act_sq_2
        else:
            absErr = act_sq_2 - n_sq_2
        self.printer.command("newtroot_2_store absolute error", f'{str(absErr)}')
        self.printer.command("newtroot_2_store percentage error", f'{str(absErr*100/act_pi)}%')
        if(bin_sq_2>act_sq_2):
            absErr = bin_sq_2 - act_sq_2
        else:
            absErr = act_sq_2 - bin_sq_2
        self.printer.command("liebpi_store absolute error", f'{str(absErr)}')
        self.printer.command("liebpi_store percentage error", f'{str(absErr*100/act_pi)}%')

        self.printer.subtitle(f'{self.conf.getSymbol("sq")}3 Store')
        act_sq_3 = actuals['actual_root_3']
        n_sq_3 = stores['newtroot_3_store']
        self.printer.subtitle("Actual Value (As Calcualted By Microsoft Calculator)")
        self.printer.command("actual_root_3", f'{str(act_sq_3)}') 
        self.printer.subtitle("Approximations")
        self.printer.command("newtroot_3_store", f'{str(n_sq_3)}')
        self.printer.subtitle("Errors")
        if(n_sq_3>act_sq_3):
            absErr = n_sq_3 - act_sq_3
        else:
            absErr = act_sq_3 - n_sq_3
        self.printer.command("newtroot_3_store absolute error", f'{str(absErr)}')
        self.printer.command("newtroot_3_store percentage error", f'{str(absErr*100/act_pi)}%')

    # Formatted Time Output
    def time(self, flag, start):
        if flag:
            self.printer.command("TIME START", 
                        str(datetime.datetime.now().strftime("%H: %M: %S.%f")[:-6]))
            return datetime.datetime.now()
        else:
            end = datetime.datetime.now()
            self.printer.command("TIME END", 
                        str(end.strftime("%H: %M: %S.%f")[:-6]))
            self.printer.command("TIME DIFF", 
                        str(end - start) + " sec")
    
    # Retrieve Valid Menu Input From User
    def getMenuInput(self):
        menput = []
        menput.append("nothing")
        while(self.ident.switch(menput[0]) == "nothing"):
            # GET INPUT
            menput = input("<< ").upper().split()
            if(len(menput) == 0):
                # NO INPUT TO VERIFY
                return menput
            else:
                ####################
                # INPUT VERIFICATION
                ##############################################
                # STEP 1: VERIFY FIRST INPUT CONTAINS FUNCTION
                firstIn = self.ident.switch(menput[0])
                if(firstIn == "nothing"):
                    self.printer.warn("Selection not found!", "menujen.getMenuInput")
                ######################
                # STEP 2: VERIFY INPUT
                else:
                    args = len(menput)
                    # DO FUNCTION MANUALLY THROUGH COMMAND LINE INTERFACE
                    if(args == 1):
                        return menput
                    else:
                        ###########################################
                        # PRE- STEP 2: GROUP INT BY NUMBER AND TYPE
                        singleArg = self.ident.isSingleArg(firstIn)
                        doubleArg = self.ident.isDoubleArg(firstIn)
                        tripleArg = self.ident.isTripleArg(firstIn)
                        specialArg = self.ident.isSpecialArg(firstIn)
                        floatArg = self.ident.isFloatArg(firstIn)
                        intArg = self.ident.isIntArg(firstIn)
                        boolArg = self.ident.isBoolArg(firstIn)
                        compoundArg = self.ident.isCompoundArg(firstIn)
                        stringArg = self.ident.isStringArg(firstIn)
                        
                        if(singleArg):
                            ############################################################
                            # STEP 2A: VERIFY NUMBER OF ARGUMENTS DOESN'T EXCEED MAXIMUM
                            #   STEP 2A-1: THROW AWAY EXTRA ARGUMENTS FOR 1 ARG FUNCTIONS
                            if(args > 2):
                                menput = [None]*2
                                menput[0] = firstIn
                                self.printer.warn("Argument Mismatch", "menujen.getMenuInput")
                                self.printer.bullet("Provide 1 Argument Only")
                                # STEP 2A-1-1a: GET FLOAT INPUT FOR FLOAT VALUED FUNCTIONS
                                if(floatArg):
                                    menput[1] = self.getFloat("Please Enter A Single Number")
                                    return menput
                                # STEP 2A-1-1b: GET INT INPUT FOR INT VALUED FUNCTIONS
                                elif(intArg):
                                    menput[1] = self.getInt("Please Enter A Single Number")
                                    return menput
                                # STEP 2A-1-1c: GET BOOL INPUT FOR BOOL VALUED FUNCTIONS
                                elif(boolArg):
                                    # BERTJEN
                                    if(firstIn == 26):
                                        self.printer.line("Calibrate Bertjen?")
                                        menput[1] = self.getBinaryDecision("Yes", "No")
                                        return menput
                                # STEP 2A-1-1d: GET STRING INPUT FOR STRING VALUED FUNCTIONS
                                elif(stringArg):
                                    if(firstIn == 29):
                                        menput[1] = self.ident.unswitch(self.getFunctionIndex())
                                        return menput
                            ####################################            
                            # STEP 2B: VERIFY INPUT MATCHES TYPE
                            #   STEP 2B-1: CHECK INPUT TYPE FOR 1 ARG FUNCTIONS
                            else:
                                # STEP 2B-1-2a: VERIFY FLOAT INPUT
                                if(floatArg):
                                    if(not helpjen.isFloat(menput[1])):
                                        self.printer.warn("Argument Not Understood", "menujen.getMenuInput")
                                        menput[1] = self.getFloat("Please Enter A Single Number")
                                        return menput
                                    else:
                                        return menput
                                # STEP 2B-1-2b: VERIFY INT INPUT
                                elif(intArg):
                                    if(not helpjen.isInt(menput[1])):
                                        self.printer.warn("Argument Not Understood", "menujen.getMenuInput")
                                        menput[1] = self.getInt("Please Enter A Single Number")
                                        return menput
                                    else:
                                        return menput
                                # STEP 2B-1-2c: VERIFY BOOL INPUT
                                elif(boolArg):
                                    if(firstIn == 26):
                                        if(menput[1].upper() != "YES" and menput[1].upper() != "NO"):
                                            self.printer.warn("Argument Not Understood", "menujen.getMenuInput")
                                            self.printer.line("Calibrate Bertjen?")
                                            menput[1] = self.getBinaryDecision("Yes", "No")
                                            return menput
                                        else:
                                            return menput
                                    else:
                                        return menput
                                # STEP 2B-1-2d: VERIFY STRING INPUT
                                elif(stringArg):
                                    if(firstIn == 29):
                                        if(self.ident.switch(menput[1]) == "nothing"):
                                            self.printer.warn("Input Not Understood", "menujen.getMenuInput")
                                            menput[1] = self.ident.unswitch(self.getFunctionIndex())
                                            return menput
                                        else:
                                            return menput
                                else:
                                    return menput

                        elif(doubleArg):
                            ############################################################
                            # STEP 2A: VERIFY NUMBER OF ARGUMENTS DOESN'T EXCEED MAXIMUM
                            #   STEP 2A-2 : THROW AWAY EXTRA ARGUMENTS FOR 2 ARG FUNCTIONS
                            if(args > 3 or args < 3):
                                menput = [None]*3
                                menput[0] = firstIn
                                self.printer.warn("Argument Mismatch", "menujen.getMenuInput")
                                self.printer.bullet("Provide 2 Arguments Only")
                                # STEP 2A-2-1a: GET FLOAT INPUT FOR FLOAT VALUED FUNCTIONS
                                if(floatArg):
                                    menput[1] = self.getFloat("Please Enter A Single Number for 1st Argument")
                                    menput[2] = self.getFloat("Please Enter  A Single Number For 2nd Argument")
                                    return menput
                                # STEP 2A-2-1b: GET BOOL INPUT FOR BOOL VALUED FUNCTIONS
                                elif(intArg):
                                    menput[1] = self.getInt("Please Enter A Single Number for 1st Argument")
                                    menput[2] = self.getInt("Please Enter  A Single Number For 2nd Argument")
                                    return menput
                                # STEP 2A-2-1c: GET BOOL INPUT FOR BOOL VALUED FUNCTIONS
                                elif(boolArg):
                                    # VERBOSE
                                    if(firstIn == 23):
                                        self.printer.line("Verbose?")
                                        menput[1] = self.getBinaryDecision("Yes", "No")
                                        self.printer.line("Extra Verbose?")
                                        menput[2] = self.getBinaryDecision("Yes", "No")
                                        return menput
                                # STEP 2A-2-1d: GET STRING INPUT FOR STRING VALUED FUNCTIONS
                                elif(stringArg):
                                    return menput
                                # STEP 2A-2-1e: GET COMPOUND INPUT FOR COMPOUND VALUED FUNCTIONS
                                elif(compoundArg):
                                    # POWER
                                    if(firstIn == 9):
                                        self.printer.line("Base?")
                                        menput[1] = self.getFloat("Please Enter A Single Number For 1st Argument")
                                        self.printer.line("Exponent?")
                                        menput[2] = self.getInt("Please Enter A Single Number For 2nd Argument")
                                        return menput
                                    else:
                                        return menput
                            #################################### 
                            # STEP 2B: VERIFY INPUT MATCHES TYPE
                            #   STEP 2B-2: CHECK INPUT TYPE FOR 2 ARG FUNCTIONS
                            else:
                                # STEP 2B-2-2a: VERIFY FLOAT INPUT
                                if(floatArg):
                                    if(not helpjen.isFloat(menput[1])):
                                        self.printer.warn("1st Argument Not Understood", "menujen.getMenuInput")
                                        menput[1] = self.getFloat("Please Enter A Single Number For 1st Argument")
                                    if(not helpjen.isFloat(menput[2])):
                                        self.printer.warn("2nd Argument Not Understood", "menujen.getMenuInput")
                                        menput[2] = self.getFloat("Please Enter A Single Number For 2nd Argument")
                                    return menput
                                # STEP 2B-2-2b: VERIFY INT INPUT
                                elif(intArg):
                                    if(not helpjen.isInt(menput[1])):
                                        self.printer.warn("1st Argument Not Understood", "menujen.getMenuInput")
                                        menput[1] = self.getInt("Please Enter A Single Number For 1st Argument")
                                    if(not helpjen.isInt(menput[2])):
                                        self.printer.warn("2nd Argument Not Understood", "menujen.getMenuInput")
                                        menput[2] = self.getInt("Please Enter A Single Number For 2nd Argument")
                                    return menput
                                # STEP 2B-2-2c: VERIFY BOOL INPUT
                                elif(boolArg):
                                    if(firstIn == 23):
                                        if(menput[1].upper() != "YES" and menput[1].upper() != "NO"):
                                            self.printer.warn("1st Argument Not Understood", "menujen.getMenuInput")
                                            self.printer.line("Verbose?")
                                            menput[1] = self.getBinaryDecision("Yes", "No")
                                        if(menput[2].upper() != "YES" and menput[2].upper() != "NO"):
                                            self.printer.warn("2nd Argument Not Understood", "menujen.getMenuInput")
                                            self.printer.line("Extra Verbose?")
                                            menput[2] = self.getBinaryDecision("Yes", "No")
                                        return menput
                                    else:
                                        return menput
                                # STEP 2B-2-2d: VERIFY STRING INPUT
                                elif(stringArg):
                                    return menput
                                # STEP 2B-2-2e: VERIFY COMPOUND INPUT
                                elif(compoundArg):
                                    if(firstIn == 9):
                                        if(not helpjen.isFloat(menput[1])):
                                            self.printer.warn("1st Argument Not Understood", "menujen.getMenuInput")
                                            menput[1] = self.getFloat("Please Enter A Single Number For 1st Argument")
                                        if(not helpjen.isInt(menput[2])):
                                            self.printer.warn("2nd Argument Not Understood", "menujen.getMenuInput")
                                            menput[2] = self.getInt("Please Enter A Single Number For 2nd Argument")
                                            return menput
                                        else:
                                            return menput
                    
                        elif(tripleArg):
                            ############################################################
                            # STEP 2A: VERIFY NUMBER OF ARGUMENTS DOESN'T EXCEED MAXIMUM
                            #   STEP 2A-3 : THROW AWAY EXTRA ARGUMENTS FOR 3 ARG FUNCTIONS
                            if(args>4 or args<4):
                                menput = [None]*4
                                menput[0] = firstIn
                                self.printer.warn("Argument Mismatch", "menujen.getMenuInput")
                                self.printer.bullet("Provide 3 Arguments Only")
                                
                                # STEP 2A-3-1a: GET FLOAT INPUT FOR FLOAT VALUED FUNCTIONS
                                if(floatArg):
                                    menput[1] = self.getFloat("Please Enter A Single Number for 1st Argument")
                                    menput[2] = self.getFloat("Please Enter  A Single Number For 2nd Argument")
                                    menput[3] = self.getFloat("Please Enter  A Single Number For 3rd Argument")
                                    return menput
                                    
                                # STEP 2A-3-1b: GET INT INPUT FOR INT VALUED FUNCTIONS
                                elif(intArg):
                                    menput[1] = self.getInt("Please Enter A Single Number for 1st Argument")
                                    menput[2] = self.getInt("Please Enter  A Single Number For 2nd Argument")
                                    menput[3] = self.getInt("Please Enter  A Single Number For 3rd Argument")
                                    return menput
                                    
                                # STEP 2A-3-1c: GET BOOL INPUT FOR BOOL VALUED FUNCTIONS
                                elif(boolArg):
                                    return menput
                                # STEP 2A-2-1d: GET STRING INPUT FOR STRING VALUED FUNCTOINS
                                elif(stringArg):
                                    return menput
                                # STEP 2A-2-1e: GET COMPOUND INPUT FOR COMPOUND VALUED FUNCTIONS
                                elif(compoundArg):
                                    if(firstIn == 25 or firstIn == 24):
                                        menput[1] = self.getInt("Please Enter A Single Number for n")
                                        menput[2] = self.getFloat("Please Enter A Single Number For p")
                                        menput[3] = self.getInt("Please Enter  A Single Number For x")
                                        return menput
                                return menput
                            #################################### 
                            # STEP 2B: VERIFY INPUT MATCHES TYPE
                            #   STEP 2B-3: CHECK INPUT TYPE FOR 3 ARG FUNCTIONS
                            else:
                                # STEP 2B-3-2a: VERIFY FLOAT INPUT
                                if(floatArg):
                                    if(not helpjen.isFloat(menput[1])):
                                        self.printer.warn("1st Argument Not Understood", "menujen.getMenuInput")
                                        menput[1] = self.getFloat("Please Enter A Single Number For 1st Argument")
                                    if(not helpjen.isFloat(menput[2])):
                                        self.printer.warn("2nd Argument Not Understood", "menujen.getMenuInput")
                                        menput[2] = self.getFloat("Please Enter A Single Number For 2nd Argument")
                                    if(not helpjen.isFloat(menput[3])):
                                        self.printer.warn("3rd Argument Not Understood", "menujen.getMenuInput")
                                        menput[3] = self.getFloat("Please Enter A Single Number For 3rd Argument")
                                    return menput
                                # STEP 2B-3-2b: VERIFY INT INPUT
                                elif(intArg):
                                    if(not helpjen.isInt(menput[1])):
                                        self.printer.warn("1st Argument Not Understood", "menujen.getMenuInput")
                                        menput[1] = self.getInt("Please Enter A Single Number For 1st Argument")
                                    if(not helpjen.isInt(menput[2])):
                                        self.printer.warn("2nd Argument Not Understood", "menujen.getMenuInput")
                                        menput[2] = self.getInt("Please Enter A Single Number For 2nd Argument")
                                    if(not helpjen.isInt(menput[3])):
                                        self.printer.warn("3rd Argument Not Understood", "menujen.getMenuInput")
                                        menput[3] = self.getInt("Please Enter A Single Number For 3rd Argument")
                                    return menput
                                # STEP 2B-3-2c: VERIFY BOOL INPUT
                                elif(boolArg):
                                    return menput
                                # STEP 2B-3-2d: VERIFY STRING INPUT
                                elif(stringArg):
                                    return menput
                                # STEP 2B-3-2e: VERIFY COMPOUND INPUT
                                elif(compoundArg):
                                    if(not helpjen.isInt(menput[1])):
                                        self.printer.warn("1st Argument Not Understood", "menujen.getMenuInput")
                                        menput[1] = self.getInt("Please Enter A Single Number For n")
                                    if(not helpjen.isFloat(menput[2])):
                                        self.printer.warn("2nd Argument Not Understood", "menujen.getMenuInput")
                                        menput[2] = self.getFloat("Please Enter A Single Number For p")
                                    if(not helpjen.isInt(menput[3])):
                                        self.printer.warn("3rd Argument Not Understood", "menujen.getMenuInput")
                                        menput[3] = self.getInt("Please Enter A Single Number For x")
                                    return menput
                    
                        elif(specialArg):
                            ############################################################
                            # STEP 2A: VERIFY NUMBER OF ARGUMENTS DOESN'T EXCEED MAXIMUM
                            #   STEP 2A-S : THROW AWAY EXTRA ARGUMENTS FOR 3 ARG FUNCTIONS

                            # BLACKSCHOLES
                            if (firstIn == 12):
                                if(args > 8 or args < 8):
                                    menput = [None]*8
                                    menput[0] = firstIn
                                    self.printer.warn("Too Many Arguments", "menujen.getMenuInput")
                                    self.printer.bullet("Provide 7 Arguments Only")
                                    menput[1] = self.getFloat("Please Enter A Single Number for S")
                                    menput[2] = self.getFloat("Please Enter  A Single Number For K")
                                    menput[3] = self.getFloat("Please Enter  A Single Number For r")
                                    menput[4] = self.getFloat(f'Please Enter A Single Number for {self.conf.getSymbol("delta")}')
                                    menput[5] = self.getFloat(f'Please Enter  A Single Number For o {self.getSymbol("sigma")}')
                                    menput[6] = self.getFloat("Please Enter  A Single Number For t")
                                    self.printer.line("Call Or Put?")
                                    menput[7] = self.getBinaryDecision("Call", "Put")
                                    return menput
                            #################################### 
                            # STEP 2B: VERIFY INPUT MATCHES TYPE
                            #   STEP 2B-3: CHECK INPUT TYPE FOR 3 ARG FUNCTIONS
                                else:
                                    if(not helpjen.isFloat(menput[1])):
                                        self.printer.warn("S Not Understood", "menujen.getMenuInput")
                                        menput[1] = self.getFloat("Please Enter A Single Number For S")
                                    if(not helpjen.isFloat(menput[2])):
                                        self.printer.warn("K Not Understood", "menujen.getMenuInput")
                                        menput[2] = self.getFloat("Please Enter A Single Number For K")
                                    if(not helpjen.isFloat(menput[3])):
                                        self.printer.warn("r Not Understood", "menujen.getMenuInput")
                                        menput[3] = self.getFloat("Please Enter A Single Number For r")
                                    if(not helpjen.isFloat(menput[4])):
                                        self.printer.warn(f'{self.conf.getSymbol("delta")} Not Understood', "menujen.getMenuInput")
                                        menput[4] = self.getFloat(f'Please Enter A Single Number For {self.conf.getSymbol("delta")}')
                                    if(not helpjen.isFloat(menput[5])):
                                        self.printer.warn(f'{self.conf.getSymbol("sigma")} Not Understood', "menujen.getMenuInput")
                                        menput[5] = self.getFloat(f'Please Enter A Single Number For {self.conf.getSymbol("sigma")}')
                                    if(not helpjen.isFloat(menput[6])):
                                        self.printer.warn("t Not Understood", "menujen.getMenuInput")
                                        menput[6] = self.getFloat("Please Enter A Single Number For t")
                                    if(menput[7].upper() != "CALL" and menput[7].upper() != "PUT"):
                                        self.printer.warn("Option Not Understood", "menujen.getMenuInput")
                                        self.printer.line("Call or Put?")
                                        menput[7] = self.getBinaryDecision("Call", "Put")
                                    return menput
            
    # Retrieve Valid Integer Input From User
    def getInt(self, msg):
        self.printer.line(msg)
        numput = "not a number"
        while(not helpjen.isFloat(numput)):
            numput = input("<< ")
            if(helpjen.isFloat(numput)):
                self.printer.command("Input", numput)
                return int(numput)
            else:
                self.warn("Not a number!", "getInt")

    # Retrieve Valid Float Input From User
    def getFloat(self,msg):
        self.printer.line(msg)
        numput = "not a number"
        while(not helpjen.isFloat(numput)):
            numput = input("<< ")
            if(helpjen.isFloat(numput)):
                self.printer.command("Input",numput)
                return float(numput)
            else:
                self.printer.warn("Not a number!", "getFloat")

    def getString(self, msg):
        self.printer.line(msg)
        stput = input("<< ")
        return stput

    def getFunctionIndex(self):
        self.printer.line("Select A Function")
        stput = "nothing"
        while(stput == "nothing"):
            stput =  input("<< ").upper()
            stput = self.ident.switch(stput)
            if(stput != "nothing"):
                self.printer.command("Input", self.ident.unswitch(stput))
                return stput
            else:
                self.printer.warn("Not A Function!", "getFunctionIndex")

    def getBinaryDecision(self, trueOpt, falseOpt):
        self.printer.line(f'{trueOpt} or {falseOpt}?')
        opt = "not an option"
        trueUp = trueOpt.upper()
        falseUp = falseOpt.upper()
        while(opt != trueUp and opt != falseUp):
            opt = input("<< ").upper()
            if(opt != trueUp and opt != falseUp):
                self.printer.warn("Not An Option!", "getBinaryDecision")
        if opt == trueUp:
            self.printer.command("Input", trueOpt)
            return True
        else:
            self.printer.command("Input", falseOpt)
            return False

    def getTechnique(self):
        self.printer.line("Select A Technique")
        numput = "not a technique"
        while(not helpjen.isInt(numput)):
            numput = input("<< ")
            if(helpjen.isInt(numput)):
                if(self.conf.switchTechnique(int(numput)) == "nothing"):
                    self.printer.warn("Not A Technique!", "getTechnique")
                    numput = "not a technique"
                else:
                    self.printer.command("Input", numput)
                    return int(numput)
            else:
                self.printer.warn("Command Not Understood. Try Again.", "getTechnique")
                numput = "not a technique"
        return int(numput)
    
    def getAngleUnit(self):
        self.printer.line("Select A Unit Measure")
        numput = "nothing"
        while(not helpjen.isInt(numput)):
            numput = input("<< ")
            if(helpjen.isInt(numput)):
                if(self.conf.switchUnits(int(numput))=="nothing"):
                    self.printer.warn("Not A Unit Measure", "getAngleUnit")
                    numput = "not a technique"
                else:
                    self.printer.command("Input", numput)
                    return int(numput)
            else:
                self.printer.warn("Command Not Understood. Try Again.", "getAngleUnit")
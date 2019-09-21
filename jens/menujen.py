import datetime
import helpjen

class menujen:

    def __init__(self):
        self.TITLE_LINE = "                The Bertjen Calculator                   "
        self.SPACE_BUFFER = 2
        self.switcher = {
            "CF": 0,"E": 2,"F": 3,"LPI":4, 
            "M": 5, "NORMCDF": 6, "NORMPDF": 7,
            "NPI": 8, "P": 9, "SQ": 11, "BS": 12,
            "LN": 13, "ROOT": 15, "COS": 16, 
            "SIN": 17, "ASIN": 18, "TAN": 19, 
            "ACOS": 20, "ATAN": 21, "I": 22, "V": 23,
            "BINPMF": 24, "BINCDF":25, "B": 26,
            "LOG": 27, "SAV": 28,
            "Q" : 99,
        }
    
    # Manual Switch
    def switch(self, arg):
        return self.switcher.get(arg, "nothing")

    # Print Menu Options
    def printMenu(self):
        self.title()
        
        self.subtitle("Mathbert")
        
        self.subtitle("Mathbert Functions")
        # SINGLE ARGUMENT
        self.command("CF", "Count Function")
        # SINGLE ARGUMENT
        self.command("F", "Factorial Function")
        # DOUBLE ARGUMENT 
        self.command("P","Power Function")
        # DOUBLE ARGUMENT 
        self.command("LOG", "Logarithm Function")
        
        self.subtitle("Mathbert Approximations")
        # SINGLE ARGUMENT
        self.command("E","Taylor Series Exponential Approximation")
        # SINGLE ARGUMENT
        self.command("LN", "Halley's Method Natural Log Approximation")
        # SINGLE ARGUMENT
        self.command("COS", "Taylor Series Cosine Approximation")
        # SINGLE ARGUMENT
        self.command("SIN", "Taylor Series Sine Approximation")
        # SINGLE ARGUMENT
        self.command("TAN", "Taylor Series Tangent Approximation")
        # SINGLE ARGUMENT
        self.command("ACOS", "Taylor Series Arccosine Approximation")
        # SINGLE ARGUMENT
        self.command("ASIN", "Taylor Series Arcsine Approximation")
        # SINGLE ARGUMENT
        self.command("ATAN", "Taylor Series Arctangent Approximation")
        # NO ARGUMENT
        self.command("LPI", "Liebniz Series Pi Approximation")
        # NO ARGUMENT
        self.command("NPI", "Newton Series Pi Approximation")
        # DOUBLE ARGUMENT 
        self.command("ROOT", "Binomial Series Root Approximation")
        # SINGLE ARGUMENT
        self.command("SQ", "Newton's Method Square Root Approximation")
        self.divider()
        
        self.subtitle("Statbert")
        
        self.subtitle("Statbert PDFs/PMFs")
        # TRIPLE ARGUMENT 
        self.command("NORMPDF","Normal Probability Density Function")
        # TRIPLE ARGUMENT 
        self.command("BINPMF", "Binomial Probability Mass Function")
        
        self.subtitle("Statbert CDFs")
        # TRIPLE ARGUMENT 
        self.command("NORMCDF", "Normal Cumulative Distribution Function")
        # TRIPLE ARGUMENT 
        self.command("BINCDF", "Binomial Cumulative Distribution Function")
        self.divider()
        
        self.subtitle("Finbert")
        
        self.subtitle("Finbert Valuations")
        self.command("BS", "Black Scholes Option Function")
        self.divider()
        
        self.subtitle("Admin Commands")
        # SINGLE ARGUMENT
        self.command("I", "Integration Technique Settings")
        # DOUBLE ARGUMENT
        self.command("V", "Verbose Settings")
        # NO ARGUMENT
        self.command("M", "Print Help Menu")
        # SINGLE ARGUMENT
        self.command("B", "Calibrate Bertjen")
        # NO ARGUMENT
        self.command("SAV", "Save Bertjen Configuration")
        # NO ARGUMENT
        self.command("Q", "Quit")
        self.divider()

    def title(self):
        print("*"*(len(self.TITLE_LINE)+2*self.SPACE_BUFFER))
        print(str(self.TITLE_LINE).upper())
        print("*"*(len(self.TITLE_LINE) + 2*self.SPACE_BUFFER))

    def subtitle(self, msg):
        leftover = len(self.TITLE_LINE) - len(msg) + self.SPACE_BUFFER
        if leftover < 0:
            print(str(msg))
        else:
            if leftover%2 == 0:
                space = int(leftover/2)
                print(f'{"*"*space} {str(msg).upper()} {"*"*space}')
            else:
                left = int((leftover-1)/2)
                right = int((leftover+1)/2)
                print(f'{"*"*left} {str(msg).upper()} {"*"*right}')

    def bullet(self, msg):
        leftover = len(self.TITLE_LINE) - len(msg) + self.SPACE_BUFFER
        if leftover%2 ==0:
            multi = int(leftover/2)
            print(f'{"_"*multi} {str(msg)} {"_"*multi}')
        else:
            left = int(leftover/2) + 1
            right = int(leftover/2)
            print(f'{"_"*left} {str(msg)} {"_"*right}')
        
    def line(self, msg):
        print(f'>> {str(msg)}')

    def divider(self):
        print("*"*(len(self.TITLE_LINE) + 2*self.SPACE_BUFFER))
        
    def command(self, cmd, msg):
        print(f'>> {str(cmd)} : {str(msg)}')

    def argument(self, arg, msg):
        return None

    def warn(self, msg, comp):
        print(f'>> {str(comp).upper()} !! {str(msg)} !! ')

    # Print Formatted Output
    def output(self,msg):
        self.command("RESULT", msg)
    
    # Formatted Time Output
    def time(self, flag, start):
        if flag:
            self.command("TIME START", 
                        str(datetime.datetime.now().strftime("%H: %M: %S.%f")[:-4]))
            return datetime.datetime.now()
        else:
            end = datetime.datetime.now()
            self.command("TIME END", 
                        str(end.strftime("%H: %M: %S.%f")[:-4]))
            self.command("TIME DIFF", 
                        str(end - start) + " sec")
            
    # Retrieve Valid Menu Input From User
    def getMenuInput(self,):
        menput = []
        menput[0] = "nothing"
        while(self.switch(menput[0]) == "nothing"):
            self.line("Make A Selection")
            # GET INPUT
            menput = input("<< ").upper().split()
            ####################
            # INPUT VERIFICATION
            ##############################################
            # STEP 1: VERIFY FIRST INPUT CONTAINS FUNCTION
            firstIn = self.switch(menput[0])
            if(firstIn == "nothing"):
                self.warn("Selection not found!", "menujen.getMenuInput")
            ######################
            # STEP 2: VERIFY INPUT
            else:
                args = len(menput)
                if(args == 1):
                    return menput
                else:
                    ###########################################
                    # PRE- STEP 2: GROUP INT BY NUMBER AND TYPE
                    # 1 ARG : 
                    #   COUNT(0), EXP(2), FACT(3), NEWTROOT(11), LN(13)
                    #   COS(16), SIN(17), TAN(19), ACOS(20), ASIN(18), ATAN(21)
                    #    INTEGRALSET(22), BERTJEN(26)
                    singleArg = (firstIn == 0 or firstIn == 2 or firstIn == 3 or firstIn == 11
                            or firstIn == 13 or firstIn == 16 or firstIn == 17 or firstIn == 18
                            or firstIn == 19 or firstIn == 20 or firstIn == 21 or firstIn == 22
                            or firstIn == 26)
                    # 2 ARG: 
                    #   BINROOT(15), POWER(9), VERB(23), LOG(27)
                    doubleArg = firstIn == 15 or firstIn == 9 or firstIn == 23 or firstIn == 27
                    # 3 ARG: 
                    #   NORMCDF(6), NORMPDF(7), BINPMF(24), BINCDF(25)
                    tripleArg = firstIn ==  6 or firstIn == 7 or firstIn == 24 or firstIn == 25
                    # FLOAT: 
                    #   EXP(2), NEWTROOT(11), LN(13), COS(16)
                    #   SIN(17), TAN(19), ACOS(20), ASIN(18), ATAN(21),
                    #   BINROOT(15), LOG(27)
                    floatArg = (firstIn == 2 or firstIn == 11 or firstIn == 13 or firstIn == 16 or firstIn == 17 
                                or firstIn == 18 or firstIn == 19 or firstIn == 20 or firstIn == 21 or firstIn == 15
                                or firstIn == 27)
                    # DUAL ARG : 
                    #   POWER(9)
                    dualArg = firstIn == 9
                    # INT ARG : 
                    #   COUNT(0), FACT(3), INTEGRALSET(22)
                    intArg = firstIn == 0 or firstIn == 3 or firstIn == 22
                    # BOOL ARG: 
                    #   VERB(23), BERTJEN(26)
                    boolArg = firstIn == 26 or firstIn == 23
                    
                    if(singleArg):
                        ############################################################
                        # STEP 2A: VERIFY NUMBER OF ARGUMENTS DOESN'T EXCEED MAXIMUM
                        #   STEP 2A-1: THROW AWAY EXTRA ARGUMENTS FOR 1 ARG FUNCTIONS
                        if(args > 2):
                            menput = [None]*2
                            menput[0] = firstIn
                            self.warn("Too Many Arguments", "menujen.getMenuInput")
                            self.bullet("Provide 1 Argument Only")
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
                                    self.line("Calibrate Bertjen?")
                                    menput[1] = self.getBinaryDecision("Yes", "No")
                                    return menput
                        ####################################            
                        # STEP 2B: VERIFY INPUT MATCHES TYPE
                        #   STEP 2B-1: CHECK INPUT TYPE FOR 1 ARG FUNCTIONS
                        else:
                            # STEP 2B-1-2a: VERIFY FLOAT INPUT
                            if(floatArg):
                                if(not helpjen.isFloat(menput[1])):
                                    menput[1] = self.getFloat("Please Enter A Single Number")
                                    return menput
                                else:
                                    return menput
                            # STEP 2B-1-2b: VERIFY INT INPUT
                            elif(intArg):
                                if(not helpjen.isInt(menput[1])):
                                    menput[1] = self.getInt("Please Enter A Single Number")
                                    return menput
                                else:
                                    return menput
                            # STEP 2B-1-2c: VERIFY BOOL INPUT
                            elif(boolArg):
                                if(firstIn == 26):
                                    if(menput[1].upper() != "YES" or menput[1].upper() != "NO"):
                                        self.line("Calibrate Bertjen?")
                                        menput[1] = self.getBinaryDecision("Yes", "No")
                                        return menput
                                    else:
                                        return menput
                                else:
                                    return menput
                            else:
                                return menput

                    elif(doubleArg):
                        ############################################################
                        # STEP 2A: VERIFY NUMBER OF ARGUMENTS DOESN'T EXCEED MAXIMUM
                        #   STEP 2A-2 : THROW AWAY EXTRA ARGUMENTS FOR 2 ARG FUNCTIONS
                        if(args > 3):
                            menput = [None]*3
                            menput[0] = firstIn
                            self.warn("Too Many Arguments", "menujen.getMenuInput")
                            self.bullet("Provide 2 Arguments Only")
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
                                    self.line("Verbose?")
                                    menput[1] = self.getBinaryDecision("Yes", "No")
                                    self.line("Extra Verbose?")
                                    menput[2] = self.getBinaryDecision("Yes", "No")
                                    return menput
                            # STEP 2A-2-1d: GET DUAL INPUT FOR DUAL VALUED FUNCTIONS
                            elif(dualArg):
                                # POWER
                                if(firstIn == 9):
                                    self.line("Base?")
                                    menput[1] = self.getFloat("Please Enter A Single Number For 1st Argument")
                                    self.line("Exponent?")
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
                                    menput[1] = self.getFloat("Please Enter A Single Number For 1st Argument")
                                if(not helpjen.isFloat(menput[2])):
                                    menput[2] = self.getFloat("Please Enter A Single Number For 2nd Argument")
                                return menput
                            # STEP 2B-2-2b: VERIFY FLOAT INPUT
                            elif(intArg):
                                if(not helpjen.isInt(menput[1])):
                                    menput[1] = self.getInt("Please Enter A Single Number For 1st Argument")
                                if(not helpjen.isInt(menput[2])):
                                    menput[2] = self.getInt("Please Enter A Single Number For 2nd Argument")
                                return menput
                            # STEP 2B-2-2c: VERIFY FLOAT INPUT
                            elif(boolArg):
                                if(firstIn == 23):
                                    if(menput[1].upper() != "YES" or menput[1].upper() != "NO"):
                                        self.line("Verbose?")
                                        menput[1] = self.getBinaryDecision("Yes", "No")
                                    if(menput[2].upper() != "YES" or menput[2].upper() != "NO"):
                                        self.line("Extra Verbose?")
                                        menput[2] = self.getBinaryDecision("Yes", "No")
                                    return menput
                                else:
                                    return menput
                            # STEP 2B-2-2d: VERIFY FLOAT INPUT
                            elif(dualArg):
                                if(firstIn == 9):
                                    if(not helpjen.isFloat(menput[1])):
                                        self.line("Base")
                                        menput[1] = self.getFloat("Please Enter A Single Number For 1st Argument")
                                    if(not helpjen.isInt(menput[2])):
                                        self.line("Exponent?")
                                        menput[2] = self.getInt("Please Enter A Single Number For 2nd Argument")
                                        return menput
                                    else:
                                        return menput
                
                    elif(tripleArg):
                        ############################################################
                        # STEP 2A: VERIFY NUMBER OF ARGUMENTS DOESN'T EXCEED MAXIMUM
                        #   STEP 2A-3 : THROW AWAY EXTRA ARGUMENTS FOR 3 ARG FUNCTIONS
                        if(args>4):
                            return None
                        else:
                            return None


                    # BLACKSCHOLES
                    elif(self.switch(menput[0]) == 12):
                        return None
                    
                    I
                    for index in range(0, args):
                        if(not helpjen.isFloat(menput[index])):
                            warning = f'{index}st Argument' if index == 1 else f'{index}th Argument'
                            self.warn(f'{warning} Not Understood. Please Enter Another Argument', "menujen.getMenuInput")
                            menput[index] = self.getFloat("Please Enter Another Number")
                    return menput
            
    # Retrieve Valid Integer Input From User
    def getInt(self, msg):
        self.line(msg)
        numput = "not a number"
        while(not helpjen.isFloat(numput)):
            numput = input("<< ")
            if(helpjen.isFloat(numput)):
                self.command("Input", numput)
                return int(numput)
            else:
                self.warn("Not a number!", "getInt")

    # Retrieve Valid Float Input From User
    def getFloat(self,msg):
        self.line(msg)
        numput = "not a number"
        while(not helpjen.isFloat(numput)):
            numput = input("<< ")
            if(helpjen.isFloat(numput)):
                self.command("Input",numput)
                return float(numput)
            else:
                self.warn("Not a number!", "getFloat")

    def getBinaryDecision(self, trueOpt, falseOpt):
        self.line(f'{trueOpt} or {falseOpt}?')
        opt = "not an option"
        trueUp = trueOpt.upper()
        falseUp = falseOpt.upper()
        while(opt != trueUp and opt != falseUp):
            opt = input("<< ").upper()
            if(opt != trueUp and opt != falseUp):
                self.warn("Not An Option!", "getBinaryDecision")
        if opt == trueUp:
            self.command("Input", trueOpt)
            return True
        else:
            self.command("Input", falseOpt)
            return False

    def getTechnique(self, conf):
        self.line("Select A Technique")
        numput = "not a technique"
        while(not helpjen.isInt(numput)):
            numput = input("<< ")
            if(helpjen.isInt(numput)):
                if(conf.switchTechnique(int(numput)) == "nothing"):
                    self.warn("Not A Technique!", "getTechnique")
                    self.numput = "not a technique"
                else:
                    self.command("Input", numput)
                    return int(numput)
            else:
                self.warn("Command Not Understood. Try Again.", "getTechnique")
                numput = "not a technique"
        return int(numput)
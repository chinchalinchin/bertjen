import datetime
import helpjen

class menujen:

    def __init__(self):
        self.TITLE_LINE = "                The Bertjen Calculator                   "
        self.SPACE_BUFFER = 2
        self.switcher = {
            "CF": 0,"E": 2,"F": 3,
            "LPI":4, "M": 5, "NORMCDF": 6, "NORMPDF": 7,
            "NPI": 8, "P": 9, "SQ": 11,
            "BS": 12, "LN": 13, "ROOT": 15,
            "COS": 16, "SIN": 17, "ASIN": 18,
            "TAN": 19, "ACOS": 20, "ATAN": 21,
            "I": 22, "V": 23,"Q" : 99,
        }
    
    # Manual Switch
    def switch(self, arg):
        return self.switcher.get(arg, "nothing")

    # Print Menu Options
    def printMenu(self):
        self.title()
        
        self.subtitle("Mathbert")
        
        self.subtitle("Mathbert Functions")
        self.command("CF", "Count Function")
        self.command("F", "Factorial Function")
        self.command("P","Power Function")
        
        self.subtitle("Mathbert Approximations")
        self.command("E","Infinite Series Exponential Approximation")
        self.command("COS", "Infinite Series Cosine Approximation")
        self.command("SIN", "Infinite Series Sine Approximation")
        self.command("TAN", "Infinte Series Tangent Approximation")
        self.command("ACOS", "Infinite Series Arccosine Approximation")
        self.command("ASIN", "Infinite Series Arcsine Approximation")
        self.command("ATAN", "Infinite Series Arctangent Approximation")
        self.command("LPI", "Liebniz Series Pi Approximation")
        self.command("NPI", "Newton Series Pi Approximation")
        self.command("LN", "Infinite Series Natural Log Approximation")
        self.command("ROOT", "Binomial Series Root Approximation")
        self.command("SQ", "Newton's Method Square Root Approximation")
        self.divider()
        
        self.subtitle("Statbert")
        
        self.subtitle("Statbert PDFs")
        self.command("NORMPDF","Normal Probability Density Function")
        
        self.subtitle("Statbert CDFs")
        self.command("NORMCDF", "Normal Cumulative Probability Function")
        self.divider()
        
        self.subtitle("Finbert")
        
        self.subtitle("Finbert Valuations")
        self.command("BS", "Black Scholes Option Function")
        self.divider()
        
        self.subtitle("Admin Commands")
        self.command("I", "Integration Technique Settings")
        self.command("V", "Verbose Settings")
        self.command("M", "Print Help Menu")
        self.command("Q", "Quit")
        self.divider()

    # Print Title of Function
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

    def warn(self, msg, comp):
        print(f'>> {str(comp).upper()} !! {str(msg)} !! ')

    # Print Formatted Output
    def output(self,msg):
        self.command("RESULT", msg)
    
    # Formatted Time Output
    def time(self, flag, start):
        if flag:
            self.command("TIME START", str(datetime.datetime.now().strftime("%H: %M: %S")))
            return datetime.datetime.now()
        else:
            end = datetime.datetime.now()
            self.command("TIME END", str(end.strftime("%H: %M: %S")))
            self.command("TIME DIFF", str(end - start) + " sec")
            
    # Retrieve Valid Menu Input From User
    def getMenuInput(self,):
        menput = "not a selection"
        while(self.switch(menput) == "nothing"):
            self.line("Make A Selection")
            menput = input("<< ").upper()
            if(self.switch(menput) == "nothing"):
                self.warn("Selection not found!", "getMenuInput")
            else:
                return menput
            
    # Retrieve Valid Integer Input From User
    def getInt(self, msg):
        self.line(msg)
        numput = "not a number"
        while(not helpjen.isInt(numput)):
            numput = input("<< ")
            if(helpjen.isInt(numput)):
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
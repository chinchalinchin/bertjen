class printjen():

    def __init__(self):
        self.TITLE_LINE = "                The Bertjen Calculator                   "
        self.SPACE_BUFFER = 2
        
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
        # SINGLE ARGUMENT
        self.command("SEC", "Taylor Series Secant Approximation")
        # SINGLE ARGUMENT
        self.command("CSC", "Taylor Series Cosecant Approximation")
        # SINGLE ARUGMENT
        self.command("COT", "Taylor Series Cotangent Approximation")
        # DOUBLE ARGUMENT 
        self.command("ROOT", "Binomial Series Root Approximation")
        # SINGLE ARGUMENT
        self.command("SQ", "Newton's Method Square Root Approximation")
        self.divider()

        self.subtitle("Mathbert Constants")
        # NO ARGUMENT
        self.command("LPI", "Liebniz Series Pi Approximation")
        # NO ARGUMENT
        self.command("MPI", "Machin Series Pi Approximation")
        # NO ARGUMENT
        self.command("NPI", "Newton Series Pi Approximation")

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
        # SINGLE ARGUMENT 
        self.command("N", "Angle Unit Settings")
        # NO ARGUMENT
        self.command("S", "Save Bertjen Configuration")
        # SINGLE ARGUMENT
        self.command("B", "Calibrate Bertjen")
        # NO ARGUMENT
        self.command("M", "Print Menu")
        # SINGLE ARGUMENT
        self.command("H", "Help Function")
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

    def argument(self, arg, msg, which):
        print(f'--{arg} : type : {which} :  {msg} ')

    def warn(self, msg, comp):
        print(f'>> {str(comp).upper()} !! {str(msg)} !! ')

    # Print Formatted Output
    def output(self,msg):
        self.command("RESULT", msg)
import datetime

class statbert:

    def __init__(self, myConfig, myPrinter, myMath):
        self.conf = myConfig
        self.math = myMath
        self.printer = myPrinter
        self.norm_root_store = None

    # Binomial Probability Mass Function
    def binomialMass(self, n, p, x):
        if n < 0 :
            raise Exception("Number Of Trials Not Understood")
        elif x > n or x < 0:
            raise Exception("Input Not Understood")
        elif p>1 or p<0:
            raise Exception("Probability Of Success Not Understood")
        else:
            success = self.math.power(p, x)
            failure = self.math.power(p, n - x)
            comb = self.math.factorial(n)/(self.math.factorial(x)*self.math.factorial(n-x))
            prob = success*failure*comb
        return prob

    # Binomial Cumulative Probability Distribution
    def binomialDistribution(self, n, p, x):
        if n < 0 :
            raise Exception("Number Of Trials Not Understood")
        elif x > n or x < 0:
            raise Exception("Input Not Understood")
        elif(p>1 or p<0):
            raise Exception("Probability Of Success Not Understood")
        else:
            sum = 0
            for index in range(0, x+1):
                sum = sum + self.binomialMass(n, p, index)
            return sum

    # Normal Probability Density Function
    def normalDensity(self, x, mu, sigma):
        if sigma == 0:
            raise Exception("Variance Undefined")
        else:
            exponent = -1*self.math.power((x - mu)/sigma, 2)/2
            if self.conf.EXTRA_VERBOSE:
                self.printer.warn("Checking Store For Normal Root Constant", "normalDensity")
            if(self.norm_root_store == None):
                if self.conf.EXTRA_VERBOSE:
                    self.printer.warn("No Normal Root Found, Calculating Normal Root Constant", "normalDensity")
                self.norm_root_store = self.math.newtRoot(2*self.math.preferredPi())
            elif self.conf.EXTRA_VERBOSE:
                self.printer.warn("Using Normal Root Constant Stored From Previous Calculations", "normalDensity")
            term = self.math.exp(exponent)/(sigma*self.norm_root_store)
            return term
        
    # Normal Cumulative Probability Function
    def normalDistribution(self, x, mu, sigma):
        # No variance, no distribution
        if sigma == 0:
            raise Exception("Variance Undefined")
        else:
            if self.conf.VERBOSE:
                self.printer.warn(f'Current Integration Technique: {self.conf.getIntegrationTechnique()}', "normalIntegral")
                
            # Determine if symmetry can be used
            if self.conf.VERBOSE:
                self.printer.warn("Looking For Symmetry To Simplify Calculation", "normalIntegral")
            if x == mu:
                if self.conf.VERBOSE:
                    self.printer.warn("Symmetry Found, Returning Known Value", "normalIntegral")
                return 0.5
            elif x > mu:
                if self.conf.VERBOSE:
                    self.printer.warn("Symmetry Found, Setting Start Point To Mean", "normalIntegral")
                start = mu
                LHint = 0.5
                RHint = 0.5
                Sint = 0.5
                MDint = 0.5
                TPint = 0.5
            elif x < mu:
                if self.conf.VERBOSE:
                    self.printer.warn("No Symmetry Found", "normalIntegral")
                start = mu - 5 * sigma
                LHint = 0
                RHint = 0
                Sint = 0
                MDint = 0
                TPint = 0
                if(x<start):
                    raise Exception("Probability Negligible")

            # Integrate density
            current = 0
            delta = (x - start)/self.conf.NORM_ACC
            startTime = datetime.datetime.now()
            # Apply Lefthand and Righthand Approximation
            if self.conf.getIntegrationTechnique() == "ENDPOINT":
                if self.conf.VERBOSE:
                    self.printer.warn(f'Max # Of Iterations: {str(self.conf.NORM_ACC)}', "normalIntegral")
                for index in range(0, self.conf.NORM_ACC):
                    old = current
                    
                    LHX = start + delta*index
                    LHcont = self.normalDensity(LHX, mu, sigma)*delta
                    LHint = LHint + LHcont

                    RHX = start + delta*index + delta
                    RHcont = self.normalDensity(RHX, mu, sigma)*delta
                    RHint = RHint + RHcont

                    current = (RHint + LHint)/2
                    
                    now = datetime.datetime.now()
                    if (self.conf.VERBOSE and now-startTime>datetime.timedelta(seconds=self.conf.LAG)):
                        self.printer.warn("Still Computing", "normalIntegral")
                        self.printer.warn(f'Iteration {str(index)}', "normalIntegral")
                        self.printer.warn(f'Current LH Estimate: {str(LHint)}', "normalIntegral")
                        self.printer.warn(f'Current RH Estimate: {str(RHint)}', "normalIntegral")
                        startTime = datetime.datetime.now()
                    if(old == current):
                        if self.conf.VERBOSE:
                            self.printer.warn(f'Halted After {str(index)} Iterations', "normalIntegral")
                        return current
                return current
            # Apply Midpoint Approximation
            elif self.conf.getIntegrationTechnique() == "TRAPEZOID":
                if self.conf.VERBOSE:
                    self.printer.warn(f'Max # Of Iterations: {str(self.conf.NORM_ACC)}', "normalIntegral")
                    TPX1 = 0
                    previousTPcont0 = 1
                for index in range(1, self.conf.NORM_ACC):
                    old = current
                    TPX0 = start + delta*(index - 1)
                    TPcont0 = self.normalDensity(TPX0, mu, sigma)*delta
                    if(TPX1 != previousTPcont0):
                        TPX1 = start + delta*index
                        TPcont1 = self.normalDensity(TPX1, mu, sigma)*delta
                    TPcont = (TPcont1 + TPcont0)/2
                    TPint = TPint + TPcont
                    TPcont1 = TPcont0
                    previousMDcont0 = TPcont0
                    current = TPint

                    now = datetime.datetime.now()
                    if (self.conf.VERBOSE and now-startTime>datetime.timedelta(seconds=self.conf.LAG)):
                        self.printer.warn("Still Computing", "normalIntegral")
                        self.printer.warn(f'Iteration {str(index)}', "normalIntegral")
                        self.printer.warn(f'Current TRAP Estimate: {str(TPint)}', "normalIntegral")
                        startTime = datetime.datetime.now()
                    if(old == current):
                        if self.conf.VERBOSE:
                            self.printer.warn(f'Halted After {str(index)} Iterations', "normalIntegral")
                        return current
                return current
            # Apply Trapezoid Approximation
            elif self.conf.getIntegrationTechnique() == "MIDPOINT":
                if self.conf.VERBOSE:
                    self.printer.warn(f'Max # Of Iterations: {str(self.conf.NORM_ACC)}', "normalIntegral")
                for index in range(0, self.conf.NORM_ACC):
                    old = current

                    MDX = start + delta*(index + 0.5)
                    MDcont = self.normalDensity(MDX, mu, sigma)*delta
                    MDint = MDint + MDcont

                    current = MDint

                    now = datetime.datetime.now()
                    if (self.conf.VERBOSE and now-startTime>datetime.timedelta(seconds=self.conf.LAG)):
                        self.printer.warn("Still Computing", "normalIntegral")
                        self.printer.warn(f'Iteration {str(index)}', "normalIntegral")
                        self.printer.warn(f'Current MID Estimate: {str(MDint)}', "normalIntegral")
                        startTime = datetime.datetime.now()
                    if(old == current):
                        if self.conf.VERBOSE:
                            self.printer.warn(f'Halted After {str(index)} Iterations', "normalIntegral")
                        return current
                return current
            # Apply Simpson's Approxmation
            elif self.conf.getIntegrationTechnique() == "SIMPSON":
                if self.conf.VERBOSE:
                    self.printer.warn(f'Max # Of Iterations: {str(self.conf.NORM_ACC/2)}', "normalIntegral")
                f0 = self.normalDensity(start, mu, sigma)
                fn = self.normalDensity(x, mu, sigma)
                modDelta = delta /3
                Sint = Sint + (f0 + fn)*modDelta
                for index in range(1, int(self.conf.NORM_ACC/2) + 1):
                    old = current
                    if index != self.conf.NORM_ACC/2 - 1:
                        x1 = start + 2*delta*index
                        x2 = start + delta*(2*index-1)
                        fx1 = self.normalDensity(x1, mu, sigma)
                        fx2 = self.normalDensity(x2, mu, sigma)
                        Sint = Sint + (2*fx1 + 4*fx2)*modDelta
                    else:
                        x2 = start + delta*(2*index-1)
                        fx2 = self.normalDensity(x2, mu, sigma)
                        Sint = Sint +4*fx2*modDelta
                    current = Sint
                    now = datetime.datetime.now()
                    if (self.conf.VERBOSE and now-startTime>datetime.timedelta(seconds=self.conf.LAG)):
                        self.printer.warn("Still Computing", "normalIntegral")
                        self.printer.warn(f'Iteration {str(index)}', "normalIntegral")
                        self.printer.warn(f'Current Simpson Estimate: {str(current)}', "normalIntegral")
                        startTime = datetime.datetime.now()
                    if(old == current):
                        if self.conf.VERBOSE:
                            self.printer.warn(f'Halted After {str(index)} Iterations', "normalIntegral")
                        return current
                return current

    def standardize(self, x, mu, sigma):
        return (x-mu)/sigma
import datetime
import helpjen

class mathbert:
    ########################################################################
    ########################################################################
    #                     CALCULATOR FUNCTIONS                             #
    ########################################################################
    ########################################################################
    # MATHEMATICAL
    ########################################################################
    # Sum First N Natural Numbers Manually

    def __init__(self, myConfig, myPrinter):
        self.conf = myConfig
        self.printer = myPrinter
        self.newt_pi_store = None
        self.e_store = None

    # Sum First N Natural Numbers Formulaically
    def countFormula(self, n):
        count = n*(n+1)/2
        return count

    # Factorial of a Number
    def factorial(self, n):
        if(not helpjen.isInt(n)):
            raise Exception("Decimal Factorials Undefined, Consider Using Gamma Function")
        elif n < 0:
            raise Exception("Negative Factorials Undefined")
        elif n == 1 or n == 0:
            return 1
        else:
            return n*self.factorial(n-1)

    # Power of a Base
    def power(self, x, a):
        multi = 1
        if(a != 0):
            for index in range(1, a+1):
                multi = multi*x
            return multi
        else:
            return 1

    # Infinite Sum Approximation of Natural Exponent
    def exp(self, a):
        if a != 1 or self.e_store == None:
            if self.conf.EXTRA_VERBOSE:
                self.printer.warn(f'Max # Of Iterations: {str(self.conf.SERIES_ACC)}', "exp")
            startTime = datetime.datetime.now()
            sum = 0
            for index in range(0, self.conf.SERIES_ACC):
                num = self.power(a, index)
                den = self.factorial(index)
                old = sum
                sum = sum + num/den
                now = datetime.datetime.now()
                if (self.conf.EXTRA_VERBOSE and now-startTime > datetime.timedelta(seconds=self.conf.LAG)):
                    self.printer.warn("Still Computing", "exp")
                    self.printer.warn(f'Iteration  {str(index)}', "exp")
                    self.printer.warn(f'Current Value {str(sum)}', "exp")
                startTime = datetime.datetime.now()
                if(old == sum):
                    if(a == 1):
                        self.e_store = sum
                    if self.conf.EXTRA_VERBOSE:
                        self.printer.warn(f'Halted After {str(index)} Iterations', "exp")
                    return sum
            if(a == 1):
                self.e_store = sum
            return sum
        else:
            return self.e_store

    # Infinite Sum Approximation of Sine
    def sin(self, x):
        sum = 0
        if self.conf.VERBOSE:
            self.printer.warn(f'Max # Of Iterations: {str(2*self.conf.TRIG_ACC)}', "sin")
        startTime = datetime.datetime.now()
        for index in range(0, int(2*self.conf.TRIG_ACC)):
            old = sum
            num = self.power(-1, index)*self.power(x, 2*index+1)
            den = self.factorial(2*index+1)
            sum = sum + num/den
            now = datetime.datetime.now()
            if (self.conf.VERBOSE and now-startTime > datetime.timedelta(seconds=self.conf.LAG)):
                self.printer.warn("Still Computing", "sin")
                self.printer.warn(f'Iteration  {str(index)}', "sin")
                self.printer.warn(f'Current Value {str(sum)}', "sin")
                startTime = datetime.datetime.now()
            if(old == sum):
                if self.conf.VERBOSE:
                    self.printer.warn(f'Halted After {str(index)} Iterations', "sin")
                return sum
        return sum

    # Infinite Series Cosine Approximation
    def cos(self, x):
        sum = 0
        if self.conf.VERBOSE:
            self.printer.warn(f'Max # Of Iterations: {str(2*self.conf.TRIG_ACC)}', "cos")
        startTime = datetime.datetime.now()
        for index in range(0, int(2*self.conf.TRIG_ACC)):
            old = sum
            num = self.power(-1, index)*self.power(x, 2*index)
            den = self.factorial(2*index)
            sum = sum + num/den
            now = datetime.datetime.now()
            if (self.conf.VERBOSE and now-startTime > datetime.timedelta(seconds=self.conf.LAG)):
                self.printer.warn("Still Computing", "cos")
                self.printer.warn(f'Iteration {str(index)}', "cos")
                self.printer.warn(f'Current Value {str(sum)}', "cos")
                startTime = datetime.datetime.now()
            if(old == sum):
                if self.conf.VERBOSE:
                    self.printer.warn(f'Halted After {str(index)} Iterations', "cos")
                return sum
        return sum

    # Infinite Series Tangent Approximation
    ## ( Technically )
    def tan(self, x):
        cosine = self.cos(x)
        if(cosine == 0):
            raise Exception("Undefined at x = 0")
        else:
            sine = self.sin(x)
            tangent = sine/cosine
            return tangent

    # Infinite Series Arcsine Approximatoin
    def arcsin(self, x):
        if(x > 1 or x < -1):
            raise Exception("Outside Of Function Range")
        else:
            sum = 0
            if self.conf.VERBOSE:
                self.printer.warn(f'Max # of Iterations: {str(int(self.conf.TRIG_ACC))}', "arcsin")
            startTime = datetime.datetime.now()
            for index in range(0, int(self.conf.TRIG_ACC)):
                old = sum
                num = self.factorial(2*index)*self.power(x, 2*index+1)
                den = self.power(4, index)*self.power(self.factorial(index), 2)*(2*index+1)
                sum = sum + num/den
                now = datetime.datetime.now()
                if (self.conf.VERBOSE and now-startTime > datetime.timedelta(seconds=self.conf.LAG)):
                    self.printer.warn("Still Computing", "arcsin")
                    self.printer.warn(f'Iteration {str(index)}', "arcsin")
                    self.printer.warn(f'Current Value {str(sum)}', "arcsin")
                    startTime = datetime.datetime.now()
                if(old == sum):
                    if self.conf.VERBOSE:
                        self.printer.warn(f'Halted After {str(index)} Iterations', "arcsin")
                    return sum
            return sum

    def arccos(self, x):
        if(x > 1 or x < -1):
            raise Exception("Outside Of Function Range")
        else:
            pi = self.newtPi()
            arcosine = pi/2 - self.arcsin(x)
            return arcosine

    def arctan(self, x):
        sum = 0
        if self.conf.VERBOSE:
            self.printer.warn(f'Max # Of Iterations: {str(int(self.conf.TRIG_ACC))}', "arctan")
        startTime = datetime.datetime.now()
        for index in range(0, int(self.conf.TRIG_ACC)):
            old = sum
            num = self.power(-1, index)*self.power(x, 2*index+1)
            den = 2*index + 1
            sum = sum + num/den
            now = datetime.datetime.now()
            if(self.conf.VERBOSE and now - startTime > datetime.timedelta(seconds=self.conf.LAG)):
                self.printer.warn("Still Computing", "arctan")
                self.printer.warn(f'Iteration {str(index)}', "arctan")
                self.printer.warn(f'Current Value {str(sum)}', "arcsin")
                startTime = datetime.datetime.now()
            if(old == sum):
                if self.conf.VERBOSE:
                    self.printer.warn(f'Halted After {str(index)} Iterations', "arctan")
                return sum
        return sum

    # Newton's Method Square Root Approximation
    def newtRoot(self, n):
        if self.conf.VERBOSE:
            self.printer.warn("Max # Of Iterations: " + str(self.conf.SQ_ACC), "newtRoot")
        current = self.nearestPerfectRoot(n)
        startTime = datetime.datetime.now()
        for index in range(0, self.conf.SQ_ACC):
            old = current
            current = 0.5*(old+n/old)
            now = datetime.datetime.now()
            if (self.conf.VERBOSE and now-startTime > datetime.timedelta(seconds=self.conf.LAG)):
                self.printer.warn("Still Computing", "newtRoot")
                self.printer.warn(f'Iteration {str(index)}', "newtRoot")
                self.printer.warn(f'Current Value {str(current)}', "newtRoot")
                startTime = datetime.datetime.now()
            if(old == current):
                if self.conf.VERBOSE:
                    self.printer.warn(f'Halted After {str(index)} Iterations', "newtRoot")
                return current
        return current

    # Binomial Series Root Approximation
    def binRoot(self, x, r):
        if(x < 0 or x > 2):
            raise Exception("Outside Radius of Convergenece")
        if self.conf.VERBOSE:
            self.printer.warn(f'Max # Of Iterations: {str(self.conf.ROOT_ACC)}', "binRoot")
        current = 0
        startTime = datetime.datetime.now()
        for index in range(0, self.conf.ROOT_ACC):
            old = current
            coeff = self.pochhammer(r, index)
            current = current + coeff*self.power(x-1, index)
            now = datetime.datetime.now()
            if (self.conf.VERBOSE and now-startTime > datetime.timedelta(seconds=self.conf.LAG)):
                self.printer.warn(f'{str(index)} ST ITERATION', "binRoot")
                self.printer.warn(f'Coefficient: {str(coeff)}', "binRoot")
                self.printer.warn(f'Power Of x: {str(self.power(x-1,index))}', "binRoot")
                self.printer.warn(f'Multipicand: {str(coeff*self.power(x-1,index))}', "binRoot")
                self.printer.warn(f'Current Sum: {str(current)}', "binRoot")
                self.startTime = datetime.datetime.now()
            if(old == current):
                if self.conf.VERBOSE:
                    self.printer.warn(f'Halted After {str(index)} Iterations', "binRoot")
                return current
        return current

    def log(self, x, a):
        if x == 0:
            raise Exception("Log Undefined At X = 1")
        elif x==1:
            return 0
        else:
            lnx = self.naturalLog(x)
            lnbase = self.naturalLog(a)
            return lnx/lnbase

    # Newton's Method Natural Log Approximation
    def naturalLog(self, n):
        if n == 0:
            raise Exception("Ln Undefined At X = 1")
        elif n == 1:
            return 0
        else:
            if self.conf.VERBOSE:
                self.printer.warn(f'Max # Of Iterations:  {str(self.conf.LN_ACC)}', "naturalLog")
            current = self.nearestPerfectLn(n)
            startTime = datetime.datetime.now()
            for index in range(0, self.conf.LN_ACC):
                old = current
                current = old + 2 * (n - self.exp(old))/(n+self.exp(old))
                now = datetime.datetime.now()
                if (self.conf.VERBOSE and now-startTime > datetime.timedelta(seconds=self.conf.LAG)):
                    self.printer.warn("Still Computing", "naturalLog")
                    self.printer.warn(f'Iteration {str(index)}', "naturalLog")
                    self.printer.warn(f'Current Value = {str(current)}', "naturalLog")
                    startTime = datetime.datetime.now()
                if(old == current):
                    if self.conf.VERBOSE:
                        self.printer.warn(f'Halted After {str(index)} Iterations', "naturalLog")
                    return current
            return current

    # Liebniz's Approximation Of Pi
    def liebPi(self):
        sum = 0
        if self.conf.VERBOSE:
            self.printer.warn(f'Max # Of Iterations: {str(self.conf.LPI_ACC)}', "liebPi")
        startTime = datetime.datetime.now()
        for index in range(0, self.conf.LPI_ACC):
            old = sum
            sum = sum + self.power(-1, index)/(2*index+1)
            now = datetime.datetime.now()
            if (self.conf.VERBOSE and now-startTime > datetime.timedelta(seconds=self.conf.LAG)):
                    self.printer.warn("Still Computing", "liebPi")
                    self.printer.warn(f'Iteration {str(index)}', "liebPi")
                    self.printer.warn(f'Current Value = {str(sum)}', "liebPi")
                    startTime = datetime.datetime.now()
            if old == sum:
                if self.conf.VERBOSE:
                    self.printer.warn(f'Halted After {str(index)} Iterations', "liebPi")
                return 4*sum
        return 4*sum

    # Newton's Approximation of Pi
    def newtPi(self):
        if self.conf.EXTRA_VERBOSE:
            self.printer.warn("Checking Store for Pi", "newtPi")
        if self.newt_pi_store == None:
            if self.conf.EXTRA_VERBOSE:
                self.printer.warn("No Pi Store Found, Calculating Pi", "newtPi")
            sum = 0
            if self.conf.VERBOSE:
                self.printer.warn(f'Max # Of Iterations: {str(self.conf.NPI_ACC)}', "newtPi")
            for index in range(0, self.conf.NPI_ACC):
                old = sum
                sum = sum + self.power(2, index)*self.power(self.factorial(index),2)/self.factorial(2*index+1)
                if old == sum:
                    if self.conf.VERBOSE:
                        self.printer.warn(f'Halted After {str(index)} Iterations', "newtPi")
                    self.newt_pi_store = 2*sum
                    return 2*sum
            self.newt_pi_store = 2*sum
            return 2*sum
        else:
            if self.conf.VERBOSE:
                self.printer.warn("Using Pi Stored From Previous Calculations", "newtPi")
            return self.newt_pi_store
   
    ########################################################################
      
    # Find Nearest Square
    def nearestPerfectRoot(self, n):
        num = int(n)
        if(num == 0 or num == 1):
            return 1
        for index in range(1,num):
            if(self.power(index,2)>n):
                upperDist = self.power(index,2) - n
                lowerDist = n - self.power(index-1,2)
                if(upperDist<lowerDist):
                    return index
                elif index != 1:
                    return (index-1)
            return 1

    # Find Nearest Perfect Natural Log
    def nearestPerfectLn(self, n):
        num = int(n)
        if num == 1 or num == 0:
            return 0
        else:
            for index in range(1, num):
                if(self.exp(index)>n):
                    upperDist = self.exp(index) - n
                    lowerDist = n - self.exp(index - 1)
                    if(upperDist<lowerDist):
                        return index
                    elif index != 1:
                        return (index-1)
        
    # Pochhammer Coefficient
    def pochhammer(self, r, k):
        coeff = 1
        for index in range(0,k):
            coeff = coeff * (r-index)
        coeff = coeff / self.factorial(k)
        return coeff


import datetime
import helpjen
from ratchet import ratchet

class mathbert:
    
    def __init__(self, myConfig, myPrinter):
        self.conf = myConfig
        self.printer = myPrinter
        self.wrench = ratchet(self.conf, self.printer, self)
        self.initStores()
        self.loadStores(self.conf.retrieveConstantStore(), self.conf.retrieveActualStore())

    # Initialize Stores For Constants
    def initStores(self):
        self.newtpi_store = None
        self.liebpi_store = None
        self.machinpi_store = None
        self.e_store = None
        self.newtroot_2_store = None
        self.newtroot_3_store = None
        self.binroot_2_store = None

    # Pass In Stores
    def loadStores(self, stores, actuals):
        if(stores["e_store"]):
            self.e_store = float(stores['e_store'])
        if(stores["newtpi_store"]):
            self.newtpi_store = float(stores['newtpi_store'])
        if(stores["liebpi_store"]):
            self.liebpi_store = float(stores['liebpi_store'])
        if(stores["newtroot_2_store"]):
            self.newtroot_2_store = float(stores['newtroot_2_store'])
        if(stores["newtroot_3_store"]):
            self.newtroot_3_store = float(stores['newtroot_3_store'])
        if(stores["binroot_2_store"]):
            self.binroot_2_store = float(stores['binroot_2_store'])
        if(stores["machinpi_store"]):
            self.machinpi_store = float(stores['machinpi_store'])

    # Count Integer Function
    def countFormula(self, n):
        count = n*(n+1)/2
        return count

    # Factorial Function
    def factorial(self, n):
        if(not helpjen.isInt(n)):
            raise Exception("Decimal Factorials Undefined, Consider Using Gamma Function")
        elif n < 0:
            raise Exception("Negative Factorials Undefined")
        elif n == 1 or n == 0:
            return 1
        else:
            return n*self.factorial(n-1)

    # Power Function
    def power(self, x, a):
        multi = 1
        if(a != 0):
            for index in range(1, a+1):
                multi = multi*x
            return multi
        else:
            return 1

    # Taylor Sum Approximation of Natural Exponent
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

    # Taylor Sum Approximation of Sine
    ## Defaults to radians
    def sin(self, x):
        # Get special angles
        x = self.unrevolve(x)
        if(self.conf.ANGLE_CHOICE==0):
            half_rev = self.preferredPi()
            sixth_rev = self.preferredPi()/3
            eighth_rev = self.preferredPi()/4
            twelveth_rev =self.preferredPi()/6
        elif(self.conf.ANGLE_CHOICE==1):
            half_rev = 180
            sixth_rev = 60
            eighth_rev = 45
            twelveth_rev = 30

        # Look for inputted special angle
        # SIN of 180, -180, 0, 360, -360
        if(x == half_rev or x == -half_rev or x==0 or x==2*half_rev or x == -2*half_rev):
            return 0
        # SIN of 90, -270
        elif(x== half_rev/2 or x ==-3*half_rev/2):
            return 1
        # SIN of -90, 270
        elif(x == 3*half_rev/2 or x == -half_rev/2):
            return -1
        # SIN OF 60, -300, 120, -240
        elif(x == sixth_rev or x == -5*sixth_rev or x == 2*sixth_rev or x == -4*sixth_rev):
            return self.getPreferredRoot3()/2
        # SIN OF -60, 300, -120, 240
        elif(x == -sixth_rev or x == 5*sixth_rev or x == -2*sixth_rev or x ==4*sixth_rev):
            return -self.getPreferredRoot3()/2
        # SIN OF 45, -315, 135, -225
        elif(x == eighth_rev or x == -7*eighth_rev or x == 3*eighth_rev or x == -5*eighth_rev):
            return self.getPreferredRoot2()/2
        # SIN OF -45, 315, -135, 225
        elif(x == -eighth_rev or x == 7*eighth_rev or x == -3*eighth_rev or x == 5*eighth_rev):
            return -self.getPreferredRoot2()/2
        # SIN OF 30, -330, 150, -210
        elif(x == twelveth_rev or x == -11*twelveth_rev or x == 5*twelveth_rev or x == -7*twelveth_rev):
            return 0.5
        # SIN OF -30, 330, -150, 210
        elif(x== -twelveth_rev or x == 11*twelveth_rev or x == -5*twelveth_rev or x == 7*twelveth_rev):
            return -0.5
        else:
            # No special angle inputted, use approximation
            # Infinte series assumes radians   
            if(self.conf.ANGLE_CHOICE == 1):
                x = self.degToRad(x)
            
            # Approximate
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
                    if sum > 1 or sum < -1:
                        raise Exception(f'Not Enough Terms: {2*(self.conf.TRIG_ACC)} To Approximate Input: {x}')
                    else:
                        return sum
            if sum > 1 or sum < -1:
                raise Exception(f'Not Enough Terms: {2*(self.conf.TRIG_ACC)} To Approximate Input: {x}')
            else:
                return sum

    # Taylor Series Cosine Approximation
    def cos(self, x):
        # Get special angles
        if(self.conf.ANGLE_CHOICE==0):
            half_rev = self.preferredPi()
            sixth_rev = self.preferredPi()/3
            eighth_rev = self.preferredPi()/4
            twelveth_rev =self.preferredPi()/6
        elif(self.conf.ANGLE_CHOICE==1):
            half_rev = 180
            sixth_rev = 60
            eighth_rev = 45
            twelveth_rev = 30

        # Look for inputted special angles
        # COS of 180, -180
        if(x == half_rev or x == -half_rev):
            return -1
        # COS of 90, - 270, -90, 270
        elif(x== half_rev/2 or x ==-3*half_rev/2 or x == 3*half_rev/2 or x == -half_rev/2):
            return 0
        # COS of 0, 360, -360
        elif(x==0 or x==2*half_rev or x == -2*half_rev):
            return 1
        # TODO: Look for more special angles
        else:
            # No special angle found, use approximation
            # Infinite series assumes radians
            if(self.conf.ANGLE_CHOICE == 1):
                x = self.degToRad(x)

            # Approximate
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
                    if sum > 1 or sum < -1:
                        raise Exception(f'Not Enough Terms: {2*(self.conf.TRIG_ACC)} To Approximate Input: {x}')
                    else:
                        return sum
            if sum > 1 or sum < -1:
                raise Exception(f'Not Enough Terms: {2*(self.conf.TRIG_ACC)} To Approximate Input: {x}')
            else:
                return sum

    # Taylor Series Tangent Approximation
    ## ( Technically )
    def tan(self, x):
        cosine = self.cos(x)
        if(cosine == 0):
            raise Exception("Undefined at x = 0")
        else:
            sine = self.sin(x)
            tangent = sine/cosine
            return tangent

    # Secant Function Using Cosine Taylor Series
    def sec(self, x):
        unrX = self.unrevolve(x)
        if(self.conf.ANGLE_CHOICE == 0):
            pi = self.preferredPi()
            if(unrX == pi/2):
                raise Exception(f'Secant Undefined At {self.conf.getSymbol("pi")}/2 rad')
            elif(unrX == -pi/2):
                raise Exception(f'Secant Undefined At -{self.conf.getSymbol("pi")}/2 rad')
        elif(self.conf.ANGLE_CHOICE == 1):
            if(unrX == 90):
                raise Exception(f'Secant Undefined At 90 deg')
            elif(unrX == -90):
                raise Exception(f'Secant Undefined At -90 deg')
        cosine = self.cos(x)
        if(cosine==0):
            raise Exception(f'Secant Undefined At Cos({str(x)}) = 0')
        return 1/cosine

    # Cosecant Function Using Sine Taylor Series
    def csc(self, x):
        unrX = self.unrevolve(x)
        if(self.conf.ANGLE_CHOICE == 0):
            pi = self.preferredPi()
            if(unrX == pi):
                raise Exception(f'Cosecant Undefined At {self.conf.getSymbol("pi")} rad')
            elif(unrX == -pi):
                raise Exception(f'Cosecant Undefinted At -{self.conf.getSymbol("pi")} rad')
        elif(self.conf.ANGLE_CHOICE == 1):
            if(unrX == 180):
                raise Exception(f'Cosecant Undefined At 180 deg')
            elif(unrX == -180):
                raise Exception(f'Cosecant Undefinted At -180 deg')
        sine = self.sin(x)
        if(sine ==0):
            raise Exception(f'Cosecant Undefined At Sin({str(x)}) = 0')
        else:
            return 1/sine

    # Cotangent Function Using Tangent Taylor Series
    def cot(self, x):
        tangent = self.tan(x)
        if(tangent == 0):
            raise Exception(f'Cotangent Undefined At Tan({str(x)}) = 0')
        else:
            return 1/tangent

    # Taylor Series Arc Sine Approximatoin
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
                    if(self.conf.ANGLE_CHOICE == 1):
                        sum = self.radToDeg(sum)
                    return sum
            if(self.conf.ANGLE_CHOICE == 1):
                sum = self.radToDeg(sum)
            return sum

    # Taylor Series Arc Cosine Approximation
    def arccos(self, x):
        if(x > 1 or x < -1):
            raise Exception("Outside Of Function Range")
        else:
            if(self.conf.ANGLE_CHOICE == 0):
                pi = self.newtPi()
                shift = pi/2
            elif(self.conf.ANGLE_CHOICE == 1):
                shift = 90
            arcosine = shift - self.arcsin(x)
            return arcosine
                       
    # Taylor Series Arc Tangent Approximation
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
                if(self.conf.ANGLE_CHOICE == 1):
                    sum = self.radToDeg(sum)
                return sum
        if(self.conf.ANGLE_CHOICE == 1):
            sum = self.radToDeg(sum)
        return sum

    # Newton's Method Square Root Approximation
    def newtRoot(self, n):
        if self.conf.VERBOSE:
            self.printer.warn("Checking Stores For Common Roots")
        if(n==2 and self.newtroot_2_store != None):
            if self.conf.VERBOSE:
                self.printer.warn(f'Using {self.conf.getSymbol("sq")}2 Stored From Previous Calculations',
                                    "mathbert.newtRoot")
            return self.newtroot_2_store
        elif(n==3 and self.newtroot_3_store != None):
            if self.conf.VERBOSE:
                self.printer.warn(f'Using {self.conf.getSymbol("sq")}3 Stored From Previous Calculations',
                                    "mathbert.newtRoot")
            return self.newtroot_3_store

        if self.conf.VERBOSE:
            self.printer.warn("Max # Of Iterations: " + str(self.conf.SQ_ACC), "newtRoot")
        current = self.nearestPerfectRoot(n)
        startTime = datetime.datetime.now()
        for index in range(0, self.conf.SQ_ACC):
            old = current
            current = 0.5*(old+n/old)
            now = datetime.datetime.now()
            if (self.conf.VERBOSE and now-startTime > datetime.timedelta(seconds=self.conf.LAG)):
                self.printer.warn("Still Computing", "mathbert.newtRoot")
                self.printer.warn(f'Iteration {str(index)}', "mathbert.newtRoot")
                self.printer.warn(f'Current Value {str(current)}', "mathbert.newtRoot")
                startTime = datetime.datetime.now()
            if(old == current):
                if self.conf.VERBOSE:
                    self.printer.warn(f'Halted After {str(index)} Iterations', "mathbert.newtRoot")
                if(n==2):
                    self.newtroot_2_store = current
                elif(n==3):
                    self.newtroot_3_store = current
                return current
        return current

    # Binomial Series Root Approximation
    def binRoot(self, x, r):
        if(x < 0 or x > 2):
            raise Exception("Outside Radius of Convergenece")
        if self.conf.VERBOSE:
            self.printer.warn("Checking Stores For Common Roots")
        if(x == 2 and r == 0.5 and self.binroot_2_store != None):
            if self.conf.VERBOSE:
                self.printer.warn(f'Using {self.conf.getSymbol("sq")}2 Stored From Previous Calculations',
                                    "mathbert.binRoot")
            return self.binroot_2_store
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
                if(x == 2 and r == 0.5):
                    self.binroot_2_store = current
                return current
        if(x == 2 and r == 0.5):
            self.binroot_2_store = current
        return current

    # Change Of Base Formula Using Taylor Series Exponential Approximation
    def log(self, x, a):
        if x == 0:
            raise Exception("Log Undefined At X = 1")
        elif x==1:
            return 0
        else:
            lnx = self.naturalLog(x)
            lnbase = self.naturalLog(a)
            return lnx/lnbase

    # Halley's Method Natural Log Approximation
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
        if self.conf.EXTRA_VERBOSE:
            self.printer.warn("Checking Store for Pi", "mathbert.liebPi")
        if self.liebpi_store == None:
            if self.conf.EXTRA_VERBOSE:
                self.printer.warn("No Pi Store Found, Calculating Pi", "mathbert.liebPi")
            sum = 0
            if self.conf.VERBOSE:
                self.printer.warn(f'Max # Of Iterations: {str(self.conf.LPI_ACC)}', "mathbert.liebPi")
            startTime = datetime.datetime.now()
            for index in range(0, self.conf.LPI_ACC):
                old = sum
                sum = sum + self.power(-1, index)/(2*index+1)
                now = datetime.datetime.now()
                if (self.conf.VERBOSE and now-startTime > datetime.timedelta(seconds=self.conf.LAG)):
                        self.printer.warn("Still Computing", "mathbert.liebPi")
                        self.printer.warn(f'Iteration {str(index)}', "mathbert.liebPi")
                        self.printer.warn(f'Current Value = {str(sum)}', "mathbert.liebPi")
                        startTime = datetime.datetime.now()
                if old == sum:
                    if self.conf.VERBOSE:
                        self.printer.warn(f'Halted After {str(index)} Iterations', "mathbert.liebPi")
                    self.liebpi_store = 4*sum
                    return 4*sum
            self.liebpi_store = 4*sum
            return 4*sum
        else:
            if self.conf.VERBOSE:
                self.printer.warn("Using Pi Stored From Previous Calculations", "mathbert.newtPi")
            return self.liebpi_store

    # Newton's Approximation of Pi
    def newtPi(self):
        if self.conf.EXTRA_VERBOSE:
            self.printer.warn("Checking Store for Pi", "mathbert.newtPi")
        if self.newtpi_store == None:
            if self.conf.EXTRA_VERBOSE:
                self.printer.warn("No Pi Store Found, Calculating Pi", "mathbert.newtPi")
            sum = 0
            if self.conf.VERBOSE:
                self.printer.warn(f'Max # Of Iterations: {str(self.conf.NPI_ACC)}', "mathbert.newtPi")
            for index in range(0, self.conf.NPI_ACC):
                old = sum
                sum = sum + self.power(2, index)*self.power(self.factorial(index),2)/self.factorial(2*index+1)
                if old == sum:
                    if self.conf.VERBOSE:
                        self.printer.warn(f'Halted After {str(index)} Iterations', "mathbert.newtPi")
                    self.newtpi_store = 2*sum
                    return 2*sum
            self.newtpi_store = 2*sum
            return 2*sum
        else:
            if self.conf.VERBOSE:
                self.printer.warn("Using Pi Stored From Previous Calculations", "mathbert.newtPi")
            return self.newtpi_store
   
    # Machin's Approximation of Pi
    def machinPi(self):
        if self.conf.EXTRA_VERBOSE:
            self.printer.warn("Checking Store for Pi", "mathbert.machinPi")
        if self.machinpi_store == None:
            if self.conf.EXTRA_VERBOSE:
                self.printer.warn("No Pi Store Found, Calculating Pi", "mathbert.machinPi")
            unitHolder = self.conf.getAngleUnits()
            if unitHolder != 1:
                self.conf.setAngleUnits(0)
            machin_first_term = 16 * self.arctan(1/5)
            machin_second_term = 4 * self.arctan(1/239)
            if unitHolder != 1:
                self.conf.setAngleUnits(unitHolder)
            machin_pi = machin_first_term - machin_second_term
            self.machinpi_store = machin_pi
            return machin_pi
        else:
            if self.conf.VERBOSE:
                self.printer.warn("Using Pi Stored From Previous Calculations", "mathbert.machinPi")
            return self.machinpi_store
    
    # HELPER FUNCTIONS
      
    # Preferred Pi
    def preferredPi(self):
        return self.machinPi()

    def preferredRoot2(self):
        return self.newtRoot(2)

    def preferredRoot3(self):
        return self.newtRoot(3)

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
        
    # Pochhammer Coefficient For Binomial Series
    def pochhammer(self, r, k):
        coeff = 1
        for index in range(0,k):
            coeff = coeff * (r-index)
        coeff = coeff / self.factorial(k)
        return coeff

    # Remove multiple of 2*pi from an argument
    def unrevolve(self, x):
        # Determine single revolution measure
        ## 2*pi rads
        revolution = 0
        if(self.conf.ANGLE_CHOICE == 0):
            revolution = 2*self.preferredPi()
        ## 360 degs
        elif(self.conf.ANGLE_CHOICE == 1):
            revolution = 360
        # Add revolution
        if x < -revolution:
            while(x<-revolution):
                x = x + revolution
            return x
        # Substract revolution
        elif x > revolution:
            while(x>revolution):
                x = x - revolution
            return x
        else:
            return x

    def degToRad(self, deg):
        pi = self.preferredPi()
        return deg*pi/180

    def radToDeg(self, rad):
        pi = self.preferredPi()
        return rad*180/pi

    def calibrate(self):
        self.wrench.calibrate()
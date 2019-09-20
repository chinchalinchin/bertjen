import datetime

class finbert:

    def __init__(self, myConfig, myMenu, myMath, myStat):
        self.conf = myConfig
        self.math = myMath
        self.stat = myStat
        self.menu = myMenu

    # Black Scholes Formula
    def BSF(self, s, k, r, d, o, t, opt):
        if(o==0):
            if opt:
                if s>k:
                    return (s-k)
                else:
                    return 0
            else:
                if s<k:
                    return (k-s)
                else:
                    return 0  
        if self.conf.VERBOSE:
            self.menu.warn("Calculating Black Scholes Parameters", "BSF")
        d1 = self.d1(s,k,r,d,o,t)
        if self.conf.VERBOSE:
            self.menu.warn(f'Black Scholes D1: {d1}', "BSF")
        d2 = self.d2(s,k,r,d,o,t)
        if self.conf.VERBOSE:
            self.menu.warn(f'Black Scholes D2: {d2}', "BSF")
        dS = s * self.math.exp(-r*t)
        if self.conf.VERBOSE:
            self.menu.warn(f'Discounted Spot Price: {dS}', "BSF")
        dK = k * self.math.exp(-d*t)
        if self.conf.VERBOSE:
            self.menu.warn(f'Discounted Strike Price: {dK}', 'BSF')
        value = 0
        Probd1 = 0
        Probd2 = 0
        if self.conf.VERBOSE:
            self.menu.warn("Calculating Risk Free Probabilities", "BSF")
        if opt:
            Probd1 = self.stat.normalIntegral(d1, 0, 1)
            if self.conf.VERBOSE:
                self.menu.warn(f'P(d1)={Probd1}', "BSF")
            Probd2 = self.stat.normalIntegral(d2, 0, 1)
            if self.conf.VERBOSE:
                self.menu.warn(f'P(d2)={Probd2}', "BSF")
            value = dS*Probd1-dK*Probd2
        else:
            Probd1 = self.stat.normalIntegral(-d1, 0, 1)
            if self.conf.VERBOSE:
                self.menu.warn(f'P(-d1)={Probd1}', "BSF")
            Probd2 = self.stat.normalIntegral(-d2, 0, 1)
            if self.conf.VERBOSE:
                self.menu.warn(f'P(-d2)={Probd1}', "BSF")
            value = dK*Probd2 - dS*Probd1
        return value

    def annuityImmediate(self, r, n):
        return None

    def annuityDue(self, r, n):
        return None

    # Black Scholes d1
    def d1(self, s, k, r, d, o, t):
        num = self.math.naturalLog(s/k) + ( r - d + 0.5* self.math.power(o,2))*t
        den = self.math.newtRoot(t)*o
        return num/den

    # Black Scholes d2
    def d2(self, s, k, r, d, o, t):
        thisD2 = self.d1(s,k,r,d,o,t) - o*self.math.newtRoot(t)
        return thisD2
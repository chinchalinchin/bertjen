class identijen:
    
    def __init__(self):
        self.switcher = {
            "CF": 0,"E": 2,"F": 3,"LPI":4, 
            "M": 5, "NORMCDF": 6, "NORMPDF": 7,
            "NPI": 8, "P": 9, "SQ": 11, "BS": 12,
            "LN": 13, "ROOT": 15, "COS": 16, 
            "SIN": 17, "ASIN": 18, "TAN": 19, 
            "ACOS": 20, "ATAN": 21, "I": 22, "V": 23,
            "BINPMF": 24, "BINCDF":25, "B": 26,
            "LOG": 27, "S": 28, "H": 29,
            "SEC": 30, "CSC": 31, "COT": 32,
            "N": 33, "MPI": 34,
            "Q" : 99,
        }
        self.unswitcher = {
            0: "CF", 2: "E", 2: "LPI",
            5: "M", 6: "NORMCDF", 7:"NORMPDF",
            8: "NPI", 9: "P", 11: "SQ", 12: "BS",
            13: "LN", 15: "ROOT", 16: "COS",
            17: "SIN", 18: "ASIN", 19: "TAN",
            20: "ACOS", 21: "ATAN", 22: "I", 23: "V",
            24: "BINPMF", 25: "BINCDF", 26: "B",
            27: "LOG", 28: "S", 29: "H",
            30: "SEC", 31: "CSC", 32: "COT",
            33: "N", 34: "MPI",
            99: "Q" 
        }
    
    def switch(self, arg):
        return self.switcher.get(arg, "nothing")
    
    def unswitch(self, arg):
        return self.unswitcher.get(arg, "nothing")
        
    # SINGLE ARG : 
    #   COUNT(0), EXP(2), FACT(3), NEWTROOT(11), LN(13)
    #   COS(16), SIN(17), TAN(19), ACOS(20), ASIN(18), ATAN(21)
    #   INTEGRALSET(22), BERTJEN(26), HELP(29), SEC(30)
    #   CSC(31), COT(32), ANG(33)
    def isSingleArg(self, firstIn):
        return (firstIn == 0 or firstIn == 2 or firstIn == 3 or firstIn == 11
                or firstIn == 13 or firstIn == 16 or firstIn == 17 or firstIn == 18
                or firstIn == 19 or firstIn == 20 or firstIn == 21 or firstIn == 22
                or firstIn == 26 or firstIn == 29 or firstIn == 30 or firstIn == 31
                or firstIn == 32 or firstIn == 33)

    # DOUBLE ARG: 
    #   BINROOT(15), POWER(9), VERB(23), LOG(27)
    def isDoubleArg(self, firstIn):
        return (firstIn == 15 or firstIn == 9 or firstIn == 23 or firstIn == 27)

    # TRIPLE ARG: 
    #   NORMCDF(6), NORMPDF(7), BINPMF(24), BINCDF(25) 
    def isTripleArg(self, firstIn):
        return (firstIn ==  6 or firstIn == 7 or firstIn == 24 or firstIn == 25)

    # SPECIAL ARG:
    #   BLACKSCHOLES(12)
    def isSpecialArg(self, firstIn):
        return (firstIn == 12)

    # FLOAT ARG: 
    #   EXP(2), NEWTROOT(11), LN(13), COS(16)
    #   SIN(17), TAN(19), ACOS(20), ASIN(18), ATAN(21),
    #   BINROOT(15), LOG(27), NORMCDF(6), NORMPDF(7),
    #   SEC(30), CSC(31), COT(32)
    def isFloatArg(self, firstIn):
        return (firstIn == 2 or firstIn == 11 or firstIn == 13 or firstIn == 16 or firstIn == 17 
                or firstIn == 18 or firstIn == 19 or firstIn == 20 or firstIn == 21 or firstIn == 15
                or firstIn == 27 or firstIn == 6 or firstIn == 7 or firstIn == 30 or firstIn == 31
                or firstIn == 32)

    # INT ARG : 
    #   COUNT(0), FACT(3), INTEGRALSET(22)
    def isIntArg(self, firstIn):
        return (firstIn == 0 or firstIn == 3 or firstIn == 22 or firstIn == 33)

    # BOOL ARG: 
    #   VERB(23), BERTJEN(26)
    def isBoolArg(self, firstIn):
        return (firstIn == 26 or firstIn == 23)

    # STRING ARG:
    #   HELP(29)
    def isStringArg(self, firstIn):
        return firstIn == 29

    # COMPOUND ARG : 
    #   POWER(9), BLACKSCHOLES(12), BINPMF(24)
    #   BINCDF(25)
    # TODO: BINCDF AND BINPMF ARE COMPOUND, DUMBASS!
    def isCompoundArg(self, firstIn):
        return (firstIn == 9 or firstIn == 12 or firstIn == 24 or firstIn == 25)

    # NO OUTPUT FUNCTION : 
    def isNoOutput(self, firstIn):
        return (firstIn == 26 or firstIn == 23 or firstIn == 22 or firstIn == 29
                or firstIn == 5 or firstIn == 33)

    # TRIG FUNCTIONS:
    #   COS(16), SIN(17), TAN(19), ACOS(20), ASIN(18), ATAN(21)
    #   SEC(30), CSC(31), COT(32)
    def isTrigFunction(self, firstIn):
        return (firstIn == 16 or firstIn == 17 or firstIn == 19 or firstIn == 20
                or firstIn == 18 or firstIn == 21 or firstIn == 30 or firstIn == 31
                or firstIn == 32)

    # BINOMIAL FUNCTIONS:
    #   BINPMF(24), BINCDF(25)
    def isBinomialFunction(self, firstIn):
        return firstIn == 24 or firstIn == 25

    # NORMAL FUNCTIONS:
    #   NORMCDF(6), NORMPDF(7)
    def isNormalFunction(self, firstIn):
        return firstIn == 6 or firstIn ==7

    # ADMIN FUNCTIONS
    #   MENU(5), INTEGRATION(22), VERBOSE(23), SAVE(28), HELP(29), 
    #   ANG(33), QUIT(99)
    def isAdminFunction(self, firstIn):
        return (firstIn == 5 or firstIn == 22 or firstIn == 23 or firstIn == 28
                or firstIn == 29 or firstIn == 33 or firstIn == 99)

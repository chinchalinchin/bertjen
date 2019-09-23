class identijen:
    
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

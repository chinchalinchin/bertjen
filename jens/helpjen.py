# Determine If Input Is Float
def isFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
# Determine If Input Is Integer
def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def isNan(num):
    return num != num

def switchYesOrNo(test):
        if(test.upper() == "YES"):
            return True
        else:
            return False

def switchToBool(trueOpt, falseOpt, test):
    if(test.upper() == trueOpt.upper()):
        return True
    else:
        return False
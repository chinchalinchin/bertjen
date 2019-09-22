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

# Determine If Number Is Nan
def isNan(num):
    return num != num

# Switch Yes Or No To Boolean
def switchYesOrNo(test):
        if(test.upper() == "YES"):
            return True
        else:
            return False

# Switch Provided Options To Boolean
def switchToBool(trueOpt, falseOpt, test):
    if(test.upper() == trueOpt.upper()):
        return True
    else:
        return False
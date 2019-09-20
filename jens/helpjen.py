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
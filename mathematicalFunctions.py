def total(x):
    y = 0    
    for i in range(len(x)):
        y = y + x[i]     
    return y

def mean(x):
    y = total(x)/len(x)
    return y

def geomean(x):
    y = 1    
    for i in range(len(x)):
        y = y * x[i]
    y = y**(1/len(x))
    return y

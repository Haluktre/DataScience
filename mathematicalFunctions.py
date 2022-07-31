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

def arraymax(x):
    y = x[0]
    for i in range(len(x)):
        if y>=x[i]:
            continue
        else:
            y = x[i]
    return y

def arraymin(x):
    y = x[0]
    for i in range(len(x)):
        if y<=x[i]:
            continue
        else:
            y = x[i]
    return y

def identitymatrix(x):
    matrix = []
    for i in range(x):
        list_a = []
        for j in range(x):
            if(i==j): 
                list_a.append(1)
            else:
                list_a.append(0)
        matrix.append(list_a)
    return matrix
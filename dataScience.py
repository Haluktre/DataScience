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

def b1_parameter(x,y):
    y_total = 0
    x_total = 0
    value0 = 0
    value1 = 0
    for i in range(len(y)):
        y_total = y_total + y[i]
        x_total = x_total + x[i]
    y_mean = y_total/len(y) 
    x_mean = x_total/len(x)
    
    for j in range(len(x)):
        value0 = value0 + (y[j] - y_mean)*(x[j] - x_mean)
        value1 = value1 + (x[j] - x_mean)**2
    b1 = value0/value1
    return b1

def b0_parameter(b1,x_mean,y_mean):
    b0 = y_mean - b1*x_mean
    return b0

def leastsquares_predict(b0,b1,x):
    y_predict = b0 + b1*x
    return y_predict

def tss_ess_rss_rsquare(y,y_predicts):
    tss_val = 0
    ess_val = 0
    rss_val = 0
    for i in range(len(y)):
        print(i)
        tss_val = tss_val + (y[i]-mean(y))**2
        ess_val = ess_val + (y_predicts[i]-mean(y))**2
        rss_val = rss_val + (y[i]-y_predicts[i])**2
    R_square = ess_val/tss_val
    
    return tss_val,ess_val,rss_val,R_square
    









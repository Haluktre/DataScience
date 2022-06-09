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

class model:  
    def __init__(self):
        self.b0 = None
        self.b1 = None
        self.tss_val = None
        self.ess_val = None
        self.rss_val = None
        self.R_square = None
    
    def fit(self,x,y):
        self.__x = x
        self.__y = y
        self.__y_predicts = []
        self.__x_mean = mean(x)
        self.__y_mean = mean(y)
        self.b1_parameter()
        self.b0_parameter()
        self.leastsquares_predict()
        self.tss_ess_rss_rsquare()
        
        
    def __b1_parameter(self):
        value0 = 0
        value1 = 0   
        
        for j in range(len(self.x)):
            value0 = value0 + (self.y[j] - self.y_mean)*(self.x[j] - self.x_mean)
            value1 = value1 + (self.x[j] - self.x_mean)**2
            
        self.b1 = value0/value1 
    
    def __b0_parameter(self):
        self.b0 = self.y_mean - self.b1*self.x_mean
    
    def __leastsquares_predict(self):
        for i in range(len(self.x)):
            self.y_predicts.append(self.b0 + self.b1*self.x[i])
    
    
    def __tss_ess_rss_rsquare(self):
        self.tss_val = 0
        self.ess_val = 0
        self.rss_val = 0
        for i in range(len(self.y)):
            print(i)
            self.tss_val = self.tss_val + (self.y[i]-mean(self.y))**2
            self.ess_val = self.ess_val + (self.y_predicts[i]-mean(self.y))**2
            self.rss_val = self.rss_val + (self.y[i]-self.y_predicts[i])**2
            
        self.R_square = self.ess_val/self.tss_val
        
    









import mathematicalFunctions as mf

class SimpleLinearRegression:  
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
        self.__x_mean = mf.mean(x)
        self.__y_mean = mf.mean(y)
        self.__b1_parameter()
        self.__b0_parameter()
        self.__leastsquares_predict()
        self.__tss_ess_rss_rsquare()
        
        
    def __b1_parameter(self):
        value0 = 0
        value1 = 0   
        
        for j in range(len(self.__x)):
            value0 = value0 + (self.__y[j] - self.__y_mean)*(self.__x[j] - self.__x_mean)
            value1 = value1 + (self.__x[j] - self.__x_mean)**2
            
        self.b1 = value0/value1 
    
    def __b0_parameter(self):
        self.b0 = self.__y_mean - self.b1*self.__x_mean
    
    def __leastsquares_predict(self):
        for i in range(len(self.__x)):
            self.__y_predicts.append(self.b0 + self.b1*self.__x[i])
    
    
    def __tss_ess_rss_rsquare(self):
        self.tss_val = 0
        self.ess_val = 0
        self.rss_val = 0
        for i in range(len(self.__y)):
            print("Step:",i)
            self.tss_val = self.tss_val + (self.__y[i]-self.__y_mean)**2
            self.ess_val = self.ess_val + (self.__y_predicts[i]-self.__y_mean)**2
            self.rss_val = self.rss_val + (self.__y[i]-self.__y_predicts[i])**2
        print("Finished fit!") 
        self.R_square = self.ess_val/self.tss_val
        
    
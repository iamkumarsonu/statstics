# creating the height data list
#Mean,Median,Mode,Standard Deviation
class measureOfCentralTandency():
    def __init__(self,data):
        self.data = data
    def meanValue(self):
        sum_value = 0
        for value in self.data:
            sum_value = sum_value+value
        return sum_value/len(self.data)
    def modeValue(self):
        uniq_elem_dict = {}
        for value in self.data:
            if value in uniq_elem_dict.keys():
                uniq_elem_dict[value] = uniq_elem_dict[value]+1
            else:
                uniq_elem_dict[value] = 1
        keys,values = list(uniq_elem_dict.keys()),list(uniq_elem_dict.values())
        maxFrequency = 0
        for freq in values:
            if freq > maxFrequency:
                maxFrequency = freq
        modeList = []
        for i in range(0,len(keys)):
            if values[i] == maxFrequency:
                modeList.append(keys[i])
        if len(modeList) == 1:
            return modeList[0]
        else:
            return modeList
    def medianValue(self):
        n = len(self.data)
        for i in range(0,n):
            for j in range(0,n-i-1):
                if self.data[j]>self.data[j+1]:
                    self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
        if n%2==0:
            return (self.data[n//2]+self.data[(n//2)+1])/2
        else:
            return self.data[(n+1)//2]    
    def standardDeviation(self):
        mean_value = measureOfCentralTandency(self.data).meanValue()  
        diversion = [ (val-mean_value)**2 for val in self.data]
        variance = sum(diversion)/(len(diversion)-1)
        return variance**(1/2)
            
height_data = [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]
measureOfCentralTandency(height_data).meanValue() 
measureOfCentralTandency(height_data).modeValue()
measureOfCentralTandency(height_data).medianValue()
measureOfCentralTandency(height_data).standardDeviation()






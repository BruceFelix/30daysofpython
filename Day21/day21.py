# Exercises Day 21
# Level 1
#1 
import statistics
class Statistics():
    def __init__(self,my_list = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]):
        self.my_list = my_list
    # central tendancies
    def themean(self ,):
        return statistics.mean(self.my_list)

    def themedian(self):
        return statistics.median(self.my_list)
    
    def themode(self):
        return statistics.mode(self.my_list)
    
    #Measure of variability
    def therange(self):
        return max(self.my_list) - min(self.my_list)
        
    def thevariance(self):
        return statistics.variance(self.my_list)
    
    def thestandard(self):
        return statistics.stdev(self.my_list)
    
    #Additional measures
    def min(self):
        return min(self.my_list)
    def max(self):
        return max(self.my_list)
    def count(self):
        return self.my_list.count
    def percentile(self):
        return statistics.percentile(self.my_list)
    def frequency_distribution(self):
        return statistics.frequency(self.my_list)
data = Statistics()

print(data.themean())
print(data.themedian())
print(data.themode())
print(data.therange())
print(data.thevariance())
print(data.thestandard())
print(data.min())
print(data.max())
print(data.count())




# Exercises Day 21
# Level 1
#1 
import statistics, numpy, collections
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
        return len(self.my_list)
    def percentile(self):
        return numpy.percentile(self.my_list, 90)
    def frequency_distribution(self):
        return statistics.frequency(self.my_list)
data = Statistics()

print('Mean:',data.themean())
print("Median:",data.themedian())
print('Mode:',data.themode())
print('Range:',data.therange())
print('Variance',data.thevariance())
print('Standard Deviation',data.thestandard())
print('Min:',data.min())
print('Max:',data.max())
print('Count:',data.count())
print('Percentile:',data.percentile())
# print(data.frequency_distribution())


# Level 2
class PersonAccount():
    def __init__(self):
        self.firstname = "Bruce"
        self.lastname = "Mwangi"
        self.incomes = {10000: "salary", 20000: "pocket money"}
        self.expenses = {5000: "rent", 2000: "small bills", 1000: 'clothes'}
    def total_income(self):
        total = 0
        for income in self.incomes.keys():
            total += income
        return total

    def total_expense(self):
        all_expenses = 0
        for expense in self.expenses.keys():
            all_expenses += expense
        return all_expenses
    def account_info(self):
        print(f"{self.firstname} {self.lastname} has {self.incomes} sources of income and {self.expenses} expenses")
    def add_income(self,income):
        self.incomes.append(income)
    def add_expense(self,expense):
        self.expenses.append(expense)
    def account_balance(self):
        print(f"{self.firstname} has {self.incomes} - {self.expenses} savings")
    
person = PersonAccount()
print(person.account_info())
print(person.incomes)
print(person.expenses)
print(person.total_income())
print(person.total_expense())
print(person.account_balance())
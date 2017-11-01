
#Simple list
names = ['Stuart', 'Bruce', 'Jenny']
#Simple dictionary
ages = { 'Stuart' : 2017-1987, 'Bruce' : 2017-1954, 'Jenny' : 2017-1948  }

print(ages)
print("The keys of the dictionary ages are: ", ages.keys() )
print("The values of the dictionary ages are: ", ages.values() )

#Use zip and dict to make a new dictioary zipping9associating) custom keys with associated values
backwardsDict = dict(zip(ages.values(),ages.keys()))

print("The new backwardsDict is", backwardsDict)
# List comprehension - filtering and transforming a list
upercaseNames = [ x.upper() for x in names ]

print("Upper case names are", upercaseNames)
print("Turn backwards dictionary to a list:", list(backwardsDict.keys()))

## PANDAS STUFF
import pandas as pd

#make a series from a somple list
simple_series = pd.Series(names)
print("The simple series is", simple_series)
idx = 0

#Get a item in the series by refering to its position/index
print("The first index's item in the series is: ", simple_series[idx])
#Get serveral values by specifying several indexs
print("Grab several names at once, by refering to several indexes at once:", simple_series[[0,2]])
print("Read what the series' index is set to:", simple_series.index) 

simple_series.index = ['a','b','c']
print("We've changed the index for the sreies:", simple_series)

#Make a series but specify its index for its values
buffer = pd.Series(['Leg', 'Arm','back'], index=[1,2,3])
print("newly create buffer series :", buffer)

# You can vector add a series and all its values will respond to the operation
buffer += 'A' # Nice little vector operation where all operations(+=) is applied to all values
print("newly create buffer pd.Series(+='A') :", buffer)

print("addig to series together of disperate value typea:", simple_series + buffer)

project1 = pd.Series([1000, 2000, 500], index=["Company A", "Company B", "Company C"])
project2 = pd.Series([800, 2000 ], index=["Company D", "Company A"])

# this is the same as + of two series but using the series add() function instead to provide extra ability
# to fill missing index vallues
print(project1.add(project2, fill_value=0))

#Data frames are dictionaries of Series. Each Key is a column and the series represents the values of that column
data = { 'a': [1,2,3,4,5], 'b' : [6,7,8,9,10], 'c':[11,12,13,14,15]}

#Make a dataframe from a dictionary
df = pd.DataFrame(data)
print("Our dataframe looks like this", df)

#Make a dataframe from tuples which will be the rows and specify that the columns will be called
data1 = pd.DataFrame([(1,2,3),(4,5,6)],columns=('A','B','C')) #note you have to pass a list of rows
print(data1)
print("just column C:", data1['C']);

#Column names become attributes of the dataframe and can be refered to directly
print(data1.C)
print(data1[['A','C']]) # note you have to pass a list [] of column names

#open csv into a dataframe (A table of Columns(Series))
dfStocks = pd.read_csv(r'C:\Users\Stuart\Documents\Visual Studio 2017\Projects\InvestmentSplicing\InvestmentSplicing\stocks_2017-11-01_15-19-27.csv',sep=';')
print(dfStocks.columns)






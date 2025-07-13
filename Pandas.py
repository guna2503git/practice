# A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
# Features of DataFrame
# Potentially columns are of different types
# Size – Mutable
# Labeled axes (rows and columns)
# Can Perform Arithmetic operations on rows and columns
# pandas.DataFrame
# A pandas DataFrame can be created using the following constructor −
# pandas.DataFrame( data, index, columns, dtype, copy)
#data
#data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame.
#index
#For the row labels, the Index to be used for the resulting frame is Optional Default np.arange(n) if no index is passed.
#columns
#For column labels, the optional default syntax is - np.arange(n). This is only true if no index is passed.
#dtype
#Data type of each column.
#copy
#This command (or whatever it is) is used for copying of data, if the default is False.
# Create DataFrame
# A pandas DataFrame can be created using various inputs like −
# Lists
# dict
# Series
# Numpy ndarrays
# Another
# Create an Empty DataFrame
# A basic DataFrame, which can be created is an Empty Dataframe.
#import the pandas library and aliasing as pd
import pandas as pd
df = pd.DataFrame()
print(df)
#Create a DataFrame from Lists
#The DataFrame can be created using a single list or a list of lists.
#Example1
import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

#Example2
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

#Example3
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print(df)
#Note − Observe, the dtype parameter changes the type of Age column to floating point
#Create a DataFrame from Dict of ndarrays / Lists
#All the ndarrays must be of same length. If index is passed, then the length of the index should equal to the length of the arrays.
#If no index is passed, then by default, index will be range(n), where n is the array length.
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)
#Note − Observe the values 0,1,2,3. They are the default index assigned to each using the function range(n).
#Example 2
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)
#Note − Observe, the index parameter assigns an index to each row
#Create a DataFrame from Dict of Series
#Dictionary of Series can be passed to form a DataFrame. The resultant index is the union of all the series indexes passed.
#Example
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
#Note − Observe, for the series one, there is no label ‘d’ passed, but in the result, for the d label, NaN is appended with NaN.
#Column Selection
#Example
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df['one'])
#Column Addition
#Example
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']

print(df)
#Column Deletion
#Example
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
   'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print ("Our dataframe is:")
print(df)

# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print(df)

print ("Deleting another column using POP function:")
df.pop('two')
print(df)
#Row Selection, Addition, and Deletion
#Selection by Label
#Rows can be selected by passing row label to a loc function.
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df.loc['b'])
#Selection by integer location
#Rows can be selected by passing integer location to an iloc function.
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df.iloc[2])
#Slice Rows
#Multiple rows can be selected using ‘ : ’ operator.
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df[2:4])
#Addition of Rows
#Add new rows to a DataFrame using the append function. This function will append the rows at the end.
import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print(df)
#Deletion of Rows
#Use index label to delete or drop rows from a DataFrame. If label is duplicated, then multiple rows will be dropped.
import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)

# Drop rows with label 0
df = df.drop(0)

print(df)
#Read CSV Files
#A simple way to store big data sets is to use CSV files (comma separated files).
#CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
import pandas as pd

df = pd.read_csv('C:/Users/Admin/Desktop/ak.txt')
#Read JSON
#Big data sets are often stored, or extracted as JSON.
import pandas as pd

df = pd.read_json('C:/Users/Admin/Desktop/ak1.txt')
#Dictionary as JSON
#JSON = Python Dictionary
#JSON objects have the same format as Python dictionaries.
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)
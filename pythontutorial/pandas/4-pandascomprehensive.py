# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:05:36 2018

@author: Raghu Prasad
https://www.listendata.com/2017/12/python-pandas-tutorial.html
"""

#Importing pandas library
import pandas as pd;

#Importing Dataset
income = pd.read_csv("C:\\raghu\\kaushalya.tech\\trainingmaterial\\machinelearning\\data\\income.csv");
print(income);

#Get Variable Names
print(income.columns);
print(income.columns[0:2])

#Knowing the Variable types
print(income.dtypes)

print(income['State'].dtypes)

#Changing the data types
income.Y2008 = income.Y2008.astype(float)
print(income['Y2008'].dtypes)

#To view the dimensions or shape of the data
print(income.shape)

print(income.shape[0])
print(income.shape[1])

#To view only some of the rows

print(income.head())
print(income.head(2)) #shows first 2 rows.
print(income.tail())
print(income.tail(2)) #shows last 2 rows

#Alternatively, any of the following commands can be used to fetch first five rows.
#iloc - Purely integer-location based indexing for selection by position
income[0:5] 
income.iloc[0:5]

#Extract Unique Values
#The unique() function shows the unique levels or categories in the dataset.
income.Index.unique()
#The nunique( ) shows the number of unique values.
income.Index.nunique()

#pd.crosstab( ) is used to create a bivariate frequency distribution. Here the bivariate frequency distribution is between Index and State columns.
pd.crosstab(income.Index,income.State)

#Creating a frequency distribution
income.Index.value_counts(ascending = True)

#To draw the samples
#Here n = 5 depicts we need 5 columns and frac = 0.1 tells that we need 10 percent of the data as my sample.
income.sample(n = 5)
income.sample(frac = 0.1)


#Selecting only a few of the columns
income.loc[:,["Index","State","Y2008"]]

income.loc[:,"Index":"Y2008"]  #Selecting consecutive columns
#In the above command both Index and Y2008 are included.


#The difference between loc and iloc is that loc requires the column(rows) names to be selected while iloc requires the column(rows) indices (position).

#You can also use the following syntax to select specific variables.

data = pd.DataFrame({"A" : ["John","Mary","Julia","Kenny","Henry"], "B" : ["Libra","Capricorn","Aries","Scorpio","Aquarius"]})
data 



#Renaming all the variables.
data.columns = ['Names','Zodiac Signs']

#If only some of the variables are to be renamed then we can use rename( ) function where the new names are passed in the form of a dictionary.

data.rename(columns = {"Names":"Cust_Name"},inplace = True)

#By default in pandas inplace = False which means that no changes are made in the original dataset. Thus if we wish to alter the original dataset we need to define inplace = True.

#Suppose we want to replace only a particular character in the list of the column names then we can use str.replace( ) function. For example, renaming the variables which contain "Y" as "Year"

income.columns = income.columns.str.replace('Y' , 'Year ')
income.columns

#Setting one column in the data frame as the index
#Using set_index("column name") we can set the indices as that column and that column gets removed.

income.set_index("Index",inplace = True)
income.head()
#Note that the indices have changed and Index column is now no more a column
income.columns
income.reset_index(inplace = True)
income.head()

#Removing the columns and rows

#To drop a column we use drop( ) where the first argument is a list of columns to be removed. 

#By default axis = 0 which means the operation should take place horizontally, row wise. To remove a column we need to set axis = 1.

income.drop('Index',axis = 1)

#Alternatively
income.drop("Index",axis = "columns")
income.drop(['Index','State'],axis = 1)
income.drop(0,axis = 0)
income.drop(0,axis = "index")
income.drop([0,1,2,3],axis = 0)

#Sorting the data

#To sort the data sort_values( ) function is deployed. By default inplace = False and ascending = True.

income.sort_values("State",ascending = False)
income.sort_values("State",ascending = False,inplace = True)
income.Y2006.sort_values() 

#We have got duplicated for Index thus we need to sort the dataframe firstly by Index and then for each particular index we sort the values by Y2002

income.sort_values(["Index","Year 2014"])

#Create new variables

#Using eval( ) arithmetic operations on various columns can be carried out in a dataset.

income["difference"] = income.Y2008-income.Y2009

#Alternatively
income["difference2"] = income.eval("Y2008 - Y2009")
income.head()
#income.ratio = income.Y2008/income.Y2009 this may not work

data = income.assign(ratio = (income.Y2008 / income.Y2009))
data.head()

#Finding Descriptive Statistics
#describe( ) is used to find some statistics like mean,minimum, quartiles etc. for numeric variables.
income.describe() #for numeric variables

#To find the total count, maximum occuring string and its frequency we write include = ['object']

income.describe(include = ['object'])  #Only for strings / objects

#Mean, median, maximum and minimum can be obtained for a particular column(s) as:

income.Y2008.mean()
income.Y2008.median()
income.Y2008.min()
income.loc[:,["Y2002","Y2008"]].max()

#Groupby function
#To group the data by a categorical variable we use groupby( ) function and hence we can do the operations on each category.
income.groupby("Index").Y2008.min()
income.groupby("Index")["Y2008","Y2010"].max()

#agg( ) function is used to find all the functions for a given variable.
income.groupby("Index").Y2002.agg(["count","min","max","mean"])
#The following command finds minimum and maximum values for Y2002 and only mean for Y2003

income.groupby("Index").agg({"Y2002": ["min","max"],"Y2003" : "mean"})

#Filtering
#To filter only those rows which have Index as "A" we write:
income[income.Index == "A"]

#Alternatively
income.loc[income.Index == "A",:]

#To select the States having Index as "A":

income.loc[income.Index == "A","State"]
income.loc[income.Index == "A",:].State

#To filter the rows with Index as "A" and income for 2002 > 1500000"
income.loc[(income.Index == "A") & (income.Y2002 > 1500000),:]

#To filter the rows with index either "A" or "W", we can use isin( ) function:
income.loc[(income.Index == "A") | (income.Index == "W"),:]

#Alternatively.
income.loc[income.Index.isin(["A","W"]),:]


#Dealing with missing values
#We create a new dataframe named 'crops' and to create a NaN value we use np.nan by importing numpy.
import numpy as np
mydata = {'Crop': ['Rice', 'Wheat', 'Barley', 'Maize'],
        'Yield': [1010, 1025.2, 1404.2, 1251.7],
        'cost' : [102, np.nan, 20, 68]}
crops = pd.DataFrame(mydata)
crops

#isnull( ) returns True and notnull( ) returns False if the value is NaN.

crops.isnull()  #same as is.na in R
crops.notnull()  #opposite of previous command.
crops.isnull().sum()  #No. of missing values.
#crops.cost.isnull() firstly subsets the 'cost' from the dataframe and returns a logical vector with isnull()

#To drop all the rows which have missing values in any rows we use dropna(how = "any") . By default inplace = False . If how = "all" means drop a row if all the elements in that row are missing

crops.dropna(how = "any").shape
crops.dropna(how = "all").shape  

#Dealing with duplicates

data = pd.DataFrame({"Items" : ["TV","Washing Machine","Mobile","TV","TV","Washing Machine"], "Price" : [10000,50000,20000,10000,10000,40000]})
data

#duplicated() returns a logical vector returning True when encounters duplicated.
data.loc[data.duplicated(),:]
data.loc[data.duplicated(keep = "first"),:]

#By default keep = 'first' i.e. the first occurence is considered a unique value and its repetitions are considered as duplicates.
#If keep = "last" the last occurence is considered a unique value and all its repetitions are considered as duplicates.

data.loc[data.duplicated(keep = "last"),:] #last entries are not there,indices have changed.

#If keep = "False" then it considers all the occurences of the repeated observations as duplicates.

data.loc[data.duplicated(keep = False),:]  #all the duplicates, including unique are shown.

#To drop the duplicates drop_duplicates is used with default inplace = False, keep = 'first' or 'last' or 'False' have the respective meanings as in duplicated( )

data.drop_duplicates(keep = "first")
data.drop_duplicates(keep = "last")
data.drop_duplicates(keep = False,inplace = True)  #by default inplace = False
data

'''
This is multi line comment
This is multi line comment
This is multi line comment


'''

# IRIS data set

#Creating dummies
import pandas as pd;
iris = pd.read_csv("iris.csv")
print(iris.head()) 


#map( ) function is used to match the values and replace them in the new series automatically created.

iris["setosa"] = iris.Species.map({"setosa" : 1,"versicolor":0, "virginica" : 0})
print(iris.head())

#To create dummies get_dummies( ) is used. iris.Species.prefix = "Species" adds a prefix ' Species' to the new series created.
species_dummies = pd.get_dummies(iris.Species,prefix = "Species")
pd.get_dummies(iris.Species,prefix = "Species").iloc[:,0:1]  #1 is not included
species_dummies = pd.get_dummies(iris.Species,prefix = "Species").iloc[:,0:]
print(species_dummies)

#With concat( ) function we can join multiple series or dataframes. axis = 1 denotes that they should be joined columnwise.
iris = pd.concat([iris,species_dummies],axis = 1)
print(iris.head())

#It is usual that for a variable with 'n' categories we creat 'n-1' dummies, thus to drop the first 'dummy' column we write drop_first = True

pd.get_dummies(iris,columns = ["Species"],drop_first = True).head()

#To create a dataframe of all the ranks we use rank( )
iris.rank() 

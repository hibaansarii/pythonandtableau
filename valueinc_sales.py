# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:28:10 2023

@author: hibah
"""

import pandas as pd

# file_name = pd.read_csv('file.csv')
data = pd.read_csv('transaction2.csv')

data = pd.read_csv('transaction2.csv', sep=';' )
data.info()


#defining variables 

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = NumberofItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberofItemsPurchased * SellingPricePerItem

#CostPerTransaction calculation coloumn 

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#adding new coloumn to data frame 

data['CostPerTransaction'] = CostPerTransaction

#SalesPerTransaction calculation coloumn 

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit calculation 

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# markuo calculation

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']



roundmarkup = round(data['Markup'], 2)
data['Markup'] = round (data['Markup'], 2)

# changing data type of column 
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(year.dtype)
print(day.dtype)

my_date = day + '-' + data['Month'] + '-' + year

data['date'] = my_date

data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows 

data.head(5) #brings in 5 rows 
data.iloc[:,2]
data.iloc[4,2]

#split client keywords into coloumns 

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#creating new coloumns for the split column 

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#use lower function to change uppercase to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files - merging data sets
seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')

data = pd.merge(data, seasons, on ='Month')

#dropping coloumns

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

#export into csv
data.to_csv('ValueInc_Cleaned.csv', index = False)























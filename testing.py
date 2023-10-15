# importing pandas as pd 
import pandas as pd 

# importing numpy as np 
import numpy as np 
from datetime import *

# dictionary of lists 
dict = {'First Score':[100, 90, np.nan, 95], 
		'Second Score': [30, 45, 56, np.nan], 
		'Third Score':[np.nan, 40, 80, 98]} 

# creating a dataframe from list 
df = pd.DataFrame(dict) 
df.columns=[column.replace(" ","_") for column in df.columns]
#df1=df[df['First_Score'].notna() & df['Second_Score'].notna() & df['Third_Score'].notna()]
df.dropna(axis=0,how='all',inplace=True)
todaydate=datetime.now()
withtimestamp=todaydate.strftime("%Y-%m-%d %H:%M:%S")
df.insert(3,'date_on',withtimestamp)
print(withtimestamp)
df1=df.query('First_Score.notnull() & Second_Score.notnull()' )
# using isnull() function 
print(df1)


names = ['madhu','sudhan','reddy']

if (name :=input("enter a name : ")) in names:
	print(f"Hello, {name}!")
else:
	print("name not found")

anniversary=date(2019, 2, 24)
print(f"{anniversary:%A, %B %d, %Y}")
# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here merko nhi samjha 

path
df = pd.read_csv(path)
df['state'] = df['state'].apply(lambda x : x.lower())
df['total'] = df["Jan"] + df["Feb"] + df["Mar"]
sum_jan = df.Jan.sum()  #i think this will do
sum_feb = df.Feb.sum()
sum_mar = df.Mar.sum()
sum_row = sum_jan + sum_feb + sum_mar
sum_total = df.total.sum()
sum_df = pd.DataFrame(data = {"Jan":[sum_jan], 
                       "Feb":sum_feb, 
                       "Mar":sum_mar, 
                       "total":df.total.sum()} )
df_final = pd.concat([df, sum_df])
df_final.tail() 


# --------------
import requests

# Code starts here
url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response  =  requests.get(url)
df1 = pd.read_html(response.content)[0]
df1.drop(index=[0,1,2,3,4,5,6,7,8,9,10],inplace = True)
df1 = df1.rename(columns = df1.iloc[0,:]).iloc[1:,:]


df1['United States of America'] = df1['United States of America'].str.replace(" ","")


# Code ends here


# --------------
# Code starts here

mapping = df1.set_index('United States of America')['US'].to_dict()
df_final.insert(6, 'abbr',np.nan)
df_final['abbr'] = df_final['state'].map(mapping) 


# Code ends here


# --------------
# Code stars here
df1_missi = df_final[df_final['state'] == 'mississipi'].replace(np.nan,'MS')
df1_tennes = df_final[df_final['state'] == 'tenessee'].replace(np.nan,'TN')
df_final.replace(df_final.iloc[6],df1_missi, inplace = True)
df_final.replace(df_final.iloc[10],df1_tennes, inplace = True)
# Code ends here


# --------------
# Code starts here


df_sub = df_final.groupby('abbr')[['Jan','Feb','Mar','total']].sum()
formatted_df = df_sub.applymap(lambda x: str(x) + '$')


# Code ends here


# --------------
# Code starts here



x = df[['Jan','Feb','Mar','total']].sum()
sum_row = pd.DataFrame(x)
df_sub_sum = sum_row.transpose()
df_sub_sum = df_sub_sum.applymap(lambda x: str(x) + '$') 
final_table = formatted_df.append(df_sub_sum,ignore_index=True)
final_table.rename(index={13: "Total"})



# Code ends here




# --------------
# Code starts here
df_sub['total'] = df_sub['total'].sum()
df_sub['total'].plot(kind='pie')

# Code ends here



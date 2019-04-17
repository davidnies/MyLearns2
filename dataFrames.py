import numpy as np
import pandas as pd

def header(msg):
    print(msg)
#
# # Example 1 - load hard-coded data into a dataframe
#  header("1. load hard-coded data into a df")
# df = pd.DataFrame(
#     [['Jan', 58, 42, 74, 22, 2.95],
#     ['Feb', 61, 45, 78, 26, 3.02],
#     ['Mar', 65, 48, 84, 25, 2.34],
#     ['Apr', 67, 50, 92, 28, 1.02],
#     ['May', 71, 53, 98, 35, 0.48],
#     ['Jun', 75, 56, 107, 41, 0.11],
#     ['Jul', 77, 58, 105, 44, 0.0],
#     ['Aug', 77, 59, 102, 43, 0.03],
#     ['Sep', 77, 57, 103, 40, 0.17],
#     ['Oct', 73, 54, 96, 34, 0.81],
#     ['Nov', 64, 48, 84, 30, 1.7],
#     ['Dec', 58, 42, 73, 21, 2.56]],
#     index = [0,1,2,3,4,5,6,7,8,9,10,11],
#     columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])


# Example 2 - read text file into dataframe
header("2. read text file into a df")
filename = 'weather.txt'
df = pd.read_csv(filename)
print(df)

# # Example 3 - print first 5 or last 3 rows of df
# header("3. df.head() print first 5")
# print(df.head())
# header("3. df.tail() print last 3")
# print(df.head())


# # Example 4 - get data types, index, colums, values
# header("4. df.dtypes")
# print(df.dtypes)
# print(" ")
#
# header("4. df.index")
# print(df.index)
# print(" ")
#
# header("4. df.columns")
# print(df.columns)
# print(" ")
#
# header("4. df.values")
# print(df.values)
# print(" ")
#
# # Example 5 - Statistical Summary of each Column
# header("5. Statistical Summary of each Column")
# print(df.describe())
# print(" ")

# # Example 6 - sort records by any column
# header("6. df.sort_values('record_high', ascending=False)")
# print(df.sort_values('record_high', ascending=False))

# # Example 7 - slicing records
# header("7a. slicing -- df.avg_low --- index with single column")
# print(df.avg_low)
# print(" ")
#
# header("7b. slicing -- df[avg_low] --- index with single column")
# print(df['avg_low'])
# print(" ")
#
# header("7c. slicing -- df[2:4] --- index with single column rows 2 to 3")
# print(df[2:4])
# print(" ")
#
# header("7d. slicing -- df[['avg_low', 'avg_high']] --- index with single column rows 2 to 3")
# print(df[['avg_low', 'avg_high']])
# print(" ")
#
# header("7e. slicing -- df.loc[:,['avg_low', 'avg_high']] multiple columns: df.loc[from_row:to_row,['column1','column2'")
# print(df.loc[:, ['avg_low', 'avg_high']])
# print(" ")
#
# header("7f. slicing scalar value -- df.loc[9,['avg_precipitation']]" )
# print(df.loc[9, ['avg_precipitation']])
# print(" ")
#
# header("7g. slicing -- df.iloc[3:5,[0,3]] --- index location can receive range or list of indices")
# print(df.iloc[3:5, [0, 3]])
# print(" ")

# # Example 8 - filtering
# header("8. df[df.avg_precipitation > 1.0 --- filter on column values")
# print(df[df.avg_precipitation > 1.0])
# print(" ")
#
# header("8. df[df['month'].isin(['Jun', 'Jul', 'Aug'] --- filter on column values")
# print(df[df['month'].isin(['Jun', 'Jul', 'Aug'])])
# print(" ")

# # Example 9 - assignment -- similar to slicing
# header("9a. df.loc[9,['avg_precipitation']] = 101.3")
# df.loc[9, ['avg_precipitation']] = 101.3
# print(df.iloc[9:11])
# print(" ")
#
# header("9b. df.loc[9, ['avg_precipitations']] == np.nan")
# df.loc[9, ['avg_precipitation']] = np.nan
# print(df.iloc[9:11])
# print(" ")
#
# header("9c. df.loc[:, 'avg_low'] = np.array([5] * len(df))")
# df.loc[:, 'avg_low'] = np.array([5] * len(df))
# print(df.head())
# print(" ")
#
# header("9d. df['avg_day'] = (df.avg_low + df.avg_high) / 2")
# df['avg_day'] = (df.avg_low + df.avg_high) / 2
# print(df.head())
# print(" ")

# # Example 10 - renaming columns
# header("10. df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
# df.rename(columns = {'avg_precipitation':'avg_rain'}, inplace=True)
# print(df.head())
# print(" ")
#
# header("10a. df.columns = {'avg_precipitation':'avg_rain'}, inplace=True)")
# df.columns = ['month', 'av_hi', 'av_loc', 'rec_hi', 'rec_lo', 'av_rain']
# print(df.head())
# print(" ")

# Example 11 - iterate rows
header("11. iterate rows of df with a for loop")
for index, row in df.iterrows():
    print(index, row["month"], row["avg_high"])

print(" ")

# Example 12 write to csv file
df.to_csv('weather2.csv')


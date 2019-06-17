
import pandas as pd
import os


#path = 'C:\\Users\\David\\Desktop\\MyStuff\\FAO+database.csv'

print("Working Directory is {}".format(os.getcwd()))

pd.set_option("display.max_rows", 10)
pd.set_option("display.max_columns", 200)




df = pd.read_csv('Sample_Data.csv', sep=',', encoding='latin-1', skiprows=0)
# print(df)


# print(df.columns)





import csv
import pandas as pd

filePath = 'C:\\Users\\David\\AppData\\Local\\Programs\\Python\Python37\\ACCESS_SAMPLE_DATA.csv'

# with open(filePath, 'r') as f:
#   reader = csv.reader(f)
#   your_list = list(reader)
#
# print(your_list)


# Read the CSV into a pandas data frame (df)
#   With a df you can do many things
#   most important: visualize data with Seaborn
df=pd.read_csv(filePath,delimiter=',')


# Or export it in many ways, e.g. a list of tuples
tuples = [tuple(x) for x in df.values]

# or export it as a list of dicts
dicts = df.to_dict().values()

# print(df)

print(dicts[])
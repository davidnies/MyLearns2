import numpy as np
import pandas as pd


fileName = 'Specification_STAAR_38_2018.csv'

df = pd.read_csv(fileName)
# print(df)
# print(df.columns)
# # print(df.values)

# print(df.index)
# print(len(df.index))

# print(df.dtypes)
# df.FwStartPosition = df.FwStartPosition.astype(str)
# df.FwEndPosition = df.FwEndPosition.astype(str)
# df.FieldLength = df.FieldLength.astype(str)
# df.DiscardFlag = df.DiscardFlag.astype(str)
# df.DelimitedColumnIndex = df.DelimitedColumnIndex.astype(str)
# df.LookupInputColumn4 = df.LookupInputColumn4.astype(str)
# df.LookupInputColumn4 = df.LookupInputColumn4.astype(str)
# print(df.dtypes)

df2 = df[df.DocumentFieldName > ""]
df3 = df2
print(df2.shape)
# print(df2)
# print(df[df.DocumentFieldName > ""])
print(df2.index)
# print(df2.columns)

# print(list(df.columns.values))

# print(df2.iloc[0][1], df2.iloc[0][3], df2.iloc[0][4], df2.iloc[0][5])
print(df2.iloc[1][1], df2.iloc[1][3], df2.iloc[1][4], df2.iloc[1][5])
print(df2.iloc[2][1], df2.iloc[2][3], df2.iloc[2][4], df2.iloc[2][5])



for index, row in df.iterrows():
    nxtrow = row + 1
    num1 = df2.iloc[row][4] - df2.iloc[row][3] + 1
    num2 = df2.iloc[1][3] + df2.iloc[1][5]


# print(num1,num2)



# if df2.iloc[2][4] == (df2.iloc[2][3]:
#     print("Yes it's equal")

#for index, row in df.iterrows():
# for i in range(0, 881):
    # print(i)
    # if i < 880:
       # num1 = df2.iloc[i][4]
       # num2 = df2.iloc[i+1][3]

#       num = df2.iloc[1,4]

        # if (df2.iloc[i][4] - df2.iloc[i+1][3] != 1):
       # print(num)



# print(df2.iloc[0][3])
# print(df2.iloc[0][4])
# print(df2.iloc[0][5])



# print(df2.dtypes)




# for index, row in df2.iterrows():
#
#     if (df2[df2.FwEndPosition] == df2[df2.FwStartPosition].shift(1).item()):
#         print("Same")
#     print(index, row["DocumentFieldName"], row["FwStartPosition"], row["FwEndPosition"], row["FieldLength"])

# wb = openpyxl.load_workbook("C:\\Users\\David's\\PycharmProjects\\MyProj\\MyProj\\MyLearns\\Specification_STAAR_38_2018.xlsx")
# print(wb.sheetnames)
# sheet = wb['ColumnDefinitions']
#
# print('Reading rows....')
#
# for row in range(2, sheet.max_row +1):
#     seq = row
#     DFN = sheet['A' + str(row)].value
#     TCN = sheet['B' + str(row)].value
#     DCI = sheet['C' + str(row)].value
#     FSP = sheet['D' + str(row)].value
#     FEP = sheet['E' + str(row)].value
#     FL = sheet['F' + str(row)].value
#     DF = sheet['G' + str(row)].value
#     LT = sheet['H' + str(row)].value
#     LC = sheet['I' + str(row)].value
#     LIC = sheet['J' + str(row)].value
#     LIC2 = sheet['K' + str(row)].value
#     LIC3 = sheet['L' + str(row)].value
#     LIC4 = sheet['M' + str(row)].value
#     LOC = sheet['N' + str(row)].value
#     data = [seq,DFN,TCN,DCI,FSP,FEP,FL,DF,LT,LC,LIC,LIC2,LIC3,LIC4,LOC]
#     # print(data)
#    # print(row)
#
# #for i in range(1, 1013):
# print(data(2,2,2,2,2,2,2,2,2,2,2,2,2,2,2))
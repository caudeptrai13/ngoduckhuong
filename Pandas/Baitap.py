import pandas as pd

df = pd.read_csv('Salaries.csv') # Cau 1
print(df.head()) # Cau 2
print(df.info()) # Cau 3
print("Average of BasePay : " + str(df["BasePay"].mean())) # Cau 4
print("Maximum value of OvertimePay : " + str(df["OvertimePay"].max())) # Cau 5
print(df["JobTitle"][df["EmployeeName"].str.upper() == "JOSEPH DRISCOLL"]) # Cau 6
profit = sum(df["TotalPayBenefits"][df["EmployeeName"].str.upper() == "JOSEPH DRISCOLL"])
print("Total pay of JOSEPH DRISCOLL : " + str(profit)) #Cau 7
print(df.iloc[df["TotalPayBenefits"].idxmax()]) # Cau 8
print(df.iloc[df["TotalPayBenefits"].idxmin()]) # Cau 9
print(df.groupby(["Year"])["BasePay"].mean()) #Cau 10
Jobs= df["JobTitle"].str.upper()
print(len(Jobs.unique())) #Cau 11
print(Jobs.value_counts()[:5]) #Cau 12
print((df[df["Year"] == 2013]["JobTitle"].value_counts() == 1).sum()) #Cau 13
print(Jobs.apply(lambda x: "CHIEF" in str(x)).sum()) #Cau 14
print(df["JobTitle"].apply(lambda x: len(x)).corr(df["TotalPay"])) #Cau 15
#Jobs.index = df["EmployeeName"]


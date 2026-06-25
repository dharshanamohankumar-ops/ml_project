import pandas as pd
import re
df=pd.read_csv("data1.csv")
print("missing value")
print(df.isnull().sum())
df["name"]=df["name"].fillna("unknown")
df["rollno"]=df["rollno"].fillna("unknown")
df["mark"]=df["mark"].fillna("0")
print("\nproceesed data")
print(df)

# Read dataset
df = pd.read_csv("data1.csv")

# Rule for roll number
pattern = r'^\d{6}ECR\d{3}$'

print("\nDATA VALIDATION REPORT")
print("-" * 40)

for i in df.index:

    # Check Name
    name = str(df.loc[i, "name"])

    if not name.isalpha():
        print(f"Row {i+1}: Invalid Name -> {name}")
        df.loc[i, "name"] = str(name)

    # Check Roll Number
    roll = str(df.loc[i, "rollno"])

    if roll == "nan":
        print(f"Row {i+1}: Roll Number Missing")

    elif not re.match(pattern, roll):
        print(f"Row {i+1}: Invalid Roll Number -> {roll}")

    # Check Mark
    if pd.isnull(df.loc[i, "mark"]):
        print(f"Row {i+1}: Marks Missing")

print("\nCLEANED DATA")
print(df)



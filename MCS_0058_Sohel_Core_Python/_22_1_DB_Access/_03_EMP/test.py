import pandas as pd
emp1 = pd.read_excel("empl.xlsx")
emp2 = pd.read_excel("emp2.xlsx")
all_df_list = [emp1, emp2]
appended_df = pd.concat(all_df_list)
appended_df.to_excel("emp3.xlsx", index=False)
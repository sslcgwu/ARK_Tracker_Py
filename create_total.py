# Add the "Total_All_Fund" tab to the .xlsx data file if it does NOT exist.
import os
import pandas as pd

input_dir = r'C:\investment_ds\ark_innovation\ARK_TRACKER_Py\Input'

file_list = [f for f in os.listdir(input_dir) if f.endswith('.xlsx')]
print(file_list)

for file in file_list:
    
    raw_ds = pd.read_excel(os.path.join(input_dir, file))
    date_flag = file[-8:]

    if "Total_All_Fund" not in raw_ds.keys():
        # create & add the "Total_All_Fund" tab 
    
    else:
        print("The Total_All_Fund tab is already exist for {}".format(date_flag))

import pandas as pd
file_data = pd.read_excel("duplicate_data.xlsx")
file_data_record = file_data.drop_duplicates(subset=["marketplace","customer_id","product_category"], keep="first")
file_data_record.to_excel("Removed_Duplicates_Record.xlsx", index=False)
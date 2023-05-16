# Import your libraries
import pandas as pd
import numpy as np


#Final DF attributes:
#product_class
#product_family(alphabetic)
#media_type
#units_sold(rounded % from highest to lowest)


df_1 = pd.merge(online_orders, online_products, on=["product_id"])
df_2 = pd.merge(online_sales_promotions, online_orders, on=["promotion_id"])

df_1 = df_1[['product_id', 'product_class', 'product_family']]
df_2 = df_2[['product_id','media_type','units_sold']]

df_3 = pd.merge(df_1, df_2, on=["product_id"])

df_final = df_3.groupby(['media_type','product_class','product_family'])['units_sold'].sum().reset_index()

df_final['units_sold (%)'] = df_final['units_sold'].apply(lambda x: (x / df_final['units_sold'].sum()) * 100).round()

df_final = df_final.sort_values('units_sold (%)', ascending=False)


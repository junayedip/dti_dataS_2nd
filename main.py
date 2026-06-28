import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('customers_dirty.csv')
df = df.drop_duplicates(subset=['email', 'name']).reset_index(drop=True)
df['name'] = df['name'].str.strip().str.title()
df['product_category'] = df['product_category'].str.strip().str.title()
df['gender'] = df['gender'].str.strip().str.title()

df.to_csv('cleaned_customer.csv')
print(df.head(20))
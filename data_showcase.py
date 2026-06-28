

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv('cleaned_customer.csv')
sns.set_theme(style='whitegrid')
sns.countplot(data=df, x='product_category', palette='Set2')
plt.title("Customers per Product Category") 
plt.xticks(rotation=30, ha='right') 
plt.tight_layout() 
plt.show()
print(df.head(10))